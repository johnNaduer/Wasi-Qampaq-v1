<template>
  <div>
    <h1>Add Tenant</h1>
    <form @submit="addTenant">
      <input type="text" v-model="name" placeholder="Name">
      <input type="text" v-model="lastName" placeholder="Last Name">
      <input type="text" v-model="email" placeholder="Email">
      <input type="text" v-model="phone" placeholder="Phone">
      <input type="text" v-model="espacioNumero" placeholder="Espacio Numero">
      <button type="submit">Add Tenant</button>
    </form>
    <p>{{ message }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      name: '',
      lastName: '',
      email: '',
      phone: '',
      espacioNumero: '',
      message: ''
    };
  },
  methods: {
    addTenant(event) {
      event.preventDefault();

      const url = 'http://localhost:5001/add_tenant'; // Reemplaza con tu ruta en Flask para agregar un inquilino

      const data = {
        name: this.name,
        last_name: this.lastName,
        email: this.email,
        phone: this.phone,
        espacio_numero: this.espacioNumero
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
      this.lastName = '';
      this.email = '';
      this.phone = '';
      this.espacioNumero = '';
    }
  }
};
</script>

