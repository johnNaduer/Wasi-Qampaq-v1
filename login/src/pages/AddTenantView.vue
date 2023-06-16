<template>
  <div>
    <h1>Add Tenant</h1>
    <form @submit="addTenant">
      <input type="text" v-model="name" placeholder="Name">
      <input type="text" v-model="firstLastName" placeholder="First Last Name">
      <input type="text" v-model="secondLastName" placeholder="Second Last Name">
      <input type="text" v-model="dni" placeholder="Dni">
      <input type="text" v-model="phone" placeholder="Phone">
      <input type="text" v-model="email" placeholder="Email">
      <input type="text" v-model="startDate" placeholder="Start Date">
      <input type="text" v-model="endDate" placeholder="End Date">
      <input type="text" v-model="espacioNumero" placeholder="Espacio Numero">
      <input type="text" v-model="idProperty" placeholder="Id Property">
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
        id_property: this.idProperty       
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

