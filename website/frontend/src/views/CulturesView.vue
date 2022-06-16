<script setup>
import CulturesTable from "@/components/CulturesTable.vue";
// import DescriptionCard from "@/components/DescriptionCard.vue";
// import cultureData from "@/data/cultures.json";
import { ref, onMounted, onUpdated } from "vue";
// import Dropdown from 'primevue/dropdown';
import { useRoute } from 'vue-router';



const cultures = ref(null);

onMounted(async () => {
  async function fetchData() {
    const res = await fetch(`${process.env.VUE_APP_API_URL}/cultures`);
    const json_arr = await res.json();

    return json_arr;
  }

  await fetchData().then(data => cultures.value = data);
})

onUpdated(() => {
  cultureCardId.value = route.params.id;
  console.log(cultureCardId.value);
})



const selectedView = ref('table');
const views = ref([
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
    <CulturesTable :cultures-arr="cultures"/>

    <!-- <div class="select view">
      <span>Select view:</span>
      <Dropdown v-model="selectedView" :options="views" optionLabel="name" optionValue="code" placeholder="Table"/>
    </div>
    <div v-show="selectedView === 'table'">
      <CulturesTable :cultures-arr="cultures"/>
    </div>
    <div v-show="selectedView === 'cards'">
      <DescriptionCard :objects="cultures" />
    </div> -->
  </section>
  <section v-else>
    <router-view />
  </section>
</template>


<style scoped>
  .select {
    display: flex;
    flex-direction: column;
    margin: 0 auto 1rem;
    width: fit-content;
  }
</style>