<script setup>
import { ref, watch } from "vue";
import { useRoute } from 'vue-router';

import Button from "primevue/button/sfc";
import DataTable from 'primevue/datatable/sfc';
import Column from 'primevue/column/sfc';
import { FilterMatchMode, FilterOperator } from 'primevue/api';
import MultiSelect from 'primevue/multiselect/sfc';
import InputText from 'primevue/inputtext/sfc';
import InputNumber from 'primevue/inputnumber/sfc';



const route = useRoute();
const props = defineProps({dataArr: Array});
const trueOrFalse = ref([
    {"label": "True", "val": true},
    {"label": "False", "val": false}
]);
const loading = ref(true);
const objRefnce = ref();
const filters = ref();
const globalFilters = ref();



const initFilters = () => {
    // need to remove desc_text from table due to large size
    const temp = props.dataArr[0];
    if ('desc_text' in temp) {
        delete temp.desc_text;
    }
    objRefnce.value = temp;

    let filtersToAdd = {};
    let globalFiltArr = []
    filtersToAdd['global'] = {value: null, matchMode: FilterMatchMode.CONTAINS}

    for (let key in objRefnce.value) {
        if (typeof objRefnce.value[key] === 'boolean') {
            filtersToAdd[key] = { value: null, matchMode: FilterMatchMode.IN }
            globalFiltArr.push(key);
        }
        else if (typeof objRefnce.value[key] === 'number') {
            filtersToAdd[key] = {
                operator: FilterOperator.AND,
                constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }]
            }
        }
        else if (typeof objRefnce.value[key] === 'string' && !key.includes('color')) {
            filtersToAdd[key] = {
                operator: FilterOperator.AND,
                constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }]
            }
            globalFiltArr.push(key);
        }
    }
    
    filters.value = filtersToAdd;
    globalFilters.value = globalFiltArr;
}


function valueToHeader(value) {
    const valArr = value.split('_');
    const upperArr = valArr.map((e) => {
        return e.substring(0,1).toUpperCase() + e.substring(1);
    })
    return upperArr.join(' ');
}

function handleDataType(value) {
    if (typeof value === 'number') {
        return 'numeric';
    } else {
        return 'text';
    } 
}

const handleMatchModeVis = (value) => {
    if (typeof value === 'boolean') {
        return false;
    } else {
        return true;
    } 
}

function handleMatchModeType(value) {
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
    loading.value = false;
    initFilters();
})
</script>
<!---------------------------------------------------->
<template>
<div v-if="filters !== null || filters !== undefined || dataArr !== null || dataArr !== undefined" id="data-table" class="concept-table">
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
        <Column v-for="(colVal, colKey) in objRefnce" :field="colKey" :header="valueToHeader(colKey)" :datatype="handleDataType(colVal)" :showFilterMatchModes="handleMatchModeVis(colVal)" :filterMatchModeOptions="handleMatchModeType(colVal)" sortable>
            <!-- data -->
            <template v-if="colKey === 'id'" #body="{data}">
                <router-link :to="{name: 'cardview', params: {concept: route.params.concept, id: data.id}}" class="id-link">
                    {{data[colKey]}}
                </router-link>
            </template>
            <template v-else #body="{data}">
                <span v-if="data[colKey] === null">N/A</span>
                <span v-else>{{data[colKey]}}</span>
            </template>
            <!-- filter -->
            <template v-if="typeof colVal === 'boolean'" #filter="{filterModel}">
                <div class="mb-3 font-bold">Select {{colKey}}:</div>
                <MultiSelect v-model="filterModel.value" :options="trueOrFalse" optionLabel="label" optionValue="val" placeholder="Any" class="p-column-filter">
                    <template #option="slotProps">
                        <div class="p-multiselect-representative-option">
                            {{slotProps.option.val}}
                        </div>
                    </template>
                </MultiSelect>
            </template>
            <template v-else-if="typeof colVal === 'number'" #filter="{filterModel}">
                <InputNumber v-model="filterModel.value" :placeholder="`Filter numerically - `"/>
            </template>
            <template v-else-if="typeof colVal === 'string' || objRefnce[colKey] === null" #filter="{filterModel, filterCallback}">
                <InputText type="text" v-model="filterModel.value" @input="filterCallback()" class="p-column-filter" :placeholder="`Search by ${colKey} - `"/>
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
