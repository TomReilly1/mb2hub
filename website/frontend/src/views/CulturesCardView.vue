<script setup>
import { ref, onMounted, onUpdated } from "vue";
import { useRoute } from 'vue-router';



onMounted(async () => {
    cardId.value = route.params.id;

    async function fetchData() {
        const res = await fetch(`${process.env.VUE_APP_API_URL}/cultures/${cardId.value}`);
        const json_obj = await res.json();

        cardName.value = json_obj['name'];
        isMainCulture.value = json_obj['is_main_culture'];
        return json_obj;
    }
    await fetchData();
        //.then(data => cardArray.value = data);
})

onUpdated(() => {
    cardId.value = route.params.id;
})


const cardId = ref();
const cardName = ref();
const isMainCulture = ref();
// const cardArray = ref();
const route = useRoute();

cardId.value = route.params.id;

</script>

<!------------------------------------------------------->

<template>
    <section>
        <div class="card-desc">
            <h3>{{cardName}}</h3>
            <p v-if="isMainCulture">The {{cardName}} culture is a main culture of Calradia</p>
            <p v-else>The {{cardName}} culture is a minor culture of Calradia</p>
        </div>
    </section>
</template>

<!------------------------------------------------------->

<style scoped>
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