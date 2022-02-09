import { createRouter, createWebHashHistory } from 'vue-router'

const headers = {
  NONE: 'none',
  DEFAULT: 'MoleculeHeaderWithNavigation',
  WITH_ACCOUNT: 'MoleculeHeaderWithNavigationAndAccount',
}

const routes = [
  {
    path: '/',
    name: 'Landing Page',
    meta: {
      header: headers.NONE,
    },
    component: () => import('@/views/LandingPage.vue')
  },
  {
    path: '/login',
    name: 'Log ind',
    meta: {
      header: headers.DEFAULT,
    },
    component: () => import('@/views/Login.vue')
  },
  {
    path: '/register',
    name: 'Tilmeld dig',
    meta: {
      header: headers.DEFAULT,
    },
    component: () => import('@/views/Register.vue')
  },
  {
    path: '/bikes-near-you',
    name: 'Bikes near you',
    meta: {
      header: headers.NONE,
    },
    component: () => import('@/views/BikesNearYou.vue')
  },
  {
    path: '/bike',
    name: 'Cykel info',
    meta: {
      header: headers.WITH_ACCOUNT
    },
    component: () => import('@/views/Bike.vue')
  },
  {
    path: '/change-password',
    name: 'Skift adganskode',
    meta: {
      header: headers.DEFAULT,
    },
    component: () => import('@/views/ChangePassword.vue')
  },
  {
    path: '/help',
    name: 'Hjælp',
    meta: {
      header: headers.WITH_ACCOUNT
    },
    component: () => import('@/views/Help.vue')
  },
  {
    path: '/service',
    name: 'Service',
    meta: {
      header: headers.WITH_ACCOUNT
    },
    component: () => import('@/views/Service.vue')
  },
  {
    path: '/FAQ',
    name: 'Ofte stillede spørgsmål',
    meta: {
      header: headers.WITH_ACCOUNT
    },
    component: () => import('@/views/FAQ.vue')
  },
  {
    path: '/receipts',
    name: 'Kvitteringer',
    meta: {
      header: headers.DEFAULT
    },
    component: () => import('@/views/Receipts.vue')
  },
  {
    path: '/SkadetCykel',
    name: 'Skadet Cykel',
    meta: {
      header: headers.WITH_ACCOUNT
    },
    component: ()  => import('@/views/SkadetCykel.vue')
  },
  {
    path: '/payment',
    name: 'Betaling',
    meta: {
      header: headers.WITH_ACCOUNT
    },
    component: () => import('@/views/Payment')
  },
  {
    path: '/add-payment-methods',
    name: 'Tilføj Betalingsmetode',
    meta: {
      header: headers.NONE
    },
    component: () => import('@/views/AddPaymentMethods')
  },
  {
    path: '/account',
    name: 'Konto',
    meta: {
      header: headers.DEFAULT
    },
    component: () => import('@/views/Account.vue')
  },
  {
    path: '/payment-methods',
    name: 'Betalingsmetoder',
    meta: {
      header: headers.DEFAULT
    },
    component: () => import('@/views/ShowPaymentMethods')
  }
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
