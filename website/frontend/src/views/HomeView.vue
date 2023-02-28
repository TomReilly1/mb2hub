<script setup lang="ts">
import { ref } from "vue"

const todoItems = ref<{
    header: string,
    items: string[]
}[]>
([
  {
    'header': 'Concepts',
    'items': [
      'minor factions',
      'troop equipment loadouts',
      'companions',
      'perks',
      'workshops',
      'harnesses/horse armor',
      'melee weapons',
      'bandits',
    ]
  },
  {
    'header': 'Features',
    'items': [
      'general comparison page',
      'better/more linking in tables and cards',
      'development news',
      'map of Calradia'
    ]
  }
])
</script>
<!---------------------------------------------------------------------------->
<template>
<section class="home">
    <h1>Home</h1>
    <div class="desc-container">
        <div class="heading home-section">
            <h2>Welcome to the Bannerlord Hub!</h2>
            <p>
                This website aims to provide easy access to any relevant data for Mount & Blade II: Bannerlord. I will always try to keep up to date on the latest stable version.
            </p>
            <p>
                I am always looking to add more to this project, so any <a href="https://github.com/TomReilly1/mb2hub">suggestions are welcome!</a>
            </p>
        </div>

        <hr />

        <div class="version home-section">
            <h3 id="version-text">Current Version</h3>
            <span id="version-number">1.9.0</span>  
        </div>

        <hr />

        <div class="todo home-section">
            <h3>Here are some components I plan on implementing:</h3>
            <div class="list-container">
                <ul class="todo-list">
                    <li v-for="obj in todoItems" class="todo-list header-items">{{obj.header}}
                        <ul>
                            <li v-for="item in obj.items" class="todo-list items">{{item}}</li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>

        <hr />

        <div class="tools home-section">
            <h3>Built with:</h3>
            <div>
                <ul>
                    <li>
                        <a href="https://vuejs.org">
                            <img src="@/assets/vue_logo.svg" alt="Vue.js logo" />
                            <span>Vue.js</span>
                        </a>
                    </li>
                    <li>
                        <a href="https://www.primefaces.org/primevue/">
                            <img src="@/assets/primevue_logo.svg" alt="Primevue logo" />
                            <span>Primevue</span>
                        </a>
                    </li>
                    <li>
                        <a href="https://nodejs.org/">
                            <img src="@/assets/node_logo.svg" alt="Node.js logo" />
                            <span>Node.js</span>
                        </a>
                    </li>
                    <li>
                        <a href="https://expressjs.com/">
                            <img src="@/assets/express_logo.jpg" alt="Express.js logo" />
                            <span>Express.js</span>
                        </a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</section>
</template>
<!---------------------------------------------------------------------------->
<style scoped>
hr {
    color: rgba(200, 200, 200, 0.7);
    margin: 2rem 0;
}


h2, h3 {
    font-size: 2.3rem;
    margin: 0 0 2rem;
    font-weight: 700;
}

p a {
    text-decoration: none;
    color: var(--yellow-300);
}

p a:hover {
    color: var(--yellow-200);
}

.home {
    padding: 0 1rem;
    font-size: 2rem;
}

.home p,
.header-items,
.items {
    font-size: 1.7rem;
    color: var(--bluegray-100);
}

.desc-container {
    max-width: 60rem;
    margin: 0 auto 3rem;
    border: 0;
    padding: 2rem;
    border-radius: 1rem;
    background-color: var(--bluegray-900);
    color: var(--yellow-300);
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
}

#version-number {
    color: var(--green-300);
    font-weight: 700;
    font-size: 4.5rem;
}

.list-container {
    display: flex;
    justify-content: center;
}

.todo-list {
    width: max-content;
    max-width: 100%;
    text-align: left;
}

.tools.home-section > div {
    display: flex;
    justify-content: center;
}

.tools.home-section ul {
    width: max-content;
    max-width: 100%;
    text-align: left;
    list-style: none;
    margin-top: 0;
    padding: 0;
}

.tools.home-section li {
    display: flex;
    align-items: center;
    margin: 10px 0;
    font-size: 2rem;
    color: var(--bluegray-100);
}

.tools.home-section a {
    display: flex;
    align-items: center;
    text-decoration: none;
    color: var(--bluegray-100);
    transition: color 0.5s, text-shadow 0.5s;
}

.tools.home-section a:visited {
    color: var(--bluegray-100);
    text-decoration: none;
    transition: color 0.5s, text-shadow 0.5s;
}

.tools.home-section a:hover {
    color: var(--yellow-200);
    text-shadow: 0 0 5px rgba(220,220,220,0.5);
}

.tools.home-section img {
    width: 50px;
    height: 50px;
    margin-right: 20px;
}
  

@media screen and (max-width: 550px) {
    h2, h3 {
        font-size: 1.9rem;
        margin: 0 0 1rem;
    }

    #version-number {
        font-size: 3.5rem;
    }
    .home p,
    .header-items,
    .items {
        font-size: 1.2rem;
    }
}
</style>
