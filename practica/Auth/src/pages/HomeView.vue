<script setup>

const handleSubmit = () => {
    console.log('Hola')
}

</script>

<template>
    
    <div class="bg-image h-[100vh] ">
    <div class="flex items-center justify-center fixed inset-0">
        <form @submit.prevent="handleSubmit"
                class="border-2 border-white bg-opacity-50 text-white flex justify-center flex-col p-5 rounded-md shadow-lg">

                <h1 class="text-center text-3xl">Ingrese credenciales</h1>

                <!-- <div class="py-5">
                        <label for="" class="block text-center">Ingrese Email</label>
                    
                    </div> -->
                <input type="email" placeholder="email" class="border-white border-b-2 my-5">

                <input type="password" placeholder="password" class="border-white border-b-2 my-5">

                <button type="submit" class="my-5 py-1 bg-blue-600 rounded">Ingresar</button>
            </form>
        </div>
    </div>
</template>

<style scoped>
.bg-image {
    background-image: url('../assets/imgs/casaFondo.jpg');
}
</style>