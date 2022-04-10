import Vue from 'vue'
import VueRouter from 'vue-router';
import App from './App.vue'
import RecipeView from './components/RecipeView.vue'

Vue.config.productionTip = false

Vue.use(VueRouter)

const routes = [
  { path: '/recipes/:id', component: RecipeView }
]

const router = new VueRouter({routes})

new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
