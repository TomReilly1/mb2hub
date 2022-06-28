<script setup>
import {ref, onMounted} from "vue";
import AutoComplete from 'primevue/autocomplete';


const resultsList = ref('concept list');
const selectedConcept = ref('');
const searchAlertSmall = ref('No matches Found');


onMounted(() => {
    const searchBar = document.getElementById('srch-page-bar');
    
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
    const santzStr = temp.replace(/[^a-z -_]/gi, '');
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
    const searchBar = document.getElementById('srch-page-bar');
    const searchAlert = document.getElementById('srch-page-alert');

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
    if (e.value.concept === 'concepts') {
        window.location.href = `https://mb2hub.com/table/${e.value.id}`; // or ${e.value.concept}
    } else {
        window.location.href = `https://mb2hub.com/card/${e.value.concept}/${e.value.id}`;
    }
}
</script>
<!---------------------------------------------------------------------------->
<template>
    <section class="search">
        <h1>Search</h1>
        <div class="desc-container">
            <div class="heading-section">
                <h2>Search for a concept</h2>
            </div>
            <hr />
            <div class="search-section">
                <div class="search-container">
                    <AutoComplete id="srch-page-bar" class="" aria-describedby="srch-page-alert" v-model="selectedConcept" :suggestions="resultsList" @complete="searchConcept($event)" @item-select="directToCardPage($event)" field="name" />
                    <small id="srch-page-alert" class="p-error">{{searchAlertSmall}}</small>
                </div>
                <p>{{selectedConcept}}</p>
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

.search {
    padding: 0 1rem;
    font-size: 2rem;
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

.search-section {
    padding: 2rem 6rem;
}

.search-container {
    display: flex;
    flex-direction: column;
    align-items: center;
}

#srch-page-alert {
    font-size: 1rem;
    margin-top: 1rem;
}

@media screen and (max-width: 550px) {
    h2, h3 {
        font-size: 1.9rem;
        margin: 0 0 1rem;
    }

    .search-section {
        padding: 2rem 1rem;
    }
}

.p-autocomplete {
    width: 100%;
    min-width: 300px;
}

.p-autocomplete-item {
    font-size: 1.5rem;
}
</style>
