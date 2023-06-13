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
  }
];

const router = createRouter({
  routes,
  history: createWebHistory(),
});

export default router;
