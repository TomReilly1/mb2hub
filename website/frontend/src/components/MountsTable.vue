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
const props = defineProps({mountsArr: Array});
const cultures = ref();
const loading = ref(true);
const mountSubtypes = ref([
    {"id": "horse", "name": "horse"},
    {"id": "war_horse", "name": "war horse"}
]);
const trueOrFalse = ref([
    {"id": "True", "value": true},
    {"id": "False", "value": false}
]);


onMounted(() => {
    cultures.value = culturesData;
    loading.value = false;
})

/*
    "id": "noble_horse_battania",
    "name": "Battanian Thoroughbred",
    "culture": "battania",
    "subtype": "horse",
    "difficulty": 90,
    "is_merchandise": true,
    "maneuver": 76,
    "speed": 66,
    "charge_damage": 10,
    "health": 230
*/


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
    'subtype': {
        value: null, matchMode: FilterMatchMode.IN
    },
    'difficulty': {
        operator: FilterOperator.AND,
        constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }],
    },
    'is_merchandise': {
        value: null, matchMode: FilterMatchMode.IN
    },
    'maneuver': {
        operator: FilterOperator.AND,
        constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }],
    },
    'speed': {
        operator: FilterOperator.AND,
        constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }],
    },
    'charge_damage': {
        operator: FilterOperator.AND,
        constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }],
    },
    'health': {
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
        'subtype': {
            value: null, matchMode: FilterMatchMode.IN
        },
        'difficulty': {
            operator: FilterOperator.AND,
            constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }],
        },
        'is_merchandise': {
            value: null, matchMode: FilterMatchMode.IN
        },
        'maneuver': {
            operator: FilterOperator.AND,
            constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }],
        },
        'speed': {
            operator: FilterOperator.AND,
            constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }],
        },
        'charge_damage': {
            operator: FilterOperator.AND,
            constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }],
        },
        'health': {
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
<div id="mounts-table" class="concept-table">
    <DataTable :value="mountsArr" :paginator="true" class="p-datatable-sm" showGridlines :rows="10" rowHover dataKey="id" v-model:filters="filters" filterDisplay="menu" :loading="loading" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown" :rowsPerPageOptions="[10,25,50]" responsiveLayout="scroll" :globalFilterFields="['id','name','culture','type']">
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
                <div class="mb-3 font-bold">Culture Selector</div>
                <MultiSelect v-model="filterModel.value" :options="cultures" optionLabel="name" optionValue="id" placeholder="Any" class="p-column-filter">
                    <template #option="slotProps">
                        <div class="p-multiselect-representative-option">
                            {{slotProps.option.id}}
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
                <div class="mb-3 font-bold">Subtype Selector</div>
                <MultiSelect v-model="filterModel.value" :options="mountSubtypes" optionLabel="name" optionValue="id" placeholder="Any" class="p-column-filter">
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
        <Column header="Is Merchandise?" sortable filterField="is_merchandise" sortField="is_merchandise" :showFilterMatchModes="false" :filterMenuStyle="{'width':'14rem'}" >
            <template #body="{data}">
                {{data.is_merchandise}}
            </template>
            <template #filter="{filterModel}">
                <div class="mb-3 font-bold">True/False</div>
                <MultiSelect v-model="filterModel.value" :options="trueOrFalse" optionLabel="id" optionValue="value" placeholder="Any" class="p-column-filter">
                    <template #option="slotProps">
                        <div class="p-multiselect-representative-option">
                            {{slotProps.option.value}}
                        </div>
                    </template>
                </MultiSelect>
            </template>
        </Column>
        <Column field="maneuver" header="Maneuver" sortable dataType="numeric">
            <template #body="{data}">
                {{data.maneuver}}
            </template>
            <template #filter="{filterModel}">
                <InputNumber v-model="filterModel.value"/>
            </template>
        </Column>
        <Column field="speed" header="Speed" sortable dataType="numeric">
            <template #body="{data}">
                {{data.speed}}
            </template>
            <template #filter="{filterModel}">
                <InputNumber v-model="filterModel.value"/>
            </template>
        </Column>
        <Column field="charge_damage" header="Charge Damage" sortable dataType="numeric">
            <template #body="{data}">
                {{data.charge_damage}}
            </template>
            <template #filter="{filterModel}">
                <InputNumber v-model="filterModel.value"/>
            </template>
        </Column>
        <Column field="health" header="Health" sortable dataType="numeric">
            <template #body="{data}">
                {{data.health}}
            </template>
            <template #filter="{filterModel}">
                <InputNumber v-model="filterModel.value"/>
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

#mounts-table {
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
