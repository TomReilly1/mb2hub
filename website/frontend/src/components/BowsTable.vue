<script setup>
import { ref, onMounted } from "vue";
import bowsData from "@/data/bows_and_crossbows.json";
import { FilterMatchMode, FilterOperator } from 'primevue/api';
import InputText from 'primevue/inputtext';



onMounted(() => {
    bows.value = bowsData;
    loading.value = false;
})



const bows = ref();
const loading = ref(true);
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


const clearFilters = () => {
    initFilters();
}
        
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

</script>

<!---------------------------------------------------->

<template>
<div class="card">
    <DataTable :value="bows" :paginator="true" class="p-datatable-customers" showGridlines :rows="10" dataKey="id" v-model:filters="filters" filterDisplay="menu" :loading="loading" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown" :rowsPerPageOptions="[10,25,50]" responsiveLayout="scroll" :globalFilterFields="['id','name','culture','type']">
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
            No bows found.
        </template>
        <template #loading>
            Loading bows data. Please wait.
        </template>
        <Column field="id" header="ID" sortable>
            <template #body="{data}">
                {{data.id}}
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
        <Column field="subtype" header="Subtype" sortable>
            <template #body="{data}">
                {{data.subtype}}
            </template>
            <template #filter="{filterModel, filterCallback}">
                <InputText type="text" v-model="filterModel.value" @input="filterCallback()" class="p-column-filter" :placeholder="`Search by subtype - `" />
            </template>
        </Column>
        <Column field="difficulty" header="Difficulty" sortable></Column>
        <Column field="speed_rating" header="Speed Rating" sortable></Column>
        <Column field="missile_speed" header="Missile Speed" sortable></Column>
        <Column field="accuracy" header="Accuracy" sortable></Column>
        <Column field="fire_on_mount" header="Can Fire on Mount (t/f)" sortable></Column>
        <Column field="reload_on_mount" header="Can Reload on Mount (t/f)" sortable></Column>
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

.card {
    background-color: var(--bluegray-900);
    border: 0;
}

.card:hover {
    background-color: unset;
}

</style>


