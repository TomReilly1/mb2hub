<script setup lang="ts">
const props = defineProps({clanObj: Object})

function formatClanTier(tier: number) {
    if (tier === 1) {
        return `${tier}st tier`
    } else if (tier === 2) {
        return `${tier}nd tier`
    } else if (tier === 3) {
        return `${tier}rd tier`
    } else {
        return `${tier}th tier`
    }
}
</script>
<!------------------------------------------------------->
<template>
    <section>
        <div v-if="clanObj" class="card-desc">
            <div>
                <h2>{{clanObj.name}}</h2>
                <p>
                    The {{clanObj.name}} clan is a {{formatClanTier(clanObj.tier)}} clan of the {{clanObj.kingdom}} kingdom.
                    <span v-if="clanObj.is_ruling_clan">It is the ruling clan of its kingdom.</span>
                    Its leader is {{clanObj.owner}}.
                </p>
            </div>
        </div>
    </section>
</template>
<!------------------------------------------------------->
<style scoped>
h2 {
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
    margin: 0 0 30px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}


p {
    color: var(--bluegray-100);
    font-size: 1.5rem;
}
</style>
