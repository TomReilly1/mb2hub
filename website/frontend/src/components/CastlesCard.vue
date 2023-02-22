<script setup lang="ts">
import { computed } from 'vue'
import CardRatings from '@/components/CardRatings.vue'
import type { card as cardIntr, castles as castlesIntr } from "@/interfaces/indexIntr"


const props = defineProps<{
    dataObj: cardIntr | undefined
}>()

const castlesObj = computed(() => {
    return props.dataObj?.cardData as castlesIntr | undefined
})

const villages = computed(() => {
    return castlesObj.value?.bound_villages
})

</script>
<!------------------------------------------------------->
<template>
    <section>
        <div v-if="castlesObj && castlesObj.owner_clan" class="card-desc">
            <div>
                <h2>{{ castlesObj.name }}</h2>
                <p>
                    {{ castlesObj.name }} is a castle of the {{ castlesObj.culture }}, ruled by the <span v-if="castlesObj.owner_clan">{{ castlesObj.owner_clan.name }}</span> clan.
                    It's bound villages are
                    <template v-if="villages">
                        <router-link :to="{name: 'cardview', params: {concept: 'villages', id: villages[0]['id']}}" class="id-link">
                            {{ villages[0]['name'] }}
                        </router-link>
                        and
                        <router-link :to="{name: 'cardview', params: {concept: 'villages', id: villages[1]['id']}}" class="id-link">
                            {{ villages[1]['name'] }}
                        </router-link>
                    </template>

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
