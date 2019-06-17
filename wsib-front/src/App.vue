<template>
  <div id="app">
    <div id="nav">
    <b-field label="Enter your Warcraft log link here :">
          <b-input placeholder="No label" rounded></b-input>
      </b-field>
      <b-button size="is-medium"
                >
                <v-icon name="search" />
                Search
            </b-button>
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
