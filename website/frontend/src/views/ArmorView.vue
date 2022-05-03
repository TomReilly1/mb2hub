<script setup>

import ArmorTable from "@/components/ArmorTable.vue";
import ArmorHighestCard from "@/components/ArmorHighestCard.vue";

</script>

<template>
  <div class="armor">
    <h1>Armor</h1>
    <ArmorTable />
    <!-- <ArmorHighestCard /> -->
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