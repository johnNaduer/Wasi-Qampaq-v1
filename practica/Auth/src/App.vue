<script setup>
import { RouterLink, RouterView } from 'vue-router';

</script>

<template>
  <div>
    <router-link to="/" class="router-link">Home</router-link>
    <router-link to="/Listar" class="router-link">Registro</router-link>
  </div>
  <RouterView />
</template>
<style>
  .router-link {
  @apply inline-block px-4 py-2 border border-gray-300 rounded text-gray-700;
  }
</style>