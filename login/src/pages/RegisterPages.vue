<script setup>
import { reactive } from 'vue';
import http from '../services/http.js'

const createUser = reactive({
    name: '',
    nick:'',
    email: '',
    password: ''
})

const registerData = async () => {
    try {
        const { data } = await http.post('/register', createUser)
        console.log(data)
    } catch (error) {
        console.log(error)
    }
}


</script>
<template>
    <div class="bg-image h-[100vh]">

        <div class="flex items-center justify-center fixed inset-0">
            <form @submit.prevent="registerData"
                class="border-2 border-black text-white flex justify-center flex-col p-5 w-96 rounded-md shadow-2xl backdrop-sepia">

                <h1 class="text-center text-3xl mb-5">Registrate</h1>
                <input type="text" placeholder="Nombre" class="border-white border-b-2 mb-5 placeholder:ps-2" id="name"
                    v-model="createUser.name">
                <input type="text" placeholder="Apellidos" class="border-white border-b-2 mb-5 placeholder:ps-2" id="nick"
                    v-model="createUser.nick">
                <input type="email" placeholder="email" class="border-white border-b-2 mb-5 placeholder:ps-2" id="email"
                    v-model="createUser.email">

                <input type="password" placeholder="password" class="border-white border-b-2 mb-5 placeholder:ps-2"
                    id="password" v-model="createUser.password">
                <input type="password" placeholder="repetir password" class="border-white border-b-2 mb-5 placeholder:ps-2"
                    id="re-password">

                <div class="flex justify-center">
                    <router-link :to="{ name: 'login' }" class="text-sm pe-5">Ya tienes cuenta?</router-link>
                </div>

                <button type="submit" class="my-5 py-1 bg-gray-500 rounded" id="enviar">Registrate</button>
            </form>

        </div>
    </div>
</template>
<style scoped>
.bg-image {
    background-image: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('../assets/casaFondo.jpg');
}

#name {
    background-color: rgba(249, 249, 250, 0.1);
}

#nick{
    background-color: rgba(249, 249, 250, 0.1);
}

#email {
    background-color: rgba(249, 249, 250, 0.1);
}

#password {
    background-color: rgba(249, 249, 250, 0.1);
}

#re-password {
    background-color: rgba(249, 249, 250, 0.1);
}
</style>