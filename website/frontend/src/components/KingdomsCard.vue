<script setup lang="ts">
import { computed } from "vue"
import formatColorToHex from "@/composables/formatColorToHex"
import type { card as cardIntr, kingdoms as kingdomsIntr } from "@/interfaces/indexIntr"

const props = defineProps<{
    dataObj: cardIntr | undefined
}>()

const kingdomObj = computed(() => {
    return props.dataObj?.cardData as kingdomsIntr | undefined
})
</script>
<!------------------------------------------------------->
<template>
    <section>
        <div v-if="kingdomObj" class="card-desc">
            <div>
                <h2>{{ kingdomObj.name }}</h2>
                <p>
                    The {{ kingdomObj.title }} is a Calradian kingdom of the {{ kingdomObj.culture }} culture, ruled by its {{ kingdomObj.ruler_title }}.
                </p>
            </div>
            <hr />
            <div>
                <h3>Description</h3>
                <p>
                    {{ kingdomObj.desc_text || 'N/A' }}
                </p>
            </div>
            <hr />
            <div>
                <h3>Primary Banner Color</h3>
                <input class="color-input" type="color" :value="formatColorToHex(kingdomObj.primary_banner_color)" disabled>
                <span>Hex: {{ formatColorToHex(kingdomObj.primary_banner_color) }}</span>
            </div>
        </div>
    </section>
</template>
<!------------------------------------------------------->
<style scoped>
.color-input {
    position: static;
    z-index: 1;
    width: 80%;
    height: 10rem;
    border: 0;
    padding: 0;
}
</style>
