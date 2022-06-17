<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from 'vue-router';

import { FilterMatchMode, FilterOperator } from 'primevue/api';
import MultiSelect from 'primevue/multiselect';
import InputText from 'primevue/inputtext';
import InputNumber from 'primevue/inputnumber';

import kingdomsData from "@/data/kingdoms_list.json"
import culturesData from "@/data/cultures_list.json";



const route = useRoute();
const props = defineProps({clansArr: Array});
const loading = ref(true);
const kingdoms = ref();
const cultures = ref();
const trueOrFalse = ref([
    {"id": true, "name": "True"},
    {"id": false, "name": "False"}
]);



onMounted(() => {
    kingdoms.value = kingdomsData;
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
    'tier': {
        operator: FilterOperator.AND,
        constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }],
    },
    'owner': {
        operator: FilterOperator.AND,
        constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }]
    },
    'culture': {
        value: null, matchMode: FilterMatchMode.IN
    },
    'kingdom': {
        value: null, matchMode: FilterMatchMode.IN
    },
    'is_ruling_clan': {
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
        'tier': {
            operator: FilterOperator.AND,
            constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }],
        },
        'owner': {
            operator: FilterOperator.AND,
            constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }]
        },
        'culture': {
            value: null, matchMode: FilterMatchMode.IN
        },
        'kingdom': {
            value: null, matchMode: FilterMatchMode.IN
        },
        'is_ruling_clan': {
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
<div id="clans-table" class="concept-table">
    <DataTable :value="clansArr" :paginator="true" class="p-datatable-sm" showGridlines :rows="10" rowHover dataKey="id" v-model:filters="filters" filterDisplay="menu" :loading="loading" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown" :rowsPerPageOptions="[10,25,50]" responsiveLayout="scroll" :globalFilterFields="['id','name','tier','owner','kingdom','culture','type']">
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
            No clans found.
        </template>
        <template #loading>
            Loading clans data. Please wait.
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
        <Column field="tier" header="Tier" sortable dataType="numeric">
            <template #body="{data}">
                {{data.tier}}
            </template>
            <template #filter="{filterModel}">
                <InputNumber v-model="filterModel.value"/>
            </template>
        </Column>
        <Column field="owner" header="Head of Clan" sortable>
            <template #body="{data}">
                {{data.owner}}
            </template>
            <template #filter="{filterModel, filterCallback}">
                <InputText type="text" v-model="filterModel.value" @input="filterCallback()" class="p-column-filter" :placeholder="`Search by type - `" />
            </template>
        </Column>
        <Column header="Kingdom" sortable filterField="kingdom" sortField="kingdom" :showFilterMatchModes="false" :filterMenuStyle="{'width':'14rem'}">
            <template #body="{data}">
                {{data.kingdom}}
            </template>
            <template #filter="{filterModel}">
                <div class="mb-3 font-bold">Select Kingdom:</div>
                <MultiSelect v-model="filterModel.value" :options="kingdoms" optionLabel="id" optionValue="name" placeholder="Any" class="p-column-filter">
                    <template #option="slotProps">
                        <div class="p-multiselect-representative-option">
                            {{slotProps.option.name}}
                        </div>
                    </template>
                </MultiSelect>
            </template>
        </Column>
        <Column header="Culture" sortable filterField="culture" sortField="culture" :showFilterMatchModes="false" :filterMenuStyle="{'width':'14rem'}">
            <template #body="{data}">
                {{data.culture}}
            </template>
            <template #filter="{filterModel}">
                <div class="mb-3 font-bold">Select Culture:</div>
                <MultiSelect v-model="filterModel.value" :options="cultures" optionLabel="name" optionValue="id" placeholder="Any" class="p-column-filter">
                    <template #option="slotProps">
                        <div class="p-multiselect-representative-option">
                            {{slotProps.option.id}}
                        </div>
                    </template>
                </MultiSelect>
            </template>
        </Column>
        <Column header="Is Ruling Clan?" sortable filterField="is_ruling_clan" sortField="is_ruling_clan" :showFilterMatchModes="false" :filterMenuStyle="{'width':'14rem'}">
            <template #body="{data}">
                {{data.is_ruling_clan}}
            </template>
            <template #filter="{filterModel}">
                <div class="mb-3 font-bold">True or False:</div>
                <MultiSelect v-model="filterModel.value" :options="trueOrFalse" optionLabel="name" optionValue="id" placeholder="Any" class="p-column-filter">
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

#clans-table {
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
