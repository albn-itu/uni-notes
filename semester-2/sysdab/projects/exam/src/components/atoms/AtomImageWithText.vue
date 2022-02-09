<template>
  <div>
    <img class="image" :src="img">
    <div class="image-text-wrapper">
      <p class="image-text">{{text}}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: "AtomImageWithText",
  props: {
    img: String,
    text: String
  }
}
</script>

<style lang="scss" scoped>
.image {
  width: 100%;
  height: 100%;

  &-text {
    &-wrapper {
      text-align: left;
    }

    font-size: 1.3rem;
    position: relative;
    bottom: 4rem;
    padding-left: 1rem;
    color: white;
    background-color: rgba(0,0,0, 0.75);
  }
}
</style>