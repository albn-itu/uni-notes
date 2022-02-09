<template>
  <div>
    <div class="account-container">
      <div class="account-image">
        <i class="account-image-icon material-icons">account_circle</i>
      </div>
      <div class="account-info">
        <p class="account-name">{{ account.name }}</p>
        <p class="account-mail">{{ account.useremail }}</p>
      </div>
    </div>
    <div class="settings-container">
      <atom-settings-button-vue
        v-for="link in links"
        :key="link.name"
        @click="$router.push(link.link)"
        :class="`${link.logOut ? 'settings-log-out' : ''}`"
      >
        {{ link.name }}
      </atom-settings-button-vue>
    </div>
  </div>
</template>

<script>
import AtomSettingsButtonVue from '../components/atoms/AtomSettingsButton.vue';

export default {
  data() {
    return {
      links: [
        // FIXME: Update these when everything is in place
        {
          name: 'Administrer email og adganskoder',
          link: '/change-password'
        },
        {
          name: 'Betalingsmetoder',
          link: '/payment-methods'
        },
        {
          name: 'Kvitteringer',
          link: '/receipts'
        },
        {
          name: 'Hjælp',
          link: '/help'
        },
        {
          name: 'Log ud',
          logOut: true,
          link: '/'
        }
      ]
    }
  },
  components: {
    AtomSettingsButtonVue,
  },
  computed: {
    account() {
      return this.$store.state.fakeBackend;
    }
  }
}
</script>

<style lang="scss" scoped>
@import '@/scss/components/variables.scss';

.account {
  &-container {
    padding: 1rem 0 1rem 0;
    background: $primary-color;
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);

    color: white;
    text-align: center;
  }

  &-image {
    &-icon {
      font-size: 4rem;
    }
  }
    
  &-info {
    & > p {
      margin: 0;
    }
  }

  &-name {
    font-weight: bold;
    font-size: 1.5rem;
  }
}

.settings {
  &-log-out > :deep(a) {
    color: $error-color;
  }
}
</style>