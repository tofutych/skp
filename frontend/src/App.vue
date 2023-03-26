<template>
  <nav class="navbar is-transparent">
    <div class="navbar-brand">
      <div class="navbar-burger" data-target="navbarExampleTransparentExample">
        <span></span>
        <span></span>
        <span></span>
      </div>
    </div>

    <div id="navbarExampleTransparentExample" class="navbar-menu">
      <div class="navbar-start">
        <router-link class="navbar-item" to="/">Home</router-link>
        <div class="navbar-item has-dropdown is-hoverable">
          <a class="navbar-link">
            Add
          </a>
          <div class="navbar-dropdown is-boxed">
            <router-link class="navbar-item" to="/add/group">Group</router-link>
            <router-link class="navbar-item" to="/add/student">Student</router-link>
          </div>
        </div>
      </div>
    </div>

  </nav>
  <router-view />
</template>

<style lang="scss">
@import "../node_modules/bulma"
</style>
