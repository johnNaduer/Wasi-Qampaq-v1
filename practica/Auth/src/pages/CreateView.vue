<template>
  <div class="container mx-auto">
    <h2 class="text-2xl font-bold mb-4">Agregar Usuario</h2>
    <form class="max-w-sm" @submit="addTenant">
      <div class="mb-4">
        <label for="text" class="block text-gray-700 font-bold mb-2">Name:</label>
        <input type="text" id="" required v-model="name"
          class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-blue-500">
      </div>
      <div class="mb-4">
        <label for="text" class="block text-gray-700 font-bold mb-2">Surname:</label>
        <input type="text" id="" required v-model="firstLastName"
          class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-blue-500">
      </div>
      <div class="mb-4">
        <label for="text" class="block text-gray-700 font-bold mb-2">Second Surname:</label>
        <input type="text" id="" required v-model="secondLastName"
          class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-blue-500">
      </div>
      <div class="mb-4">
        <label for="number" class="block text-gray-700 font-bold mb-2">DNI/Inmigration Card:</label>
        <input type="text" id="" required v-model="dni"
          class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-blue-500">
      </div>
      <div class="mb-4">
        <label for="tel" class="block text-gray-700 font-bold mb-2">Phone:</label>
        <input type="text" id="" required v-model="phone"
          class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-blue-500">
      </div>
      <div class="mb-4">
        <label for="email" class="block text-gray-700 font-bold mb-2">Email:</label>
        <input type="text" id="" required v-model="email"
          class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-blue-500">
      </div>
      <div class="mb-4">
        <label for="date" class="block text-gray-700 font-bold mb-2">Star Date:</label>
        <input type="date" id="" required v-model="startDate"
          class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-blue-500">
      </div>
      <div class="mb-4">
        <label for="date" class="block text-gray-700 font-bold mb-2">Final Date:</label>
        <input type="date" id="" required v-model="endDate"
          class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-blue-500">
      </div>
       <div class="mb-4">
        <label for="date" class="block text-gray-700 font-bold mb-2">Espace-ID:</label>
        <input type="text" id="" required v-model="espacioNumero"
      class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-blue-500">
      </div>
      <div class="mb-4">
        <label for="number" class="block text-gray-700 font-bold mb-2">Property-ID:</label>
        <input type="text" id="" required v-model="idProperty"
          class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-blue-500">
      </div>
      <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
        Guardar
      </button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      firstLastName: '',
      secondLastName: '',
      dni: '',
      phone: '',
      email: '',
      startDate: '',
      endDate: '',
      espacioNumero: '',
      idProperty: '',
      message: ''
    };
  },
  methods: {
    addTenant(event) {
      event.preventDefault();

      const url = 'http://localhost:5001/add_tenant'; // Reemplaza con tu ruta en Flask para agregar un inquilino

      const data = {
        name: this.name,
        first_last_name: this.firstLastName,
        second_last_name: this.secondLastName,
        dni: this.dni,
        phone: this.phone,
        email: this.email,
        start_date: this.startDate,
        end_date: this.endDate,
        espacio_numero: this.espacioNumero,
        id_propiedad: this.idProperty
      };

      axios.post(url, data)
        .then(response => {
          this.message = response.data.message;
        })
        .catch(error => {
          console.error(error);
          this.message = 'Error al agregar el inquilino';
        });

      // Restablece los campos del formulario después de agregar el inquilino
      this.name = '';
      this.firstLastName = '';
      this.secondLastName = '';
      this.dni = '';
      this.phone = '';
      this.email = '';
      this.startDate = '';
      this.endDate = '';
      this.espacioNumero = '';
      this.idProperty = '';
    }
  }
};
</script>

