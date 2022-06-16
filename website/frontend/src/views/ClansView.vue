<script setup>
import ClansTable from "@/components/ClansTable.vue";
import { ref, onMounted } from "vue";

const clans = ref(null);

onMounted(async () => {
  async function fetchData() {
    const res = await fetch(`${process.env.VUE_APP_API_URL}/clans`);
    const json_arr = await res.json();

    return json_arr;
  }

  await fetchData().then(data => clans.value = data);
})
</script>

<template>
  <div class="clans">
    <h1>Clans</h1>
    <ClansTable :clans-arr="clans"/>
  </div>
</template>

<style scoped>

</style>