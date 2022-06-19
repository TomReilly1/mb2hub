<script setup>
const props = defineProps({armorObj: Object});


const formatArmorType = (armorType) => {
    if (armorType === 'Cape') {
        return 'shoulder armor';
    }
    else {
        const arr = armorType.split(/(?=[A-Z])/);
        const lowerArr = arr.map(e => e.toLowerCase());
        const lowerStr = lowerArr.join(' ');
        
        return lowerStr;
    }
};


// type is the 5 types of armor, cover is the 4 coverage areas
function calculateTier(armorType, armorCover, armorVal) {
    const headMax = {'head': 54};
    const shoulderMax = {'body': 22, 'arm': 12};
    const bodyMax = {'body': 57, 'arm': 20, 'leg': 25};
    const armMax = {'arm': 25};
    const legMax = {'leg': 26};

    let tier;

    if (armorType === 'HeadArmor') {
        tier = armorVal / headMax.head;
    }
    else if (armorType === 'Cape') {
        if (armorCover === 'body') {
            tier = armorVal / shoulderMax.body;
        }
        else if (armorCover === 'arm') {
            tier = armorVal / shoulderMax.arm;
        }
    }
    else if (armorType === 'BodyArmor') {
        if (armorCover === 'body') {
            tier = armorVal / bodyMax.body;
        }
        else if (armorCover === 'arm') {
            tier = armorVal / bodyMax.arm;
        }
        else if (armorCover === 'leg') {
            tier = armorVal / bodyMax.leg;
        }
    }
    else if (armorType === 'HandArmor') {
        tier = armorVal / armMax.arm;
    }
    else if (armorType === 'LegArmor') {
        tier = armorVal / legMax.leg;
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
        <div v-if="armorObj !== null && armorObj !== undefined" class="card-desc">
            <div>
                <h2>{{armorObj.name || 'Nothing passed yet'}}</h2>
                <span>
                    The {{armorObj.name}} is a type of {{formatArmorType(armorObj.type)}} that is of {{armorObj.culture}} culture.
                </span>
            </div>
            <hr />
            <div>
                <h3>Ratings</h3>
                <table class="ratings-table">
                    <tr v-if="armorObj.type === 'HeadArmor'">
                        <th>Head Armor</th>
                        <td :style="{ color: calculateTier(armorObj.type, 'head', armorObj.head_armor) }">
                            {{armorObj.head_armor}}
                        </td>
                    </tr>
                    <tr v-if="armorObj.type === 'Cape' || armorObj.type === 'BodyArmor'">
                        <th>Body Armor</th>
                        <td :style="{ color: calculateTier(armorObj.type, 'body', armorObj.body_armor) }">
                            {{armorObj.body_armor}}
                        </td>
                    </tr>
                    <tr v-if="armorObj.type === 'Cape' || armorObj.type === 'BodyArmor' || armorObj.type === 'HandArmor'">
                        <th>Arm Armor</th>
                        <td :style="{ color: calculateTier(armorObj.type, 'arm', armorObj.arm_armor) }">
                            {{armorObj.arm_armor}}
                        </td>
                    </tr>
                    <tr v-if="armorObj.type === 'BodyArmor' || armorObj.type === 'LegArmor'">
                        <th>Leg Armor</th>
                        <td :style="{ color: calculateTier(armorObj.type, 'leg', armorObj.leg_armor) }">
                            {{armorObj.leg_armor}}
                        </td>
                    </tr>
                    <tr>
                        <th>Weight</th>
                        <td>{{armorObj.weight}}</td>
                    </tr>
                </table>
                <h4>Key:</h4>
                <ul>
                    <li><span style="color: #dc3545;">red</span> = poor</li>
                    <li><span style="color: #fd7e14;">orange</span> = below average</li>
                    <li><span style="color: #f8ff15;">yellow</span> = average</li>
                    <li><span style="color: #4ad3ab;">green</span> = above average</li>
                    <li><span style="color: #69a5fe;">blue</span> = amazing</li>
                    <li><span style="color: #7f5bff;">purple</span> = the best</li>
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
    border-radius: 5%;
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

/* hr {
    margin: 30px 0;
} */
</style>
