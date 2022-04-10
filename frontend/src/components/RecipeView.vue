<template>
<div id="recipe-view">
  <div class="container my-5">
    <div class="description-section my-2">
      <div class="section-heading d-flex justify-content-between">
        <div class="h3">
          Description
        </div>
        <div class="control-options">
          <button
            id="description-toggle"
            class="btn btn-link text-decoration-none shadow-none hover-opacity-60" style="color: inherit;"
            @click="isHidden.description = !isHidden.description"
          >
            <i v-bind:class="{ 'fa-angle-down': isHidden.description, 'fa-angle-up': !isHidden.description }" class="fa-solid"></i>
          </button>
        </div>
      </div>
      <div class="section-content p text-left mt-2" v-show="!isHidden.description">
        {{ recipe.description }}
      </div>
    </div>
  </div>
</div>
</template>

<script>
let recipe = {
  id: 1,
  name: "Baked Coconut Shrimp with Springy Rice and Honey Butter Sauce",
  author: {
    name: "Lindsay",
    url: "https://pinchofyum.com/about",
  },
  cookTime: "20m",
  prepTime: "25m",
  totalTime: "45m",
  description:
    "Perfectly springy baked coconut shrimp piled high on a mountain of steamy pea-speckled and lemony rice and drizzles upon drizzles of a beautiful honey butter sauce. This is exactly the spring vacay you need!\u00a0",
  tags: ["Dinner", "American", "Bake"],
  image:
    "https://pinchofyum.com/wp-content/uploads/Baked-Coconut-Shrimp-Square.jpg",
  ingredients: [
    "3/4 cup Chef&#8217;s Cupboard Panko Breadcrumbs",
    "3/4 cup Baker&#8217;s Corner Coconut Flakes (sweetened or unsweetened, but I prefer sweetened)",
    "2 eggs, beaten",
    "1/2 cup flour",
    "1/2 teaspoon paprika",
    "1/2 teaspoon salt",
    "1 pound Fremont Fish Market Jumbo EZ Peel Raw Shrimp, thawed, tails removed (see notes)",
    "1 cup Specially Selected Jasmine Rice, uncooked",
    "10-ounce bag of Simply Nature Sweet Peas",
    "lemon juice and zest",
    "herbs or greens",
    "1 clove grated garlic",
    "2 tablespoons butter",
    "4 tablespoons melted butter",
    "2-3 tablespoons honey",
    "1-2 teaspoons Dijon mustard",
  ],
  instructions: [
    {
      name: "Prep",
      text: "Cook the rice according to package directions. (I do this in a pressure cooker)",
      url: "https://pinchofyum.com/baked-coconut-shrimp#instruction-step-1",
    },
    {
      name: "Toast the Coconut",
      text: "Preheat the oven to 425 degrees. Place panko and coconut on a baking sheet; toast for 10-15 minutes, stirring occasionally, until nice and golden brown.",
      url: "https://pinchofyum.com/baked-coconut-shrimp#instruction-step-2",
    },
    {
      name: "Coat the Coconut Shrimp",
      text: "Make three bowls: one for the flour, paprika, and salt; one for the egg, and one for the toasted coconut. Coat individual shrimp in flour / spice mix, then egg, then press into the panko until the mixture sticks to the shrimp. (I usually do all the shrimp in the flour / spice mix first, and then do the egg / panko dip so it&#8217;s a bit cleaner). Place coated shrimp back on the baking sheet. Spritz or drizzle with oil.",
      url: "https://pinchofyum.com/baked-coconut-shrimp#instruction-step-3",
    },
    {
      name: "Bake the Coconut Shrimp",
      text: "Bake shrimp at 425 for 10 minutes.",
      url: "https://pinchofyum.com/baked-coconut-shrimp#instruction-step-4",
    },
    {
      name: "Finish the Rice",
      text: "Add peas, lemon zest, herbs, garlic, and butter into the hot rice and gently fluff with a fork to combine. The peas just need to get heated through.",
      url: "https://pinchofyum.com/baked-coconut-shrimp#instruction-step-5",
    },
    {
      name: "Make the Sauce",
      text: "Whisk the melted butter with the honey and Dijon mustard. (And add whatever else you like &#8211; red pepper flakes, chili paste, lemon, etc.)",
      url: "https://pinchofyum.com/baked-coconut-shrimp#instruction-step-6",
    },
    {
      name: "Serve",
      text: "Serve shrimp with a pile of rice and generously drizzle with the sauce. HELLO! So yummy.",
      url: "https://pinchofyum.com/baked-coconut-shrimp#instruction-step-7",
    },
  ],
}

export default {
  name: "RecipeView",
  data: function() {
    return {
      recipe,
      isHidden: {
        description: false,
      }
    }
  },
}
</script>

<style>
#recipe-view {
  background-color: #FFFFFF;
  color: #0f172a;
}

.section-heading {
  border-bottom: 1.5px solid #e5e7eb;
  font-family: Montserrat, Helvetica, sans-serif;
  font-weight: 500;
}
</style>
