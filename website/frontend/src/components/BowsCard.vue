<script setup>
import { ref } from "vue";


const props = defineProps({bowObj: Object});
const strSubtype = ref('blank');


const formatBowSubtype = (subtype) => {
    if (subtype === 'crossbow_light') {
        strSubtype.value = 'light crossbow';
        return 'light crossbow';
    }
    else if (subtype === 'long_bow'){
        strSubtype.value = 'longbow';
        return 'longbow';
    }
    else {
        strSubtype.value = subtype;
        return subtype
    }
};

const calculateTier = (ratingType, ratingVal) => {
    const dmgMax = 100;
    const speedMax = 94;
    const mslMax = 97;
    const accMax = 100;

    let tier;

    if (ratingType === 'damage') {
        tier = ratingVal / dmgMax;
    } else if (ratingType === 'speed_rating') {
        tier = ratingVal / speedMax;
    } else if (ratingType === 'missile_speed') {
        tier = ratingVal / mslMax;
    } else if (ratingType === 'accuracy') {
        tier = ratingVal / accMax;
    }

    const red = '#dc3545';
    const orange = '#fd7e14';
    const yellow = '#f8ff15';
    const green = '#4ad3ab';
    const blue = '#69a5fe';
    const purple = '#7f5bff'

    if (tier == 1) {
        return purple;
    } else if (tier > 0.80) {
        return blue;
    } else if (tier > 0.60) {
        return green;
    } else if (tier > 0.40) {
        return yellow;
    } else if (tier > 0.20) {
        return orange;
    } else {
        return red;
    }
}
</script>
<!------------------------------------------------------->
<template>
    <section>
        <div v-if="bowObj !== null && bowObj !== undefined" class="card-desc">
            <div>
                <h2>{{bowObj.name || 'Nothing passed yet'}}</h2>
                <p>
                    <span>The {{bowObj.name}} is a {{formatBowSubtype(bowObj.subtype)}} of the {{bowObj.culture}} culture.</span>
                    <span v-if="strSubtype === 'bow' || strSubtype === 'fast crossbow'"> It can be fired and reloaded on a mount.</span>
                    <span v-else-if="strSubtype === 'longbow'">It cannot be fired or reloaded on a mount.</span>
                    <span v-else-if="strSubtype === 'crossbow'">It can be fired on amount, but not reloaded.</span>
                </p>
            </div>
            <hr />
            <div>
                <h3>Ratings</h3>
                <div class="btn-container">
                    <button type="button" id="bow-help-btn" data-bs-toggle="dropdown" aria-expanded="false">
                        <i class="pi pi-question-circle"></i>
                    </button>
                    <ul class="dropdown-menu" aria-labelledby="bow-help-btn">
                        <li><h6 class="dropdown-header">Damage</h6></li>
                        <li><span>The base amount of damage that can be dealt</span></li>
                        <li><h6 class="dropdown-header">Speed Rating</h6></li>
                        <li><span>How quickly the bow can reload and fire</span></li>
                        <li><h6 class="dropdown-header">Missile Speed</h6></li>
                        <li><span>How quickly the arrow/bolt reaches its target</span></li>
                        <li><h6 class="dropdown-header">Accuracy</h6></li>
                        <li><span>The base accuracy of the bow</span></li>
                        <li><h6 class="dropdown-header">Difficulty</h6></li>
                        <li><span>The Bow skill level required to wield the bow</span></li>
                    </ul>
                </div>
                <table class="ratings-table">
                    <tr>
                        <th>Damage</th>
                        <td :style="{ color: calculateTier('damage', bowObj.damage) }">
                            {{bowObj.damage}}
                        </td>
                    </tr>
                    <tr>
                        <th>Speed Rating</th>
                        <td :style="{ color: calculateTier('speed_rating', bowObj.speed_rating) }">
                            {{bowObj.speed_rating}}
                        </td>
                    </tr>
                    <tr>
                        <th>Missile Speed</th>
                        <td :style="{ color: calculateTier('missile_speed', bowObj.missile_speed) }">
                            {{bowObj.missile_speed}}
                        </td>
                    </tr>
                    <tr>
                        <th>Accuracy</th>
                        <td :style="{ color: calculateTier('accuracy', bowObj.accuracy) }">
                            {{bowObj.accuracy}}
                        </td>
                    </tr>
                    <tr>
                        <th>Difficulty</th>
                        <td>
                            {{bowObj.difficulty}}
                        </td>
                    </tr>
                    <tr>
                        <th>Weight</th>
                        <td >
                            {{bowObj.weight}}
                        </td>
                    </tr>
                </table>
                <h4>Key:</h4>
                <ul>
                    <li><span style="color: #dc3545;">red</span> = poor</li>
                    <li><span style="color: #fd7e14;">orange</span> = below average</li>
                    <li><span style="color: #f8ff15;">yellow</span> = average</li>
                    <li><span style="color: #4ad3ab;">green</span> = above average</li>
                    <li><span style="color: #69a5fe;">blue</span> = amazing</li>
                    <li><span style="color: #7f5bff;">purple</span> = the best in all of Calradia</li>
                </ul>
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
    max-width: 40rem;
    margin: 0 auto 3rem;
    padding: 40px;
    border-radius: 30px;
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

.dropdown-menu {
    background-color: var(--bluegray-600) !important;
    padding: 1rem;
    position: absolute;
    left: 50;
}

.dropdown-menu h6 {
    font-size: 1.2rem;
    color: gold;
    padding-left: 0; 
}

.dropdown-menu span {
    font-size: 1rem;
    font-weight: 500;
    color: var(--bluegray-100);
    padding-left: 15px;
}

button {
    border: 0;
    border-radius: 100%;
    background-color: rgba(150,150,150,0);
    padding: 0;
}

i {
    color: var(--yellow-400);
    border-radius: 100%;
    background-color: rgba(150,150,150,0);
    box-shadow: 0 0 1px 2px rgba(150,150,150,0);
    transition: color 0.5s, background-color 0.5s, box-shadow 0.5s;
}

i:hover {
    color: var(--yellow-300);
    background-color: rgba(150,150,150,0.3);
    box-shadow: 0 0 1px 2px rgba(150,150,150,0.3);
}
</style>
