<script setup>

</script>
<!---------------------------------------------------------------------------->
<template>
  <section class="home">
    <h1>Home</h1>
    <div class="desc-container">
      <div class="heading home-section">
        <h2>Welcome to the Bannerlord Hub!</h2>
        <p>
          This site aims to provide easy access to any relevant data for Mount & Blade II: Bannerlord.
          Because Bannerlord is in early access, I will always try to keep up to date on the latest beta version.
        </p>
        <p>
          This project is a work-in-progress so any suggestions are welcomed!
        </p>
      </div>
      <hr />
      <div class="version home-section">
        <h3 id="version-text">Current Version</h3>
        <span id="version-number">1.8.0</span>  
      </div>
      <hr />
      <div class="todo home-section">
        <h3>Here are some components I plan on implementing:</h3>
        <div class="list-container">
          <ul class="todo-list">
            <li class="todo-list header-items">Concepts
              <ul>
                <li class="todo-list items">minor factions</li>
                <li class="todo-list items">troop equipment loadouts</li>
                <li class="todo-list items">castles</li>
                <li class="todo-list items">heroes</li>
                <li class="todo-list items">perks</li>
                <li class="todo-list items">workshops</li>
                <li class="todo-list items">horses</li>
                <li class="todo-list items">harnesses/horse armor</li>
                <li class="todo-list items">melee weapons</li>
                <li class="todo-list items">draught animals</li>
                <li class="todo-list items">bandits</li>
              </ul>
            </li>
            <li class="todo-list header-items">Features
              <ul>
                <li class="todo-list items">search bar</li>
                <li class="todo-list items">general comparison page</li>
                <li class="todo-list items">percentile rankings</li>
                <li class="todo-list items">more linking in tables in cards</li>
              </ul>
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
