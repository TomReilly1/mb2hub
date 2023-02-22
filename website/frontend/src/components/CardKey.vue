<script setup lang="ts">
</script>
<!------------------------------------------------------->
<template>
    <div>
        <h4>Key</h4>
        <ul>
            <li>
                <span class="rank bad">red</span> = bad
            </li>
            <li>
                <span class="rank below-average">orange</span> = below average
            </li>
            <li>
                <span class="rank average">yellow</span> = average
            </li>
            <li>
                <span class="rank above-average">green</span> = above average
            </li>
            <li>
                <span class="rank great">blue</span> = great
            </li>
            <li>
                <span class="rank best">purple</span> = the best in all of Calradia
            </li>
        </ul>
    </div>
</template>
<!------------------------------------------------------->
<style scoped>
h4 {
    margin: 5px 0;
}

div {
    margin-top: 30px;
    background-color: rgba(33, 38, 44, 0.2);
    border-radius: 5px;
    padding: 0px 10px 10px 10px;
}

ul {
    text-align: left;
    margin: 5px 0;
    padding-left: 20px;
}

li {
    color: var(--text-color);
}

li, li > * {
    font-size: 1.1rem;
}

li > span {
    font-weight: 700;
}
</style>
