<template>
    <header>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark" aria-label="Fourth navbar example">
            <div class="container-fluid">
                <h2><router-link to="/" class="navbar-brand">MB2 Hub</router-link></h2>
                <button class="navbar-toggler collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#navbarsExample04" aria-controls="navbarsExample04" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <div class="navbar-collapse collapse" id="navbarsExample04" style="">
                    <ul class="navbar-nav me-auto mb-2 mb-md-0">
                        <li class="nav-item">
                            <router-link to="/" class="nav-link active" aria-current="page">Home</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link to="/armor" class="nav-link">Armor</router-link>
                        </li>
                        <li>
                            <a class="nav-link" href="#">Troops</a>
                        </li>
                        <li>
                            <a class="nav-link" href="#">Kingdoms</a>
                        </li>
                        <li>
                            <a class="nav-link" href="#">Cultures</a>
                        </li>
                    </ul>
                </div>
            </div>
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
        background-color: var(--bluegray-800);
        box-shadow: 0px 2px 4px 4px rgba(50,50,50,0.3);
    }

    nav {
        height: 100%;
        padding: 0 1rem;
        display: flex;
        justify-content: space-between;
    }

    nav > div {
        font-size: 1.5rem;
    }

    .nav-title {
        display: flex;
        align-items: center;
    }

    .nav-title a {
        text-decoration: unset;
    }

    .nav-title a.router-link-exact-active {
        color: var(--yellow-400);
    } 

    .nav-links {
        display: flex;
        align-items: center;
    }

    h2 .navbar-brand {
        height: fit-content;
        vertical-align: middle;
        text-align: center;
        font-size: 2rem;
    }

    a {
        margin: 0 1rem;
        padding: 1rem;
        width: 100%;
    }
</style>