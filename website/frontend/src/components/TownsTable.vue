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
const props = defineProps({townsArr: Array});
const loading = ref(true);
const cultures = ref();
const wallLevels = ref([
    {'level': 1},
    {'level': 2},
    {'level': 3}
]);


onMounted(() => {
    cultures.value = culturesData;

    loading.value = false;
})


function formatBoundVillage(village) {
    if (village === null || village === undefined) {
        return 'N/A';
    } else {
        //const res = await fetch(`${process.env.VUE_APP_API_URL}/${route.params.concept}/${village}`);
        //const json_arr = await res.json();
        //console.log(json_arr);
        return village;
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
    'owner_name': {
        operator: FilterOperator.AND,
        constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }]
    },
    'culture': {
        value: null, matchMode: FilterMatchMode.IN
    },
    'prosperity': {
        operator: FilterOperator.AND,
        constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }],
    },
    'wall_level': {
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
        'owner_name': {
            operator: FilterOperator.AND,
            constraints: [{ value: null, matchMode: FilterMatchMode.STARTS_WITH }]
        },
        'culture': {
            value: null, matchMode: FilterMatchMode.IN
        },
        'prosperity': {
            operator: FilterOperator.AND,
            constraints: [{ value: null, matchMode: FilterMatchMode.EQUALS }],
        },
        'wall_level': {
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
<div id="towns-table" class="concept-table">
    <DataTable :value="townsArr" :paginator="true" class="p-datatable-sm" showGridlines :rows="10" rowHover dataKey="id" v-model:filters="filters" filterDisplay="menu" :loading="loading" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown" :rowsPerPageOptions="[10,25,50]" responsiveLayout="scroll" :globalFilterFields="['id','name','owner_name','culture']">
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
        <Column field="owner_name" header="Owner Clan" sortable>
            <template #body="{data}">
                {{data.owner_name}}
            </template>
            <template #filter="{filterModel, filterCallback}">
                <InputText type="text" v-model="filterModel.value" @input="filterCallback()" class="p-column-filter" :placeholder="`Search by Owner - `"/>
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
        <Column field="x_position" header="X-Position" sortable></Column>
        <Column field="y_position" header="Y-Position" sortable></Column>
        <Column field="prosperity" header="Prosperity" dataType="numeric" sortable>
            <template #body="{data}">
                {{data.prosperity}}
            </template>
            <template #filter="{filterModel}">
                <InputNumber v-model="filterModel.value"/>
            </template>
        </Column>
        <Column header="Wall Level" sortable filterField="wall_level" sortField="wall_level" :showFilterMatchModes="false" :filterMenuStyle="{'width':'14rem'}">
            <template #body="{data}">
                {{data.wall_level}}
            </template>
            <template #filter="{filterModel}">
                <div class="mb-3 font-bold">Culture Picker</div>
                <MultiSelect v-model="filterModel.value" :options="wallLevels" optionLabel="level" optionValue="level" placeholder="Any" class="p-column-filter">
                    <template #option="slotProps">
                        <div class="p-multiselect-representative-option">
                            {{slotProps.option.level}}
                        </div>
                    </template>
                </MultiSelect>
            </template>
        </Column>
        <Column field="bound_village_1" header="Bound Village 1"></Column>
        <Column field="bound_village_2" header="Bound Village 2"></Column>
        <Column field="bound_village_3" header="Bound Village 3">
            <template #body="{data}">
                {{formatBoundVillage(data.bound_village_3)}}
            </template>
        </Column>
        <Column field="bound_village_4" header="Bound Village 4">
            <template #body="{data}">
                {{formatBoundVillage(data.bound_village_4)}}
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

#towns-table {
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
