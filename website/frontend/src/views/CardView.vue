<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from 'vue-router';
import ArmorsCard from "@/components/ArmorsCard.vue";
import BowsCard from "@/components/BowsCard.vue";
import ClansCard from "@/components/ClansCard.vue";
import CulturesCard from "@/components/CulturesCard.vue";
import KingdomsCard from "@/components/KingdomsCard.vue";
import LordsCard from "@/components/LordsCard.vue";
import TroopsCard from "@/components/TroopsCard.vue";


const cardData = ref();
const route = useRoute();


async function fetchData(card_conc, card_id) {
    const res = await fetch(`${process.env.VUE_APP_API_URL}/${card_conc}/${card_id}`);
    const json_arr = await res.json();
    
    return json_arr;
}


onMounted(async () => {
    await fetchData(route.params.concept, route.params.id).then(data => cardData.value = data);
})
</script>
<!------------------------------------------------------------------------>
<template>
    <section class="heading">
        <h1>{{route.params.concept}}</h1>
    </section>
    <ArmorsCard v-if="route.params.concept === 'armors'" :armor-obj="cardData"/>
    <BowsCard v-else-if="route.params.concept === 'bows'" :bow-obj="cardData"/>
    <ClansCard v-else-if="route.params.concept === 'clans'" :clan-obj="cardData"/>
    <CulturesCard v-else-if="route.params.concept === 'cultures'" :culture-obj="cardData"/>
    <KingdomsCard v-else-if="route.params.concept === 'kingdoms'" :kingdom-obj="cardData"/>
    <LordsCard v-else-if="route.params.concept === 'lords'" :lord-obj="cardData"/>
    <TroopsCard v-else-if="route.params.concept === 'troops'" :troop-obj="cardData"/>
</template>
<!------------------------------------------------------------------------>
<style scoped>
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

div > p{
    font-size: 1.2rem;
}
</style>
