<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from 'vue-router';

import Button from "primevue/button/sfc";
import DataTable from 'primevue/datatable/sfc';
import Column from 'primevue/column/sfc';
import { FilterMatchMode, FilterOperator } from 'primevue/api';
import InputText from 'primevue/inputtext/sfc';
import MultiSelect from 'primevue/multiselect/sfc';

import culturesData from "@/data/cultures_list.json";



const route = useRoute();
const props = defineProps({troopsArr: Array});
const loading = ref(true);
const cultures = ref();
const defaultGroups = ref ([
    {'id': 'Infantry', 'name': 'Infantry'},
    {'id': 'Ranged', 'name': 'Ranged'},
    {'id': 'Cavalry', 'name': 'Cavalry'},
    {'id': 'HorseArcher', 'name': 'Horse Archer'}
]);


onMounted(() => {
    cultures.value = culturesData;
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
        value: null, matchMode: FilterMatchMode.IN
    },
    'default_group': {
        value: null, matchMode: FilterMatchMode.IN
    },
    'occupation': {
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
            value: null, matchMode: FilterMatchMode.IN
        },
        'default_group': {
            value: null, matchMode: FilterMatchMode.IN
        },
        'occupation': {
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
<div id="troops-table" class="concept-table">
    <DataTable :value="troopsArr" :paginator="true" class="p-datatable-sm" showGridlines :rows="10" rowHover dataKey="id" v-model:filters="filters" filterDisplay="menu" :loading="loading" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown" :rowsPerPageOptions="[10,25,50]" responsiveLayout="scroll" :globalFilterFields="['id','name','culture','default_group','occupation']">
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
        <Column header="Culture" sortable filterField="culture" sortField="culture" :showFilterMatchModes="false" :filterMenuStyle="{'width':'14rem'}">
            <template #body="{data}">
                {{data.culture}}
            </template>
            <template #filter="{filterModel}">
                <div class="mb-3 font-bold">Select Culture</div>
                <MultiSelect v-model="filterModel.value" :options="cultures" optionLabel="name" optionValue="id" placeholder="Any" class="p-column-filter">
                    <template #option="slotProps">
                        <div class="p-multiselect-representative-option">
                            {{slotProps.option.id}}
                        </div>
                    </template>
                </MultiSelect>
            </template>
        </Column>
        <Column header="Group" sortable filterField="default_group" sortField="default_group" :showFilterMatchModes="false" :filterMenuStyle="{'width':'14rem'}">
            <template #body="{data}">
                {{data.default_group}}
            </template>
            <template #filter="{filterModel}">
                <div class="mb-3 font-bold">Select Group</div>
                <MultiSelect v-model="filterModel.value" :options="defaultGroups" optionLabel="name" optionValue="id" placeholder="Any" class="p-column-filter">
                    <template #option="slotProps">
                        <div class="p-multiselect-representative-option">
                            {{slotProps.option.id}}
                        </div>
                    </template>
                </MultiSelect>
            </template>
        </Column>
        <Column field="occupation" header="Occupation" sortable>
            <template #body="{data}">
                {{data.occupation}}
            </template>
            <template #filter="{filterModel, filterCallback}">
                <InputText type="text" v-model="filterModel.value" @input="filterCallback()" class="p-column-filter" :placeholder="`Search by occupation - `" />
            </template>
        </Column>
        <Column field="level" header="Level" sortable></Column>
        <Column field="one_handed" header="One Handed" sortable></Column>
        <Column field="two_handed" header="Two Handed" sortable></Column>
        <Column field="polearm" header="Polearm" sortable></Column>
        <Column field="bow" header="Bow" sortable></Column>
        <Column field="crossbow" header="Crossbow" sortable></Column>
        <Column field="throwing" header="Throwing" sortable></Column>
        <Column field="riding" header="Riding" sortable></Column>
        <Column field="athletics" header="Athletics" sortable></Column>
    </DataTable>
</div>
</template>
<!---------------------------------------------------->
<style lang="scss" scoped>
.global-filter {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
}

#troops-table {
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

.id-link {
    text-decoration: none;
}
</style>
