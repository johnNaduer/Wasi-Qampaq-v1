<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Manager</h1>
        <hr><br><br>
        <button
          type="button"
          class="btn btn-success btn-sm"
          @click="toggleAddBookModal">
          Add Manager
        </button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
            <th class="col">ID</th>
            <th class="col">Name</th>
            <th class="col">Last Name</th>
            <th class="col">DNI / Inmigration Card</th>
            <th class="col">Email</th>
            <th class="col">Phone</th>
            <th class="col">Start Date</th>
            <th class="col">End Date</th>
            <th class="col">Actions</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(administrator, index) in administrators" :key="administrator.id">
              <td>{{ administrator.id }}</td>
              <td>{{ administrator.name_administrador }}</td>
              <td>{{ administrator.apellidos_administrador }}</td>
              <td>{{ administrator.dni }}</td>
              <td>{{ administrator.email }}</td>
              <td>{{ administrator.phone }}</td>
              <td>{{ administrator.start_date }}</td>
              <td>{{ administrator.end_date }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm" @click="handleDeleteAdministrator(administrator)">Delete</button>

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
                  v-model="addAdministratorForm.name"
                  placeholder="Enter author">

              </div>

             <div class="mb-3">
                <label for="addBookTitle" class="form-label"> Last name: </label>

                <input type="text" class="form-control" id="addBookTitle"  v-model="addAdministratorForm.LastName" placeholder="Enter title">

             </div>

             <div class="mb-3">
                <label for="addBookTitle" class="form-label"> Dni/Inmigration Card: </label>

                <input type="text" class="form-control" id="addBookTitle" v-model="addAdministratorForm.dni" placeholder="Enter title">

             </div>

             <div class="mb-3">
                <label for="addBookTitle" class="form-label"> Email: </label>

                <input type="text" class="form-control" id="addBookTitle" v-model="addAdministratorForm.email" placeholder="Enter title">

             </div>

            <div class="mb-3">
                <label for="addBookTitle" class="form-label"> Phone: </label>

                <input type="text" class="form-control" id="addBookTitle" v-model="addAdministratorForm.phone" placeholder="Enter title">

             </div>


             <div class="mb-3">
                <label for="addBookTitle" class="form-label"> Start Date: </label>

                <input type="date" class="form-control" id="addBookTitle" v-model="addAdministratorForm.startDate" placeholder="Enter title">

             </div>

             <div class="mb-3">
                <label for="addBookTitle" class="form-label"> Final Date: </label>

                <input type="date" class="form-control" id="addBookTitle" v-model="addAdministratorForm.endDate" placeholder="Enter title">

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

      addAdministratorForm: {
      name: '',
      LastName: '',
      dni: '',
      email: '',
      phone: '',
      startDate: '',
      endDate: '',
      },

      administrators: [],
    };
  },
  methods: {
    addAdministrator(addadministrator) {
    const path = 'http://localhost:5001/add_administrator';
    axios.post(path, addadministrator)
        .then(() =>{
          this.fetchAdministrator();
        })
         .catch((error) => {

          console.log(error);
          this.fetchAdministrator();
        });
    },
     fetchAdministrator() {
      const path = 'http://localhost:5001/administrators'; // Reemplaza con la ruta correcta de tu API , solicita get a la api
      axios.get(path)
        .then((response) => {
          this.administrators = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    handleAddSubmit() {
      this.toggleAddBookModal();

      const addadministrator = {
      name_administrador: this.addAdministratorForm.name,
      apellidos_administrador: this.addAdministratorForm.LastName,
      dni: this.addAdministratorForm.dni,
      email: this.addAdministratorForm.email,
      phone: this.addAdministratorForm.phone,
      start_date: this.addAdministratorForm.startDate,
      end_date: this.addAdministratorForm.endDate,
      };

     this.addAdministrator(addadministrator);
     this.initForm();
    },

    initForm() {
      this.addAdministratorForm.name = '';
      this.addAdministratorForm.LastName = '';
      this.addAdministratorForm.dni = '';
      this.addAdministratorForm.email = '';
      this.addAdministratorForm.phone = '';
      this.addAdministratorForm.startDate = '';
      this.addAdministratorForm.endDate = '';
    },

    handleAddReset() {
      this.initForm();
    },

    handleDeleteAdministrator(administrator) {
      this.removeAdministrator(administrator.id);
    },

    removeAdministrator(administratorID) {
      const path = `http://localhost:5001/administrators/${administratorID}`;
      axios.delete(path)
       .then(() => {
         this.fetchAdministrator();
       })
        .catch((error) => {
          console.error(error);
         this.fetchAdministrator();
        });
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
    this.fetchAdministrator();
  },
};
</script>
