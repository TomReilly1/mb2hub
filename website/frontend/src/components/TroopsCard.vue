<script setup lang="ts">
import { computed } from 'vue'
import CardRatings from '@/components/CardRatings.vue'
import formatTier from "@/composables/formatTier"
import type { card as cardIntr, troops as troopsIntr } from "@/interfaces/indexIntr"


const props = defineProps<{
    dataObj: cardIntr | undefined
}>()

const troopObj = computed(() => {
    return props.dataObj?.cardData as troopsIntr | undefined
})

const tierLevel = computed(() => {
    return (troopObj.value) ? (troopObj.value.level - 1) / 5 : -1
})

const troopGroup = computed(() => {
    if (troopObj.value?.default_group) {
        const defaultGroup = troopObj.value.default_group
        return (defaultGroup === 'HorseArcher') ? 'horse archer' : defaultGroup.toLowerCase()
    }
})
</script>
<!------------------------------------------------------->
<template>
    <section>
        <div v-if="troopObj" class="card-desc">
            <div>
                <h2>{{ troopObj.name }}</h2>
                <p>
                    The {{ troopObj.name }} is a {{ formatTier(tierLevel) }} {{ troopGroup }}
                    <template v-if="troopObj.occupation === 'Soldier'">
                        unit of the {{ troopObj.culture }} culture.
                        <template v-if="troopObj.is_noble">
                            They are a noble troop, which means they are a part of the best line of troops in their respective culture. They can only be recruited in {{ troopObj.culture }} villages that are bound to castles.
                        </template>
                        <template v-else>
                            They are not a noble troop, and thus can be recruited from any {{ troopObj.culture }} town or village.
                        </template>
                    </template>
                    <template v-else-if="troopObj.occupation === 'Mercenary'">
                        mercenary troop. They can be found inside of any town tavern.
                    </template>
                    <template v-else-if="troopObj.occupation === 'CaravanGuard'">
                        unit. They can be found protecting {{ troopObj.culture }} caravans or inside of {{ troopObj.culture }} taverns.
                    </template>
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
