import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "login",
    component: () => import("../pages/LoginPages.vue"),
  },
  {
    path: "/register",
    name: "register",
    component: () => import("../pages/RegisterPages.vue"),
  }
];

const router = createRouter({
    routes,
    history:createWebHistory()
})

export default router