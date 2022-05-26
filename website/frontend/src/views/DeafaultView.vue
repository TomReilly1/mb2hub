<script setup>
import CulturesTable from "@/components/CulturesTable.vue";
import DescriptionCard from "@/components/DescriptionCard.vue";
import cultureData from `@/data/${endpoint}.json`;
import { ref, onMounted, onUpdated } from "vue";
import Dropdown from 'primevue/dropdown';
import { useRoute } from 'vue-router';



onMounted(() => {
  endpoint.value = cultureData;
  console.log(typeof endpoint.value);
})

onUpdated(() => {
  cultureCardId.value = route.params.id;
  console.log(cultureCardId.value);
})

const endpoint = ref();
const selectedView = ref('table');
const cities = ref([
  {name: 'Table', code: 'table'},
  {name: 'Cards', code: 'cards'},
]);


const cultureCardId = ref();
const route = useRoute();

cultureCardId.value = route.params.id;

</script>

<template>
  <section class="heading">
    <h1>Cultures</h1>
  </section>
  <section v-if="cultureCardId === undefined">

    

    <div class="select view">
      <span>Select view:</span>
      <Dropdown v-model="selectedView" :options="cities" optionLabel="name" optionValue="code" placeholder="Table"/>
    </div>
    <div v-show="selectedView === 'table'">
      <CulturesTable :endpoint-arr="endpoint"/>
    </div>
    <div v-show="selectedView === 'cards'">
      <DescriptionCard :objects="endpoint" />
    </div>

  </section>
  <section v-else>
    <router-view />
  </section>
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