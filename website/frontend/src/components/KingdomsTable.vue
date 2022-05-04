<script setup>
import { ref, onMounted } from "vue";
import kingdomData from "@/data/kingdoms.json";


onMounted(() => {
    kingdoms.value = kingdomData;
    loading.value = false;
})



const kingdoms = ref();
const loading = ref(true);


</script>

<!---------------------------------------------------->

<template>
<div class="card">
    <DataTable :value="kingdoms" :paginator="true" class="p-datatable-customers" showGridlines :rows="10" dataKey="id" :loading="loading" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown" :rowsPerPageOptions="[10,25,50]" responsiveLayout="scroll">
        <template #empty>
            No bows found.
        </template>
        <template #loading>
            Loading bows data. Please wait.
        </template>
        <Column field="id" header="ID" sortable></Column>
        <Column field="name" header="Name" sortable></Column>
        <Column field="culture" header="Culture" sortable></Column>
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
