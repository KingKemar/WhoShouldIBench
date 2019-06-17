<template>
  <div class="home">
    <h1>hahaha :{{ URL }}</h1>
    <img alt="Vue logo" src="../assets/logo.png">
  </div>
</template>

<script>
// @ is an alias to /src
export default {
  name: 'log',
  components: {
  },
  props: {
    URL : String
  },
  mounted() {
        if (this.$route.query.URL) {
          this.URL= this.$route.query.URL;
        }
    }
}
</script>
