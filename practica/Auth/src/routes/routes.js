import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "home",
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
    path: "/tenant",
    name: "tenant",
    component: () => import("../components/Tenants.vue"),
  },
  {
    path: "/practica",
    name: "practica",
    component: () => import("../components/Práctica.vue"),
  },
];

const router = createRouter({
  routes,
  history: createWebHistory(),
});

export default router;
