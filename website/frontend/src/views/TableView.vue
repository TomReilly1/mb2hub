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
import VillagesTable from "@/components/VillagesTable.vue";

import TroopsCompare from "@/components/TroopsCompare.vue";



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
        <div v-else-if="route.params.concept === 'troops'">
            <TroopsTable :troops-arr="conceptData"/>
            <TroopsCompare :troops-arr="conceptData"/>
        </div>
        <VillagesTable v-else-if="route.params.concept === 'villages'" :villages-arr="conceptData"/>
    </section>
    <section v-else>
        <router-view />
    </section>
</template>
<!------------------------------------------------------------------------------------->
<style lang="scss" scoped>
h1 {
    text-transform: capitalize;
}

.id-link {
    text-decoration: none;
}

.concept-table {
    background-color: var(--bluegray-900);
    border: 3px solid var(--bluegray-700);
    margin: 0 auto;
    width: fit-content;
    max-width: 98%;
    box-shadow: 0 0 1px 2px #3f4b5b;
}

:deep(.p-paginator) {
    .p-paginator-element.p-link {
        color: var(--yellow-300);
    }

    .p-paginator-element.p-link:hover {
        color: var(--yellow-500);
        background-color: var(--bluegray-800);
    }

    .p-paginator-element.p-link.p-highlight {
        color: var(--bluegray-900);
        border: 2px solid var(--bluegray-500);
        background-color: var(--yellow-300);
    }

    .p-paginator-current {
        color: var(--yellow-300);
    }
}
</style>
