<script setup>
const props = defineProps({townObj: Object});
</script>
<!------------------------------------------------------->
<template>
    <section>
        <div v-if="townObj !== null && townObj !== undefined" class="card-desc">
            <div>
                <h2>{{townObj.name}}</h2>
                <p>{{townObj.name}} is a town of the {{townObj.culture}}, ruled by the {{townObj.owner_name}} clan.</p>
            </div>
            <hr />
            <div>
                <h3>Description</h3>
                <p v-if="townObj.desc_text !== null">{{townObj.desc_text}}</p>
                <p v-else>N/A</p>
            </div>
            <hr />
            <div>
                <h3>Stats</h3>
                <table class="ratings-table">
                    <tr>
                        <th>X-Position</th>
                        <td>{{townObj.x_position}}</td>
                    </tr>
                    <tr>
                        <th>Y-Position</th>
                        <td>{{townObj.y_position}}</td>
                    </tr>
                    <tr>
                        <th>Prosperity</th>
                        <td>{{townObj.prosperity}}</td>
                    </tr>
                    <tr>
                        <th>Wall Level</th>
                        <td>{{townObj.wall_level}}</td>
                    </tr>
                </table>
            </div>
        </div>
    </section>
</template>
<!------------------------------------------------------->
<style scoped>
.ratings-table {
    background-color: var(--bluegray-800);
    border-radius: 10px;
}

th,
td {
    padding: 20px 35px;
}

th {
    font-size: 1.5rem;
    
}

td {
    font-size: 2rem;
    font-weight: 700;
    color: var(--bluegray-100);
}

h2 {
    text-transform: capitalize;
    font-size: 3rem;
    font-weight: 700;
    margin: 0 0 20px;
    border: 0;
    padding: 0;
}

h3 {
    font-size: 2rem;
    margin: 0 0 15px;
}

h4 {
    font-size: 1.3rem;
    color: var(--bluegray-100);
    margin: 25px 0 10px;
}

section > div {
    width: 96%;
    max-width: 40rem;
    margin: 0 auto 3rem;
    padding: 40px;
    border-radius: 20px;
    background-color: var(--bluegray-900);
    color: var(--yellow-300);
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
}

section > div > div {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

span {
    color: var(--bluegray-100);
    font-size: 1.5rem;
}

p {
    color: var(--bluegray-100);
    font-size: 1.2rem;
}

input {
    position: static;
    z-index: 1;
    width: 80%;
    height: 10rem;
    border: 0;
    padding: 0;
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
</style>
