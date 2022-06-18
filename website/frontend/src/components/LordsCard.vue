<script setup>
import { useRoute } from 'vue-router';


const route = useRoute();
const props = defineProps({lordObj: Object});


const fromatTroopGroup = (troopGroup) => {
    if (troopGroup === 'HorseArcher') {
        return 'horse archer';
    } else if (troopGroup === 'Infantry'){
        return troopGroup.toLowerCase();
    } else {
        return troopGroup.toLowerCase(); 
    }
};
</script>
<!------------------------------------------------------->
<template>
    <section>
        <div v-if="lordObj !== null && lordObj !== undefined" class="card-desc">
            <div>
                <h2>{{lordObj.name || 'Nothing passed yet'}}</h2>
                <p v-if="lordObj.sex === 'male'">
                    {{lordObj.name}} is a male lord of the {{lordObj.culture}} culture.
                    He is {{lordObj.age}} years old. His default battle group is {{fromatTroopGroup(lordObj.default_group)}}.
                </p>
                <p v-else>
                    {{lordObj.name}} is a female lord of the {{lordObj.culture}} culture.
                    She is {{lordObj.age}} years old. Her default battle group is {{fromatTroopGroup(lordObj.default_group)}}.
                </p>
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

section > div {
    max-width: 40rem;
    margin: 0 auto 3rem;
    padding: 40px;
    border-radius: 30px;
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
