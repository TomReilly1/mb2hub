<script setup lang="ts">
import { computed } from 'vue'
import CardRatings from '@/components/CardRatings.vue'
import type { card as cardIntr, armors as armorsIntr } from "@/interfaces/indexIntr"


const props = defineProps<{
    dataObj: cardIntr | undefined
}>()

const armorObj = computed(() => {
    return props.dataObj?.cardData as armorsIntr | undefined
})

const formatArmorType = (armorType: string) => {
    if (armorType) {
        const arr: string[] = armorType.split(/(?=[A-Z])/)
        const lowerArr: string[] = arr.map(e => e.toLowerCase())
        const lowerStr: string = lowerArr.join(' ')
        
        return lowerStr
    }
}
</script>
<!------------------------------------------------------->
<template>
    <section>
        <div v-if="armorObj" class="card-desc">
            <div>
                <h2>{{ armorObj.name }}</h2>
                <span>
                    The {{ armorObj.name }} is a type of {{ formatArmorType(armorObj.type) }} that is of {{ armorObj.culture }} culture.
                </span>
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
