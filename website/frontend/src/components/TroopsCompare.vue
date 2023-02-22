<script setup lang="ts">
import { ref, toRef } from 'vue'

import AutoComplete from 'primevue/autocomplete'
import type AutoCompleteDropdownClickEvent from 'primevue/autocomplete'
import Chart from "primevue/chart"

import type { troops as troopsIntr } from "@/interfaces/indexIntr"


const props = defineProps<{
    troopsArr: troopsIntr[]
}>()

const chartTroop1 = ref({
    'one_handed': 30,
    'two_handed': 10,
    'polearm': 30,
    'bow': 10,
    'crossbow': 30,
    'throwing': 10,
    'riding': 30,
    'athletics': 10
})
const chartTroop2 = ref({
    'one_handed': 10,
    'two_handed':20,
    'polearm': 10,
    'bow': 20,
    'crossbow': 10,
    'throwing': 20,
    'riding': 10,
    'athletics': 20
})

// interface troopSkillIntr {
//     one_handed: number
//     two_handed: number
//     polearm: number
//     bow: number
//     crossbow: number
//     throwing: number
//     riding: number
//     athletics: number
// }
interface chartIntr {
    label: string,
    backgroundColor: String,
    borderColor: String,
    pointBackgroundColor: String,
    pointBorderColor: String,
    pointHoverBackgroundColor: String,
    pointHoverBorderColor: String,
    data: number[]
}


const chartData = ref({
    labels: ['One Handed', 'Two Handed', 'Polearm', 'Bow', 'Crossbow', 'Throwing', 'Riding', 'Athletics'],
    datasets: [
        {
            label: 'N/A',
            backgroundColor: 'rgba(100,100,255,0.2)',
            borderColor: 'rgba(100,100,255,1)',
            pointBackgroundColor: 'rgba(50,50,255,1)',
            pointBorderColor: 'rgba(50,50,255,1)',
            pointHoverBackgroundColor: 'rgba(50,50,255,1)',
            pointHoverBorderColor: 'rgba(50,50,255,1)',
            data: [
                chartTroop1.value.one_handed,
                chartTroop1.value.two_handed,
                chartTroop1.value.polearm,
                chartTroop1.value.bow,
                chartTroop1.value.crossbow,
                chartTroop1.value.throwing,
                chartTroop1.value.riding,
                chartTroop1.value.athletics
            ]
        },
        {
            label: 'N/A',
            backgroundColor: 'rgba(255,50,50,0.2)',
            borderColor: 'rgba(255,50,50,1)',
            pointBackgroundColor: 'rgba(255,100,100,1)',
            pointBorderColor: 'rgba(255,100,100,1)',
            pointHoverBackgroundColor: 'rgba(255,100,100,1)',
            pointHoverBorderColor: 'rgba(255,100,100,1)',
            data: [
                chartTroop2.value.one_handed,
                chartTroop2.value.two_handed,
                chartTroop2.value.polearm,
                chartTroop2.value.bow,
                chartTroop2.value.crossbow,
                chartTroop2.value.throwing,
                chartTroop2.value.riding,
                chartTroop2.value.athletics
            ]
        }
    ]
})

const chartOptions = ref({
    resizeDelay: 20,
    plugins: {
        legend: {
            labels: {
                color: 'rgb(149, 163, 184)',
                font: function(context: any) {
                    let width = context.chart.width
                    let size = width / 26
                    return {
                        size: size,
                        weight: 600
                    }
                },
                padding: 20
            }
        }
    },
    elements: {
        line: {
            tension: 0.01
        }
    },
    scales: {
        r: {
            spanGaps: true,
            ticks: { 
                stepSize: 20,
                color: 'rgb(255, 205, 54)',
                backdropColor: 'rgba(50, 57, 67, 1)',
                backdropPadding: 2,
                font: function(context: any) {
                    let width = context.chart.width
                    let size = width / 48
                    return {
                        size: size,
                        weight: 600
                    }
                }
            },
            suggestedMin: 0,
            suggestedMax: 100,
            pointLabels: {
                color: '#fff',
                font: function(context: any) {
                    let width = context.chart.width
                    let size = width / 40
                    return {
                        size: size,
                        weight: 600
                    }
                }
            },
            grid: {
                color: '#fff',
            },
            angleLines: {
                color: '#fff'
            }
        }
    }
})


