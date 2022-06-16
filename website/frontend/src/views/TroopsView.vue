<script setup>
import TroopsTable from "@/components/TroopsTable.vue";
import { ref, onMounted } from "vue";


const troops = ref(null);


onMounted(async () => {
  async function fetchData() {
    const res = await fetch(`${process.env.VUE_APP_API_URL}/troops`);
    const json_arr = await res.json();

    return json_arr;
  }

  await fetchData().then(data => troops.value = data);
})
</script>

<template>
  <div class="troops">
    <h1>Troops</h1>
    <TroopsTable :troops-arr="troops"/>
  </div>
</template>

<style scoped>

</style>