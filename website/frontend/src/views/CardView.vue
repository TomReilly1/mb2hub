<script setup>
import { ref, onMounted, onUpdated, watch, onBeforeMount } from "vue";
import { useRoute } from 'vue-router';
import CulturesCard from "@/components/CulturesCard.vue";



console.log('made it to card view');


const cardData = ref();
const route = useRoute();



async function fetchData(card_conc, card_id) {
    console.log('fetch data card view');
    console.log(route.params.concept, route.params.id);
    const res = await fetch(`${process.env.VUE_APP_API_URL}/${card_conc}/${card_id}`);
    const json_arr = await res.json();
    
    return json_arr;
}


onMounted(async () => {
    console.log(route.params.concept, route.params.id);
    console.log('on mounted card view');
    await fetchData(route.params.concept, route.params.id).then(data => cardData.value = data);
    
    console.log(cardData.value);
})
</script>
<!------------------------------------------------------->
<template>
    <section class="heading">
        <h1>{{route.params.concept}}</h1>
    </section>
    <section v-if="route.params.concept === 'cultures'">
        <!-- <CulturesCard v-bind="cardData"/> -->
        <CulturesCard :culture-obj="cardData"/>
    </section>
    <section v-else>
        <div class="card-desc">
            <p>this is NOT culture</p>
        </div>
    </section>
</template>
<!------------------------------------------------------->
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
