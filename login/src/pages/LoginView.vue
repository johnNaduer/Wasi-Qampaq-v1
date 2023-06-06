<script setup>
import { ref } from 'vue';
import Modal from '../components/Modal.vue'

const modal = ref(false)

const openModal = () => {
    modal.value = true
}

const closeModal = () => {
    modal.value = false
}
</script>

<template>
    <div class="h-[100vh] bg-blue-300">
        <div class="flex items-center justify-around container w-8/12 mx-auto h-screen">
            <div>
                <h1 class="text-5xl">Nombre</h1>
                <p class="text-xl font-semibold">Nombre te ayuda a conseguir Habitaciones</p>
                <p class="text-xl font-semibold">y/o Departamentos al mejor precio</p>
            </div>
            <div>
                <form action="" @submit.prevent=""
                    class="border-2 border-white bg-white w-96 flex justify-center flex-col p-5 rounded-md shadow-xl shadow-gray-300">
                    <input type="gmail" placeholder="Correo electrónico"
                        class="border-gray-400 border px-3 py-1 rounded-md mb-5">
                    <input type="password" placeholder="Contraseña"
                        class="border-gray-400 border px-3 py-1 rounded-md mb-5">
                    <button type="submit" class=" bg-blue-600 py-3 rounded-md text-xl text-white font-semibold mb-3">
                        Iniciar sesión </button>
                    <router-link to="/recuperar_password" class="text-center text-blue-500 mb-5">¿Has olvidado la
                        contraseña?</router-link>
                    <hr />
                    <button class="mt-5 bg-green-500 text-xl py-3 rounded text-white font-semibold mb-3" @click="openModal"> Crear cuenta nueva
                    </button>
                </form>
            </div>
        </div>

        <div v-if="modal">
            <Modal :closeModal="closeModal"/>
        </div>

    </div>
</template>

<style scoped></style>