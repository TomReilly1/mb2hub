<script setup lang="ts">
import { computed } from "vue"
import CardRatings from "@/components/CardRatings.vue"
import type { card as cardIntr, goods as goodsIntr } from "@/interfaces/indexIntr"

const props = defineProps<{
    dataObj: cardIntr | undefined
}>()

const goodObj = computed(() => {
    return props.dataObj?.cardData as goodsIntr
})
</script>
<!------------------------------------------------------->
<template>
    <section>
        <div v-if="goodObj" class="card-desc">
            <div>
                <h2>{{ goodObj.name }}</h2>
                <p>
                    <span>{{ goodObj.name }} ({{ goodObj.plural }}) is a type of tradable good in Calradia. </span>
                    <span v-if="goodObj.is_food">It is classified as a consumable, so it will be used as party rations and provide a morale boost.</span>
                    <span v-else-if="goodObj.id === 'wine'">It is not classified as a consumable, so it will not be used as party rations. However, wine does provide a morale boost. This makes wine unique because it is the only good that provides a morale boost wihtout being used as party rations.</span>
                    <span v-else>It is not classified as a consumable, so it will not be used as party rations and it will not provide a morale boost.</span>
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
