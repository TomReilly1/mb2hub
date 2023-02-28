<script setup lang="ts">
import { ref, onBeforeMount } from "vue"
import { useRoute, onBeforeRouteUpdate } from 'vue-router'
import router from "@/router"

import CardKey from "@/components/CardKey.vue"

import ArmorsCard from "@/components/ArmorsCard.vue"
import BowsCard from "@/components/BowsCard.vue"
import CastlesCard from "@/components/CastlesCard.vue"
import ClansCard from "@/components/ClansCard.vue"
import CulturesCard from "@/components/CulturesCard.vue"
import DraughtAnimalsCard from "@/components/DraughtAnimalsCard.vue"
import GoodsCard from "@/components/GoodsCard.vue"
import KingdomsCard from "@/components/KingdomsCard.vue"
import LordsCard from "@/components/LordsCard.vue"
import MountsCard from "@/components/MountsCard.vue"
import ShieldsCard from "@/components/ShieldsCard.vue"
import TownsCard from "@/components/TownsCard.vue"
import TroopsCard from "@/components/TroopsCard.vue"
import VillagesCard from "@/components/VillagesCard.vue"

import formatHeader from "@/composables/formatHeader"

import type { card as cardIntr } from "@/interfaces/indexIntr"


const dataObj = ref<cardIntr>()
const route = useRoute()


onBeforeMount(async () => {
    const data = await fetchData(route.params.concept, route.params.id)
    dataObj.value = data
})

onBeforeRouteUpdate(async (to, from) => {
    const data = await fetchData(to.params.concept, to.params.id)
    dataObj.value = data
})

async function fetchData(concept: string | string[], id: string | string[]) {
    const url: string = `${import.meta.env.VITE_API_URL}/concept/${concept}/item/${id}`
    try {
        const response: Response = await fetch(url)
        const data = await response.json()
        return data
    } catch (error) {
        console.error(error)
        router.push('/404')
    }
}
</script>
<!------------------------------------------------------------------------>
<template>
    <section class="heading">
        <h1>{{ formatHeader(route.params.concept as string) }}</h1>
    </section>
    <ArmorsCard v-if="route.params.concept === 'armors'" :data-obj="dataObj">
        <slot><CardKey /></slot>
    </ArmorsCard>
    <BowsCard v-else-if="route.params.concept === 'bows'" :data-obj="dataObj">
        <slot><CardKey /></slot>
    </BowsCard>
    <CastlesCard v-else-if="route.params.concept === 'castles'" :data-obj="dataObj">
        <slot><CardKey /></slot>
    </CastlesCard>
    <ClansCard v-else-if="route.params.concept === 'clans'" :data-obj="dataObj"/>
    <CulturesCard v-else-if="route.params.concept === 'cultures'" :data-obj="dataObj"/>
    <DraughtAnimalsCard v-else-if="route.params.concept === 'draught_animals'" :data-obj="dataObj"/>
    <GoodsCard v-else-if="route.params.concept === 'goods'" :data-obj="dataObj">
        <slot><CardKey /></slot>
    </GoodsCard>
    <KingdomsCard v-else-if="route.params.concept === 'kingdoms'" :data-obj="dataObj"/>
    <LordsCard v-else-if="route.params.concept === 'lords'" :data-obj="dataObj"/>
    <MountsCard v-else-if="route.params.concept === 'mounts'" :data-obj="dataObj">
        <slot><CardKey /></slot>
    </MountsCard>
    <ShieldsCard v-else-if="route.params.concept === 'shields'" :data-obj="dataObj">
        <slot><CardKey /></slot>
    </ShieldsCard>
    <TownsCard v-else-if="route.params.concept === 'towns'" :data-obj="dataObj">
        <slot><CardKey /></slot>
    </TownsCard>
    <TroopsCard v-else-if="route.params.concept === 'troops'" :data-obj="dataObj">
        <slot><CardKey /></slot>
    </TroopsCard>
    <VillagesCard v-else-if="route.params.concept === 'villages'" :data-obj="dataObj">
        <slot><CardKey /></slot>
    </VillagesCard>
</template>
<!------------------------------------------------------------------------>
<style scoped>
:deep(h1) {
    text-transform: capitalize;
}

:deep(hr) {
    margin: 30px 0;
}

:deep(h2) {
    text-transform: capitalize;
    font-size: 3rem;
    font-weight: 700;
    margin: 0 0 20px;
    border: 0;
    padding: 0;
}

:deep(h3) {
    font-size: 2.2rem;
    margin: 0;
    border: 0;
    padding: 0 0 20px;
}

:deep(p) {
    font-size: 1.3rem;
    color: var(--text-color);
    margin: 0;
}

:deep(span) {
    color: var(--bluegray-100);
    font-size: 1.2rem;
}

/* CARD */
:deep(.card-desc) {
    width: 96%;
    max-width: 40rem;
    margin: 0 auto 3rem;
    padding: 40px;
    border-radius: 20px;
    background-color: var(--bluegray-900);
    color: var(--yellow-300);
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
}

:deep(.card-desc > div) {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

/* RANKS */
:deep(.rank.average) {
    color: #ffe510;
}
:deep(.rank.below-average) {
    color: var(--orange-400);
}
:deep(.rank.bad) {
    color: var(--red-400);
}
:deep(.rank.above-average) {
    color: var(--green-400);
}
:deep(.rank.great) {
    color: var(--blue-400);
}
:deep(.rank.best) {
    color: var(--purple-400);
}

:deep(.rank.unranked) {
    color: var(--bluegray-200);
}


:deep(a) {
    color: var(--yellow-400);
}

:deep(a:hover) {
    color: var(--yellow-100);
}

</style>
