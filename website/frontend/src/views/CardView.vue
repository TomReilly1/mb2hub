<script setup>
import { ref, onMounted, onUpdated } from "vue";
import { useRoute } from 'vue-router';



onMounted(() => {
    cardId.value = route.params.id;
    console.log(cardId.value);
})

onUpdated(() => {
    cardId.value = route.params.id;
    console.log(cardId.value);
})


const cardId = ref();
const route = useRoute();

cardId.value = route.params.id;

</script>
<!------------------------------------------------------->
<template>
    <section>
        <h2>{{cardId}}</h2>
    </section>
</template>
<!------------------------------------------------------->
<style scoped>
    h1 {
        font-size: 3.5rem;
        text-decoration: underline;
        margin: 0;
        border: 0;
        padding: 2rem 0;
    }
</style>