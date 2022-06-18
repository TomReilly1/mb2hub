<template>
<header>
  <nav class="navbar navbar-expand navbar-dark" aria-label="Global Navbar">
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
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Tables</a>
            <ul class="dropdown-menu" aria-labelledby="navbarDropdown">
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
          </li>
          <!-- <li class="nav-item">
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
          </li> -->
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
    background-color: var(--bluegray-900);
    box-shadow: 0 0 7px 4px rgba(0, 0, 0, 0.3);
}

.navbar {
    padding: 0.5rem 1rem;
}

.navbar-brand {
    font-size: 2rem;
    color: var(--yellow-400) !important;
    transition: color 0.3s;
}
.dropdown-menu {
  border: 2px solid var(--bluegray-700);
  background-color: var(--bluegray-800) !important;
}

nav > div {
    font-size: 1.3rem;
}

nav a {
    font-family: 'Libre Baskerville', 'Domine', serif;
    font-weight: 900;
    color: var(--yellow-400);
}

nav a.router-link-exact-active {
    color: var(--yellow-600);
}

a[data-v-32814f80]:hover {
    color: var(--yellow-200) !important;
}
</style>
