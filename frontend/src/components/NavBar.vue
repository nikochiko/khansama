<template>
<div id="navbar" class="container d-flex justify-content-between">
  <h3 class="d-none d-sm-block">
    Khansama.app
  </h3>

  <h3 class="d-sm-none">
    KH
  </h3>

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
}

#search {
  background-color: rgb(243 244 246);
  color: rgb(107 114 128);
  max-width: 50%;
}
</style>
