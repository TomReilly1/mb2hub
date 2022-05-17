<script setup>

import KingdomsTable from "@/components/KingdomsTable.vue";

</script>

<template>
  <div class="kingdoms">
    <h1>Kingdoms</h1>
    <KingdomsTable />
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