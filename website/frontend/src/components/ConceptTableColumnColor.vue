<script setup lang="ts">
const props = defineProps<{
    colorData: any
}>()

const formatColor = (color: string) => {
    const hexValue = color.slice(-6)
    return '#' + hexValue
}
</script>
<!------------------------------------------------------->
<template>
    <input type="color" :value="formatColor(colorData)" class="color-input" disabled>
</template>
<!------------------------------------------------------->
<style scoped>

</style>
