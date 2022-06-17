<script setup>
import ArmorTable from "@/components/ArmorTable.vue";
import BowsTable from "@/components/BowsTable.vue";
import ClansTable from "@/components/ClansTable.vue";
import CulturesTable from "@/components/CulturesTable.vue";
import KingdomsTable from "@/components/KingdomsTable.vue";
import LordsTable from "@/components/LordsTable.vue";
import TroopsTable from "@/components/TroopsTable.vue";

import { ref, onMounted, onUpdated, watch } from "vue";
import { useRoute } from 'vue-router';


const conceptData = ref(null);
const route = useRoute();


async function fetchData(conc) {
    const res = await fetch(`${process.env.VUE_APP_API_URL}/${conc}`);
    const json_arr = await res.json();
    
    return json_arr;
}


onMounted(async () => {
    await fetchData(route.params.concept).then(data => conceptData.value = data);
    
    console.log(conceptData.value);
})

onUpdated(async () => {
    console.log(route.params.concept);
    console.log(route.params.id);
})


watch(route, async () => {
    console.log("CHANGED ROUTE");
    
    conceptData.value = null;
    if (route.params.concept !== undefined && route.params.id === undefined) {
        console.log("flag");
        await fetchData(route.params.concept).then(data => conceptData.value = data);
    }
})
</script>
<!------------------------------------------------------------------------------------->
<template>
    <section class="heading">
        <h1>{{route.params.concept}}</h1>
    </section>
    <section v-if="route.params.id === undefined">
        <ArmorTable v-if="route.params.concept === 'armors'" :armors-arr="conceptData"/>
        <BowsTable v-if="route.params.concept === 'bows'" :bows-arr="conceptData"/>
        <ClansTable v-if="route.params.concept === 'clans'" :clans-arr="conceptData"/>
        <CulturesTable v-else-if="route.params.concept === 'cultures'" :cultures-arr="conceptData"/>
        <KingdomsTable v-else-if="route.params.concept === 'kingdoms'" :kingdoms-arr="conceptData"/>
        <LordsTable v-else-if="route.params.concept === 'lords'" :lords-arr="conceptData"/>
        <TroopsTable v-else-if="route.params.concept === 'troops'" :troops-arr="conceptData"/>
    </section>
    <section v-else>
        <router-view />
    </section>
</template>
<!------------------------------------------------------------------------------------->
<style>
h1 {
    text-transform: capitalize;
}

.id-link {
    text-decoration: none;
}
</style>
