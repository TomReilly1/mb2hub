<script setup lang="ts">
import { computed } from "vue"
import CardRatings from "@/components/CardRatings.vue"
import type { card as cardIntr, villages as villagesIntr } from "@/interfaces/indexIntr"

const props = defineProps<{
    dataObj: cardIntr | undefined
}>()

const villageObj = computed(() => {
    return props.dataObj?.cardData as villagesIntr | undefined
})

const settlementType = computed(() => {
    if (villageObj.value?.bound_settlement.id) {
        return (villageObj.value.bound_settlement.id.includes('castle')) ? 'castles' : 'towns'
    } else {
        return 'undefined'
    }
})

const formatVillageType = computed(() => {
    return villageObj.value?.village_type.replace(/([_])/, ' ')
})
</script>
<!------------------------------------------------------->
<template>
    <section>
        <div v-if="villageObj && villageObj.bound_settlement" class="card-desc">
            <div>
                <h2>{{ villageObj.name }}</h2>
                <p>
                    {{ villageObj.name }} is a village of the {{ villageObj.culture }} culture.
                    It operates as a {{ formatVillageType }}.
                    It is bound to the settlement, 
                    <router-link v-if="settlementType" :to="{ name: 'cardview', params: {concept: settlementType, id: villageObj.bound_settlement.id} }">
                        {{ villageObj.bound_settlement.name }}
                    </router-link>
                </p>
            </div>
            <hr />
            <div>
                <h3>Description</h3>
                <p>
                    {{ villageObj.desc_text || 'N/A' }}
                </p>
            </div>
            <hr />
            <div>
                <CardRatings :data-obj="dataObj" />
                <slot></slot>
            </div>
        </div>
    </section>
</template>
<!------------------------------------------------------->
<style scoped>
.ratings-table {
    background-color: var(--bluegray-800);
    border-radius: 10px;
}

th,
td {
    padding: 20px 35px;
}

th {
    font-size: 1.5rem;
    
}

td {
    font-size: 2rem;
    font-weight: 700;
    color: var(--bluegray-100);
}

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

h4 {
    font-size: 1.3rem;
    color: var(--bluegray-100);
    margin: 25px 0 10px;
}

section > div {
    width: 96%;
    max-width: 40rem;
    margin: 0 auto 3rem;
    padding: 40px;
    border-radius: 20px;
    background-color: var(--bluegray-900);
    color: var(--yellow-300);
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
}

section > div > div {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

input {
    position: static;
    z-index: 1;
    width: 80%;
    height: 10rem;
    border: 0;
    padding: 0;
}

ul {
    text-align: left;
}

li, li > * {
    font-size: 1.1rem;
}

li > span {
    font-weight: 700;
}
</style>
