<template>
    <header>
        <nav class="navbar navbar-expand-lg navbar-dark bg-dark" aria-label="Global Navbar">
            <div class="container-fluid">
                <router-link to="/" class="navbar-brand">MB2 Hub</router-link>
                <button class="navbar-toggler collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#navbar" aria-controls="navbar" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>

                <div class="navbar-collapse collapse" id="navbar" style="">
                    <ul class="navbar-nav me-auto mb-2 mb-md-0">
                        <li class="nav-item">
                            <router-link to="/" class="nav-link">Home</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link to="/armor" class="nav-link">Armor</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link to="/bows" class="nav-link">Bows</router-link>
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
    header {
        background-color: var(--bluegray-800);
        box-shadow: 0px 2px 4px 4px rgba(50,50,50,0.3);
    }

    .navbar-brand {
        font-size: 2rem;
    }

    nav > div {
        font-size: 1.5rem;
    }

    .nav-title a.router-link-exact-active {
        color: var(--yellow-400);
    } 
</style>