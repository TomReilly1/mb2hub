<template>
  <section class="home">
    <h1>Home</h1>
    <div class="desc container">
      <h3>Welcome to MB2 Hub!</h3>
      <p>This site aims to be a reference to data relevent to Mount & Blade II: Bannerlord, aiming more towards the statistical side of things such as armor ratings and troop skill levels.</p>
      <p>This project is a work-in-progress so any suggestions or critiques for this website are welcomed!</p>
    </div>
    <div class="version container">
      <h3 id="version-text">Current Version</h3>
      <span id="version-number">1.7.2</span>  
    </div>
    <div class="todo container">
      <h3>Here are some components I plan on implementing:</h3>
      <ul class="todo list">
        <li class="todo list items">Add minor factions</li>
        <li class="todo list items">Add clans</li>
        <li class="todo list items">Add melee weapons
          <ul>
            <li>will be hard to add since melee weapon stats are not stored in game's xml files</li>
          </ul>
        </li>
        <li class="todo list items">Add troop equipment loadouts</li>
        <li class="todo list items">Add towns</li>
        <li class="todo list items">Add castles</li>
        <li class="todo list items">Add villages</li>
        <li class="todo list items">Add lords</li>
        <li class="todo list items">Add heroes</li>
        <li class="todo list items">Add perks</li>
        <li class="todo list items">Add workshops</li>

        <li class="todo list items">Add horses</li>
        <li class="todo list items">Add harnesses/horse armor</li>
        <li class="todo list items">Add draught animals</li>
        <li class="todo list items">Add trading goods</li>
        <li class="todo list items">Add bandits</li>
      </ul>
    </div>
  </section>

</template>

<script setup>

</script>

<style scoped>
  h1 {
    font-size: 3.5rem;
    text-decoration: underline;
    margin: 0;
    border: 0;
    padding: 2rem 0 2.5rem;
  }

  h3 {
    font-size: 2.5rem;
    margin: 0 0 2rem;
    font-weight: 700;
  }

  .home {
    padding: 0 1rem;
    font-size: 2rem;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }

  .home p, li {
    font-size: 1.7rem;
    color: aliceblue;
  }

  .container {
    max-width: 70rem;
    margin: 0 auto 3rem;
    padding: 2rem;
    border-radius: 1rem;
    background-color: var(--bluegray-700);
    color: var(--yellow-300);
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  }

  .version.container {
    max-width: 28rem;
  }

  /* #version-text {
  
  } */

  #version-number {
    color: var(--green-300);
    font-weight: 700;
    font-size: 3rem;
  }

  .todo.container ul{
    text-align: left;
  }

</style>