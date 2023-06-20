<template>
    <div>
      <button type="button" v-on:click="toggleModal()">
        Add
      </button>
      <div v-if="showModal" class="overflow-x-hidden overflow-y-auto fixed inset-0 z-50 outline-none focus:outline-none justify-center items-center flex">
        <div class="relative w-auto my-6 mx-auto max-w-6xl">
          <!--content-->
          <div class="border-0 rounded-lg shadow-lg relative flex flex-col w-full bg-white outline-none focus:outline-none">
            <!--header-->
            <div class="flex items-start justify-between p-5 border-b border-solid border-slate-200 rounded-t">
              <h3 class="text-3xl font-semibold">
                Add Administrator
              </h3>
            </div>
            <!--body-->
            <div class="relative p-6 flex-auto">
              <div>
              <form class="flex flex-wrap -mx-4">
                <div class="w-full md:w-1/2 px-4 mb-4">
                  <label for="name" >Name</label>
                  <input type="text" id="name" v-model="name" />
                </div>
                <div class="w-full md:w-1/2 px-4 mb-4">
                  <label for="surname" >Surname</label>
                  <input type="text" id="surname" v-model="surname" />
                </div>
                <div class="w-full md:w-1/2 px-4 mb-4">
                  <label for="secondSurname" >Second Surname</label>
                  <input type="text" id="secondSurname" v-model="secondSurname" />
                </div>
                <div class="w-full md:w-1/2 px-4 mb-4">
                  <label for="dni" >DNI/Inmigration Card</label>
                  <input type="number" id="dni" v-model="dni" />
                </div>
                <div class="w-full md:w-1/2 px-4 mb-4">
                  <label for="phone" >Phone</label>
                  <input type="tel" id="phone" v-model="phone" />
                </div>
                <div class="w-full md:w-1/2 px-4 mb-4">
                  <label for="email" >Email</label>
                  <input type="email" id="email" v-model="email" />
                </div>
                <div class="w-full md:w-1/2 px-4 mb-4">
                  <label for="startDate" >Start Date</label>
                  <input type="date" id="startDate" v-model="startDate" />
                </div>
                <div class="w-full md:w-1/2 px-4 mb-4">
                  <label for="finalDate" >Final Date</label>
                  <input type="date" id="finalDate" v-model="finalDate" />
                </div>
                <div class="w-full md:w-1/2 px-4 mb-4">
                  <label for="finalDate" >Espace-ID</label>
                  <input type="number" id="finalDate" v-model="finalDate" />
                </div>
                <div class="w-full md:w-1/2 px-4 mb-4">
                  <label for="propertyId" >Property-ID</label>
                  <input type="number" id="propertyId" v-model="propertyId" />
                </div>
              </form>
            </div>
            </div>
            <!--footer-->
            <div class="flex items-center justify-end p-6 border-t border-solid border-slate-200 rounded-b">
              <button  type="button" v-on:click="toggleModal()">
                Close
              </button>
              <button type="button" v-on:click="toggleModal()">
                Save 
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