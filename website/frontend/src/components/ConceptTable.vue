<script setup lang="ts">
import { ref, watch, onMounted } from "vue"
import { useRoute, type RouteLocationNormalizedLoaded } from 'vue-router'

import Button from "primevue/button"
import DataTable from 'primevue/datatable'
import Column from 'primevue/column'
import { FilterMatchMode, FilterOperator } from 'primevue/api'
import MultiSelect from 'primevue/multiselect'
import InputText from 'primevue/inputtext'
import InputNumber from 'primevue/inputnumber'
import Skeleton from "primevue/skeleton"

interface dataColsIntr {
    dataHeader: string
    dataType: string
}

const route: RouteLocationNormalizedLoaded = useRoute()
const props = defineProps<{
    dataArr: object[]
}>()
const trueOrFalse = ref([
    {"label": "True", "val": true},
    {"label": "False", "val": false}
])
const loading = ref<boolean>(true)
const objRefnce = ref<dataColsIntr[]>()
const dummyData = ref(new Array(6))
const filters = ref()
const globalFilters = ref()


const initFilters = () => {
    if (props.dataArr[0] === undefined) {
        return
    }

    // need to remove desc_text from table due to large size
    const temp: any = props.dataArr[0]
    if (temp.desc_text !== undefined) {
        delete temp.desc_text
    }

    if (temp.desc_text) {
        delete temp.desc_text
    }

    let dataColsArr: dataColsIntr[] = []
    for (const key in temp) {
        const typeOf: string = typeof temp[key]
        dataColsArr.push({
            'dataHeader': key,
            'dataType': typeOf
        })
    }
    objRefnce.value = dataColsArr

    let filtersToAdd: any = {}
    let globalFiltArr = []
    filtersToAdd['global'] = {value: null, matchMode: FilterMatchMode.CONTAINS}

    for (let key in temp) {
        if (typeof temp[key] === 'boolean') {
            filtersToAdd[key] = { value: null, matchMode: FilterMatchMode.IN }
            globalFiltArr.push(key);
        }
        else if (typeof temp[key] === 'number') {
            filtersToAdd[key] = {
                operator: FilterOperator.AND,
                constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }]
            }
        }
        else if (typeof temp[key] === 'string' && !key.includes('color')) {
            filtersToAdd[key] = {
                operator: FilterOperator.AND,
                constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }]
            }
            globalFiltArr.push(key)
        }
    }
    
    filters.value = filtersToAdd
    globalFilters.value = globalFiltArr
}


function valueToHeader(value: string) {
    const valArr = value.split('_')
    const upperArr = valArr.map((e) => {
        return e.substring(0,1).toUpperCase() + e.substring(1)
    })
    return upperArr.join(' ')
}

function handleDataType(value: string) {
    return (typeof value === 'number') ? 'numeric' : 'text'
}

const handleMatchModeVis = (value: string) => {
    return typeof value !== 'boolean'
}

function handleMatchModeType(value: string) {
    if (typeof value === 'number') {
        return [
            {label: 'Equals', value: FilterMatchMode.EQUALS},
            {label: 'Not Equals', value: FilterMatchMode.NOT_EQUALS},
            {label: 'Less Than', value: FilterMatchMode.LESS_THAN},
            {label: 'Less Than Or Equal To', value: FilterMatchMode.LESS_THAN_OR_EQUAL_TO},
            {label: 'Greater Than', value: FilterMatchMode.GREATER_THAN},
            {label: 'Greater Than Or Equal To', value: FilterMatchMode.GREATER_THAN_OR_EQUAL_TO},
        ]
    } else {
        return [
            {label: 'Starts With', value: FilterMatchMode.STARTS_WITH},
            {label: 'Contains', value: FilterMatchMode.CONTAINS},
            {label: 'Not Contains', value: FilterMatchMode.NOT_CONTAINS},
            {label: 'Ends With', value: FilterMatchMode.ENDS_WITH},
            {label: 'Equals', value: FilterMatchMode.EQUALS},
            {label: 'Not Equals', value: FilterMatchMode.NOT_EQUALS},
        ]
    } 
}


