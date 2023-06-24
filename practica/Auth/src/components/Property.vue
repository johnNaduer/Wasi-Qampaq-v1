<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Property</h1>
        <hr><br><br>
        <button
          type="button"
          class="btn btn-success btn-sm"
          @click="toggleAddBookModal">
          Add Property
        </button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
            <th class="col">ID</th>
            <th class="col">ID administrator</th>
            <th class="col">Name</th>
            <th class="col">Direction</th>
            <th class="col">Phone</th>
            <th class="col">Description</th>
            <th class="col">Actions</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(property, index) in propertys" :key="property.id">
              <td>{{ property.id }}</td>
              <td>{{ property.id_administrator }}</td>
              <td>{{ property.name }}</td>
              <td>{{ property.direction }}</td>
              <td>{{ property.phone }}</td>
              <td>{{ property.description }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm" @click="handleDeleteProperty(property)">Delete</button>

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
                <label for="addBookAuthor" class="form-label">ID:</label>

                <input type="text"
                  class="form-control"
                  id="addBookAuthor"
                  v-model="addPropertyForm.id"
                  placeholder="Enter author">

              </div>

             <div class="mb-3">
                <label for="addBookTitle" class="form-label"> ID administrador: </label>

                <input type="text" class="form-control" id="addBookTitle"  v-model="addPropertyForm.idAdministrador" placeholder="Enter title">

             </div>

             <div class="mb-3">
                <label for="addBookTitle" class="form-label"> Name: </label>

                <input type="text" class="form-control" id="addBookTitle" v-model="addPropertyForm.name" placeholder="Enter title">

             </div>

             <div class="mb-3">
                <label for="addBookTitle" class="form-label"> Direction: </label>

                <input type="text" class="form-control" id="addBookTitle" v-model="addPropertyForm.Direction" placeholder="Enter title">

             </div>

            <div class="mb-3">
                <label for="addBookTitle" class="form-label"> Phone: </label>

                <input type="text" class="form-control" id="addBookTitle" v-model="addPropertyForm.Phone" placeholder="Enter title">

             </div>


             <div class="mb-3">
                <label for="addBookTitle" class="form-label"> Description: </label>

                <input type="text" class="form-control" id="addBookTitle" v-model="addPropertyForm.Description" placeholder="Enter title">

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

      addPropertyForm: {      
      id: '',
      idAdministrador: '',
      name: '',
      Direction: '',
      Phone: '',
      Description: '',
      },

      propertys: [],
    };
  },
  methods: {
    addProperty(addproperty) {
    const path = 'http://localhost:5001/add_property';
    axios.post(path, addproperty)
        .then(() =>{
          this.fetchProperty();
        })
         .catch((error) => {

          console.log(error);
          this.fetchProperty();
        });
    },
     fetchProperty() {
      const path = 'http://localhost:5001/properties';
      axios.get(path)
        .then((response) => {
          this.propertys = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    handleAddSubmit() {
      this.toggleAddBookModal();

      const addproperty = {
      id: this.addPropertyForm.id,
      id_administrator: this.addPropertyForm.idAdministrador,
      name: this.addPropertyForm.name,
      direction: this.addPropertyForm.Direction,
      phone: this.addPropertyForm.Phone,
      description: this.addPropertyForm.Description,
      };

     this.addProperty(addproperty);
     this.initForm();
    },

    initForm() {
      this.addPropertyForm.id = '';
      this.addPropertyForm.idAdministrador = '';
      this.addPropertyForm.name = '';
      this.addPropertyForm.Direction = '';
      this.addPropertyForm.Phone = '';
      this.addPropertyForm.Description = '';
    },

    handleAddReset() {
      this.initForm();
    },

    handleDeleteProperty(property) {
      this.removeProperty(property.id);
    },

    removeProperty(propertyID) {
      const path = `http://localhost:5001/properties/${propertyID}`;
      axios.delete(path)
       .then(() => {
         this.fetchProperty();
       })
        .catch((error) => {
          console.error(error);
         this.fetchProperty();
        });
    },

    toggleAddBookModal() {
      const body = document.querySelector('body');
      this.activeAddBookModal = !tihis.activeAddBookModal;
      if (this.activeAddBookModal) {
        body.classList.add('modal-open');
      } else {
        body.classList.remove('modal-open');
      }
    },
  },
  created() {
    this.fetchProperty();
  },
};
</script>
