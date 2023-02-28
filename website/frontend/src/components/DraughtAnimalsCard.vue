<script setup lang="ts">
import { computed } from "vue"
import CardRatings from "@/components/CardRatings.vue"
import type { card as cardIntr, draughtAnimals as draughtAnimalsIntr } from "@/interfaces/indexIntr"


const props = defineProps<{
    dataObj: cardIntr | undefined
}>()

const draughAnimalObj = computed(() => {
    return props.dataObj?.cardData as draughtAnimalsIntr | undefined
})

const isCamel = computed(() => {
    return draughAnimalObj.value?.name.toLowerCase().includes('camel')
})
</script>
<!------------------------------------------------------->
<template>
    <section>
        <div v-if="draughAnimalObj" class="card-desc">
            <div>
                <h2>{{ draughAnimalObj.name }}</h2>
                <p>
                    The {{ draughAnimalObj.name }} is a draught animal of {{ draughAnimalObj.culture }} culture. It can be found in any town or village
                    <template v-if="draughAnimalObj.culture === 'aserai'">, but is typically found in those of aserai culture</template>.
                </p>
                <small v-if="isCamel">* Camels may be referred to as horses in the game for classification purposes.</small>
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

</style>
