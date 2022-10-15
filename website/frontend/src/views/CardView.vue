<script setup lang="ts">
import { ref, onMounted } from "vue"
import { useRoute, onBeforeRouteUpdate } from 'vue-router'
import router from "@/router"

import ArmorsCard from "@/components/ArmorsCard.vue"
import BowsCard from "@/components/BowsCard.vue"
import CastlesCard from "@/components/CastlesCard.vue"
import ClansCard from "@/components/ClansCard.vue"
import CulturesCard from "@/components/CulturesCard.vue"
import GoodsCard from "@/components/GoodsCard.vue"
import KingdomsCard from "@/components/KingdomsCard.vue"
import LordsCard from "@/components/LordsCard.vue"
import MountsCard from "@/components/MountsCard.vue"
import TownsCard from "@/components/TownsCard.vue"
import TroopsCard from "@/components/TroopsCard.vue"
import VillagesCard from "@/components/VillagesCard.vue"


const cardData = ref()
const route = useRoute()


onMounted(async () => {
    await fetch(`${import.meta.env.VITE_API_URL}/${route.params.concept}/${route.params.id}`)
        .then(res => res.json())
        .then(data => cardData.value = data)
        .catch(() => {
            router.push('/404')
        })
})

onBeforeRouteUpdate(async (to, from) => {
    await fetch(`${import.meta.env.VITE_API_URL}/${to.params.concept}/${to.params.id}`)
        .then(res => res.json())
        .then(data => cardData.value = data)
        .catch(() => {
            router.push('/404')
        })
})
</script>
<!------------------------------------------------------------------------>
<template>
    <section class="heading">
        <h1>{{route.params.concept}}</h1>
    </section>
    <ArmorsCard v-if="route.params.concept === 'armors'" :armor-obj="cardData"/>
    <BowsCard v-else-if="route.params.concept === 'bows'" :bow-obj="cardData"/>
    <CastlesCard v-else-if="route.params.concept === 'castles'" :castle-obj="cardData"/>
    <ClansCard v-else-if="route.params.concept === 'clans'" :clan-obj="cardData"/>
    <CulturesCard v-else-if="route.params.concept === 'cultures'" :culture-obj="cardData"/>
    <GoodsCard v-else-if="route.params.concept === 'goods'" :good-obj="cardData"/>
    <KingdomsCard v-else-if="route.params.concept === 'kingdoms'" :kingdom-obj="cardData"/>
    <LordsCard v-else-if="route.params.concept === 'lords'" :lord-obj="cardData"/>
    <MountsCard v-else-if="route.params.concept === 'mounts'" :mount-obj="cardData"/>
    <TownsCard v-else-if="route.params.concept === 'towns'" :town-obj="cardData"/>
    <TroopsCard v-else-if="route.params.concept === 'troops'" :troop-obj="cardData"/>
    <VillagesCard v-else-if="route.params.concept === 'villages'" :village-obj="cardData"/>
</template>
<!------------------------------------------------------------------------>
<style scoped>
:deep(hr) {
    margin: 30px 0;
}

h1 {
    text-transform: capitalize;
}

h3 {
    font-size: 3rem;
    margin: 0;
    border: 0;
    padding: 0 0 20px;
}

div {
    max-width: 40rem;
    margin: 0 auto 3rem;
    padding: 2rem;
    border-radius: 1rem;
    background-color: var(--bluegray-700);
    color: var(--yellow-300);
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
}

:deep(p) {
    font-size: 1.2rem;
    margin: 0;
}
</style>
