<script setup>
import { ref } from 'vue';

import AutoComplete from 'primevue/autocomplete';

const props = defineProps({troopsArr: Array});

const chartData = ref({
    labels: ['One Handed', 'Two Handed', 'Polearm', 'Bow', 'Crossbow', 'Throwing', 'Riding', 'Athletics'],
    datasets: [
        {
            label: 'My First dataset',
            backgroundColor: 'rgba(179,181,198,0.2)',
            borderColor: 'rgba(179,181,198,1)',
            pointBackgroundColor: 'rgba(179,181,198,1)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgba(179,181,198,1)',
            data: [65, 59, 90, 81, 56, 55, 40]
        },
        {
            label: 'My Second dataset',
            backgroundColor: 'rgba(255,99,132,0.2)',
            borderColor: 'rgba(255,99,132,1)',
            pointBackgroundColor: 'rgba(255,99,132,1)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgba(255,99,132,1)',
            data: [28, 48, 40, 19, 96, 27, 100]
        }
    ]
});

const chartOptions = ref({
    plugins: {
        legend: {
            labels: {
                color: '#495057'
            }
        }
    },
    scales: {
        r: {
            pointLabels: {
                color: '#495057',
            },
            grid: {
                color: '#ebedef',
            },
            angleLines: {
                color: '#ebedef'
            }
        }
    }
});
</script>
<!------------------------------------------------------------------------->
<template>
<div>
    <AutoComplete v-model="selectedCountry1" :suggestions="filteredCountries" @complete="searchCountry($event)" field="name" />
</div>
<div>
    <Chart type="radar" :data="chartData" :options="chartOptions" />
</div>
</template>
<!------------------------------------------------------------------------->
<style scoped>

</style>
