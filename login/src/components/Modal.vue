<template>
  <div class="fixed inset-0 flex items-center justify-center z-50 bg-black bg-opacity-50">
    <div class="bg-white p-8">
      <form @submit.prevent="handleSubmit"
            class="border-2 border-white bg-white w-96 flex justify-center flex-col p-5 rounded-md shadow-xl shadow-gray-300">
        <input v-model="name" type="text" placeholder="Nombres y Apellidos"
               class="border-gray-400 border px-3 py-1 rounded-md mb-5">
        <input v-model="email" type="email" placeholder="Correo electrónico"
               class="border-gray-400 border px-3 py-1 rounded-md mb-5">
        <input v-model="password" type="password" placeholder="Contraseña"
               class="border-gray-400 border px-3 py-1 rounded-md mb-5">
        <input v-model="confirmPassword" type="password" placeholder="Repite Contraseña"
               class="border-gray-400 border px-3 py-1 rounded-md mb-5">
        <button class="mt-5 bg-green-500 text-xl py-3 rounded text-white font-semibold mb-3">
          Crear cuenta nueva
        </button>
        <button @click="closeModal">Cerrar</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';

const name = ref('');
const email = ref('');
const password = ref('');
const confirmPassword = ref('');

const handleSubmit = () => {
  // Enviar los datos al backend para almacenarlos en tu modelo

  axios.post('http://localhost:5001/register', {
    name: name.value,
    email: email.value,
    password: password.value,
    password_2: confirmPassword.value
  })
    .then(response => {
      // Manejar la respuesta del backend
      console.log(response.data);
    })
    .catch(error => {
      // Manejar el error en caso de que ocurra
      console.error(error);
    });
};

defineProps({
  closeModal: Function,
});
</script>


