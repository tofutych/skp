import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import GroupView from '../views/GroupView.vue'
import StudentView from '../views/StudentView.vue'
import AddGroupView from '../views/AddGroupView.vue'
import AddStudentView from '../views/AddStudentView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/:slug/',
    name: 'group',
    component: GroupView
  },
  {
    path: '/:slug/:id/',
    name: 'student',
    component: StudentView
  },
  {
    path: '/add/group/',
    name: 'addgroup',
    component: AddGroupView
  },
  {
    path: '/add/student/',
    name: 'addstudent',
    component: AddStudentView
  },


]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
