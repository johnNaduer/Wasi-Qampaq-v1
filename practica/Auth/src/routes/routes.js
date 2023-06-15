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
    path: "/listar",
    name: "listar",
    component: () => import("../pages/ListarView.vue"),
  },
];

const router = createRouter({
  routes,
  history: createWebHistory(),
});

export default router;
