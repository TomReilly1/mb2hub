<script setup>
import { ref, onMounted, onUpdated } from "vue";
import { useRoute } from 'vue-router';

console.log('made it to culture card component');

const route = useRoute();
const props = defineProps({cultureObj: Object});


</script>
<!------------------------------------------------------->
<template>
    <section>
        <div v-if="cultureObj !== null && cultureObj !== undefined" class="card-desc">
            <h2>{{cultureObj.name || 'Nothing passed yet'}}</h2>
            <p v-if="cultureObj.is_main_culture">The {{cultureObj.name}} culture is a main culture of Calradia</p>
            <p v-else>The {{cultureObj.name}} culture is a minor culture of Calradia</p>
            <h3>Description</h3>
            <p>{{cultureObj.desc_text}}</p>
        </div>
    </section>
</template>
<!------------------------------------------------------->
<style scoped>
    h2 {
        text-transform: capitalize;
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
        background-color: var(--bluegray-800);
        color: var(--yellow-300);
        box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
    }

    div > p{
        color: var(--bluegray-100);
        font-size: 1.2rem;
    }
</style>
