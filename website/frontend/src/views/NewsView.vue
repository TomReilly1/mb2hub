<script setup>
import { onMounted, ref } from "vue";
import router from "@/router";

async function fetchNewsData() {
    await fetch(`${process.env.VUE_APP_API_URL}/news`)
    // await fetch(`https://www.taleworlds.com/en/News/505`)
        .then(res => {
            console.log(res.text());
            var parser = new DOMParser();
	        var doc = parser.parseFromString(response.data, 'text/html');
            console.log(doc);
        })
        .then(data => conceptData.value = data)
        .catch(() => {
            router.push('/404');
        });
}

onMounted(async () => {
    await fetchNewsData();
})

</script>
<!---------------------------------------------------------------------------->
<template>
<section class="news">
    <h1>News</h1>
    <div class="desc-container">
        <div class="heading home-section">
            <h2>Updates & Hotfixes</h2>
            <p>
                Here listed is the most recent news on updates and hotfixes. This information is taken directly from the
                <a href="https://www.taleworlds.com/en/News">TaleWorlds website.</a> 
            </p>
        </div>
    </div>
    <div class="desc-container">
        <div class="version home-section">
            <h3 id="version-text">Current Version</h3>
            <span id="version-number">1.8.0</span>  
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
                        <a href="https://expressjs.com/">
                            <img src="@/assets/express_logo.jpg" alt="Express.js logo" />
                            <span>Express.js</span>
                        </a>
                    </li>
                    <li>
                        <a href="https://www.meilisearch.com/">
                            <img src="@/assets/meili_logo.svg" alt="Meilisearch logo" />
                            <span>Meilisearch</span>
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

    .home p,
    .header-items,
    .items {
        font-size: 1.2rem;
    }
}
</style>
