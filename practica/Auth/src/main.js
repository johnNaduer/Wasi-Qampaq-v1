import { createApp } from 'vue'
import App from './App.vue'
import './style.css'
import router from './routes/routes'
import 'bootstrap/dist/css/bootstrap.css'

createApp(App).use(router).mount('#app')

