<script setup>
import {ref, onMounted} from "vue";
import AutoComplete from 'primevue/autocomplete';
import router from "@/router";


const resultsList = ref('concept list');
const selectedConcept = ref('');
const searchAlertSmall = ref('');


onMounted(() => {
    const searchBar = document.getElementById('navbar-search-bar');
    
    searchBar.addEventListener('keydown', (e) => {
        console.log('key == ' + e.key);
        console.log('code == ' + e.code);
        console.log('code == ' + e.repeat);

        if (e.repeat !== true && e.code === 'Enter' && e.key === 'Enter') {
            for (let result of resultsList.value) {
                console.log(selectedConcept.value);
                console.log(result.name);
                if (selectedConcept.value === result.name) {
                    console.log('IT IS A MATCH');
                    if (result.concept === 'concepts') {
                        window.location.href = `https://mb2hub.com/table/${result.id}`; // or ${result.concept}
                    } else {
                        window.location.href = `https://mb2hub.com/card/${result.concept}/${result.id}`;
                    }
                }
            }
        }
    });
});


async function getSearchResults() {
    const temp = selectedConcept.value;
    const santzStr = temp.replace(/[^a-z ]/gi, '');
    console.log('santzStr == ' + santzStr);
    const paramsObj = {searchstr: santzStr};
    const searchParams = new URLSearchParams(paramsObj);
    const searchStr = searchParams.toString(); 
    console.log('searchStr == ' + searchStr);

    const res = await fetch(`${process.env.VUE_APP_API_URL}/search?${searchStr}`);
    console.log(res);
    const json = await res.json();
    console.log(json);
    console.log(json.hits);

    if (json.nbHits === 0) {
        resultsList.value = [];
        setSearchBarAlert(false, 'Search was successful, but no matches found.')
    } else {
        resultsList.value = json.hits;
        setSearchBarAlert(true);
    }
    
}


const searchConcept = (event) => {
    console.log('Reached searchConcept() function');
    setTimeout(async () => {
        console.log('Reached setTimeout() function');
        if (selectedConcept.value === '') {
            resultsList.value = '';
            console.log('selectedConcept is empty');
            setSearchBarAlert(false, 'The selected input is empty');
        } else if (selectedConcept.value === undefined) {
            console.log('selectedConcept is undefined');
            setSearchBarAlert(false, 'The selected input is undefined');
        } else if (selectedConcept.value === null) {
            console.log('selectedConcept is null');
            setSearchBarAlert(false, 'The selected input is null');
        } else {
            await getSearchResults();
        }
    }, 1000);
};


function setSearchBarAlert(matchFound, status='match found') {
    const searchBar = document.getElementById('navbar-search-bar');
    const searchAlert = document.getElementById('navbar-search-alert');

    searchAlertSmall.value = status;

    if (matchFound || status.includes('empty')) {
        if (searchBar.classList.contains('p-invalid')) {
            searchBar.classList.remove("p-invalid");
        }
        if (searchAlert.style.visibility !== "hidden" || searchAlert.style.visibility === "visible") {
             searchAlert.style.visibility = "hidden";
        }
    } else {
        if (!searchBar.classList.contains('p-invalid')) {
            searchBar.classList.add("p-invalid");
        }
        if (searchAlert.style.visibility === "hidden" || searchAlert.style.visibility !== "visible") {
             searchAlert.style.visibility = "visible";
        }
    }
}


const directToCardPage = (e) => {
    console.log(e);
    console.log(e.value.concept);

    if (e.value.concept === 'concepts') {
        window.location.href = `https://mb2hub.com/table/${e.value.id}`; // or ${e.value.concept}
        // router.push(`/table/${e.value.id}`);
    } else {
        window.location.href = `https://mb2hub.com/card/${e.value.concept}/${e.value.id}`;
        // router.push(`/card/${e.value.concept}/${e.value.id}`);
    }
}
</script>
<!---------------------------------------------------------------------------->
<template>
<div class="search-container">
    <i class="pi pi-search" style="font-size: 1.4rem; padding: 0 10px;"></i>
    <AutoComplete id="navbar-search-bar" aria-describedby="navbar-search-alert" v-model="selectedConcept" :suggestions="resultsList" @complete="searchConcept($event)" @item-select="directToCardPage($event)" field="name" placeholder="Search..."/>
    <small id="navbar-search-alert" class="p-error">{{searchAlertSmall}}</small>
</div>
</template>
<!---------------------------------------------------------------------------->
<style lang="scss" scoped>
.search-container {
    display: flex;
    flex-direction: row;
    align-items: center;
    width: 100%;
    max-width: 450px;
}

.search-container .p-autocomplete.p-component.p-inputwrapper {
    width: 100%;
    max-width: 90%;
    margin-right: 10px;
}

#navbar-search-bar.p-autocomplete-input.p-inputtext.p-component {
    width: 100% !important;
}

#navbar-search-alert {
    font-size: 0.7rem;
    margin-top: 2px;
}
</style>
