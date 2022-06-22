<script setup>
import GlobalHeader from "@/components/GlobalHeader";
import GlobalFooter from "@/components/GlobalFooter";
</script>
<!--------------------------------------------------------------------->
<template>
    <GlobalHeader />
    <router-view />
    <GlobalFooter />
</template>
<!--------------------------------------------------------------------->
<!-- BOOTSTRAP BREAKPOINTS
Extra Small         n/a     <576px
Small	            sm	    ≥576px
Medium	            md	    ≥768px
Large	            lg	    ≥992px
Extra large	        xl	    ≥1200px
Extra extra large   xxl	    ≥1400px
 -->
<style>
#app {
    font-family: 'Open Sans', 'Poppins', 'Merriweather Sans', Arial, sans-serif;
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

h1 {
    color: var(--bluegray-900);
    font-size: 4.5rem;
    font-family: Georgia, 'Times New Roman', Times, serif;
    text-decoration: underline;
    margin: 0;
    border: 0;
    padding: 2rem 0 2.5rem;
    text-shadow: 0px 0px 4px aliceblue;
}
</style>
