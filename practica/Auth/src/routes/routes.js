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
    path: "/modal_admin_add",
    name: "add",
    component: () => import("../components/AdminModalAdd.vue"),
  },
  {
    path: "/modal_admin_delete",
    name: "delete",
    component: () => import("../components/AdminModalDelete.vue"),
  },
  {
    path: "/modal_admin_editar",
    name: "editar",
    component: () => import("../components/AdminModalEdit.vue"),
  },
  {
    path: "/inquilino",
    name: "inquilino",
    component: () => import("../pages/TenantsView.vue"),
  },
  {
    path: "/administrator",
    name: "administrator",
    component: () => import("../pages/AdministratorView.vue"),
  },
];

const router = createRouter({
  routes,
  history: createWebHistory(),
});

export default router;
