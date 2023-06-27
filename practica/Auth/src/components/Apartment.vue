<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Apartment</h1>
        <hr><br><br>
        <button
          type="button"
          class="btn btn-success btn-sm"
          @click="toggleAddBookModal">
          Add Apartment
        </button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
            <th class="col">ID</th>
            <th class="col">ID propiedad</th>
            <th class="col">Numero</th>
            <th class="col">Descripcion</th>
            <th class="col">Precio</th>
            <th class="col">Disponibilidad</th>
            <th class="col">Actions</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(espacio, index) in espacios" :key="espacio.id">
              <td>{{ espacio.id }}</td>
              <td>{{ espacio.id_propiedad }}</td>
              <td>{{ espacio.numero }}</td>
              <td>{{ espacio.descripcion }}</td>
              <td>{{ espacio.precio }}</td>
              <td>{{ espacio.disponibilidad }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm">Update</button>
                  <button type="button" class="btn btn-danger btn-sm" @click="handleDeleteEspacio(espacio)">Delete</button>

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
                <label for="addBookAuthor" class="form-label">ID property</label>

                <input type="text"
                  class="form-control"
                  id="addBookAuthor"
                  v-model="addEspacioForm.id_propiedad"
                  placeholder="Enter author">

              </div>

             <div class="mb-3">
                <label for="addBookTitle" class="form-label"> number: </label>

                <input type="text" class="form-control" id="addBookTitle"  v-model="addEspacioForm.numero" placeholder="Enter title">

             </div>

             <div class="mb-3">
                <label for="addBookTitle" class="form-label"> Description: </label>

                <input type="text" class="form-control" id="addBookTitle" v-model="addEspacioForm.descripcion" placeholder="Enter title">

             </div>

             <div class="mb-3">
                <label for="addBookTitle" class="form-label"> Price: </label>

                <input type="text" class="form-control" id="addBookTitle" v-model="addEspacioForm.precio" placeholder="Enter title">

             </div>

            <div class="mb-3">
                <label for="addBookTitle" class="form-label"> availability: </label>

                <input type="text" class="form-control" id="addBookTitle" v-model="addEspacioForm.disponibilidad" placeholder="Enter title">

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

      addEspacioForm: {      
        id_propiedad: '',
        numero: '',
        descripcion: '',
        precio: '',
        disponibilidad: '',
      },

      espacios: [],
    };
  },
  methods: {
    addEspacio(addEspacio) {
    const path = 'http://localhost:5001/add_espacio';
    axios.post(path, addEspacio)
        .then(() =>{
          this.fetchEspacios();
        })
         .catch((error) => {

          console.log(error);
          this.fetchEspacios();
        });
    },
     fetchEspacios() {
      const path = 'http://localhost:5001/espacios';
      axios.get(path)
        .then((response) => {
          this.espacios = response.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    handleAddSubmit() {
      this.toggleAddBookModal();

      const addEspacio = {
        id_propiedad: this.addEspacioForm.id_propiedad,
        numero: this.addEspacioForm.numero,
        descripcion: this.addEspacioForm.descripcion,
        precio: this.addEspacioForm.precio,
        disponibilidad: this.addEspacioForm.disponibilidad,
      };

     this.addEspacio(addEspacio);
     this.initForm();
    },

    initForm() {
      this.addEspacioForm.id_propiedad = '';
      this.addEspacioForm.numero = '';
      this.addEspacioForm.descripcion = '';
      this.addEspacioForm.precio = '';
      this.addEspacioForm.disponibilidad = '';
    },

    handleAddReset() {
      this.initForm();
    },

    handleDeleteEspacio(espacio) {
      this.removeEspacio(espacio.id);
    },

    removeEspacio(espacioID) {
      const path = `http://localhost:5001/espacios/${espacioID}`;
      axios.delete(path)
       .then(() => {
         this.fetchProperty();
       })
        .catch((error) => {
          console.error(error);
         this.fetchEspacios();
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
    this.fetchEspacios();
  },
};
</script>
