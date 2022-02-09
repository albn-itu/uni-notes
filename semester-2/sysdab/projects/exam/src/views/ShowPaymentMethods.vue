<template>
  <molecule-credit-cards-information v-on:cardRemoved="removeCreditCard"></molecule-credit-cards-information>
  <atom-add-payment-method class="button"></atom-add-payment-method>
</template>

<script>
import MoleculeCreditCardsInformation from "@/components/molecules/MoleculeCreditCardsInformation";
import AtomAddPaymentMethod from "@/components/atoms/AtomAddPaymentMethod";
export default {
  name: "ShowPaymentMethods",
  components: {AtomAddPaymentMethod, MoleculeCreditCardsInformation},
  methods: {
    removeCreditCard(cardNumber) {
      this.$store.dispatch("deleteCreditCard", cardNumber);
    }
  }
}
</script>

<style scoped>
.button {
  width: 60%;
}

.button > :deep(.button-text) {
  font-size: 1.2rem;
}

@media only screen and (max-width: 1150px) {
  .button {
    width: 300px;
  }
  .button > :deep(.button-text) {
    font-size: 1rem;
  }
}
</style>