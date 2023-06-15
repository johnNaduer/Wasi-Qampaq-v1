import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "home",
    component: () => import("../pages/HomeView.vue"),
  },
  {
    path: "/login",
    name: "login",
    component: () => import("../pages/LoginView.vue"),
  },
  {
    path: "/recuperar_password",
    name: "recuperar_password",
    component: () => import("../pages/RecuperarPassword.vue"),
  },
  {
    path: "/add_tenant",
    name: "add_tenant",
    component: () => import("../pages/AddTenantView.vue"),
  },

];

const router = createRouter({
  routes,
  history: createWebHistory(),
});

export default router;
