<script setup lang="ts">
import {ref} from "vue"
import AutoComplete, { type AutoCompleteItemUnselectEvent } from 'primevue/autocomplete'
import router from "@/router"

import type {searchObj} from "@/interfaces/indexIntr"


const resultsList = ref<searchObj[]>([])
const selectedConcept = ref<string>('')
const searchAlertSmall = ref<string>('')


async function getSearchResults() {
    const temp: string = selectedConcept.value
    const santzStr: string = temp.replace(/[^a-z ]/gi, '')
    const paramsObj: {searchstr: string} = {searchstr: santzStr}
    const searchParams = new URLSearchParams(paramsObj)
    const searchStr: string = searchParams.toString()

    const res: Response = await fetch(`${import.meta.env.VITE_API_URL}/search?${searchStr}`)
    const json_arr: searchObj[] = await res.json()
    if (json_arr.length === 0) {
        resultsList.value = []
        setSearchBarAlert(false, 'Search was successful, but no matches found.')
    } else {
        resultsList.value = json_arr
        setSearchBarAlert(true)
    }
}


const searchConcept = async () => {
    setTimeout(async () => {
        if (selectedConcept.value === '') {
            resultsList.value = []
            console.log('selectedConcept is empty')
            setSearchBarAlert(false, 'The selected input is empty')
        } else if (selectedConcept.value === undefined) {
            console.log('selectedConcept is undefined')
            setSearchBarAlert(false, 'The selected input is undefined')
        } else if (selectedConcept.value === null) {
            console.log('selectedConcept is null')
            setSearchBarAlert(false, 'The selected input is null')
        } else {
            getSearchResults()
        }
    }, 2000);
};


function setSearchBarAlert(matchFound: boolean, status: string = 'match found') {
    const searchBar: HTMLElement | null = document.getElementById('navbar-search-bar')
    if (searchBar === null) {
        throw 'searchBar element is null'
    }
    const searchAlert = document.getElementById('navbar-search-alert')
        if (searchAlert === null) {
        throw 'searchAlert element is null'
    }

    searchAlertSmall.value = status

    if (matchFound || status.includes('empty')) {
        if (searchBar.classList.contains('p-invalid')) {
            searchBar.classList.remove("p-invalid")
        }
        if (searchAlert.style.visibility !== "hidden") {
             searchAlert.style.visibility = "hidden"
        }
    } else {
        if (!searchBar.classList.contains('p-invalid')) {
            searchBar.classList.add("p-invalid")
        }
        if (searchAlert.style.visibility === "hidden" || searchAlert.style.visibility !== "visible") {
             searchAlert.style.visibility = "visible"
        }
    }
}


const directToCardPage = (e: AutoCompleteItemUnselectEvent) => {
    selectedConcept.value = ''

    router.push({
        name: 'cardview',
        params: {
            'concept': e.value.concept,
            'id': e.value.id
        },
        replace: true
    })
}
</script>
<!---------------------------------------------------------------------------->
<template>
<div class="search-container">
    <i class="pi pi-search" style="font-size: 1.4rem; padding: 0 10px;"></i>
    <AutoComplete id="navbar-search-bar" aria-describedby="navbar-search-alert" v-model="selectedConcept" :suggestions="resultsList" @complete="searchConcept()" @item-select="directToCardPage($event)" field="name" placeholder="Search..."/>
    <small id="navbar-search-alert" class="p-error">{{searchAlertSmall}}</small>
</div>
</template>
<!---------------------------------------------------------------------------->
<style scoped>
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
