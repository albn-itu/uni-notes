<template>
  <div class="card">
      <div class="card-content">
          <span class="card-title">{{ title }}</span>
          <slot />
      </div>
      <div class="card-action">
        <slot name="actions" />
      </div>
  </div>
</template>

<script>
export default {
    name: 'AtomCardWithActions',
    props: {
        title: String
    }
}
</script>
