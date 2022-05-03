<template>
  <section class="home">
    <h1>Home</h1>
    <div class="description">
      <span>Welcome to MB2 Hub!</span>
      <p>This site aims to be a reference to data relevent to Mount & Blade II: Bannerlord, aiming more towards the statistical side of things such as armor ratings and troop skill levels.</p>
      <p>This project is a work-in-progress so any suggestions or critiques for this website are welcomed!</p>
      <span>Hope you enjoy!</span>  
    </div>
    <!-- <div class="surface-card p-4 shadow-2 border-round">
      <div class="text-3xl font-medium text-900 mb-3">Card Title</div>
      <div class="font-medium text-500 mb-3">Vivamus id nisl interdum, blandit augue sit amet, eleifend mi.</div>
      <div style="height: 150px" class="border-2 border-dashed surface-border"></div>
    </div> -->
    <div class="version-container">
      <span id="version-text">Current Version:</span>
      <br>
      <span id="version-number">1.7.2</span>  
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

  .home {
    padding: 0 1rem;
    font-size: 1.7rem;
    font-weight: 700;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }

  .home p {
    font-size: 1.5rem;
    font-weight: 500;
  }

  .home > div {
    max-width: 70rem;
    margin: 0 auto 3rem;
    padding: 2rem;
    border-radius: 1rem;
    background-color: var(--bluegray-700);
    color: var(--yellow-300);
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  }

  .home .version-container {
    max-width: 20rem;
  }

  #version-number {
    color: var(--green-300);
  }

</style>