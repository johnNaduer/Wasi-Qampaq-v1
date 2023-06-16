<script setup>
import { RouterLink, RouterView } from 'vue-router';

</script>

<template>
  <div>
    <router-link to="/" class="router-link-primary">Home</router-link>
    <router-link to="/inquilino" class="router-link-secondary">Tenants</router-link>
    <router-link to="/register" class="router-link-secondary">Registro</router-link>
  </div>
  <RouterView />
</template>
<style>
  .router-link-primary {
  @apply inline-block px-4 py-2 bg-violet-500 text-white font-bold rounded;
  }

  .router-link-secondary {
  @apply inline-block px-4 py-2 bg-gray-300 text-gray-800 rounded;
  }
</style>