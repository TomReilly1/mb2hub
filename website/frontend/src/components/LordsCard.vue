<script setup lang="ts">
import { computed } from "vue"
import formatTroopGroup from "@/composables/formatTroopGroup"
import type { card as cardIntr, lords as lordsIntr } from "@/interfaces/indexIntr"


const props = defineProps<{
    dataObj: cardIntr | undefined
}>()

const lordObj = computed(() => {
    return props.dataObj?.cardData as lordsIntr | undefined
})

</script>
<!------------------------------------------------------->
<template>
    <section>
        <div v-if="lordObj" class="card-desc">
            <div>
                <h2>{{ lordObj.name }}</h2>
                <p>
                    {{ lordObj.name }} is a {{ lordObj.sex }} lord of the {{ lordObj.culture }} culture.
                    They are {{ lordObj.age }} years old. Their default battle group is {{ formatTroopGroup(lordObj.default_group) }}.
                </p>
            </div>
        </div>
    </section>
</template>
<!------------------------------------------------------->
<style scoped>

</style>
