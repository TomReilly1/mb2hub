<script setup>
import { ref, onMounted } from "vue";


onMounted(() => {
    loading.value = false;
})


const props = defineProps({kingdomsArr: Array});
const loading = ref(true);
</script>
<!------------------------------------------------------------------->
<template>
<div id="kingdom-table">
    <DataTable :value="kingdomsArr" class="p-datatable-sm" showGridlines dataKey="id" :loading="loading" responsiveLayout="scroll">
        <template #empty>
            No Kingdoms found.
        </template>
        <template #loading>
            Loading Kingdoms data. Please wait.
        </template>
        <Column field="id" header="ID" sortable></Column>
        <Column field="name" header="Name" sortable></Column>
        <Column field="culture" header="Culture" sortable></Column>
    </DataTable>
</div>
</template>
<!------------------------------------------------------------------->
<style scoped>
.global-filter {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
}

#kingdom-table {
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
