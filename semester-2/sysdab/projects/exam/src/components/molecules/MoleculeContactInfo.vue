<template>
  <div class="contact-info">
      <img :src="img" />
      <p class="contact-title">{{ title }}</p>
      <p class="contact-info">{{ info }}</p>
  </div>
</template>

<script>
export default {
    name: 'MoleculeContactInfo',
    props: {
        title: String,
        info: String,
        img: String
    }
}
</script>

<style lang="scss" scoped>
@import '@/scss/components/variables.scss';

.contact {
    &-info {
        text-align: center;
    }

    &-title {
        color: black;
    }

    &-info {
        color: $primary-color
    }
}
</style>