<template>
  <div class="container">
    <atom-icon-button class="left center-align action-button" @click="$router.go(-1)">chevron_left</atom-icon-button>
    <atom-title class="centered" tag="h4" :title="title"/>
    <atom-icon-button class="left center-align action-button hidden-button">chevron_left</atom-icon-button>
  </div>
  <div class="divider"></div>
</template>

<script>
import AtomTitle from "@/components/atoms/AtomTitle";
import AtomIconButton from "@/components/atoms/AtomIconButton";

export default {
  name: "MoleculeHeaderWithNavigation",
  components: {
    AtomTitle,
    AtomIconButton
  },
  props: {
    title: String,
  }
}
</script>

<style lang="scss" scoped>
.material-icons{
  font-size: 40px
}

.container {
  padding: 1rem 0 1rem 0;
  display: flex;
}

.action-button {
  background-color: white !important;
  margin: auto 0 auto 0;

  :deep(i) {
    color: grey !important;
  }
}
.centered {
  margin: 1rem auto 1rem auto;
}

.hidden-button {
  visibility: hidden;
}
</style>