<script setup>
import LordsTable from "@/components/LordsTable.vue";
import { ref, onMounted } from "vue";


const lords = ref(null);


onMounted(async () => {
  async function fetchData() {
    const res = await fetch(`${process.env.VUE_APP_API_URL}/lords`);
    const json_arr = await res.json();

    return json_arr;
  }

  await fetchData().then(data => lords.value = data);
})
</script>

<template>
  <div class="lords">
    <h1>Lords</h1>
    <LordsTable :lords-arr="lords"/>
  </div>
</template>

<style scoped>

</style>