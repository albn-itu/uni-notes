<template>
  <div class="forgotten-container">
      <p class="forgotten-text">{{ text }}</p>
      <p class="forgotten-link orange-text" v-bind="$attrs">{{ buttonText }}</p>
  </div>
</template>

<script>
export default {
    name: 'MoleculeForgotten',
    inheritAttrs: false,
    props: {
        text: String,
        buttonText: String
    }
}
</script>

<style lang="scss" scoped>
.forgotten {
    &-container {
        width: 100%;
        display: flex;
        background-color: #f5f5f5;
        justify-content: center;
        padding: 1rem 0 1rem 0;
    }

    &-link {
        margin-left: 1rem;
        cursor: pointer;
    }
}
</style>