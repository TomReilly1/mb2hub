<template>
    <header>
        <nav class="navbar navbar-expand-md navbar-dark bg-dark" aria-label="Global Navbar">
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
                            <router-link to="/table/armors" class="nav-link">Armors</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link to="/table/bows" class="nav-link">Bows</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link to="/table/troops" class="nav-link">Troops</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link to="/table/kingdoms" class="nav-link">Kingdoms</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link to="/table/cultures" class="nav-link">Cultures</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link to="/table/lords" class="nav-link">Lords</router-link>
                        </li>
                        <li class="nav-item">
                            <router-link to="/table/clans" class="nav-link">Clans</router-link>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    </header>

</template>
<!------------------------------------------------------------------------------------>
<script setup>
    
</script>
<!------------------------------------------------------------------------------------>
<style scoped>
    header {
        background-color: var(--bluegray-800);
        box-shadow: 0px 2px 4px 4px rgba(50,50,50,0.3);
    }

    .navbar-brand {
        font-size: 2rem;
        color: var(--yellow-400) !important;
    }

    .navbar {
        padding: 0.5rem 1rem;
    }

    nav > div {
        font-size: 1.3rem;
    }

    .nav-link:hover {
        color: var(--yellow-200) !important;
    }
</style>