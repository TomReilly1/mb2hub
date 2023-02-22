<script setup lang="ts">
import { ref, reactive, onMounted, onBeforeMount, watch, computed } from "vue"
import { useRoute } from 'vue-router'
import router from "@/router"

import type { card as cardIntr, rankings as rankIntr, rankingFormats as rankFormatsIntr} from "@/interfaces/indexIntr"


const route = useRoute()
const props = defineProps<{
    dataObj: cardIntr | undefined
}>()

const ratings = (l_dataObj: cardIntr | undefined) => {
    if (!props.dataObj) {
        return
    }
    if (!l_dataObj) {
        return
    }

    const attributes: Record<string, any> = l_dataObj.cardData
    let l_ratings: Record<string, number> = {}

    for (const i in attributes) {
        if (typeof attributes[i] == 'number') {
            l_ratings[i] = attributes[i]
        }
    }

    return l_ratings
}

const ratingsWithoutRanks = (l_dataObj: cardIntr | undefined) => {
    if (!l_dataObj) {
        return
    }
    const l_ratings: Record<string, number> | undefined = ratings(l_dataObj)
    if (!l_ratings) {
        return
    }

    const ratingsEntries: [string, number][] = Object.entries(l_ratings)
    const ratingsWithRanksKeys = Object.keys(l_dataObj.rankData.attributes)

    let ratingsWithoutRanks: Record<string, number> = {}
    for (const [key, val] of ratingsEntries) {
        if (ratingsWithRanksKeys.includes(key)) {
            continue
        } else {
            ratingsWithoutRanks[key] = val
        }
    }

    console.log(ratingsWithoutRanks)

    return ratingsWithoutRanks
}

const totalRecords = () => {
    return props.dataObj?.rankData.totalRecords
}

const roundPercentRank = (percent: number) => {
    return (percent * 100).toFixed(2).toString() + '%'
}

const capitalizeString = (value: string) => {
    const firstLetterCaptlz: string = value.slice(0, 1).toUpperCase()
    return firstLetterCaptlz + value.slice(1)
}

const generatePercentRankColor = (attrName: string) => {
    let rank_perc: number

    if (props.dataObj === undefined) {
        return
    } else {
        try {
            rank_perc = props.dataObj.rankData.attributes[attrName].percent
        } catch (error) {
            return
        }
    }
    
    if (rank_perc == 1) {
        return 'best'
    } else if (rank_perc > 0.80) {
        return 'great'
    } else if (rank_perc > 0.60) {
        return 'above-average'
    } else if (rank_perc > 0.40) {
        return 'average'
    } else if (rank_perc > 0.20) {
        return 'below-average'
    } else {
        return 'bad'
    }
}

const generateStandardRankColor = (attrName: string) => {
    let rank_stan: number 
    let total_count: number
    let step_amnt: number
    const l_totalRecords: number | undefined = totalRecords()

    if (props.dataObj === undefined || l_totalRecords === undefined) {
        return
    } else {
        try {
            rank_stan = props.dataObj.rankData.attributes[attrName].standard
            total_count = l_totalRecords
            step_amnt = total_count / 5
        } catch (error) {
            return
        }
    }

    if (rank_stan == 1) {
        return 'best'
    } else if (rank_stan < step_amnt) {
        return 'great'
    } else if (rank_stan < (step_amnt*2)) {
        return 'above-average'
    } else if (rank_stan < (step_amnt*3)) {
        return 'average'
    } else if (rank_stan < (step_amnt*4)) {
        return 'below-average'
    } else {
        return 'bad'
    }
}
</script>
<!------------------------------------------------------->
<template>
    <div>
        <h3>Ratings</h3>
        <table v-if="dataObj" class="ratings-table">
            <tr>
                <th></th>
                <th>Rating</th>
                <th>Percentile Rank</th>
                <th>Standard Rank</th>
            </tr>
            <tr v-for="(value, key) in dataObj.rankData.attributes">
                <th>{{ capitalizeString(key) }}</th>
                <td class="rank">{{ dataObj.cardData[key] }}</td>
                <td class="rank" :class="generatePercentRankColor(key)">{{ roundPercentRank(value.percent) }}</td>
                <td class="rank" :class="generateStandardRankColor(key)">{{ value.standard }}</td>
            </tr>
            <tr v-for="(value, key) in ratingsWithoutRanks">
                <th>{{ key }}</th>
                <td class="rank">{{ value }}</td>
                <td class="rank">&mdash;</td>
                <td class="rank">&mdash;</td>
            </tr>
        </table>
    </div>
</template>
<!------------------------------------------------------->
<style scoped>
.rank.average {
    color: white;
}
.rank.below-average {
    color: var(--yellow-400);
}
.rank.bad {
    color: var(--red-400);
}
.rank.above-average {
    color: var(--green-400);
}
.rank.great {
    color: var(--blue-400);
}
.rank.best {
    color: var(--purple-400);
}

ul {
    text-align: left;
}

li, li > * {
    font-size: 1.1rem;
}

li > span {
    font-weight: 700;
}

.ratings-table {
    background-color: var(--bluegray-800);
    width: 100%;
}

table,th,td {
    border: 1px solid var(--bluegray-600);
    border-collapse: collapse;
}

th,
td {
    padding: 5px 10px;
}

th {
    font-size: 1.1rem;
    
}

td {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--bluegray-200);
}

h3 {
    font-size: 2rem;
    margin: 0 0 15px;
}

</style>
