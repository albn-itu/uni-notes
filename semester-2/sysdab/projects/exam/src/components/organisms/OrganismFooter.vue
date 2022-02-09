<template>
  <footer class="page-footer">
      <div class="footer-container">
          <div class="row">
              <div class="col 16 s12">
                <atom-title tag="h5" :title="title" />
                <!-- TODO: AtomText here -->
              </div>
              <div class="col 14 offset-12 s12">
                  <atom-title tag="h5" title="Links" />
                  <molecule-footer-router-links :links="routerLinks" />
              </div>
          </div>
      </div>
  </footer>
</template>

<script>
import AtomTitle from '../atoms/AtomTitle.vue'
import MoleculeFooterRouterLinks from '../molecules/MoleculeFooterRouterLinks.vue'

export default {
    name: 'OrganismFooter',
    components: {
        AtomTitle,
        MoleculeFooterRouterLinks

    },
    props: {
        title: String,
        routerLinks: Array
    }
}
</script>
<style lang="scss" scoped>
.footer-container {
    width: 85%;
    margin: 0 auto;
}
</style>
