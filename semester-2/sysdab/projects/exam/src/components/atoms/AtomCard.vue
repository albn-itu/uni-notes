<template>
  <div class="card">
      <div class="card-content">
          <span v-if="title != undefined && title.length > 0" class="card-title">{{ title }}</span>
          <slot />
      </div>
  </div>
</template>

<script>
export default {
    name: 'AtomCard',
    props: {
        title: String
    }
}
</script>
