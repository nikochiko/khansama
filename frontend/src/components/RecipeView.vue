<template>
  <div id="recipe-view">

    <div class="container mt-4 mb-2">

      <div class="mt-2 text-left">
        <a href="/"><i class="fa-solid fa-arrow-left"></i> Back</a>
      </div>

      <div
        class="d-flex justify-content-between flex-wrap align-items-center mb-2"
      >
        <div class="recipe-title text-left w-xs-100">
          <div class="h3 mb-0">{{ recipe.name }}</div>
          <div v-if="recipe.author">
            By
            <span class="text-muted"
              ><a :href="recipe.author.url" target="_blank">{{
                recipe.author.name
              }}</a></span
            >
          </div>
        </div>
        <div class="recipe-time text-middle text-muted w-xs-100">
          <i class="fa-solid fa-fire-burner"></i> {{ recipe.totalTime }}
        </div>
      </div>

      <div class="text-left mb-4">
        <a :href="recipe.url">Link to Original</a>
      </div>

      <div class="recipe-section description-section my-2">
        <div class="section-heading d-flex justify-content-between">
          <div class="h4">Description</div>
          <div class="control-options">
            <button
              id="description-toggle"
              class="
                btn btn-link
                text-decoration-none
                shadow-none
                hover-opacity-60
              "
              style="color: inherit"
              @click="isHidden.description = !isHidden.description"
            >
              <i
                v-bind:class="{
                  'fa-angle-down': isHidden.description,
                  'fa-angle-up': !isHidden.description,
                }"
                class="fa-solid"
              ></i>
            </button>
          </div>
        </div>
        <div
          class="section-content p text-left mt-2"
          v-show="!isHidden.description"
        >
          {{ recipe.description }}
        </div>
      </div>

      <div class="recipe-section ingredients-section my-2">
        <div class="section-heading d-flex justify-content-between">
          <div class="h4">Ingredients</div>
          <div class="control-options">
            <button
              id="ingredients-checklist-reset"
              class="
                btn btn-link
                text-decoration-none
                shadow-none
                hover-opacity-60
              "
              style="color: inherit"
              @click="resetIngredientsChecklist"
            >
              <i
                class="fa-solid fa-rotate"
              ></i>
            </button>
            <button
              id="ingredients-checklist-toggle"
              class="
                btn btn-link
                text-decoration-none
                shadow-none
                hover-opacity-60
              "
              style="color: inherit"
              @click="
                showChecklist.ingredients = !showChecklist.ingredients;
                isHidden.ingredients = false;
              "
            >
              <i
                v-bind:class="{
                  'fa-list-check': !showChecklist.ingredients,
                  'fa-list': showChecklist.ingredients,
                }"
                class="fa-solid"
              ></i>
            </button>
            <button
              id="ingredients-toggle"
              class="
                btn btn-link
                text-decoration-none
                shadow-none
                hover-opacity-60
              "
              style="color: inherit"
              @click="isHidden.ingredients = !isHidden.ingredients"
            >
              <i
                v-bind:class="{
                  'fa-angle-down': isHidden.ingredients,
                  'fa-angle-up': !isHidden.ingredients,
                }"
                class="fa-solid"
              ></i>
            </button>
          </div>
        </div>
        <div
          class="section-content p text-left mt-2"
          v-show="!isHidden.ingredients"
        >
          <ul v-show="!showChecklist.ingredients" class="px-3">
            <li v-for="ingredient in recipe.ingredients" :key="ingredient">
              {{ ingredient }}
            </li>
          </ul>
          <div v-show="showChecklist.ingredients">
            <div
              class="form-check"
              v-for="ingredient in recipe.ingredients"
              :key="ingredient"
            >
              <input type="checkbox" class="ingredient-checkbox form-check-input" />
              <label class="form-check-label">{{ ingredient }}</label>
            </div>
          </div>
        </div>
      </div>

      <div class="recipe-section instructions-section my-2">
        <div class="section-heading d-flex justify-content-between">
          <div class="h4">Instructions</div>
          <div class="control-options">
            <button
              id="instructions-toggle"
              class="
                btn btn-link
                text-decoration-none
                shadow-none
                hover-opacity-60
              "
              style="color: inherit"
              @click="isHidden.instructions = !isHidden.instructions"
            >
              <i
                v-bind:class="{
                  'fa-angle-down': isHidden.instructions,
                  'fa-angle-up': !isHidden.instructions,
                }"
                class="fa-solid"
              ></i>
            </button>
          </div>
        </div>
        <div
          class="section-content p text-left mt-2"
          v-show="!isHidden.instructions"
        >
          <ol class="px-3">
            <li
              v-for="instruction in recipe.instructions"
              class="mb-2"
              :key="instruction.step"
            >
              <span class="font-weight-bold" v-if="instruction.name"
                >{{ instruction.name }}.
              </span>
              <span class="instruction-text">{{ instruction.text }} </span>
              <a v-if="instruction.url" target="_blank" :href="instruction.url"
                ><i class="fa-solid fa-arrow-right"></i
              ></a>
            </li>
          </ol>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

let recipe = {};

export default {
  name: "RecipeView",
  data: function () {
    return {
      recipe,
      isHidden: {
        description: true,
        ingredients: true,
        instructions: true,
      },
      showChecklist: {
        ingredients: false,
      },
    };
  },
  methods: {
    resetIngredientsChecklist: function() {
      let elements = document.getElementsByClassName("ingredient-checkbox")
      for (const el of elements) {
        el.checked = false;
      }
    }
  },
  created() {
    // Simple GET request using axios
    axios
      .get(`http://localhost:5000/recipes/${this.$route.params.id}`)
      .then((response) => {
        console.log(response);
        this.recipe = response.data;
      });
  },
};
</script>

<style>
#recipe-view {
  background-color: #ffffff;
  color: #0f172a;
  font: system-ui;
}

.section-heading {
  border-bottom: 1.5px solid #e5e7eb;
  font-family: system-ui, Montserrat, Helvetica, sans-serif;
  font-weight: 500;
}

.section-content {
  font-size: 1.1rem;
}

.recipe-section {
  padding: 40px inherit 40px inherit !important;
}
</style>
