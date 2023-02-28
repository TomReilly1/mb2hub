<script setup lang="ts">
import { computed } from "vue"

import CardRatings from "@/components/CardRatings.vue"
import type { card as cardIntr, shields as shieldsIntr } from "@/interfaces/indexIntr"


const props = defineProps<{
    dataObj: cardIntr | undefined
}>()

const shieldObj = computed(() => {
    return props.dataObj?.cardData as shieldsIntr | undefined
})

</script>
<!------------------------------------------------------->
<template>
    <section>
        <div v-if="shieldObj" class="card-desc">
            <div>
                <h2>{{ shieldObj.name }}</h2>
                <p>
                    <span>The {{ shieldObj.name }} is a shield of the {{ shieldObj.culture }} culture. </span>
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
