<script setup>
import KingdomsTable from "@/components/KingdomsTable.vue";
import { ref, onMounted } from "vue";


const kingdoms = ref(null);


onMounted(async () => {
  async function fetchData() {
    const res = await fetch(`${process.env.VUE_APP_API_URL}/kingdoms`);
    const json_arr = await res.json();

    return json_arr;
  }

  await fetchData().then(data => kingdoms.value = data);
})
</script>

<template>
  <div class="kingdoms">
    <h1>Kingdoms</h1>
    <KingdomsTable :kingdoms-arr="kingdoms"/>
  </div>
</template>

<style scoped>

</style>