<script setup lang="ts">
import { ref, watch, onMounted } from "vue"
import { useRoute, type RouteLocationNormalizedLoaded } from 'vue-router'

const props = defineProps<{
    concept: string
    id: string
    data: any
}>()
const route: RouteLocationNormalizedLoaded = useRoute()
</script>
<!------------------------------------------------------->
<template>
    <router-link :to="{name: 'cardview', params: {concept: props.concept, id: props.id}}" class="id-link">
        {{ data }}
    </router-link>
</template>
<!------------------------------------------------------->
<style scoped>

</style>
