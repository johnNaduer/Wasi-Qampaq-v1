<template>
  <div>
    <button class="bg-pink-500 text-white active:bg-pink-600 font-bold uppercase text-sm px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150" type="button" v-on:click="toggleModal()">
      Agregar
    </button>
    <div v-if="showModal" class="overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none justify-center items-center flex">
      <div class="relative w-auto my-6 mx-auto max-w-6xl">
        <!--content-->
        <div class="border-0 rounded-lg shadow-lg relative flex flex-col w-full bg-white outline-none focus:outline-none">
          <!--header-->
          <div class="flex items-start justify-between p-5 border-b border-solid border-slate-200 rounded-t">
            <h3 class="text-3xl font-semibold">
              Agregar Inquilino
            </h3>
            <button class="p-1 ml-auto bg-transparent border-0 text-black opacity-5 float-right text-3xl leading-none font-semibold outline-none focus:outline-none" v-on:click="toggleModal()">
              <span class="bg-transparent text-black opacity-5 h-6 w-6 text-2xl block outline-none focus:outline-none">
                ×
              </span>
            </button>
          </div>
          <!--body-->
          <div class="relative p-6 flex-auto">
            <div>
            <form class="flex flex-wrap -mx-4">
              <div class="w-full md:w-1/2 px-4 mb-4">
                <label for="name" class="block text-sm font-medium text-gray-700">Name</label>
                <input type="text" id="name" v-model="name" class="w-full bg-gray-100 border border-gray-300 rounded py-2 px-3 focus:outline-none focus:bg-white focus:border-blue-500" />
              </div>
              <div class="w-full md:w-1/2 px-4 mb-4">
                <label for="surname" class="block text-sm font-medium text-gray-700">Surname</label>
                <input type="text" id="surname" v-model="surname" class="w-full bg-gray-100 border border-gray-300 rounded py-2 px-3 focus:outline-none focus:bg-white focus:border-blue-500" />
              </div>
              <div class="w-full md:w-1/2 px-4 mb-4">
                <label for="secondSurname" class="block text-sm font-medium text-gray-700">Second Surname</label>
                <input type="text" id="secondSurname" v-model="secondSurname" class="w-full bg-gray-100 border border-gray-300 rounded py-2 px-3 focus:outline-none focus:bg-white focus:border-blue-500" />
              </div>
              <div class="w-full md:w-1/2 px-4 mb-4">
                <label for="dni" class="block text-sm font-medium text-gray-700">DNI/Inmigration Card</label>
                <input type="number" id="dni" v-model="dni" class="w-full bg-gray-100 border border-gray-300 rounded py-2 px-3 focus:outline-none focus:bg-white focus:border-blue-500" />
              </div>
              <div class="w-full md:w-1/2 px-4 mb-4">
                <label for="phone" class="block text-sm font-medium text-gray-700">Phone</label>
                <input type="tel" id="phone" v-model="phone" class="w-full bg-gray-100 border border-gray-300 rounded py-2 px-3 focus:outline-none focus:bg-white focus:border-blue-500" />
              </div>
              <div class="w-full md:w-1/2 px-4 mb-4">
                <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
                <input type="email" id="email" v-model="email" class="w-full bg-gray-100 border border-gray-300 rounded py-2 px-3 focus:outline-none focus:bg-white focus:border-blue-500" />
              </div>
              <div class="w-full md:w-1/2 px-4 mb-4">
                <label for="startDate" class="block text-sm font-medium text-gray-700">Start Date</label>
                <input type="date" id="startDate" v-model="startDate" class="w-full bg-gray-100 border border-gray-300 rounded py-2 px-3 focus:outline-none focus:bg-white focus:border-blue-500" />
              </div>
              <div class="w-full md:w-1/2 px-4 mb-4">
                <label for="finalDate" class="block text-sm font-medium text-gray-700">Final Date</label>
                <input type="date" id="finalDate" v-model="finalDate" class="w-full bg-gray-100 border border-gray-300 rounded py-2 px-3 focus:outline-none focus:bg-white focus:border-blue-500" />
              </div>
              <div class="w-full px-4 mb-4">
                <label for="propertyId" class="block text-sm font-medium text-gray-700">Property-ID</label>
                <input type="number" id="propertyId" v-model="propertyId" class="w-full bg-gray-100 border border-gray-300 rounded py-2 px-3 focus:outline-none focus:bg-white focus:border-blue-500" />
              </div>
            </form>
          </div>
          </div>
          <!--footer-->
          <div class="flex items-center justify-end p-6 border-t border-solid border-slate-200 rounded-b">
            <button class="text-red-500 bg-transparent border border-solid border-red-500 hover:bg-red-500 hover:text-white active:bg-red-600 font-bold uppercase text-sm px-6 py-3 rounded outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150" type="button" v-on:click="toggleModal()">
              Close
            </button>
            <button class="text-red-500 background-transparent font-bold uppercase px-6 py-2 text-sm outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150" type="button" v-on:click="toggleModal()">
              Save 
            </button>
          </div>
        </div>
      </div>
    </div>
    <div v-if="showModal" class="opacity-25 fixed inset-0 z-40 bg-black"></div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const showModal = ref(false);

function toggleModal() {
  showModal.value = !showModal.value;
}
</script>