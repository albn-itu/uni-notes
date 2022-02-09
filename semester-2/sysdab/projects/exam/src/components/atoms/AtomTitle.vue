<template>
  <component :is="tag">{{ title }}</component>
</template>

<script>
export default {
    name: 'AtomTitle',
    props: {
      tag: String,
      title: String
    }
}
</script>
