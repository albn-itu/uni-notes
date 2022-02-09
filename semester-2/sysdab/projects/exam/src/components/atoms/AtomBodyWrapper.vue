<template>
  <div class="main-wrapper card">
      <slot />
  </div>
</template>

<script>
export default {
    name: 'AtomBodyWrapper'
}
</script>

<style lang="scss" scoped>
.main-wrapper {
    width: clamp(27rem, 50vw, 40rem);
    border-radius: 16px;
    box-shadow: 0 0 1.11111vw rgba(50,50,93,.25),0 0 .34722vw rgba(77,77,77,.1);
    margin: 2rem auto 0 auto;
    padding: 0.2rem 0 0 0;
    min-height: 100%;
    display: flex;
    flex-direction: column;
}
</style>