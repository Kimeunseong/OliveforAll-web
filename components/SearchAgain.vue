<template>
  <div class="text-center">
    <router-link to="/search">
      <v-btn class="ma-2" outlined color="indigo" @click="gotoMain()">
        다시 검색하기
      </v-btn>
    </router-link>
  </div>
</template>

<script>
export default {
  // methods: {
  //   gotoMain:
  // }
};
</script>

<style>
a {
  text-decoration: none;
}
</style>
