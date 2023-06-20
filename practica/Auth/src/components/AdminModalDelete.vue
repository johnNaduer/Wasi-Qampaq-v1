<template>
    <div>
      <button type="button" v-on:click="toggleModal()">
        Delete
      </button>
      <div v-if="showModal" class="overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none justify-center items-center flex">
        <div class="relative w-auto my-6 mx-auto max-w-6xl">
          <!--content-->
          <div class="border-0 rounded-lg shadow-lg relative flex flex-col w-full bg-white outline-none focus:outline-none">
            <!--header-->
            <div class="flex items-start justify-between p-5 border-b border-solid border-slate-200 rounded-t">
              <h3 class="text-3xl font-semibold">
                Elimar Información
              </h3>
            </div>
            <!--body-->
            <div class="relative p-6 flex-auto">
                Esta acción eliminará permanentemente el registro del Administrador. Todos los datos asociados a este administrador se perderán. ¿Estás seguro de que deseas continuar?
            </div>
            <!--footer-->
            <div class="flex items-center justify-end p-6 border-t border-solid border-slate-200 rounded-b">
              <button type="button" v-on:click="toggleModal()">
                Cancel
              </button>
              <button  type="button" v-on:click="toggleModal()">
                Acept
              </button>
            </div>
          </div>
        </div>
      </div>
      <div v-if="showModal" ></div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  
  const showModal = ref(false);
  
  function toggleModal() {
    showModal.value = !showModal.value;
  }
  </script>