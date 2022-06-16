<script setup>
import BowsTable from "@/components/BowsTable.vue";
import { ref, onMounted } from "vue";


const bows = ref(null);


onMounted(async () => {
  async function fetchData() {
    const res = await fetch(`${process.env.VUE_APP_API_URL}/bows`);
    const json_arr = await res.json();

    return json_arr;
  }
  
  await fetchData().then(data => bows.value = data);
})
</script>

<template>
  <div class="bows">
    <h1>Bows</h1>
    <BowsTable :bows-arr="bows"/>
  </div>
</template>

<style scoped>

</style>