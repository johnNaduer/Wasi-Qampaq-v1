<template>
    <div class="p-4">
        <div class="card">
            <h2 class="text-2xl font-bold mb-4 text-center">Tenants</h2>
            <div>
                <ModalView />
            </div>
            <div class="card-body">
                <table id="data" class="w-full bg-white rounded-lg shadow-lg">
                    <thead>
                        <tr>
                            <th class="px-6 py-4 bg-blue-500 text-white">Id</th> 
                            <th class="px-6 py-4 bg-blue-500 text-white">Name</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">Surname</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">Second Surname</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">DNI/Inmigration Card</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">Phone</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">Email</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">Start Date</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">Final Date</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">Espacio-Numero</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">Property-ID</th>
                            <th class="px-6 py-4 bg-blue-500 text-white">Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(tenant, index) in tenants" :key="tenant.id">
                        <td class="px-6 py-4 border">{{ tenant.id }}</td>
                        <td class="px-6 py-4 border">{{ tenant.name }}</td>
                        <td class="px-6 py-4 border">{{ tenant.first_last_name }}</td>
                        <td class="px-6 py-4 border">{{ tenant.second_last_name }}</td>
                        <td class="px-6 py-4 border">{{ tenant.dni }}</td>
                        <td class="px-6 py-4 border">{{ tenant.phone }}</td>
                        <td class="px-6 py-4 border">{{ tenant.email }}</td>
                        <td class="px-6 py-4 border">{{ tenant.start_date }}</td>
                        <td class="px-6 py-4 border">{{ tenant.end_date }}</td>
                        <td class="px-6 py-4 border">{{ tenant.espacio_numero }}</td>
                        <td class="px-6 py-4 border">{{ tenant.id_propiedad }}</td>
                                                   
                       <td class="px-6 py-4 border">
                            <div class="flex justify-end">
                                <button @click="editData(index)" class="px-4 py-2 bg-green-500 text-white rounded-full mr-2 hover:bg-green-600 transition-colors duration-200 ease-in-out">Editar</button>
                                <button @click="deleteData(index)" class="px-4 py-2 bg-red-500 text-white rounded-full hover:bg-red-600 transition-colors duration-200 ease-in-out">Eliminar</button>
                            </div>
                        </td>    
                        </tr>
                    </tbody>
                </table>
            </div>        
          <EditTenant v-if="isModalVisible" :tenant="selectedTenant" @close="isModalVisible = false"/>
        </div>
    </div>
</template>


<script>

import axios from 'axios';
import ModalView from '../components/ModalView.vue';


export default {
  data() {
    return {
      tenants: [], // Agrega la propiedad "tenants" para almacenar la lista de inquilinos
      isModalVisible: false,
      selectedTenant: null, // propiead para almacenar el inquilino selecto
    };
  },
  created() {
    this.fetchTenants(); // Llama al método para obtener los datos de los inquilinos cuando se carga el componente
  },
  methods: {
    fetchTenants() {
      // Realiza una solicitud GET a la API para obtener la lista de inquilinos
      const url = 'http://localhost:5001/tenants'; // Reemplaza con la ruta correcta de tu API
      axios.get(url)
        .then(response => {
          this.tenants = response.data; // Asigna los datos de los inquilinos a la propiedad "tenants"
        })
        .catch(error => {
          console.error(error);
        });
    },
    editData(index) {
      this.selectedTenant = this.tenants[index]; //asigna el inquilino seleccionado a selectedTenant
      this.isModalVisible = true; // muestra el formulario de edicion (modal)
    },
    deleteData(index) {
       const tenantId = this.tenants[index].id; // Obtiene el ID del inquilino a eliminar

      // Realiza una solicitud DELETE a la API para eliminar el inquilino
      const url = `http://localhost:5001/tenants/${tenantId}`; // Reemplaza con la ruta correcta de tu API
      axios
        .delete(url)
        .then(response => {
          // Elimina el inquilino de la lista local
          this.tenants.splice(index, 1);
        })
        .catch(error => {
          console.error(error);
        });
    }
  }
};
</script>

























<style scoped>

</style>
