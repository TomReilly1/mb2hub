<script setup lang="ts">
import { ref, onBeforeUpdate, onMounted, onBeforeMount, computed } from "vue"

import CardRatings from "@/components/CardRatings.vue"
import formatBowSubtype from "@/composables/formatBowSubtype"
import type { card as cardIntr, bows as bowsIntr } from "@/interfaces/indexIntr"


const props = defineProps<{
    dataObj: cardIntr | undefined
}>()

const bowObj = computed(() => {
    return props.dataObj?.cardData as bowsIntr | undefined
})

const bowSubtype = computed(() => {
    return (bowObj.value) ? formatBowSubtype(bowObj.value.subtype) : 'not available'
})
</script>
<!------------------------------------------------------->
<template>
    <section>
        <div v-if="bowObj" class="card-desc">
            <div>
                <h2>{{ bowObj.name }}</h2>
                <p>
                    <span>The {{ bowObj.name }} is a {{ bowSubtype }} of the {{ bowObj.culture }} culture. </span>
                    <span v-if="bowSubtype === 'bow' || bowSubtype === 'fast crossbow'"> It can be fired and reloaded on a mount.</span>
                    <span v-else-if="bowSubtype === 'longbow'"> It cannot be fired nor reloaded on a mount.</span>
                    <span v-else-if="bowSubtype === 'crossbow'"> It can be fired on a mount, but it cannot be reloaded.</span>
                </p>
            </div>
            <hr />
            <div>
                <CardRatings :data-obj="dataObj"/>
                <slot></slot>                
            </div>
        </div>
    </section>
</template>
<!------------------------------------------------------->
<style scoped>

</style>
