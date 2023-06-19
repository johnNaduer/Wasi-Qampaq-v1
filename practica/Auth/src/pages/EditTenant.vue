<template>
  <div>
    <h2 class="text-2xl font-bold mb-4">Editar Inquilino</h2>
    <form @submit.prevent="updateTenant">
      <div class="mb-4">
        <label class="block text-gray-700 font-bold mb-2" for="name">Nombre:</label>
        <input v-model="tenant.name" type="text" id="name" name="name" class="form-input w-full">
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 font-bold mb-2" for="firstLastName">Primer Apellido:</label>
        <input v-model="tenant.first_last_name" type="text" id="firstLastName" name="firstLastName" class="form-input w-full">
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 font-bold mb-2" for="secondLastName">Segundo Apellido:</label>
        <input v-model="tenant.second_last_name" type="text" id="secondLastName" name="secondLastName" class="form-input w-full">
      </div>
      <!-- Agrega los demás campos que deseas editar -->
      <div class="flex justify-end">
        <button type="submit" class="px-4 py-2 bg-blue-500 text-white rounded-full hover:bg-blue-600 transition-colors duration-200 ease-in-out">Guardar</button>
      <button @click="closeModal">Cancelar</button>
      </div>
    </form>
  </div>
</template>





<!--
<script>
import axios from 'axios';

export default {
  data() {
    return {
      tenant: {} // Objeto para almacenar los datos del inquilino a editar
    };
  },
  created() {
    // Obtiene los datos del inquilino a editar cuando se carga el componente
    const tenantId = this.$route.params.id; // Obtén el ID del inquilino desde la ruta
    this.fetchTenant(tenantId);
  },
  methods: {
    fetchTenant(id) {
      // Realiza una solicitud GET a la API para obtener los datos del inquilino a editar
      const url = `http://localhost:5001/tenants/${id}`;
      axios.get(url)
        .then(response => {
          this.tenant = response.data; // Asigna los datos del inquilino a editar al objeto "tenant"
        })
        .catch(error => {
          console.error(error);
        });
    },
    updateTenant() {
      const url = `http://localhost:5001/tenants/${this.tenant.id}`;
      axios.put(url, this.tenant)
        .then(response => {
          // Maneja la respuesta exitosa de la actualización del inquilino
          console.log('Inquilino actualizado:', response.data);
          // Redirecciona a la página de visualización de inquilinos u otra acción
        })
        .catch(error => {
          console.error(error);
          // Maneja el error en caso de fallo en la actualización del inquilino
        });
    },
    closeModal() {
      this.$emit('close'); // Emite el evento 'close' para cerrar el modal
    }
  }
};
</script>
-->
