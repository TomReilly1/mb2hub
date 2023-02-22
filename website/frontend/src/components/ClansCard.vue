<script setup lang="ts">
import { computed } from "vue"
import formatTier from "@/composables/formatTier"
import type { card as cardIntr, clans as clansIntr } from "@/interfaces/indexIntr"


const props = defineProps<{
    dataObj: cardIntr | undefined
}>()

const clanObj = computed(() => {
    return props.dataObj?.cardData as clansIntr | undefined
})
</script>
<!------------------------------------------------------->
<template>
    <section>
        <div v-if="clanObj && clanObj.owner_lord" class="card-desc">
            <div>
                <h2>{{ clanObj.name }}</h2>
                <p>
                    The {{ clanObj.name }} clan is a {{ formatTier(clanObj.tier) }} tier clan of the {{ clanObj.kingdom }} kingdom.
                    <span v-if="clanObj.is_ruling_clan">It is the ruling clan of its kingdom.</span>
                    Its leader is 
                    <router-link :to="{name: 'cardview', params: {concept: 'lords', id: clanObj.owner_lord.id}}" class="id-link">
                        {{ clanObj.owner_lord.name }}
                    </router-link>.
                </p>
            </div>
        </div>
    </section>
</template>
<!------------------------------------------------------->
<style scoped>

</style>
