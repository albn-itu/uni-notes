<template>
  <router-link class="grey-text text-lighten-3" v-bind="$attrs"><slot /></router-link>
</template>

<script>
export default {
    name: 'AtomFooterRouterLink'
}
</script>