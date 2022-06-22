<script setup>
import { ref, onMounted, watch } from "vue";
import { useRoute } from 'vue-router';

import ArmorsTable from "@/components/ArmorsTable.vue";
import BowsTable from "@/components/BowsTable.vue";
import ClansTable from "@/components/ClansTable.vue";
import CulturesTable from "@/components/CulturesTable.vue";
import GoodsTable from "@/components/GoodsTable.vue";
import KingdomsTable from "@/components/KingdomsTable.vue";
import LordsTable from "@/components/LordsTable.vue";
import TownsTable from "@/components/TownsTable.vue";
import TroopsTable from "@/components/TroopsTable.vue";



const conceptData = ref(null);
const route = useRoute();


async function fetchData(conc) {
    const res = await fetch(`${process.env.VUE_APP_API_URL}/${conc}`);
    const json_arr = await res.json();
    
    return json_arr;
}


onMounted(async () => {
    await fetchData(route.params.concept).then(data => conceptData.value = data);
})


watch(route, async () => {
    conceptData.value = null;

    if (route.params.concept !== undefined && route.params.id === undefined) {
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
        <ArmorsTable v-if="route.params.concept === 'armors'" :armors-arr="conceptData"/>
        <BowsTable v-if="route.params.concept === 'bows'" :bows-arr="conceptData"/>
        <ClansTable v-if="route.params.concept === 'clans'" :clans-arr="conceptData"/>
        <CulturesTable v-else-if="route.params.concept === 'cultures'" :cultures-arr="conceptData"/>
        <GoodsTable v-else-if="route.params.concept === 'goods'" :goods-arr="conceptData"/>
        <KingdomsTable v-else-if="route.params.concept === 'kingdoms'" :kingdoms-arr="conceptData"/>
        <LordsTable v-else-if="route.params.concept === 'lords'" :lords-arr="conceptData"/>
        <TownsTable v-else-if="route.params.concept === 'towns'" :towns-arr="conceptData"/>
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
