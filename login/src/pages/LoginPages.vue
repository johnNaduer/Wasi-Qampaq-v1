<script setup>
import { reactive } from 'vue';
import http from '../services/http.js'


const user = reactive({
    email:'',
    password:''
})

const login = async () => {
    try {
        const {data} = await http.post('/login', user);
        console.log(data)
    } catch (error) {
        console.log(error?.response?.data);
    }
} 
</script>

<template>
    <div class="bg-image h-[100vh]">

        <div class="flex items-center justify-center fixed inset-0">
            <form @submit.prevent="login"
                class="border-2 border-black text-white flex justify-center flex-col p-5 rounded-md shadow-2xl backdrop-sepia">

                <h1 class="text-center text-3xl">Ingrese credenciales</h1>
                <input type="email" placeholder="email" class="border-white border-b-2 my-5 placeholder:ps-2" id="email" v-model="user.email">

                <input type="password" placeholder="password" class="border-white border-b-2 my-5 placeholder:ps-2"
                    id="password" v-model="user.password">

                <div class="flex justify-between">
                    <router-link :to="{ name: 'register' }" class="text-sm pe-5">Create una cuenta</router-link>
                    <router-link :to="{ name: 'login' }" class="text-sm ps-5">Olvidaste tu contraseña?</router-link>
                </div>

                <button type="submit" class="my-5 py-1 bg-gray-500 rounded" id="enviar">Ingresar</button>
            </form>

        </div>
    </div>
</template>

<style scoped>
.bg-image {
    background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('../assets/casaFondo.jpg');
}

#email {
    background-color: rgba(249, 249, 250, 0.1);
}

#password {
    background-color: rgba(249, 249, 250, 0.1);
}

/* #enviar {
  background-color: rgba(255, 255, 255, 0.1);
} */
</style>