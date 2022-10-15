<script setup lang="ts">

</script>
<!---------------------------------------------------------------------------->
<template>
<section>
    <h1>Error</h1>
    <div class="desc-container">
        <div class="heading home-section">
            <h2>Page not found</h2>
            <p>
                Try visiting the home page and refreshing the browser.
            </p>
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

section {
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
