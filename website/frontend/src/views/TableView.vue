<script setup>
import { ref, onMounted, watch } from "vue";
import { useRoute } from 'vue-router';

import ConceptTable from "@/components/ConceptTable.vue";
import TroopsCompare from "@/components/TroopsCompare.vue";



const conceptData = ref(null);
const route = useRoute();


async function fetchData(conc) {
    const res = await fetch(`${process.env.VUE_APP_API_URL}/${conc}`);
    const json_arr = await res.json();
    
    return json_arr;
}


onMounted(async () => {
    await fetchData(route.params.concept).then(data => conceptData.value = data);
})


watch(route, async () => {
    conceptData.value = null;

    if (route.params.concept !== undefined && route.params.id === undefined) {
        await fetchData(route.params.concept).then(data => conceptData.value = data);
    }
})
</script>
<!------------------------------------------------------------------------------------->
<template>
    <section class="heading">
        <h1>{{route.params.concept}}</h1>
    </section>
    <section v-if="route.params.id === undefined">
        <div>
            <ConceptTable :data-arr="conceptData"/>
            <TroopsCompare v-if="route.params.concept === 'troops'" :troops-arr="conceptData"/>
        </div>
    </section>
    <section v-else>
        <router-view />
    </section>
</template>
<!------------------------------------------------------------------------------------->
<style lang="scss" scoped>
h1 {
    text-transform: capitalize;
}

.id-link {
    text-decoration: none;
}

.concept-table {
    background-color: var(--bluegray-900);
    border: 3px solid var(--bluegray-700);
    margin: 0 auto;
    width: fit-content;
    max-width: 98%;
    box-shadow: 0 0 1px 2px #3f4b5b;
}

:deep(.p-paginator) {
    .p-paginator-element.p-link {
        color: var(--yellow-300);
    }

    .p-paginator-element.p-link:hover {
        color: var(--yellow-500);
        background-color: var(--bluegray-800);
    }

    .p-paginator-element.p-link.p-highlight {
        color: var(--bluegray-900);
        border: 2px solid var(--bluegray-500);
        background-color: var(--yellow-300);
    }

    .p-paginator-current {
        color: var(--yellow-300);
    }
}
</style>
