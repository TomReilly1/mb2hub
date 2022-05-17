<script setup>

import CulturesTable from "@/components/CulturesTable.vue";
import DescriptionCard from "@/components/DescriptionCard.vue";
import cultureData from "@/data/cultures.json";
import { ref, onMounted } from "vue";
import Dropdown from 'primevue/dropdown';



onMounted(() => {
  cultures.value = cultureData;
  console.log(typeof cultures.value);
})


const cultures = ref();
const selectedView = ref();
const cities = ref([
  {name: 'Table', code: 'table'},
  {name: 'Cards', code: 'cards'},
]);


</script>

<template>
  <div class="cultures">
    <h1>Cultures</h1>
    <div class="select view">
      <span>Select view:</span>
      <Dropdown v-model="selectedView" :options="cities" optionLabel="name" optionValue="code" placeholder="Table"/>
    </div>
    <CulturesTable :cultures-arr="cultures"/>
    <DescriptionCard :objects="cultures" />
  </div>
</template>

<style scoped>
  h1 {
    font-size: 3.5rem;
    text-decoration: underline;
    margin: 0;
    border: 0;
    padding: 2rem 0;
  }

  .select {
    display: flex;
    flex-direction: column;
    margin: 0 auto 1rem;
    width: fit-content;
  }

</style>