<template>
  <atom-button v-for="card in creditCards" class="button" :key="card" @click="func">
    <p class="button-text"> {{card.type}} ENDER MED - {{card.cardNumber.slice(card.cardNumber.length-4)}}</p>
  </atom-button>
</template>
<script>
import AtomButton from "@/components/atoms/AtomButton";
export default {
  name: "AtomCreditCard",
  components: {AtomButton},
  props: {
    func: Function,
  },
  computed: {
    creditCards() {
      return this.$store.state.creditCards;
    },
  }
}
</script>
<style scoped>
  .button {
    width: 337px;
    height: 64px;
    margin: auto auto 20px;
    background-color: white;
    cursor: pointer;
  }
  .button-text {
    font-size: 20px;
    margin: 0 auto;
    line-height: 64px;
    color: #6200ee;
    font-weight: bold;
    text-align: center;
  }

  @media only screen and (min-width: 1000px) {
    .button {
      width: 422px;
      height: 80px;
    }

    .button-text {
      line-height: 80px;
    }
  }
</style>