watch(() => props.dataArr, () => {
    loading.value = false
    initFilters()
    console.log(props.dataArr)
})
</script>
<!---------------------------------------------------->
<template>
<!-- <div v-if="filters !== null || filters !== undefined || dataArr !== null || dataArr !== undefined" id="data-table" class="concept-table"> -->
<div v-if="!loading" id="data-table" class="concept-table">
    <DataTable :value="dataArr" :paginator="true" class="p-datatable-sm" showGridlines :rows="10" rowHover dataKey="id" v-model:filters="filters" filterDisplay="menu" :loading="loading" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown" :rowsPerPageOptions="[10,25,50]" responsiveLayout="scroll" :globalFilterFields="globalFilters">
        <template v-if="filters !== undefined" #header>
            <div class="flex justify-content-between global-filter">
                <Button type="button" icon="pi pi-filter-slash" label="Clear" class="p-button-outlined" @click="initFilters()" />
                <span class="p-input-icon-left">
                    <i class="pi pi-search" />
                    <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
                </span>
            </div>
        </template>
        <template #empty>
            No data found.
        </template>
        <template #loading>
            Loading data. Please wait.
        </template>
        <!-- <Column v-for="(colVal, colKey) in objRefnce" :header="valueToHeader(colKey)" :datatype="handleDataType(colVal)" :showFilterMatchModes="handleMatchModeVis(colVal)" :filterMatchModeOptions="handleMatchModeType(colVal)" sortable> -->
        <Column v-for="col in objRefnce" :field="col.dataHeader" :header="valueToHeader(col.dataHeader)" :datatype="handleDataType(col.dataType)" :showFilterMatchModes="handleMatchModeVis(col.dataHeader)" :filterMatchModeOptions="handleMatchModeType(col.dataHeader)" sortable>
            <!-- data -->
            <template v-if="col.dataHeader === 'id'" #body="{data}">
                <router-link :to="{name: 'cardview', params: {concept: route.params.concept, id: data.id}}" class="id-link">
                    {{data[col.dataHeader]}}
                </router-link>
            </template>
            <template v-else #body="{data}">
                <span v-if="data[col.dataHeader] === null">N/A</span>
                <span v-else>{{data[col.dataHeader]}}</span>
            </template>
            <!-- filter -->
            <template v-if="col.dataType === 'boolean'" #filter="{filterModel}">
                <div class="mb-3 font-bold">Select {{col.dataHeader}}:</div>
                <MultiSelect v-model="filterModel.value" :options="trueOrFalse" optionLabel="label" optionValue="val" placeholder="Any" class="p-column-filter">
                    <template #option="slotProps">
                        <div class="p-multiselect-representative-option">
                            {{slotProps.option.val}}
                        </div>
                    </template>
                </MultiSelect>
            </template>
            <template v-else-if="col.dataType === 'number'" #filter="{filterModel}">
                <InputNumber v-model="filterModel.value" :placeholder="`Filter numerically - `"/>
            </template>
            <template v-else-if="col.dataType === 'string' || objRefnce[col.dataHeader] === null" #filter="{filterModel, filterCallback}">
                <InputText type="text" v-model="filterModel.value" @input="filterCallback()" class="p-column-filter" :placeholder="`Search by ${col.dataHeader} - `"/>
            </template>
        </Column>
    </DataTable>
</div>
<div v-else id="data-table" class="concept-table">
    <DataTable :value="dummyData">
        <Column>
            <template #header>
                <Skeleton width="5rem" height="0.8rem" />
            </template>
            <template #body>
                <Skeleton size="30px" />
            </template>
        </Column>
        <Column>
            <template #header>
                <Skeleton width="5rem" height="0.8rem"/>
            </template>
            <template #body>
                <Skeleton size="30px" />
            </template>
        </Column>
        <Column>
            <template #header>
                <Skeleton width="5rem" height="0.8rem"/>
            </template>
            <template #body>
                <Skeleton size="30px" />
            </template>
        </Column>
        <Column>
            <template #header>
                <Skeleton width="5rem" height="0.8rem"/>
            </template>
            <template #body>
                <Skeleton size="30px" />
            </template>
        </Column>
    </DataTable >
</div>
</template>
<!---------------------------------------------------->
<style scoped>
.global-filter {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
}

#data-table {
    background-color: var(--bluegray-900);
    border: 3px solid var(--bluegray-700);
    margin: 0 auto;
    width: fit-content;
    max-width: 98%;
    box-shadow: 0 0 1px 2px #3f4b5b;
}

a {
    color: var(--yellow-400);
}

a:hover {
    color: var(--yellow-100);
}

.router-link-active {
    color: var(--yellow-200)
}
</style>
