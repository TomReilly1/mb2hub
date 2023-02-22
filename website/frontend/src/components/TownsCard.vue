<script setup lang="ts">
import { computed } from 'vue'
import CardRatings from '@/components/CardRatings.vue'
import type { card as cardIntr, towns as townsIntr } from "@/interfaces/indexIntr"


const props = defineProps<{
    dataObj: cardIntr | undefined
}>()

const townObj = computed(() => {
    return props.dataObj?.cardData as townsIntr | undefined
})
</script>
<!------------------------------------------------------->
<template>
    <section>
        <div v-if="townObj && townObj.owner_clan" class="card-desc">
            <div>
                <h2>{{ townObj.name }}</h2>
                <p>
                    {{ townObj.name }} is a town of the {{ townObj.culture }} culture, ruled by the {{ townObj.owner_clan.name }} clan.
                </p>
            </div>
            <hr />
            <div>
                <h3>Description</h3>
                <p>
                    {{ townObj.desc_text || 'N/A' }}
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

</style>
