<script setup>
const props = defineProps({kingdomObj: Object});


const formatColor = (color) => {
    const hexValue = color.slice(-6);
    return '#' + hexValue;
};
</script>
<!------------------------------------------------------->
<template>
    <section>
        <div v-if="kingdomObj !== null && kingdomObj !== undefined" class="card-desc">
            <div>
                <h2>{{kingdomObj.name || 'Nothing passed yet'}}</h2>
                <span>
                    The {{kingdomObj.title}} is a Calradian kingdom of the {{kingdomObj.culture}} culture, ruled by its {{kingdomObj.ruler_title}}.
                </span>
            </div>
            <hr />
            <div>
                <h3>History</h3>
                <p>{{kingdomObj.desc_text}}</p>
            </div>
            <hr />
            <div>
                <h3>Primary Banner Color</h3>
                <input type="color" :value="formatColor(kingdomObj.primary_banner_color)" disabled>
                <span>Hex: {{formatColor(kingdomObj.primary_banner_color)}}</span>
            </div>
        </div>
    </section>
</template>
<!------------------------------------------------------->
<style scoped>
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
    margin: 0 0 30px;
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
</style>
