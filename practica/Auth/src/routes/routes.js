import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/login",
    name: "login",
    component: () => import("../pages/HomeView.vue"),
  },
  {
    path: "/register",
    name: "register",
    component: () => import("../pages/RegisterView.vue"),
  },
  {
    path: "/modal",
    name: "formulario",
    component: () => import("../components/ModalAddView.vue"),
  },
  {
    path: "/modaleliminar",
    name: "eliminar",
    component: () => import("../components/ModalDeleteView.vue"),
  },
  {
    path: "/modaleditar",
    name: "editar",
    component: () => import("../components/ModalEditView.vue"),
  },
  {
    path: "/tenants",
    name: "inquilino",
    component: () => import("../pages/TenantsView.vue"),
  },
  {
    path: "/",
    name: "tenant",
    component: () => import("../components/Tenants.vue"),
  },
  {
    path: "/practica",
    name: "practica",
    component: () => import("../components/Práctica.vue"),
  },
  {
    path: "/tabla",
    name: "tabla",
    component: () => import("../pages/Tabla.vue"),
  },
  {
    path: "/boton",
    name: "boton",
    component: () => import("../components/Boton.vue"),
  },
];

const router = createRouter({
  routes,
  history: createWebHistory(),
});

export default router;
