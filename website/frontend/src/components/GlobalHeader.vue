<template>
    <header>
        <nav>
            <ul>
                <li>
                    <h2>MB2 HUB</h2>
                </li>
                <li>
                    <router-link to="/">Home</router-link>
                </li>
                <li>
                    <router-link to="/armor">Armor</router-link>
                </li>
                <li>
                    <router-link to="/about">About</router-link>
                </li>
            </ul>
        </nav>
    </header>

</template>



<script setup>
    
</script>



<style scoped>
    nav, ul, h2 {
        margin: 0;
        padding: 0;
    }

    header {
        height: 5rem;
        background-color: lightgreen;
    }

    nav {
        height: 100%;
    }

    ul {
        display: flex;
        justify-content: space-around;
        align-items: center;
        height: 100%;
        margin: 0;
        padding: 0;
        list-style: none;
    }

    li {
        width: 100%;
        font-size: 1.5rem;
    }

    a {
        height: 100%;
        width: 100%;
    }
</style>