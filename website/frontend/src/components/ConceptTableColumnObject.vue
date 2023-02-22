<script setup lang="ts">
import { ref, watch, onMounted } from "vue"
import { useRoute, type RouteLocationNormalizedLoaded } from 'vue-router'
import type { basicObj } from "@/interfaces/indexIntr"


const props = defineProps<{
    header: string
    obj: basicObj
    arr?: basicObj[]
}>()
const route: RouteLocationNormalizedLoaded = useRoute()


const getConceptFromObject = (dataHeader: string, id: string) => {
    switch (dataHeader) {
        case 'owner_clan':
            return 'clans'
        case 'owner_lord':
            return 'lords'
        case 'bound_settlement':
            return getSettlementType(id)
        case 'bound_villages':
            return 'villages'
        case 'upgrade_targets':
            return 'troops'
        default:
            throw Error('Error: could not generate concept based off object data header')
    }
}

const getSettlementType = (input: string) => {
    return (input.includes('castle')) ? 'castles' : 'towns'
}

const isLastObject = (arr: basicObj[], obj: basicObj) => {
    return arr.indexOf(obj) < arr.length - 1
}
</script>
<!------------------------------------------------------->
<template >
    <router-link :to="{name: 'cardview', params: {concept: getConceptFromObject(header, obj.id), id: obj.id}}" class="id-link">
        {{ obj.name }}
    </router-link>
    <template v-if="arr">
        <span v-if="isLastObject(arr, obj)">, </span>
    </template>
</template>
<!------------------------------------------------------->
<style scoped>

</style>
