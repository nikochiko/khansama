<template>
  <div class="container">

    <div class="d-flex justify-content-between">
      <div class="h2 text-left">Your Recipes</div>
      <a href="/new" class="h1">
        <i class="fa-solid fa-circle-plus"></i>
      </a>
    </div>
    <div class="row">
      <div
        class="col-xs-12 col-md-6 col-lg-4 rounded-md py-2 recipe-list-item"
        v-for="recipe in recipes"
        :key="recipe.id"
      >
        <div class="recipe-list-item-inner w-100 h-100 pb-2">
          <a :href="recipeLink(recipe)" class="hover-opacity-60">
            <img :src="recipe.image" class="recipe-list-image twentyone-nine" />
          </a>
          <div class="d-flex justify-content-between align-items-center px-2">
            <a
              :href="recipeLink(recipe)"
              class="
                left-flex
                py-2
                align-middle
                text-left
                pr-1
                text-truncate
                h6
                mb-0
              "
            >
              {{ recipe.name }}
            </a>
            <div class="right-flex pl-1 text-right text-muted">
              {{ recipe.totalTime }}
            </div>
          </div>
          <div class="tags pb-1 d-flex justify-content start px-2">
            <template v-for="tag in recipe.tags">
              <div
                class="rounded badge activity-badge mr-1"
                :style="getStyleForRecipeTag(tag)"
                :key="tag"
                v-show="tag"
              >
                <div class="activity-badge-text">{{ tag }}</div>
              </div>
            </template>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

let recipes = [
  {
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
  },
  {
    id: 2,
    name: "Baked Coconut Shrimp with Springy Rice and Honey Butter Sauce 2",
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
  },
  {
    id: 3,
    name: "Baked Coconut Shrimp with Springy Rice and Honey Butter Sauce 3",
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
  },
];

export default {
  name: "RecipeListing",
  data: function () {
    return {
      recipes,
    };
  },
  methods: {
    getStyleForRecipeTag: function (tag) {
      console.log(tag);
      let styles = [
        "background-color: #fde68a; color: #f59e0b;",
        "background-color: rgba(137,76,255,0.1); color: #894cff;",
      ];
      return styles[1];
    },
    recipeLink: function (recipe) {
      return `/recipes/${recipe.id}`;
    },
  },
  created() {
    // Simple GET request using axios
    axios.get("http://localhost:5000/recipes").then((response) => {
      console.log(response);
      this.recipes = response.data;
    });
  },
};
</script>

<style>
.recipe-list-image {
  border-radius: 0.75rem 0.75rem 0 0;
  height: 100%;
  width: 100%;
  object-fit: cover;
}

.twentyone-nine {
  width: 100%;
}

@media screen and (max-width: 576px) {
  .twentyone-nine {
    height: 180px;
  }
}

@media screen and (min-width: 576px) and (max-width: 768px) {
  .twentyone-nine {
    height: 200px;
  }
}

@media screen and (min-width: 768px) {
  .twentyone-nine {
    height: 250px;
  }
}

.recipe-list-item {
  /* background-color: rgb(31 41 55); */
}

.recipe-list-item-inner {
  border-radius: 0.75rem;
  background-color: rgba(241, 245, 249, 0.6);
}

.background-glass {
  /* From https://css.glass */
  background: rgba(0, 0, 0, 0.2);
  border-radius: 0.75rem;
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(5px);
  -webkit-backdrop-filter: blur(5px);
}

.clock-svg {
  position: relative;
  top: 0.15em;
}

.badge {
  font-size: 0.875rem;
  border-radius: 0.25rem;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out,
    border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  background-color: rgba(82, 113, 137, 0.1);
  color: #527189;
  display: inline-block;
  font-weight: 600;
  line-height: 24px;
  padding: 0.25rem 0.75rem;
  text-align: center;
  vertical-align: baseline;
  white-space: nowrap;
}

.activity-badge,
.opportunity-preference-badge {
  align-items: center;
  display: inline-flex;
  font-size: 0.8125rem;
  max-width: 100%;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

.activity-badge .activity-badge-text,
.opportunity-preference-badge .activity-badge-text {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/*
@media screen and (min-width: 992px) and (max-width: 1200px) {
  .twentyone-nine {
    height: 350px;
  }
}

@media screen and (min-width: 1200px) and (max-width: 1400px) {
  .twentyone-nine {
    height: 400px;
  }
}
*/
</style>
