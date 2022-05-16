<script setup>
import { ref, onMounted } from "vue";


const props = defineProps({culturesArr: Array})
const loading = ref(true);
onMounted(() => {
    loading.value = false;
})
</script>

<!---------------------------------------------------->

<template>
<div class="table">
    <DataTable :value="culturesArr" :paginator="true" class="p-datatable" showGridlines :rows="10" dataKey="id" :loading="loading" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown" :rowsPerPageOptions="[10,25,50]" responsiveLayout="scroll">
        <template #empty>
            No culture found.
        </template>
        <template #loading>
            Loading culture data. Please wait.
        </template>
        <Column field="id" header="ID" sortable></Column>
        <Column field="name" header="Name" sortable></Column>
        <Column field="isMainCulture" header="Is Main Culture?" sortable></Column>
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

.table {
    background-color: var(--bluegray-900);
    border: 0;
    margin: 0 auto;
    width: fit-content;
}

.table:hover {
    background-color: unset;
}

</style>
