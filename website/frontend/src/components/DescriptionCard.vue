<script setup>
import { ref, onMounted } from "vue";

const props = defineProps({objects: Array})

// const objects = ref();

</script>

<template>
<section class="card container">
    <div v-for="object of objects" class="desc card">
        <ul>
            <li v-for="(value, key) in object" class="desc list items">
                {{key}}: {{value}}
            </li>
        </ul>
    </div>
</section>

</template>

<style scoped>
    .desc.card {
        width: 15rem;
        background-color: cornflowerblue;
        padding: 0 0 0 1rem;
        margin: 1rem;
        text-align: left;
    }

    section.container {
        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        justify-content: space-around;
        margin: 1rem auto;
    }
</style>
