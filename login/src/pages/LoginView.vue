<template>
  <div>
    <form @submit="submitForm">
      <h3>ingresar email</h3>
      <input type="text" v-model="email" placeholder="Email">
      <h3>ingresar contraseña</h3>
      <input type="password" v-model="password" placeholder="Password">
      <button type="submit">Login</button>
    </form>
    <p>{{ message }}</p>
  </div>
</template>

<script>
import { useRouter } from 'vue-router';
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: '',
      message: ''
    };
  },
  methods: {
    submitForm(event) {
      event.preventDefault();

      const url = 'http://localhost:5001/login';
      const data = {
        email: this.email,
        password: this.password
      };

      axios.post(url, data)
        .then(response => {
          this.message = response.data.message;
          //redirigre a la pagina "add tenant"
          const router = useRouter();
          router.push('/add_tenant');
        })
        .catch(error => {
          console.error(error);
          this.message = 'Error en el inicio de sesión';
        });
    }
  }
};
</script>

