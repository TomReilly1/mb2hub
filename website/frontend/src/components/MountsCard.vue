<script setup lang="ts">
import { ref } from "vue"


const props = defineProps({mountObj: Object})
const strSubtype = ref('blank')


const formatBowSubtype = (subtype: string) => {
    if (subtype === 'crossbow_light') {
        strSubtype.value = 'light crossbow'
        return 'light crossbow'
    }
    else if (subtype === 'long_bow'){
        strSubtype.value = 'longbow'
        return 'longbow'
    }
    else {
        strSubtype.value = subtype
        return subtype
    }
};

const calculateTier = (ratingType: string, ratingVal: number) => {
    const speedMax = 68
    const speedmin = 44
    const speedComp = speedMax - speedmin
    const mnvrMax = 82
    const mnvrMin = 55
    const mnvrComp = mnvrMax - mnvrMin
    const hlthMax = 300
    const hlthMin = 200
    const hlthComp = hlthMax - hlthMin


    let tier: number


    if (ratingType === 'maneuver') {
        tier = (ratingVal-mnvrMin) / mnvrComp
    } else if (ratingType === 'speed') {
        tier = (ratingVal-speedmin) / speedComp
    } else if (ratingType === 'health') {
        tier = (ratingVal-hlthMin) / hlthComp
    } else {
        throw new Error("could not determine rating type")
    }

    const red = '#dc3545'
    const orange = '#fd7e14'
    const yellow = '#f8ff15'
    const green = '#4ad3ab'
    const blue = '#69a5fe'
    const purple = '#7f5bff'

    if (tier == 1) {
        return purple
    } else if (tier > 0.80) {
        return blue
    } else if (tier > 0.60) {
        return green
    } else if (tier > 0.40) {
        return yellow
    } else if (tier > 0.20) {
        return orange
    } else {
        return red
    }
}
</script>
<!------------------------------------------------------->
<template>
    <section>
        <div v-if="mountObj" class="card-desc">
            <div>
                <h2>{{mountObj.name}}</h2>
                <p>
                    <span>The {{mountObj.name}} is a mount of the {{mountObj.culture}} culture.</span>
                    <span v-if="mountObj.is_merchandise"> It is considered merchandise, meaning it can be bought from town markets or villages.</span>
                    <span v-else>It is not considered merchandise, meaning it cannot be bought from town markets or villages, and must be gained through tournaments or gifts. This also means troops cannot use them to upgrade to mounted units.</span>
                    <span v-if="mountObj.subtype === 'war_horse'"> It is a war horse, meaning it can be used to upgrade certain mounted troops, typically those of higher tiers such as tier 3, 4, or 5.</span>
                </p>
            </div>
            <hr />
            <div>
                <h3>Ratings</h3>
                <table class="ratings-table">
                    <tr>
                        <th>Charge Damage</th>
                        <td>
                            {{mountObj.charge_damage}}
                        </td>
                    </tr>
                    <tr>
                        <th>Maneuver</th>
                        <td :style="{ color: calculateTier('maneuver', mountObj.maneuver) }">
                            {{mountObj.maneuver}}
                        </td>
                    </tr>
                    <tr>
                        <th>Speed</th>
                        <td :style="{ color: calculateTier('speed', mountObj.speed) }">
                            {{mountObj.speed}}
                        </td>
                    </tr>
                    <tr>
                        <th>Health</th>
                        <td :style="{ color: calculateTier('health', mountObj.health) }">
                            {{mountObj.health}}
                        </td>
                    </tr>
                    <tr>
                        <th>Difficulty</th>
                        <td>
                            {{mountObj.difficulty}}
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
                    <li><span style="color: #ffffff;">white</span> = not applicable / stats too similar</li>
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
