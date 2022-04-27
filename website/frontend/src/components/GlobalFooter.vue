<template>
    <footer>
        <div class="footer">
            <ul>
                <li>
                    <span>&#169; MB2 Hub</span>
                </li>
                <li>
                    <i class="pi pi-github" style="font-size: 2rem"></i>
                </li>
            </ul>
        </div>
    </footer>
</template>



<script setup>
    
</script>



<style scoped>
    footer {
        position: absoulte;
        bottom: 0;
        background-color: lightgreen;
        height: 10rem;
        width: 100%;
    }

    .footer {
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: middle;
    }

    ul {
        padding: 0;
        margin: 0;
        list-style: none;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: middle;
    }

    li {
        font-size: 1.5rem;
        padding: 1rem 0;
    }

    
</style>