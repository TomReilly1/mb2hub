<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import GlobalHeader from '@/components/GlobalHeader.vue'
import GlobalFooter from '@/components/GlobalFooter.vue'


// SORUCE: https://dev.to/nirazanbasnet/dont-use-100vh-for-mobile-responsive-3o97

// Detect the height of the app by using JS
// Setting the height of the page (using javascript) with the window.innerheight property.

const documentHeight = () => {
    const doc = document.documentElement
    doc.style.setProperty('--doc-height', `${window.innerHeight}px`)
}
window.addEventListener('resize', documentHeight)
documentHeight()
</script>
<!---------------------------------------------------------------------------->
<template>
    <GlobalHeader />
    <router-view />
    <GlobalFooter />
</template>
<!---------------------------------------------------------------------------->
<style>
#app {
    font-family: 'Open Sans', 'Poppins', 'Merriweather Sans', Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: var(--yellow-300);
    background-color: var(--gray-900);
    background-image: url('./assets/background.webp');
    background-attachment: fixed;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    min-height: 100vh;
    position: relative;
    padding-bottom: 8rem;
}

@media screen and (max-width: 500px) {
    #app {
        min-height: calc(100vh + 2rem);
    }
}

h1 {
    color: var(--bluegray-900);
    font-size: 4.5rem;
    font-family: Georgia, 'Times New Roman', Times, serif;
    text-decoration: underline;
    margin: 0;
    border: 0;
    padding: 2rem 0 2.5rem;
    text-shadow: 0px 0px 4px aliceblue;
}

.id-link {
    text-decoration: none;
}

/***** Primevue Custom Styles *****/
.navbar-concepts .p-dropdown-items-wrapper {
    width: auto;
}

.navbar-concepts .p-dropdown-item-group {
    padding: 10px 0 0 15px !important;
    color: var(--yellow-300) !important;
    text-decoration: underline;
    font-size: 1.3rem;
}

.navbar-concepts .p-dropdown-item,
.navbar-concepts .p-dropdown-item:visited {
    margin: 0.5rem 0 !important;
    padding: 0 !important;
    text-decoration: none;
    font-size: 1.1rem;
}

.navbar-concepts .p-dropdown-item.p-highlight a {
    color: var(--bluegray-900) !important;
}

.navbar-item.navbar-concept .p-dropdown.p-component.p-inputwrapper .p-dropdown-label.p-inputtext {
    font-size: 1.3rem;
    color: var(--bluegray-300);
    padding-right: 0;
}

.navbar-item.navbar-concept .p-dropdown.p-component.p-inputwrapper .p-dropdown-label.p-inputtext.p-placeholder {
    color: var(--bluegray-300);
}

.p-dropdown-item.p-highlight {
    color: var(--bluegray-900) !important;
    background-color: var(--yellow-300) !important;
}

.p-button.p-component.p-button-icon-only.p-autocomplete-dropdown {
    background-color: var(--yellow-300) !important;
    border: 1px solid var(--bluegray-500);
}
.p-dropdown.p-component.p-inputwrapper:hover,
.p-dropdown.p-component.p-inputwrapper:active {
    background-color: var(--bluegray-800);
}

.p-button.p-component.p-button-outlined {
    color: var(--yellow-300);
}

.p-button.p-component.p-button-outlined:hover,
.p-button.p-button-outlined:enabled:hover {
    color: var(--yellow-300) !important;
    background-color: var(--bluegray-800) !important;
}


.p-multiselect.p-component.p-inputwrapper .p-multiselect-label-container {
    color: var(--yellow-300);
}

.p-multiselect-panel.p-component .p-multiselect-items .p-multiselect-item.p-highlight {
    color: var(--bluegray-900);
    background-color: var(--yellow-300);
    border: 1px solid rgba(125, 125, 125, 0.3);
}

.p-multiselect-panel.p-component .p-multiselect-items .p-checkbox .p-highlight, 
.p-multiselect-panel.p-component .p-multiselect-header .p-checkbox .p-highlight {
    background-color: var(--green-300);
    border: 1px solid var(--green-500);
}

.p-multiselect-panel.p-component .p-checkbox .p-checkbox-box:hover {
    background-color: var(--green-500);
    border: 1px solid var(--green-700);
}

.p-multiselect-panel.p-component .p-checkbox .p-checkbox-box.p-highlight:hover {
    background-color: var(--red-500);
    border: 1px solid var(--red-700);
}

.p-column-filter-buttonbar .p-button.p-component:not(.p-button-outlined) {
    color: var(--bluegray-900);
    background-color: var(--yellow-300);
    border-color: var(--bluegray-100);
}

.p-column-filter-buttonbar .p-button.p-component:not(.p-button-outlined):hover {
    background-color: var(--green-400);
}

.p-button.p-component.p-column-filter-add-button.p-button-text {
    color: var(--bluegray-100);
    background-color: unset;
    border: unset;
}

.p-button.p-component.p-column-filter-add-button.p-button-text:hover {
    color: var(--green-300);
}

.p-column-filter-menu-button.p-link.p-column-filter-menu-button-active {
    background-color: var(--yellow-400);
}

.p-column-filter-menu-button.p-link.p-column-filter-menu-button-active:hover {
    background-color: var(--yellow-300);
}

th.p-sortable-column.p-highlight .p-column-header-content .p-column-title {
    color: var(--yellow-300);
}

.p-autocomplete.p-component.p-inputwrapper > #srch-page-bar.p-autocomplete-input.p-inputtext.p-component {
    width: 100%;
}

.p-autocomplete.p-component.p-inputwrapper > #navbar-search-bar.p-autocomplete-input.p-inputtext.p-component {
    width: 100%;
}
</style>
