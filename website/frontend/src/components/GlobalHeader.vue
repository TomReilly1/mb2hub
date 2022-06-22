<script setup>
</script>
<!------------------------------------------------------------------------------------>
<template>
<header>
  <nav class="navbar navbar-expand-md navbar-dark" aria-label="Global Navbar">
    <div class="container-fluid">
      <router-link to="/" class="navbar-logo">MB2 Hub</router-link>
      <button class="navbar-toggler collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#navbar" aria-controls="navbar" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
      </button>
      <div class="navbar-collapse collapse" id="navbar" style="">
        <ul class="navbar-nav me-auto mb-2 mb-md-0">
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="equipment-nav-drop" role="button" data-bs-toggle="dropdown" aria-expanded="false">Equipment</a>
            <ul class="dropdown-menu" aria-labelledby="equipment-nav-drop">
              <li class="nav-item">
                <router-link to="/table/armors" class="nav-link">Armors</router-link>
              </li>
              <li class="nav-item">
                <router-link to="/table/bows" class="nav-link">Bows</router-link>
              </li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="people-nav-drop" role="button" data-bs-toggle="dropdown" aria-expanded="false">People</a>
            <ul class="dropdown-menu" aria-labelledby="people-nav-drop">
              <li class="nav-item">
                <router-link to="/table/lords" class="nav-link">Lords</router-link>
              </li>
              <li class="nav-item">
                <router-link to="/table/troops" class="nav-link">Troops</router-link>
              </li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="politics-nav-drop" role="button" data-bs-toggle="dropdown" aria-expanded="false">Politics</a>
            <ul class="dropdown-menu" aria-labelledby="equipment-nav-drop">
              <li class="nav-item">
                <router-link to="/table/clans" class="nav-link">Clans</router-link>
              </li>
              <li class="nav-item">
                <router-link to="/table/cultures" class="nav-link">Cultures</router-link>
              </li>
              <li class="nav-item">
                <router-link to="/table/kingdoms" class="nav-link">Kingdoms</router-link>
              </li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="trading-nav-drop" role="button" data-bs-toggle="dropdown" aria-expanded="false">Trading</a>
            <ul class="dropdown-menu" aria-labelledby="equipment-nav-drop">
              <li class="nav-item">
                <router-link to="/table/goods" class="nav-link">Goods</router-link>
              </li>
            </ul>
          </li>
          <li class="nav-item dropdown">
            <a class="nav-link dropdown-toggle" href="#" id="settlements-nav-drop" role="button" data-bs-toggle="dropdown" aria-expanded="false">Settlements</a>
            <ul class="dropdown-menu" aria-labelledby="equipment-nav-drop">
               <li class="nav-item">
                <router-link to="/table/towns" class="nav-link">Towns</router-link>
              </li>
              <li class="nav-item">
                <router-link to="/table/villages" class="nav-link">Villages</router-link>
              </li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</header>
</template>
<!------------------------------------------------------------------------------------>
<style scoped>
header {
    background-color: var(--bluegray-900);
    box-shadow: 0 0 7px 4px rgba(0, 0, 0, 0.3);
}

.navbar {
    padding: 0.5rem 1rem;
}

.container-fluid {
  padding: 0 !important;
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

@media screen and (max-width: 910px) {
    nav > div {
        font-size: 1.2rem;
    }
}
@media screen and (max-width: 860px) {
    nav > div {
        font-size: 1.1rem;
    }
}
@media screen and (max-width: 820px) {
    nav > div {
        font-size: 1rem;
    }
}
@media screen and (max-width: 768px) {
    nav > div {
        font-size: 1rem;
    }
    .dropdown-menu {
        position: relative;
        left: calc(50% - 6rem);
        width: 12rem;
        max-width: 12rem;
        text-align: center;
    }
}
</style>
