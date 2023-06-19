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
    component: () => import("../components/ModalView.vue"),
  },
  {
    path: "/crear",
    name: "crear",
    component: () => import("../pages/CreateView.vue"),
  },
  {
    path: "/editar",
    name: "editar",
    component: () => import("../pages/EditarView.vue"),
  },
  {
    path: "/inquilino",
    name: "inquilino",
    component: () => import("../pages/TenantsView.vue"),
  },
  {
    path: "/update",
    name: "update",
    component: () => import("../pages/EditTenant.vue"),
  },
];

const router = createRouter({
  routes,
  history: createWebHistory(),
});

export default router;
