<template>
  <div class="card">
    <!-- <span>Highest Rated Armor</span> -->
    <ul>
      <li>Helm with highest Head AR:</li>
      <li>Warlord Helmet over Full Mail <br> Closed Decorated Goggled Helmet</li>
      <li>54</li>
    </ul>
    <!-- <ul>
      <li>Helm with highest Head AR:</li>
      <li>Cape with highest Body AR:</li>
      <li>Cape with highest Arm AR:</li>
      <li>Torso with hightest Body AR:</li>
      <li>Torso with hightest Arm AR:</li>
      <li>Torso with hightest Leg AR:</li>
      <li>Gloves with hightest Arm AR:</li>
      <li>Boots with hightest Leg AR:</li>
    </ul>
    <ul>
      <li>Warlord Helmet over Full Mail <br> Closed Decorated Goggled Helmet</li>
      <li>Heavy Warlord Pauldrons <br> Reinforced Bronze Scale Shoulder Guards</li>
      <li>Reinforced Bronze Scale Shoulder Guards <br> Decorated Leather Harness over Scale</li>
      <li>Heavy Scale Armor over Mail Hauberk</li>
      <li>Brigandine over Hauberk</li>
      <li>Mastercrafted Southern Scale over Chain Hauberk <br> Heavy Lamellar over Hauberk <br> Brigandine over Hauberk</li>
      <li>Scale Warlord Bracers</li>
      <li>Scaled Boots</li>
    </ul>
    <ul>
      <li>54</li>
      <li>20</li>
      <li>12</li>
      <li>57</li>
      <li>20</li>
      <li>25</li>
      <li>26</li>
      <li>25</li>
    </ul> -->
  </div>
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

  .card {
    display: flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    padding: 0;
    font-size: 1.7rem;
    font-weight: 700;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }

  .card p {
    font-size: 1.5rem;
    font-weight: 500;
  }

  .card > div {
    max-width: 70rem;
    margin: 0 auto 3rem;
    padding: 2rem;
    border-radius: 1rem;
    background-color: var(--bluegray-700);
    color: var(--yellow-300);
    box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  }

  ul {
    display: flex;
    width: 90%;
    margin: 0;
    padding: 0;
    list-style: none;
    font-size: 1rem;
  }
  
  li {
    width: 33.333%;
  }
</style>