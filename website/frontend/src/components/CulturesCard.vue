<script setup lang="ts">
const props = defineProps({cultureObj: Object})
</script>
<!------------------------------------------------------->
<template>
    <section>
        <div v-if="cultureObj" class="card-desc">
            <div>
                <h2>{{cultureObj.name || 'Nothing passed yet'}}</h2>
                <span v-if="cultureObj.is_main_culture">The {{cultureObj.name}} culture is a main culture of Calradia.</span>
                <span v-else>The {{cultureObj.name}} culture is a minor culture of Calradia</span>
            </div>
            <hr />
            <div>
                <h3>History</h3>
                <p v-if="cultureObj.is_main_culture">{{cultureObj.desc_text}}</p>
                <span v-else>N/A</span>
            </div>
        </div>
    </section>
</template>
<!------------------------------------------------------->
<style scoped>
h2 {
    text-transform: capitalize;
    font-size: 3rem;
    font-weight: 700;
    margin: 0 0 20px;
    border: 0;
    padding: 0;
}

h3 {
    font-size: 2rem;
    margin: 0 0 15px;
}

.card-desc {
    width: 96%;
    max-width: 40rem;
    margin: 0 auto 3rem;
    padding: 40px;
    border-radius: 20px;
    background-color: var(--bluegray-900);
    color: var(--yellow-300);
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
}

.card-desc > div {
    margin: 0 0 30px;
}

span {
    color: var(--bluegray-100);
    font-size: 1.5rem;
}

p{
    color: var(--bluegray-100);
    font-size: 1.2rem;
}
</style>