const troops = toRef(props, 'troopsArr')
const selectedTroop1 = ref()
const filteredTroops1 = ref()
const selectedTroop2 = ref()
const filteredTroops2 = ref()


const searchTroop = (event: AutoCompleteDropdownClickEvent, flag: number) => {
    setTimeout(() => {
        if (flag === 0) {
            if (!event.query.trim().length) {
                filteredTroops1.value = [...troops.value]
            }
            else {
                filteredTroops1.value = troops.value.filter((trp) => {
                    return trp.name.toLowerCase().startsWith(event.query.toLowerCase())
                })
            }
        } else if (flag === 1) {
            if (!event.query.trim().length) {
                filteredTroops2.value = [...troops.value]
            }
            else {
                filteredTroops2.value = troops.value.filter((trp) => {
                    return trp.name.toLowerCase().startsWith(event.query.toLowerCase())
                })
            }
        }
    }, 250)
}

function logSelectedValue(event: AutoCompleteDropdownClickEvent, flag: number) {
    const labels: string[] = chartData.value.labels
    const datasets: chartIntr = chartData.value.datasets[flag]

    if (flag === 0) {
        chartTroop1.value = Object.assign({}, event.value)
        datasets.label = selectedTroop1.value.name
        for (let i of labels) {
            const label: string = i.replaceAll(' ', '_').toLowerCase()
            const labelIndex: number = labels.indexOf(i)
            datasets.data[labelIndex] = chartTroop1.value[label]
        }
    } else if (flag === 1) {
        chartTroop2.value = Object.assign({}, event.value)
        datasets.label = selectedTroop2.value.name
        for (let i of labels) {
            const label = i.replaceAll(' ', '_').toLowerCase()
            const labelIndex = labels.indexOf(i)
            datasets.data[labelIndex] = chartTroop2.value[label]
        }
    }
}
</script>
<!------------------------------------------------------------------------->
<template>
<div class="chart-section">
    <h3>Comparison Chart</h3>
    <AutoComplete v-model="selectedTroop1" :suggestions="filteredTroops1" @complete="searchTroop($event, 0)" @item-select="logSelectedValue($event, 0)" :dropdown="true" field="name" forceSelection spellcheck="false" placeholder="Select a troop...">
        <template #item="slotProps">
            <div class="country-item">
                <div class="ml-2">{{slotProps.item.name}}</div>
            </div>
        </template>
    </AutoComplete>
    <AutoComplete v-model="selectedTroop2" :suggestions="filteredTroops2" @complete="searchTroop($event, 1)" @item-select="logSelectedValue($event, 1)" :dropdown="true" field="name" forceSelection spellcheck="false" placeholder="Select a troop...">
        <template #item="slotProps">
            <div class="country-item">
                <div class="ml-2">{{slotProps.item.name}}</div>
            </div>
        </template>
    </AutoComplete>
    <div class="chart-container">
        <Chart type="radar" :data="chartData" :options="chartOptions" />
        <small>Note: each level on the chart increments by 20</small>
    </div>
</div>

</template>
<!------------------------------------------------------------------------->
<style scoped>
h3 {
    color: var(--yellow-300);
    font-size: 2.3rem;
    font-weight: bold;
    /* text-decoration: underline; */
    margin: 0;
    padding: 20px;
}

.chart-section {
    margin: 6rem auto;
    width: 94%;
    max-width: 900px;
    
    background: var(--bluegray-900);
    border-radius: 30px;
}

.chart-container {
    width: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    padding: 0 5px 25px;
}

.p-autocomplete {
    margin: 1rem;
}

.p-chart {
    /* min-width: 340px; */
    width: 100%;
    margin: 1rem 0 0;
}


</style>
