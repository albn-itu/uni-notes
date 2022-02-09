<template>
  <atom-button class="grid button" v-bind="$attrs" @click="newPaymentMethod">
    <p class="plus">+</p>
    <p class="button-text">TILFØJ BETALINGSKORT</p>
    <i class="gg-credit-card"></i>
  </atom-button>
</template>

<script>
import AtomButton from "@/components/atoms/AtomButton";
export default {
  name: 'AtomAddPaymentMethod',
  inheritAttrs: false,
  components: {
    AtomButton
  },
  methods: {
    newPaymentMethod() {
      this.$router.push({name: 'Tilføj Betalingsmetode'})
    }
  },
}
</script>
<style scoped>
.button-text {
  font-size: 20px;
  margin: 0 auto;
  line-height: 64px;
  color: #6200ee;
  font-weight: bold;
  text-align: center;
}

.button {
  width: 337px;
  height: 64px;
  margin: 20px auto;
  background-color: white;
  cursor: pointer;
}

.plus {
  font-size: 20px;
  margin: 0 auto;
  line-height: 64px;
  font-weight: bold;
  color: black;
}

.grid {
  display: grid;
  grid-auto-flow: column;
}

.gg-credit-card {
  top: 24px;
  justify-self: center;
  color: black;
}

@media only screen and (min-width: 1000px) {
  .button {
    width: 422px;
    height: 80px;
  }

  .button-text {
    line-height: 80px;
  }

  .plus {
    line-height: 80px;
  }

  .gg-credit-card {
    top: 33px;
  }
}
</style>
