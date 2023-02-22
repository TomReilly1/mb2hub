<script setup lang="ts">
import { computed } from "vue"
import CardRatings from "@/components/CardRatings.vue"
import type { card as cardIntr, mounts as mountsIntr } from "@/interfaces/indexIntr"


const props = defineProps<{
    dataObj: cardIntr | undefined
}>()

const mountObj = computed(() => {
    return props.dataObj?.cardData as mountsIntr | undefined
})

const isCamel = computed(() => {
    return mountObj.value?.name.toLowerCase().includes('camel')
})
</script>
<!------------------------------------------------------->
<template>
    <section>
        <div v-if="mountObj" class="card-desc">
            <div>
                <h2>{{ mountObj.name }}</h2>
                <p>
                    The {{ mountObj.name }} is a mount of the {{ mountObj.culture }} culture.
                    <template v-if="mountObj.subtype === 'noble_horse'"> It is a noble horse which are considered to be the best breed of horses. As such, noble horses are used by lords.</template>
                    <template v-else-if="mountObj.subtype === 'war_horse'"> It is a war horse, meaning it can be used to upgrade certain mounted troops, typically those of mid or higher tiers such as tier 3, 4, or 5. War horses are considered better than normal horses, but worse than noble horses. </template>
                    <template v-else-if="mountObj.subtype === 'horse'"> It is a normal horse, meaning it can be used to upgrade certain infantry troops to mounted troops, typically those of lower or mid tiers such as tier 1, 2, 3, or 4. Although still formidable, Normal horses are considered the worst of the mounts when compared to noble horses and war horses. </template>
                    <template v-if="mountObj.is_merchandise"> It is considered merchandise, meaning it can be bought from town markets or villages. </template>
                    <template v-else> It is not considered merchandise, meaning it cannot be bought from town markets or villages, and must be gained through tournaments or gifts. This also means troops cannot use them to upgrade to mounted units. </template>
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
