<template>
  <ul>
      <li v-for="(link, index) in links" :key="link.name + index">
          <atom-footer-router-link :to="link.to">{{ link.name }}</atom-footer-router-link>
      </li>
  </ul>
</template>

<script>
import AtomFooterRouterLink from '@/components/atoms/AtomFooterRouterLink.vue'

export default {
    name: 'MoleculeFooterRouterLinks',
    components: {
        AtomFooterRouterLink
    },
    props: {
        links: Array
    }
}
</script>
