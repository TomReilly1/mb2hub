<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from 'vue-router';

import Button from "primevue/button/sfc";
import DataTable from 'primevue/datatable/sfc';
import Column from 'primevue/column/sfc';
import { FilterMatchMode, FilterOperator } from 'primevue/api';
import MultiSelect from 'primevue/multiselect/sfc';
import InputText from 'primevue/inputtext/sfc';
import InputNumber from 'primevue/inputnumber/sfc';

import culturesData from "@/data/cultures_list.json";



const route = useRoute();
const props = defineProps({bowsArr: Array});
const cultures = ref();
const loading = ref(true);


onMounted(() => {
    cultures.value = culturesData;
    loading.value = false;
})


const bowTypes = ref([
    {"id": "bow", "name": "Bow"},
    {"id": "crossbow", "name": "Crossbow"}
]);

const bowSubTypes = ref([
    {"id": "bow", "name": "Bow"},
    {"id": "crossbow", "name": "Crossbow"},
    {"id": "long_bow", "name": "Long Bow"},
    {"id": "crossbow_fast", "name": "Fast Crossbow"}
]);


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
    'type': {
        value: null, matchMode: FilterMatchMode.IN
    },
    'subtype': {
        value: null, matchMode: FilterMatchMode.IN
    },
    'difficulty': {
        operator: FilterOperator.AND,
        constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }],
    },
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
        'type': {
            value: null, matchMode: FilterMatchMode.IN
        },
        'subtype': {
            value: null, matchMode: FilterMatchMode.IN
        },
        'difficulty': {
            operator: FilterOperator.AND,
            constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }],
        },
    }
}

const clearFilters = () => {
    initFilters();
}
</script>
<!---------------------------------------------------->
<template>
<div id="bows-table" class="concept-table">
    <DataTable :value="bowsArr" :paginator="true" class="p-datatable-sm" showGridlines :rows="10" rowHover dataKey="id" v-model:filters="filters" filterDisplay="menu" :loading="loading" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown" :rowsPerPageOptions="[10,25,50]" responsiveLayout="scroll" :globalFilterFields="['id','name','culture','type']">
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
            No bows data found.
        </template>
        <template #loading>
            Loading bows data. Please wait.
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
        <Column header="Culture" sortable filterField="culture" sortField="culture" :showFilterMatchModes="false" :filterMenuStyle="{'width':'14rem'}" >
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
        <Column field="weight" header="Weight" sortable></Column>
        <Column header="Type" sortable filterField="type" sortField="type" :showFilterMatchModes="false" :filterMenuStyle="{'width':'14rem'}">
            <template #body="{data}">
                {{data.type}}
            </template>
            <template #filter="{filterModel}">
                <div class="mb-3 font-bold">Select Type:</div>
                <MultiSelect v-model="filterModel.value" :options="bowTypes" optionLabel="name" optionValue="name" placeholder="Any" class="p-column-filter">
                    <template #option="slotProps">
                        <div class="p-multiselect-representative-option">
                            {{slotProps.option.name}}
                        </div>
                    </template>
                </MultiSelect>
            </template>
        </Column>
        <Column header="Subtype" sortable filterField="subtype" sortField="subtype" :showFilterMatchModes="false" :filterMenuStyle="{'width':'14rem'}">
            <template #body="{data}">
                {{data.subtype}}
            </template>
            <template #filter="{filterModel}">
                <div class="mb-3 font-bold">Select Subtype:</div>
                <MultiSelect v-model="filterModel.value" :options="bowSubTypes" optionLabel="name" optionValue="id" placeholder="Any" class="p-column-filter">
                    <template #option="slotProps">
                        <div class="p-multiselect-representative-option">
                            {{slotProps.option.id}}
                        </div>
                    </template>
                </MultiSelect>
            </template>
        </Column>
        <Column field="difficulty" header="Difficulty" sortable dataType="numeric">
            <template #body="{data}">
                {{data.difficulty}}
            </template>
            <template #filter="{filterModel}">
                <InputNumber v-model="filterModel.value"/>
            </template>
        </Column>
        <Column field="damage" header="Damage" sortable></Column>
        <Column field="speed_rating" header="Speed Rating" sortable></Column>
        <Column field="missile_speed" header="Missile Speed" sortable></Column>
        <Column field="accuracy" header="Accuracy" sortable></Column>
        <Column field="fire_on_mount" header="Fire on Mount?" sortable></Column>
        <Column field="reload_on_mount" header="Reload on Mount?" sortable></Column>
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

#bows-table {
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
