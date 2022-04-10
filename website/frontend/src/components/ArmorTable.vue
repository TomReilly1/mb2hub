<script setup>
import { ref, onMounted } from "vue";
import TableService from "@/services/TableService";


const armor = ref()
const tableService = ref(new TableService())
const columns = ref([
  {field: "id", header: "ID"},
  {field: "name", header: "Name"},
  {field: "culture", header: "Culture"},
  {field: "weight", header: "Weight"},
  {field: "type", header: "Type"},
  {field: "head_ar", header: "Head AR"},
  {field: "body_ar", header: "Body AR"},
  {field: "arm_ar", header: "Arm AR"},
  {field: "leg_ar", header: "Leg AR"}
])


onMounted(() => {
  tableService.value.getArmorData()
  .then(data => armor.value = data)
})




</script>

<!---------------------------------------------------->

<template>
<div class="card">
    <DataTable :value="armor" sortMode="multiple" removableSort responsiveLayout="scroll">
        <Column field="id" header="id" :sortable="true"></Column>
        <Column field="name" header="Name" :sortable="true"></Column>
        <Column field="culture" header="Culture" filterField="culture" :showFilterMenu="false" :sortable="true"></Column>
        <Column field="weight" header="Weight" :sortable="true"></Column>
        <Column field="type" header="Type" :sortable="true"></Column>
        <Column field="head_ar" header="head_ar" :sortable="true"></Column>
        <Column field="body_ar" header="body_ar" :sortable="true"></Column>
        <Column field="arm_ar" header="arm_ar" :sortable="true"></Column>
        <Column field="leg_ar" header="leg_ar" :sortable="true"></Column>
    </DataTable>
</div>
</template>

<!---------------------------------------------------->

<style scoped>

</style>