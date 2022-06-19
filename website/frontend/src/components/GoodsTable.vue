<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from 'vue-router';

import { FilterMatchMode, FilterOperator } from 'primevue/api';
import MultiSelect from 'primevue/multiselect';
import InputText from 'primevue/inputtext';
import InputNumber from 'primevue/inputnumber';


const route = useRoute();
const props = defineProps({goodsArr: Array});
const loading = ref(true);


onMounted(() => {
    loading.value = false;
})


function formatBonus(bonus) {
    if (bonus === null) {
        return 0;
    } else {
        return bonus;
    }
}


const filters = ref({
    'global': {value: null, matchMode: FilterMatchMode.CONTAINS},
    'id': {
        operator: FilterOperator.AND,
        constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }]
    },
    'name': {
        operator: FilterOperator.AND,
        constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }]
    },
    'value': {
        operator: FilterOperator.AND,
        constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }]
    },
    'is_food': {
        value: null, matchMode: FilterMatchMode.IN
    }
});

const initFilters = () => {
    filters.value = {
        'global': {value: null, matchMode: FilterMatchMode.CONTAINS},
        'id': {
            operator: FilterOperator.AND,
            constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }]
        },
        'name': {
            operator: FilterOperator.AND,
            constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }]
        },
        'value': {
            operator: FilterOperator.AND,
            constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }]
        },
        'is_food': {
            value: null, matchMode: FilterMatchMode.IN
        }
    }
}

const clearFilters = () => {
    initFilters();
}
</script>
<!------------------------------------------------------------------->
<template>
<div id="kingdom-table" class="concept-table">
    <DataTable :value="goodsArr" :paginator="true" class="p-datatable-sm" showGridlines :rows="25" rowHover dataKey="id" v-model:filters="filters" filterDisplay="menu" :loading="loading" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown" :rowsPerPageOptions="[10,25,50]" responsiveLayout="scroll" :globalFilterFields="['id','name','value','is_food']">
        <template #header>
            <div class="flex justify-content-between global-filter">
                <Button type="button" icon="pi pi-filter-slash" label="Clear" class="p-button-outlined" @click="clearFilters()" />
                <span class="p-input-icon-left">
                    <i class="pi pi-search" />
                    <InputText v-model="filters['global'].value" placeholder="Keyword Search" />
                </span>
            </div>
        </template>
        <template #empty>
            No goods data found.
        </template>
        <template #loading>
            Loading goods data. Please wait.
        </template>
        <Column field="id" header="ID" sortable>
            <template #body="{data}">
                <router-link :to="{name: 'cardview', params: {concept: route.params.concept, id: data.id}}" class="nav-link">
                    {{data.id}}
                </router-link>
            </template>
            <template #filter="{filterModel, filterCallback}">
                <InputText type="text" v-model="filterModel.value" @input="filterCallback()" class="p-column-filter" :placeholder="`Search by id - `"/>
            </template>
        </Column>
        <Column field="name" header="Name" sortable>
            <template #body="{data}">
                {{data.name}}
            </template>
            <template #filter="{filterModel, filterCallback}">
                <InputText type="text" v-model="filterModel.value" @input="filterCallback()" class="p-column-filter" :placeholder="`Search by name - `"/>
            </template>
        </Column>
        <Column field="plural" header="Plural Name" sortable></Column>
        <Column header="Value" field="value" dataType="numeric" sortable>
            <template #body="{data}">
                {{data.value}}
            </template>
            <template #filter="{filterModel}">
                <InputNumber v-model="filterModel.value"/>
            </template>
        </Column>
        <Column field="weight" header="Weight"></Column>
        <Column field="is_food" header="Is food?" sortable></Column>
        <Column field="morale_bonus" header="Morale Bonus" sortable>
            <template #body="{data}">
                {{formatBonus(data.morale_bonus)}}
            </template>
        </Column>
    </DataTable>
</div>
</template>
<!------------------------------------------------------------------->
<style scoped>
.global-filter {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
}

#kingdom-table {
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

.color-data {
    margin: 0;
    border: 0;
    padding: 0;
    width: 100%;
    max-width: 75px;
}

.color-data::after {
    height: 100%;
    /* vertical-align: middle; */
}

.color-text::after {
    float: left;
    margin: 0;
    border: 0;
    padding: 0;
}

.center-header {
    text-align: center;
    justify-content: center;
    background-color: aqua !important;
}
</style>
