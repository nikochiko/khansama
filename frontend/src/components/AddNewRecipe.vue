<template>
  <div class="container">
    <form @submit.prevent="handleSubmit">
      <div class="row my-2">
        <div class="col-8">
          <input
            id="newUrl"
            name="newUrl"
            class="form-control"
            placeholder="Paste your recipe URL here"
            v-model="newUrl"
          />
        </div>
        <div class="col-4">
          <button @click="readClipboard" class="btn btn-secondary">
            <i class="fa-solid fa-paste"></i>
          </button>
        </div>
      </div>
      <div class="row my-2">
        <div class="col">
          <button type="submit" class="btn btn-primary btn-submit">
            Create a beautiful UI
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "AddNewRecipe",
  data: function () {
    return {
      newUrl: "",
    };
  },
  methods: {
    handleSubmit: function (e) {
      let newUrl = e.target.elements.newUrl.value;
      axios
        .get(`http://localhost:5000/khansify?url=${newUrl}`)
        .then((response) => {
          let id = response.data.id;
          window.location = `/recipes/${id}`;
        });
    },
    readClipboard: function () {
      navigator.clipboard
        .readText()
        .then((cliptext) => (this.newUrl = cliptext));
    },
  },
};
</script>

<style></style>
