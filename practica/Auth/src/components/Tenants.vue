<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Tenant</h1>
        <hr><br><br>
        <button
          type="button"
          class="btn btn-success btn-sm"
          @click="toggleAddBookModal">
          Add Tenant
        </button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
            <th class="col">ID</th>
            <th class="col">Name</th>
            <th class="col">Surname</th>
            <th class="col">Second Surname</th>
            <th class="col">DNI / Inmigration Card</th>
            <th class="col">Phone</th>
            <th class="col">Email</th>
            <th class="col">Start Date</th>
            <th class="col">Final Date</th>
            <th class="col">Espace-ID</th>
            <th class="col">Property-ID</th>
            <th class="col">Actions</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(tenant, index) in tenants" :key="tenant.id">
              <td>{{ tenant.id }}</td>
              <td>{{ tenant.name }}</td>
              <td>{{ tenant.first_last_name }}</td>
              <td>{{ tenant.second_last_name }}</td>
              <td>{{ tenant.dni }}</td>
              <td>{{ tenant.phone }}</td>
              <td>{{ tenant.email }}</td>
              <td>{{ tenant.start_date }}</td>
              <td>{{ tenant.end_date }}</td>
              <td>{{ tenant.espacio_numero }}</td>
              <td>{{ tenant.id_propiedad }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm">Delete</button>

                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- add new book modal -->
    <div
      ref="addBookModal"
      class="modal fade"
      :class="{ show: activeAddBookModal, 'd-block': activeAddBookModal }"
      tabindex="-1"
      role="dialog">
      <div class="modal-dialog" role="document">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title">Add a new Tenant</h5>
            <button
              type="button"
              class="close"
              data-dismiss="modal"
              aria-label="Close"
              @click="toggleAddBookModal">
              <span aria-hidden="true">&times;</span>
            </button>
          </div>
          <div class="modal-body">
            <form>
              <div class="mb-3">
                <label for="addBookAuthor" class="form-label">Name:</label>
                 
                <input type="text"
                  class="form-control"
                  id="addBookAuthor"
                  v-model="addTenantForm.name"
                  placeholder="Enter author">
              
              </div>
                          
             <div class="mb-3">
                <label for="addBookTitle" class="form-label"> Surname: </label>
                
                <input type="text" class="form-control" id="addBookTitle" v-model="addTenantForm.firstLastName" placeholder="Enter title">
                
             </div>          

             <div class="mb-3">
                <label for="addBookTitle" class="form-label"> Second Surname: </label>
                
                <input type="text" class="form-control" id="addBookTitle"  v-model="addTenantForm.secondLastName" placeholder="Enter title">
                
             </div>  

             <div class="mb-3">
                <label for="addBookTitle" class="form-label"> Dni/Inmigration Card: </label>
                
                <input type="text" class="form-control" id="addBookTitle" v-model="addTenantForm.dni" placeholder="Enter title">
                
             </div>               

             <div class="mb-3">
                <label for="addBookTitle" class="form-label"> Phone: </label>

                <input type="text" class="form-control" id="addBookTitle" v-model="addTenantForm.phone" placeholder="Enter title">

             </div>   

             <div class="mb-3">
                <label for="addBookTitle" class="form-label"> Email: </label>
                
                <input type="text" class="form-control" id="addBookTitle" v-model="addTenantForm.email" placeholder="Enter title">
                
             </div>              

             <div class="mb-3">
                <label for="addBookTitle" class="form-label"> Start Date: </label>
                
                <input type="date" class="form-control" id="addBookTitle" v-model="addTenantForm.startDate" placeholder="Enter title">
                
             </div>           

             <div class="mb-3">
                <label for="addBookTitle" class="form-label"> Final Date: </label>
                
                <input type="date" class="form-control" id="addBookTitle" v-model="addTenantForm.endDate" placeholder="Enter title">
                
             </div>             

            <div class="mb-3">
                <label for="addBookTitle" class="form-label"> Espace-Number: </label>
            
                <input type="text" class="form-control" id="addBookTitle" v-model="addTenantForm.espacioNumero" placeholder="Enter title">
                
             </div>

             <div class="mb-3">
                <label for="addBookTitle" class="form-label"> Property-Id: </label>
                
                <input type="text" class="form-control" id="addBookTitle" v-model="addTenantForm.idProperty" placeholder="Enter title">
                
             </div>
             

             <!--
              <div class="mb-3 form-check">
                
                <input
                  type="checkbox"
                  class="form-check-input"
                  id="addBookRead"
                  v-model="addBookForm.read">                
                <label class="form-check-label" for="addBookRead">Read?</label>
              </div>
             --> 

              <div class="btn-group" role="group">
                <button
                  type="button"
                  class="btn btn-primary btn-sm"
                  @click="handleAddSubmit">
                  Submit
                </button>
                <button
                  type="button"
                  class="btn btn-danger btn-sm"
                  @click="handleAddReset">
                  Reset
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div v-if="activeAddBookModal" class="modal-backdrop fade show"></div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      activeAddBookModal: false,
      
      addTenantForm: {
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
      },
    
      tenants: [],
    };
  },
  methods: {
    addTenant(addtenant) {
    const path = 'http://localhost:5001/add_tenant';
    },
     fetchTenants() {
      const path = 'http://localhost:5001/tenants'; // Reemplaza con la ruta correcta de tu API , solicita get a la api
      axios.get(path)
        .then((response) => {
          this.tenants = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    handleAddSubmit() {
      this.toggleAddBookModal();

      const addtenant = {
      name: this.addTenantForm.name,
      first_last_name: this.addTenantForm.firstLastName, 
      second_last_name: this.addTenantForm.secondLastName, 
      dni: this.addTenantForm.dni,      
      phone: this.addTenantForm.phone,      
      email: this.addTenantForm.email, 
      start_date: this.addTenantForm.startDate,       
      end_date: this.addTenantForm.endDate,       
      espacio_numero: this.addTenantForm.espacioNumero,
      id_propiedad: this.addTenantForm.idProperty, 
      };

    },
    toggleAddBookModal() {
      const body = document.querySelector('body');
      this.activeAddBookModal = !this.activeAddBookModal;
      if (this.activeAddBookModal) {
        body.classList.add('modal-open');
      } else {
        body.classList.remove('modal-open');
      }
    },
  },
  created() {
    this.fetchTenants();
  },
};
</script>
