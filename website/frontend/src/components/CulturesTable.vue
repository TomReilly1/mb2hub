<script setup>
import { ref, onMounted } from "vue"
import { useRoute } from 'vue-router'

import DataTable from 'primevue/datatable/sfc'
import Column from 'primevue/column/sfc'
import MultiSelect from 'primevue/multiselect/sfc';

const route = useRoute()
const props = defineProps({culturesArr: Array})
const loading = ref(true)


onMounted(() => {
    loading.value = false
})


const columns = ref ([
    {field: 'id', header: 'ID'},
    {field: 'name', header: 'Name'},
    {field: 'is_main_culture', header: 'Is Main Culture?'}
])

const selectedColumns = ref(columns.value)

const onToggle = (val) => {
    selectedColumns.value = columns.value.filter(col => val.includes(col))
}


</script>
<!--------------------------------------------------------------------------------->
<template>
<div id="cultures-table" class="concept-table">
    <DataTable :value="culturesArr" class="p-datatable-sm" showGridlines rowHover dataKey="id" :loading="loading" responsiveLayout="scroll">
        <template #header>
            <div style="text-align:left">
                <MultiSelect :modelValue="selectedColumns" :options="columns" optionLabel="header" @update:modelValue="onToggle"
                    placeholder="Select Columns" style="width: 20em; color: lightskyblue;"/>
            </div>
        </template>
        <template #empty>
            No cultures data found.
        </template>
        <template #loading>
            Loading cultures data. Please wait.
        </template>
        <Column v-if="selectedColumns.find(o => o.field === 'id')" field="id" header="ID" sortable>
            <template #body="{data}">
                <router-link :to="{name: 'cardview', params: {concept: route.params.concept, id: data.id}}" class="nav-link">
                    {{data.id}}
                </router-link>
            </template>
        </Column>
        <Column v-if="selectedColumns.find(o => o.field === 'name')" field="name" header="Name" sortable></Column>
        <Column v-if="selectedColumns.find(o => o.field === 'is_main_culture')" field="is_main_culture" header="Is Main Culture?" sortable></Column>
    </DataTable>
</div>
</template>
<!--------------------------------------------------------------------------------->
<style scoped>
.global-filter {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
}

#cultures-table {
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
