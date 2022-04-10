import Vue from 'vue'
import VueRouter from 'vue-router'
import RecipeListing from '../components/RecipeListing.vue'
import RecipeView from '../components/RecipeView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: RecipeListing,
  },
  {
    path: '/recipes/:id',
    name: 'recipes',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: RecipeView,
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
