<script setup>
</script>
<template>
    <div class="bg-image h-[100vh] ">
        <div class="flex items-center justify-center fixed inset-0 backdrop-brightness-50 ">
            <form class="bg-black bg-opacity-50 text-white flex justify-center flex-col p-8 rounded-md shadow-lg">
                <h1 class="text-center text-3x1">Register</h1>
                <input type="text" placeholder="name" class="text-black border-white border-b-2 my-3">
                <input type="email" placeholder="email" class="text-black border-white border-b-2 my-0.3">
                <input type="password" placeholder="password" class="text-black border-white border-b-2 my-3">
                <input type="password" placeholder="confirm password" class="text-black border-white border-b-2 my-1">
                <button type="submit" class="my-5 py-1 bg-violet-600 rounded cursor-pointer">
                    Submit
                </button>
            </form>
        </div>
    </div>
</template>
<style scoped>
    .bg-image {
    background-image: url('../assets/imgs/registro_atardecer.jpg');
}

</style>
