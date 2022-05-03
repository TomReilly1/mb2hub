<script setup>

import TroopsTable from "@/components/TroopsTable.vue";

</script>

<template>
  <div class="troops">
    <h1>Troops</h1>
    <TroopsTable />
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
</style>