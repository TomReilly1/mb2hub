<template>
    <footer>
        <div class="footer">
            <ul>
                <li>
                    <a href="https://www.github.com/TomReilly1">
                        <i class="pi pi-github" style="font-size: 2rem"></i>
                    </a>
                </li>
            </ul>
        </div>
    </footer>
</template>
<!---------------------------------------------------------->
<script setup lang="ts">
    
</script>
<!---------------------------------------------------------->
<style scoped>
    footer {
        position: absolute;
        right: 0;
        bottom: 0;
        left: 0;
        height: 8rem;
        width: 100%;
        margin: 30px 0 0;
    }

    .footer {
        height: 100%;
        display: flex;
        justify-content: center;
        align-items: middle;
        background-color: var(--gray-900);
        margin: 30px 0 0;
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

    a {
        color: var(--yellow-400);
        height: 100%;
    }

    a:hover {
        color: var(--yellow-300);
    }

    i {
        border-radius: 100%;
        background-color: rgba(0, 0, 0, 0.2);
        box-shadow: 0 0 20px 5px rgba(0, 0, 0, 0.8);
        transition: background-color 0.3s, box-shadow 0.3s;
    }

    i:hover {
        background-color: var(--bluegray-900);
        box-shadow: 0 0 0 4px var(--bluegray-900);
    }
</style>