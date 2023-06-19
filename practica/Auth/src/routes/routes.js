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
    name: "editar",
    component: () => import("../components/ModalView.vue"),
  },
  {
    path: "/inquilino",
    name: "inquilino",
    component: () => import("../pages/TenantsView.vue"),
  },
];

const router = createRouter({
  routes,
  history: createWebHistory(),
});

export default router;
