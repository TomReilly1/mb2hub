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
import type * as intr from "@/interfaces/indexIntr"

import ConceptTableColumnId from "@/components/ConceptTableColumnId.vue"
import ConceptTableColumnColor from "@/components/ConceptTableColumnColor.vue"
import ConceptTableColumnArray from "@/components/ConceptTableColumnArray.vue"
import ConceptTableColumnObject from "@/components/ConceptTableColumnObject.vue"


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
const filters = ref()
const globalFilters = ref()


const initFilters = () => {
    if (props.dataArr[0] === undefined) {
        return
    }

    console.log('initFilters reached')

    let temp: any = {}
    switch (route.params.concept) {
        case 'armors':
            temp = temp as intr.armors
            break;
        case 'bows':
            temp = temp as intr.bows
            break;
        case 'castles':
            temp = temp as intr.castles
            break;
        case 'cultures':
            temp = temp as intr.cultures
            break;
        case 'goods':
            temp = temp as intr.goods
            break;
        case 'kingdoms':
            temp = temp as intr.kingdoms
            break;
        case 'lords':
            temp = temp as intr.lords
            break;
        case 'mounts':
            temp = temp as intr.mounts
            break;
        case 'troops':
            temp = temp as intr.troops
            break;
        case 'villages':
            temp = temp as intr.villages
            break;
        default:
            console.log('interface not found')
            break;
    }

    temp = props.dataArr[0]

    // need to remove desc_text from table due to large size
    if (temp.desc_text) {
        delete temp.desc_text
    }

    let dataColsArr: dataColsIntr[] = []
    for (const key in temp) {
        const typeOf: string = generateColumnDataType(key, temp[key])

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
        else if (typeof temp[key] === 'number' || key.includes('_armor')) {
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

function handleBodyStyle(header: string) {
    return (header.includes('color')) ? 'text-align: center' : ''
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

const generateColumnDataType = (key: string, val: any) => {
    const l_valType: string = typeof val 
    
    if (key.includes('_armor')) {
        return 'number'
    } else if (key.includes('color')) {
        return 'color'
    } else if (Array.isArray(val)) {
        return 'array'
    } else if (l_valType === 'object') {
        return 'object'
    } else {
        return l_valType
    }
}

// const getConceptFromObject = (dataHeader: string, id: string) => {
//     switch (dataHeader) {
//         case 'owner_clan':
//             return 'clans'
//         case 'owner_lord':
//             return 'lords'
//         case 'bound_settlement':
//             return getSettlementType(id)
//         case 'bound_villages':
//             return 'villages'
//         case 'upgrade_targets':
//             return 'troops'
//         default:
//             throw Error('Error: could not generate concept based off object data header')
//             break
//     }
// }

const getSettlementType = (input: string) => {
    return (input.includes('castle')) ? 'castles' : 'towns'
}

watch(() => props.dataArr, () => {
    loading.value = false
    initFilters()
    console.log(props.dataArr)
})
</script>
<!---------------------------------------------------->
<template>
<div id="data-table" class="concept-table">
    <DataTable :value="dataArr" :paginator="true" class="p-datatable-sm" showGridlines :rows="10" rowHover dataKey="id" v-model:filters="filters" filterDisplay="menu" :loading="loading" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown" :rowsPerPageOptions="[10,25,50]" responsiveLayout="scroll" :globalFilterFields="globalFilters" >
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
        <Column v-for="col in objRefnce" :field="col.dataHeader" :header="valueToHeader(col.dataHeader)" :datatype="handleDataType(col.dataType)" :showFilterMatchModes="handleMatchModeVis(col.dataHeader)" :filterMatchModeOptions="handleMatchModeType(col.dataHeader)" :bodyStyle="handleBodyStyle(col.dataHeader)" :sortable="col.dataType !== 'array' && col.dataType !== 'object'">
            <!-- data -->
            <template v-if="col.dataHeader === 'id'" #body="{data}">
                <ConceptTableColumnId :concept="(route.params.concept as string)" :id="data.id" :data="data[col.dataHeader]" />
            </template>
            <template v-else-if="col.dataType === 'color'" #body="{data}" bodyStyle="display: flex; justify-content: center;">
                <ConceptTableColumnColor :color-data="data[col.dataHeader]" />
            </template>
            <template v-else-if="col.dataType === 'array'" #body="{data}">
                <ConceptTableColumnObject v-for="obj in data[col.dataHeader]" :header="col.dataHeader" :obj="obj" :arr="data[col.dataHeader]"/>
            </template>
            <template v-else-if="col.dataType === 'object'" #body="{data}">
                <ConceptTableColumnObject :header="col.dataHeader" :obj="data[col.dataHeader]"/>
            </template>
            <template v-else #body="{data}">
                <span v-if="data[col.dataHeader] === null">N/A</span>
                <span v-else-if="data[col.dataHeader] === ''">EMPTY</span>
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

:deep(a) {
    color: var(--yellow-400);
}

:deep(a:hover) {
    color: var(--yellow-100);
}

.router-link-active {
    color: var(--yellow-200)
}

.color-input {
    width: 100px;
    padding: 0;
}
</style>
