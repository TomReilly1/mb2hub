<template>
  <section class="home">
    <div>
      <h1>Home</h1>
      <p>MB2 Hub aims to be a reference to data relevent to Mount & Blade II: Bannerlord. This site aims to be somehat of a wiki, but more aimed towards the statistical side of things such as armor ratings and troop skill levels.</p>
      <p>Any suggestions or critiques for this website are welcomed! Hope you enjoy!</p>
    </div>
    <!-- <div class="surface-card p-4 shadow-2 border-round">
      <div class="text-3xl font-medium text-900 mb-3">Card Title</div>
      <div class="font-medium text-500 mb-3">Vivamus id nisl interdum, blandit augue sit amet, eleifend mi.</div>
      <div style="height: 150px" class="border-2 border-dashed surface-border"></div>
    </div> -->
  </section>
</template>

<script setup>

</script>

<style scoped>
  .home {
    padding: 0 1rem;
    display: flex;
    justify-content: center;
    font-size: 1.7rem;
    margin-top: 5rem;
  }

  .home p {
    font-size: 1.5rem;
  }

  .home > div {
    max-width: 70rem;
    padding: 2rem;
    border-radius: 1rem;
    background-color: var(--bluegray-700);
    color: var(--yellow-400);
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  }

</style>