<script setup>
import { ref, onMounted } from "vue";


const props = defineProps({culturesArr: Array})
const loading = ref(true);
onMounted(() => {
    loading.value = false;
})

</script>

<!------------------------------------------------------------------------------------------------->

<template>
<div class="culture-table">
    <DataTable :value="culturesArr" :paginator="true" class="p-datatable" showGridlines :rows="10" dataKey="id" :loading="loading" paginatorTemplate="FirstPageLink PrevPageLink PageLinks NextPageLink LastPageLink CurrentPageReport RowsPerPageDropdown" :rowsPerPageOptions="[10,25,50]" responsiveLayout="scroll">
        <template #empty>
            No culture found.
        </template>
        <template #loading>
            Loading culture data. Please wait.
        </template>
        <!-- <Column field="id" header="ID" sortable></Column> -->
        <Column field="id" header="ID" class="id-field" sortable>
            <template #body="{data}">
                <router-link :to="{name: 'culturescard', params: {id: data.id}}" class="nav-link">
                    {{data.id}}
                </router-link>
            </template>
        </Column>
        <Column field="name" header="Name" sortable></Column>
        <Column field="isMainCulture" header="Is Main Culture?" sortable></Column>
    </DataTable>
</div>
</template>

<!-- const routes = [
  {
    path: '/user/:username',
    name: 'user',
    component: User
  }
]

To link to a named route, you can pass an object to the router-link component's to prop:

<router-link :to="{ name: 'user', params: { username: 'erina' }}">
  User
</router-link>
 -->



<!---------------------------------------------------->

<style scoped>

.global-filter {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
}

.culture-table {
    background-color: var(--bluegray-900);
    border: 0;
    margin: 0 auto;
    width: fit-content;
}

.culture-table:hover {
    background-color: unset;
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
