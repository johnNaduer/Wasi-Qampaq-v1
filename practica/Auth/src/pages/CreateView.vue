<template>
    <div class="container mx-auto">
      <h2 class="text-2xl font-bold mb-4">Agregar Usuario</h2>
      <form class="max-w-sm">
        <div class="mb-4">
          <label for="text" class="block text-gray-700 font-bold mb-2">Name:</label>
          <input type="text" id="" required
            class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-blue-500">
        </div>
        <div class="mb-4">
          <label for="text" class="block text-gray-700 font-bold mb-2">Surname:</label>
          <input type="text" id=""  required
            class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-blue-500">
        </div>
        <div class="mb-4">
          <label for="text" class="block text-gray-700 font-bold mb-2">Second Surname:</label>
          <input type="text" id=""  required
            class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-blue-500">
        </div>
        <div class="mb-4">
          <label for="number" class="block text-gray-700 font-bold mb-2">DNI/Inmigration Card:</label>
          <input type="number" id=""  required
            class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-blue-500">
        </div>
        <div class="mb-4">
          <label for="tel" class="block text-gray-700 font-bold mb-2">Phone:</label>
          <input type="tel" id=""  required
            class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-blue-500">
        </div>
        <div class="mb-4">
          <label for="email" class="block text-gray-700 font-bold mb-2">Email:</label>
          <input type="email" id=""  required
            class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-blue-500">
        </div>
        <div class="mb-4">
          <label for="date" class="block text-gray-700 font-bold mb-2">Star Date:</label>
          <input type="date" id=""  required
            class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-blue-500">
        </div>
        <div class="mb-4">
          <label for="date" class="block text-gray-700 font-bold mb-2">Final Date:</label>
          <input type="date" id="" required
            class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-blue-500">
        </div>
        <div class="mb-4">
          <label for="number" class="block text-gray-700 font-bold mb-2">Property-ID:</label>
          <input type="number" id="" required
            class="w-full px-3 py-2 border border-gray-300 rounded-sm focus:outline-none focus:border-blue-500">
        </div>
        <button type="submit" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
          Guardar
        </button>
      </form>
    </div>
  </template>
