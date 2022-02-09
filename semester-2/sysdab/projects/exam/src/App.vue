<template>
  <atom-body-wrapper>
    <header>
      <component v-if="currentHeader != 'none'" :is="currentHeader" :title="currentName" />
    </header>
    <main class="main-content">
      <router-view/>
    </main>
    <organism-footer :routerLinks="footerRouterLinks" class="footer"></organism-footer>
  </atom-body-wrapper>
</template>

<script>
import M from 'materialize-css'
import OrganismFooter from './components/organisms/OrganismFooter.vue'
import AtomBodyWrapper from '@/components/atoms/AtomBodyWrapper.vue'

import MoleculeHeaderWithNavigation from '@/components/molecules/MoleculeHeaderWithNavigation';
import MoleculeHeaderWithNavigationAndAccount from '@/components/molecules/MoleculeHeaderWithNavigationAndAccount';
import MoleculeHeaderWithNavigationAndSaveButton from '@/components/molecules/MoleculeHeaderWithNavigationAndSaveButton';

export default {
  components: {
    AtomBodyWrapper,
    MoleculeHeaderWithNavigation,
    MoleculeHeaderWithNavigationAndAccount,
    MoleculeHeaderWithNavigationAndSaveButton,
    OrganismFooter
  },
  mounted() {
    M.AutoInit()
  },
  data: () => {
    return {
      footerRouterLinks: [
        {
          to: '/',
          name: 'Hjem',
        },
        {
          to: '/login',
          name: 'Log ind',
        },
        {
          to: '/register',
          name: 'Registrer',
        },
        {
          to: '/help',
          name: 'Hjælp',
        },
        {
          to: '/FAQ',
          name: 'FAQ',
        }
      ],
      currentPage: null
    }
  },
  watch: {
    $route (to, from) {
      if (Object.keys(to.meta).length == 0) {
        this.currentPage = from;
      } else {
        this.currentPage = to;
      }
    }
  },
  computed: {
    currentHeader() {
      if (this.currentPage == null) {
        return 'none';
      }

      return this.currentPage.meta.header;
    },
    currentName() {
      return this.currentPage.name;
    }
  }
}
</script>
<style scoped>
  .main-content {
    flex: 1 1 0;
  }

  .footer {
    background-color: #6200ee;
  }
</style>