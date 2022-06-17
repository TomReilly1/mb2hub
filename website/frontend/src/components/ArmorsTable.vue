<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from 'vue-router';

import { FilterMatchMode, FilterOperator } from 'primevue/api';
import InputText from 'primevue/inputtext';



const route = useRoute();
const props = defineProps({armorsArr: Array});
const loading = ref(true);


onMounted(() => {
    loading.value = false;
})


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
    'culture': {
        operator: FilterOperator.AND,
        constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }]
    },
    'type': {
        operator: FilterOperator.AND,
        constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }]
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
        'culture': {
            operator: FilterOperator.AND,
            constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }]
        },
        'type': {
            operator: FilterOperator.AND,
            constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }]
        }
    }
}

const clearFilters = () => {
    initFilters();
}
</script>
<!---------------------------------------------------->
<template>
<div id="armors-table" class="concept-table">
    <DataTable :value="armorsArr" :paginator="true" class="p-datatable-sm" showGridlines :rows="10" rowHover dataKey="id" v-model:filters="filters" filterDisplay="menu" :loading="loading"   paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown" :rowsPerPageOptions="[10,25,50]" responsiveLayout="scroll" :globalFilterFields="['id','name','culture','type']">
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
            No armor found.
        </template>
        <template #loading>
            Loading armor data. Please wait.
        </template>
        <Column field="id" header="ID" sortable>
            <template #body="{data}">
                <router-link :to="{name: 'cardview', params: {concept: route.params.concept, id: data.id}}" class="id-link">
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
        <Column field="culture" header="Culture" sortable>
            <template #body="{data}">
                {{data.culture}}
            </template>
            <template #filter="{filterModel, filterCallback}">
                <InputText type="text" v-model="filterModel.value" @input="filterCallback()" class="p-column-filter" :placeholder="`Search by culture - `" />
            </template>
        </Column>
        <Column field="weight" header="Weight" sortable></Column>
        <Column field="type" header="Type" sortable>
            <template #body="{data}">
                {{data.type}}
            </template>
            <template #filter="{filterModel, filterCallback}">
                <InputText type="text" v-model="filterModel.value" @input="filterCallback()" class="p-column-filter" :placeholder="`Search by type - `" />
            </template>
        </Column>
        <Column field="head_armor" header="Head AR" sortable></Column>
        <Column field="body_armor" header="Body AR" sortable></Column>
        <Column field="arm_armor" header="Arm AR" sortable></Column>
        <Column field="leg_armor" header="Leg AR" sortable></Column>
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

#armors-table {
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
