<template>
    <GlobalHeader />
    <router-view />
    <GlobalFooter />
</template>
<!--------------------------------------------------------------------->
<script setup>
import GlobalHeader from "@/components/GlobalHeader";
import GlobalFooter from "@/components/GlobalFooter";
</script>
<!--------------------------------------------------------------------->
<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: var(--yellow-300);
    background-color: var(--bluegray-200);
    background-image: url('./assets/background.webp');
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    min-height: 100vh;
    position: relative;
    padding-bottom: 10rem;
}

nav {
    padding: 30px;
}

nav a {
    font-family: 'Libre Baskerville', 'Domine', serif;
    font-weight: 900;
    color: var(--yellow-400);
}

nav a.router-link-exact-active {
    color: var(--yellow-600);
}

h1 {
    color: var(--bluegray-700);
    font-size: 4.5rem;
    font-family: Georgia, 'Times New Roman', Times, serif;
    text-decoration: underline;
    margin: 0;
    border: 0;
    padding: 2rem 0 2.5rem;
    text-shadow: 0px 0px 10px aliceblue;
}
</style>
