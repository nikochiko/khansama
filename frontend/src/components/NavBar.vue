<template>
<div id="navbar" class="d-flex justify-content-between align-items-center mb-2">
  <div class="d-none d-sm-block mb-0 h3 heading-recipes">
    Khansama.app
  </div>

  <div class="d-sm-none font-weight-bold mb-0 h3 heading-recipes">
    KH
  </div>

  <input id="search" class="form-control border-0" placeholder="Search" />
</div>
</template>

<script>
export default {
  name: 'NavBar',
}
</script>

<style>
#navbar {
  padding: 20px 10px 20px 10px;
  background: rgba(255, 255, 255, 0.2);
  box-shadow: 0 4px 30px rgba(0, 0, 0, 0.1);
}

#navbar .heading-recipes {
  font-family: 'Josefin Sans', sans-serif;
}

#search {
  background-color: rgb(243 244 246);
  color: rgb(107 114 128);
  max-width: min(50%, 400px);
}

@media screen and (min-width: 576px) {
  #navbar {
    padding: 20px 30px 20px 30px;
  }
}
</style>
