<template>
  <!-- <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link>
  </nav> -->
  <GlobalHeader />
  <router-view />
  <!-- <GlobalFooter /> -->

</template>

<script setup>
import GlobalHeader from "@/components/GlobalHeader";
// import GlobalFooter from "@/components/GlobalFooter";

</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: var(--yellow-300);
  background-color: var(--bluegray-900);
  height: 65rem;
  position: relative;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: var(--yellow-400);
}

nav a.router-link-exact-active {
  color: var(--yellow-600);
}

</style>
