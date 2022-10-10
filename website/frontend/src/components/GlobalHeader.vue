<script setup lang="ts">
import { ref, onMounted } from "vue"
import Dropdown from "primevue/dropdown"
import SearchBar from "@/components/SearchBar.vue"

onMounted(() => {
    const navLinks = document.getElementsByClassName('route')
    const navbar = document.getElementById('navbar')

    for (let link of navLinks) {
        link.addEventListener('click', () => {
            navbar.classList.toggle('show')
        })
    }
})


const selectedLink = ref();

const groupedLinks = ref<{
    label: string
    items: {label: string, value: string}[];
}[]>
([
    {
        label: 'Animals',
        items: [
            {label: 'Mounts', value: 'mounts'}
        ]
    },
    {
        label: 'Equipment',
        items: [
            {label: 'Armors', value: 'armors'},
            {label: 'Bows', value: 'bows'}
        ]
    },
    {
        label: 'People',
        items: [
            {label: 'Lords', value: 'lords'},
            {label: 'Troops', value: 'troops'}
        ]
    },
    {
        label: 'Politics',
        items: [
            {label: 'Clans', value: 'clans'},
            {label: 'Cultures', value: 'cultures'},
            {label: 'Kingdoms', value: 'kingdoms'}
        ]
    },
    {
        label: 'Trading',
        items: [
            {label: 'Goods', value: 'goods'}
        ]
    },
    {
        label: 'Settlements',
        items: [
            {label: 'Castles', value: 'castles'},
            {label: 'Towns', value: 'towns'},
            {label: 'Villages', value: 'villages'}
        ]
    }
]);

const resetDropdown = () => {
    const navbar = document.querySelector('.navbar-concept')
    const drpdwn = navbar.querySelector('.p-dropdown.p-component.p-inputwrapper')
    const spn = drpdwn.querySelector('span.p-dropdown-label.p-inputtext')



    drpdwn.classList.toggle('p-inputwrapper-filled')
    spn.classList.toggle('p-placeholder')
    spn.textContent = 'Select concept'
}

</script>
<!------------------------------------------------------------------------------------>
<template>
<header>
    <nav class="navbar">
        <div class="navbar-item navbar-title">
            <router-link to="/" class="navbar-logo">MB2 Hub</router-link>
        </div>

        <div class="navbar-item navbar-concept">
            <Dropdown v-model="selectedLink" :options="groupedLinks" optionLabel="label" optionGroupLabel="label" optionGroupChildren="items" @change="resetDropdown()" scroll-height="250px" panelClass="navbar-concepts" placeholder="Select concept">
                <template #optiongroup="slotProps">
                    <div class="flex align-items-center">
                        {{slotProps.option.label}}
                    </div>
                </template>
                <template #option="slotProps">
                    <router-link :to="`/table/${slotProps.option.value}`" class="dropdown-item">{{slotProps.option.label}}</router-link>
                </template>
            </Dropdown>
        </div>

        <div class="navbar-item navbar-search">
            <SearchBar />
        </div>
    </nav>
</header>
</template>
<!------------------------------------------------------------------------------------>
<style scoped>
a.dropdown-item {
    display: flex;
    align-items: center;
    height: 2rem;
    width: 100%;
    margin: 0;
    padding: 0 0 0 20px;
    text-decoration: none;
    color: var(--bluegray-100);
}

a.dropdown-item:visited {
    color: var(--bluegray-100);
}


header {
    background-color: var(--bluegray-900);
    box-shadow: 0 0 7px 4px rgba(0, 0, 0, 0.3);
}

.navbar {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    padding: 0.5rem 1rem;
    width: 100%;
    height: 4rem;
}

.navbar-item {
    width: 300px;
    display: flex;
    justify-content: center;
    align-items: center;
}


.navbar-item.navbar-concept,
.navbar-item.navbar-title {
    width: 210px;
}

.navbar-item.navbar-search {
    justify-content: end;
    width: calc(100% - 420px);
}

.container-fluid {
  padding: 0 !important;
}

.navbar-item.navbar-concept .p-dropdown.p-component.p-inputwrapper {
    border: 0;
    background-color: var(--bluegray-900);
    transition: background-color 0.6s, box-shadow 0.6s;
}

.navbar-item.navbar-concept .p-dropdown.p-component.p-inputwrapper:hover {
    border: 0;
    background-color: var(--bluegray-800);
    box-shadow: inset 0 0 2px 2px rgba(0, 0, 0, 0.1);
}

.navbar-logo {
    font-size: 2.2rem;
    font-family: 'Libre Baskerville', 'Domine', Georgia, 'Times New Roman', Times, serif;
    text-decoration: none;
    color: var(--yellow-400);
    padding: 0 1rem 0 0.5rem;
    transition: color 0.3s;
}

.dropdown-menu {
    border: 2px solid var(--bluegray-700);
    background-color: var(--bluegray-900);
    box-shadow: 0 0 10px 2px rgba(0, 0, 0, 0.5);
    text-align: center;
    width: min-content;
    min-width: 8rem;
    padding: 10px;
}

nav > div {
    font-size: 1.3rem;
}

nav a {
    font-family: 'Libre Baskerville', 'Domine', serif;
    font-weight: 900;
}

.nav-link:hover,
.navbar-logo:hover {
    color: var(--yellow-200) !important;
}

.nav-link:active,
.navbar-logo:active {
    color: var(--yellow-200) !important;
}

@media screen and (max-width: 754px) {
    .navbar {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        padding: 0.5rem 0;
        width: 100%;
        height: fit-content;
    }

    .navbar-item {
        margin: 0.5rem 0;
    }

    .navbar-item.navbar-concept,
    .navbar-item.navbar-title {
        display: flex;
        width: fit-content;
    }

    .navbar-item.navbar-title {
        justify-content: end;
        /* margin-left: 15px; */
    }

    .navbar-item.navbar-concept {
        justify-content: start;
        /* margin-right: 15px; */
    }

    .navbar-item.navbar-search {
        width: 100%;
        display: flex;
        justify-content: center;
    }

    .navbar-logo {
        font-size: 1.8rem;
    }
}
</style>
