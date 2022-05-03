<script setup>
import { ref, onMounted } from "vue";
import TableService from "@/services/TableService";
import { FilterMatchMode, FilterOperator } from 'primevue/api';
import InputText from 'primevue/inputtext';



onMounted(() => {
    tableService.value.getNpcsData()
    .then(data => {
        troops.value = data;
        loading.value = false;
        console.log(data);
        console.log(troops.value)
    });
})

// tableService.value.getArmorData()
// .then(data => {
//     armor.value = data;
//     loading.value = false;
//     console.log(data);
//     console.log(armor.value)
// });


const troops = ref();
const tableService = ref(new TableService());
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
    'default_group': {
        operator: FilterOperator.AND,
        constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }]
    },
    'occupation': {
        operator: FilterOperator.AND,
        constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }]
    }
});

const loading = ref(true);

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
        'default_group': {
            operator: FilterOperator.AND,
            constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }]
        },
        'occupation': {
            operator: FilterOperator.AND,
            constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }]
        }
    }
}

</script>

<!---------------------------------------------------->

<template>
<div class="card">
    <DataTable :value="troops" :paginator="true" class="p-datatable-customers" showGridlines :rows="10" dataKey="id" v-model:filters="filters" filterDisplay="menu" :loading="loading"   paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown" :rowsPerPageOptions="[10,25,50]" responsiveLayout="scroll" :globalFilterFields="['id','name','culture','default_group','occupation']">
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
        <Column field="default_group" header="Group" sortable>
            <template #body="{data}">
                {{data.default_group}}
            </template>
            <template #filter="{filterModel, filterCallback}">
                <InputText type="text" v-model="filterModel.value" @input="filterCallback()" class="p-column-filter" :placeholder="`Search by Group - `" />
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


