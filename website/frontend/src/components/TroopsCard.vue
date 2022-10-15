<script setup lang="ts">
const props = defineProps({troopObj: Object})


const fromatTroopGroup = (troopGroup: string) => {
    if (troopGroup === 'HorseArcher') {
        return 'horse archer'
    } else if (troopGroup === 'Infantry'){
        return troopGroup.toLowerCase()
    } else {
        return troopGroup.toLowerCase()
    }
};


function calculateLevelTier(levelVal :number) {
    const tier = (levelVal - 1) / 5

    if (tier === 1) {
        return `${tier}st tier`
    } else if (tier === 2) {
        return `${tier}nd tier`
    } else if (tier === 3) {
        return `${tier}rd tier`
    } else {
        return `${tier}th tier`
    }
}


function calculateSkillTier(skillType: string, skillVal: number) {
    let tier: number

    if (skillType === 'one_handed' || skillType === 'two_handed') {
        tier = skillVal / 220
    } else if (skillType === 'polearm' || skillType === 'bow') {
        tier = skillVal / 260
    } else if (skillType === 'crossbow') {
        tier = skillVal / 140
    } else if (skillType === 'throwing') {
        tier = skillVal / 150
    } else if (skillType === 'riding') {
        tier = skillVal / 200
    } else if (skillType === 'athletics') {
        tier = skillVal / 180
    } else {
        throw new Error("could not determine skill type")
    }

    const red = '#dc3545'
    const orange = '#fd7e14'
    const yellow = '#f8ff15'
    const green = '#4ad3ab'
    const blue = '#69a5fe'
    const purple = '#b851ff'

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
        <div v-if="troopObj" class="card-desc">
            <div>
                <h2>{{troopObj.name || 'Nothing passed yet'}}</h2>
                <p v-if="troopObj.occupation === 'Soldier'">
                    <span>The {{troopObj.name}} is a {{calculateLevelTier(troopObj.level)}} {{fromatTroopGroup(troopObj.default_group)}} unit of the {{troopObj.culture}} culture.</span>
                    <span v-if="troopObj.level == 31"> They can be found in {{troopObj.culture}} villages.</span>
                    <span v-else> They can be found in {{troopObj.culture}} villages and towns.</span>
                </p>
                <p v-else-if="troopObj.occupation === 'Mercenary'">
                    The {{troopObj.name}} is a {{calculateLevelTier(troopObj.level)}} {{fromatTroopGroup(troopObj.default_group)}} mercenary troop. They can be found inside of any town tavern.
                </p>
                <p v-else-if="troopObj.occupation === 'CaravanGuard'">
                    The {{troopObj.name}} is a {{calculateLevelTier(troopObj.level)}} {{fromatTroopGroup(troopObj.default_group)}} unit. They can be found protecting {{troopObj.culture}} caravans or inside of {{troopObj.culture}} taverns.
                </p>
            </div>
            <hr />
            <div>
                <h3>Ratings</h3>
                <table class="ratings-table">
                    <tr>
                        <th>One Handed</th>
                        <td :style="{ color: calculateSkillTier('one_handed', troopObj.one_handed) }">
                            {{troopObj.one_handed}}
                        </td>
                    </tr>
                    <tr>
                        <th>Two Handed</th>
                        <td :style="{ color: calculateSkillTier('two_handed', troopObj.two_handed) }">
                            {{troopObj.two_handed}}
                        </td>
                    </tr>
                    <tr>
                        <th>Polearm</th>
                        <td :style="{ color: calculateSkillTier('polearm', troopObj.polearm) }">
                            {{troopObj.polearm}}
                        </td>
                    </tr>
                    <tr>
                        <th>Bow</th>
                        <td :style="{ color: calculateSkillTier('bow', troopObj.bow) }">
                            {{troopObj.bow}}
                        </td>
                    </tr>
                    <tr>
                        <th>Crossbow</th>
                        <td :style="{ color: calculateSkillTier('crossbow', troopObj.crossbow) }">
                            {{troopObj.crossbow}}
                        </td>
                    </tr>
                    <tr>
                        <th>Throwing</th>
                        <td :style="{ color: calculateSkillTier('throwing', troopObj.throwing) }">
                            {{troopObj.throwing}}
                        </td>
                    </tr>
                    <tr>
                        <th>Riding</th>
                        <td :style="{ color: calculateSkillTier('riding', troopObj.riding) }">
                            {{troopObj.riding}}
                        </td>
                    </tr>
                    <tr>
                        <th>Athletics</th>
                        <td :style="{ color: calculateSkillTier('athletics', troopObj.athletics) }">
                            {{troopObj.athletics}}
                        </td>
                    </tr>
                </table>
                <h4>Key:</h4>
                <ul>
                    <li><span style="color: #dc3545;">red</span> = poor / farthest from the best</li>
                    <li><span style="color: #fd7e14;">orange</span> = below average / halfway between worst and average</li>
                    <li><span style="color: #f8ff15;">yellow</span> = average / halfway between worst and best</li>
                    <li><span style="color: #4ad3ab;">green</span> = above average / halfway between average and best</li>
                    <li><span style="color: #69a5fe;">blue</span> = amazing / closest to the best</li>
                    <li><span style="color: #b851ff;">purple</span> = the best</li>
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
    /* margin: 0 0 30px; */
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

/* span {
    color: var(--bluegray-100);
    font-size: 1.5rem;
} */

p {
    color: var(--bluegray-100);
    font-size: 1.5rem;
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

td span {
    padding: 10px;
    border: 1px solid rgba(230, 212, 52, 0.2);
    border-radius: 90%;
    box-shadow: 0 0 5px 5px rgba(230, 212, 52, 0.2);
}
</style>
