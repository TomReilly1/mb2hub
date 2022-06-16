<script setup>
import { ref, onMounted } from "vue";
import culturesData from "@/data/cultures_list.json";
import sexesData from "@/data/sexes_list.json";
import { FilterMatchMode, FilterOperator } from 'primevue/api';
import MultiSelect from 'primevue/multiselect';
import InputText from 'primevue/inputtext';
import InputNumber from 'primevue/inputnumber';

onMounted(() => {
    cultures.value = culturesData;
    sexes.value = sexesData;

    loading.value = false;
})

const props = defineProps({lordsArr: Array});
const cultures = ref();
const sexes = ref();
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
        value: null, matchMode: FilterMatchMode.IN
    },
    'age': {
        operator: FilterOperator.AND,
        constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }],
    },
    'sex': {
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
        'culture': {
            value: null, matchMode: FilterMatchMode.IN
        },
        'age': {
            operator: FilterOperator.AND,
            constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }],
        },
        'sex': {
            value: null, matchMode: FilterMatchMode.IN 
        }
    }
}


const clearFilters = () => {
    initFilters();
}


</script>

<!---------------------------------------------------->

<template>
<div id="lords-table">
    <DataTable :value="lordsArr" :paginator="true" class="p-datatable-sm" showGridlines :rows="10" rowHover dataKey="id" v-model:filters="filters" filterDisplay="menu" :loading="loading" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown" :rowsPerPageOptions="[10,25,50]" responsiveLayout="scroll" :globalFilterFields="['id','name', 'culture', 'age', 'type']">
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
            No lords found.
        </template>
        <template #loading>
            Loading lords data. Please wait.
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
        <Column header="Culture" sortable filterField="culture" sortField="culture" :showFilterMatchModes="false" :filterMenuStyle="{'width':'14rem'}">
            <template #body="{data}">
                {{data.culture}}
            </template>
            <template #filter="{filterModel}">
                <div class="mb-3 font-bold">Culture Picker</div>
                <MultiSelect v-model="filterModel.value" :options="cultures" optionLabel="name" optionValue="id" placeholder="Any" class="p-column-filter">
                    <template #option="slotProps">
                        <div class="p-multiselect-representative-option">
                            {{slotProps.option.id}}
                        </div>
                    </template>
                </MultiSelect>
            </template>
        </Column>
        <Column field="default_group" header="Group" sortable></Column>
        <Column field="age" header="Age" sortable dataType="numeric">
            <template #body="{data}">
                {{data.age}}
            </template>
            <template #filter="{filterModel}">
                <InputNumber v-model="filterModel.value"/>
            </template>
        </Column>
        <Column header="Male/Female" sortable filterField="sex" sortField="sex" :showFilterMatchModes="false" :filterMenuStyle="{'width':'14rem'}">
            <template #body="{data}">
                {{data.sex}}
            </template>
            <template #filter="{filterModel}">
                <div class="mb-3 font-bold">Select Sex:</div>
                <MultiSelect v-model="filterModel.value" :options="sexes" optionLabel="name" optionValue="id" placeholder="Any" class="p-column-filter">
                    <template #option="slotProps">
                        <div class="p-multiselect-representative-option">
                            {{slotProps.option.id}}
                        </div>
                    </template>
                </MultiSelect>
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

#lords-table {
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
