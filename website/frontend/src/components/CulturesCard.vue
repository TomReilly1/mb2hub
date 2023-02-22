<script setup lang="ts">
import { computed } from "vue"
import type { card as cardIntr, cultures as culturesIntr } from "@/interfaces/indexIntr"

const props = defineProps<{
    dataObj: cardIntr | undefined
}>()

const cultureObj = computed(() => {
    return props.dataObj?.cardData as culturesIntr | undefined
})

const cultureStatus = (isMainCulture: boolean): string => {
    return (isMainCulture) ? 'major' : 'minor'
}
</script>
<!------------------------------------------------------->
<template>
    <section>
        <div v-if="cultureObj" class="card-desc">
            <div>
                <h2>{{ cultureObj.name }}</h2>
                <p>
                    The {{ cultureObj.name }} culture is a {{ cultureStatus(cultureObj.is_main_culture) }} culture of Calradia.
                </p>
            </div>
            <hr />
            <div>
                <h3>Description</h3>
                <p>
                    {{ cultureObj.desc_text || 'N/A' }}
                </p>
            </div>
        </div>
    </section>
</template>
<!------------------------------------------------------->
<style scoped>

</style>
