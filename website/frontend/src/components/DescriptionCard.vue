<script setup>
import { ref, onMounted } from "vue";

const props = defineProps({objects: Array})

// const objects = ref();

</script>

<template>
<section class="container">
    <div v-for="object of objects" class="card">
        <ul class="list key">
            <li v-for="(value, key) in object">
                {{key}}:
            </li>
        </ul>
        <ul class="list value">
            <li v-for="(value, key) in object">
                {{value}}
            </li>
        </ul>
    </div>
</section>

</template>

<style scoped>
    .container {
        display: flex;
        flex-direction: column;
        flex-wrap: wrap;
        justify-content: space-around;
        align-items: center;
        margin: 1rem auto;
    }

    .card {
        display: flex;
        flex-direction: row;
        width: 80%;
        min-width: 300px;
        background-color: cornflowerblue;
        padding: 0;
        margin: 1rem;
        text-align: left;
    }

    .list {
        display: flex;
        flex-direction: column;
        list-style: none;
        width: 50%;
        margin: 0;
        padding: 0;
    }

    .list.item {
        font-size: 1.3rem;
    }

    .list.key > li{
        font-size: 1.3rem;
    }

    .list.value > li{
        font-size: 1.5rem;
    }    

</style>
