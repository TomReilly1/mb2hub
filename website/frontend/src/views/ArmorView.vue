<script setup>
import { ref, onMounted } from "vue";
import ArmorTable from "@/components/ArmorTable.vue";


const armors = ref(null);

onMounted(async () => {
  async function fetchData() {
    const res = await fetch(`${process.env.VUE_APP_API_URL}/armors`);
    const json_arr = await res.json();

    return json_arr;
  }

  await fetchData().then(data => armors.value = data);
})
</script>
<!------------------------------------------------------------------------------------------------->
<template>
  <div class="armor">
    <h1>Armor</h1>
    <ArmorTable :armors-arr="armors"/>
  </div>
</template>
<!------------------------------------------------------------------------------------------------->
<style scoped>

</style>