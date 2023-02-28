<template>
  <v-row class="PageLayout" justify="center">
    <v-col class="MainInfo">
      <h1>Olive for<br />ALL</h1>
      <br />
      <!-- <v-img src="../assets/OFO_Logo.png"></v-img> -->
      <div>올리브영 가고, 켜고, 그리고 찍고!</div>
      <br /><br />
      <h3>
        제품을 검색하면 AI가 사진 속 제품을 확인하고<br />
        온라인몰의 리뷰를 요약해드려요 :)<br /><br />
      </h3>
      <router-link to="/search">
        <v-btn
          class="ma-2"
          color="#FFCD4A"
          text-color="#FFFFFF"
          @click="gotoMain()"
          x-large
        >
          &nbsp;&nbsp;&nbsp;검색하러 가기!&nbsp;&nbsp;&nbsp;
        </v-btn>
      </router-link>
    </v-col>
    <v-img
      justify="center"
      lazy-src="https://picsum.photos/id/11/10/6"
      max-height="500"
      max-width="400"
      src="../assets/mainPageImg.png"
    ></v-img>
  </v-row>
</template>

<script>
export default {};
</script>

<style>
.MainInfo {
  padding: 50px;
  padding-top: 100px;
  margin: 10px;
  /* justify-content: center; */
}
.PageLayout {
  padding: 50px;
  padding-left: 100px;
  padding-right: 100px;
  background-position: center center;
}
</style>
