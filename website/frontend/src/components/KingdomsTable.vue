<script setup>
import { ref, onMounted } from "vue";
import { useRoute } from 'vue-router';


const route = useRoute();
const props = defineProps({kingdomsArr: Array});
const loading = ref(true);


onMounted(() => {
    loading.value = false;
})


const formatColor = (color) => {
    const hexValue = color.slice(-6);
    return '#' + hexValue;
};
</script>
<!------------------------------------------------------------------->
<template>
<div id="kingdom-table" class="concept-table">
    <DataTable :value="kingdomsArr" class="p-datatable-sm" rowHover showGridlines dataKey="id" :loading="loading" responsiveLayout="scroll">
        <template #empty>
            No kingdoms data found.
        </template>
        <template #loading>
            Loading kingdoms data. Please wait.
        </template>
        <Column field="id" header="ID" headerStyle="justify-content: center; text-align: center;" sortable>
            <template #body="{data}">
                <router-link :to="{name: 'cardview', params: {concept: route.params.concept, id: data.id}}" class="id-link">
                    {{data.id}}
                </router-link>
            </template>
        </Column>
        <Column field="name" header="Name" sortable></Column>
        <Column field="title" header="Kingdom Title" sortable></Column>
        <Column field="ruler_title" header="Ruler Title" sortable></Column>
        <Column field="culture" header="Culture" sortable></Column>
        <Column field="primary_banner_color" header="Banner Color-1" bodyStyle="text-align: center;">
            <template #body="{data}">
                <input type="color" :value="formatColor(data.primary_banner_color)" class="color-data" disabled>
                <span class="color-text">{{formatColor(data.primary_banner_color)}}</span>
            </template>
        </Column>
        <Column field="secondary_banner_color" header="Banner Color-2" bodyStyle="text-align: center;">
            <template #body="{data}">
                <input type="color" :value="formatColor(data.secondary_banner_color)" class="color-data" disabled>
                <span class="color-text">{{formatColor(data.secondary_banner_color)}}</span>
            </template>
        </Column>
        <Column field="color_1" header="Color-1" bodyStyle="text-align: center;">
            <template #body="{data}">
                <input type="color" :value="formatColor(data.color_1)" class="color-data" disabled>
                <span class="color-text">{{formatColor(data.color_1)}}</span>
            </template>
        </Column>
        <Column field="color_2" header="Color-2" bodyStyle="text-align: center;">
            <template #body="{data}">
                <input type="color" :value="formatColor(data.color_2)" class="color-data" disabled>
                <span class="color-text">{{formatColor(data.color_2)}}</span>
            </template>
        </Column>
        <Column field="alternative_color_1" header="Alt Color-1" bodyStyle="text-align: center;">
            <template #body="{data}">
                <input type="color" :value="formatColor(data.alternative_color_1)" class="color-data" disabled>
                <span class="color-text">{{formatColor(data.alternative_color_1)}}</span>
            </template>
        </Column>
        <Column field="alternative_color_2" header="Alt Color-2" bodyStyle="text-align: center;">
            <template #body="{data}">
                <input type="color" :value="formatColor(data.alternative_color_2)" class="color-data" disabled>
                <span class="color-text">{{formatColor(data.alternative_color_2)}}</span>
            </template>
        </Column>
    </DataTable>
</div>
</template>
<!------------------------------------------------------------------->
<style scoped>
.global-filter {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
}

#kingdom-table {
    background-color: var(--bluegray-900);
    border: 3px solid var(--bluegray-700);
    margin: 0 auto;
    width: fit-content;
    max-width: 98%;
    box-shadow: 0 0 1px 2px #3f4b5b;
}

a {
    color: var(--yellow-400);
}

a:hover {
    color: var(--yellow-100);
}

.router-link-active {
    color: var(--yellow-200)
}

.color-data {
    margin: 0;
    border: 0;
    padding: 0;
    width: 100%;
    max-width: 75px;
}

.color-data::after {
    height: 100%;
    /* vertical-align: middle; */
}

.color-text::after {
    float: left;
    margin: 0;
    border: 0;
    padding: 0;
}

.center-header {
    text-align: center;
    justify-content: center;
    background-color: aqua !important;
}
</style>
