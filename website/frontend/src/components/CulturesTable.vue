<script setup>
import { ref, onMounted } from "vue";
import cultureData from "@/data/cultures.json";


onMounted(() => {
    cultures.value = cultureData;
    loading.value = false;
})



const cultures = ref();
const loading = ref(true);


</script>

<!---------------------------------------------------->

<template>
<div class="card">
    <DataTable :value="cultures" :paginator="true" class="p-datatable-customers" showGridlines :rows="10" dataKey="id" :loading="loading" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown" :rowsPerPageOptions="[10,25,50]" responsiveLayout="scroll">
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

.card {
    background-color: var(--bluegray-900);
    border: 0;
}

.card:hover {
    background-color: unset;
}

</style>
