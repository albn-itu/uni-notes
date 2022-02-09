<template>
  <atom-card v-for="card in creditCards" :key="card" class="card">
    <div class="column">
    <img src="../../images/1920px-Visa_2014_logo_detail.png" class="image" v-if="card.type == 'VISA'">
      <img src="../../images/DK_Logo_CMYK_Konturstreg.webp" class="image master" v-if="card.type == 'DANKORT'">
      <img src="../../images/MasterCard_Logo.svg.png" class="image master" v-if="card.type == 'MASTERCARD'">
      <p class="credit-card" >{{card.type}} - {{card.cardNumber.slice(card.cardNumber.length-4)}}</p>
    </div>
      <p class="date">Udløber {{card.expireDate}}</p>
    <hr class="solid">
    <atom-button class="button" @click="$emit('cardRemoved', card.cardNumber)">FJERN</atom-button>
  </atom-card>
</template>
<script>
import AtomCard from "@/components/atoms/AtomCard";
import AtomButton from "@/components/atoms/AtomButton";
export default {
  name: "AtomCreditCard",
  components: {AtomButton, AtomCard, },
  props: {
    func: Function,
  },
  computed: {
    creditCards() {
      return this.$store.state.creditCards;
    },
  },
}
</script>
<style scoped>

hr.solid {
  border-top: 1px solid gray;
  margin-left: -25px;
  margin-right: -24px;
}

.card {
  width: 60%;
  margin: 2rem auto;
}

.button {
  position: relative;
  left: 80%;
  background-color: white;
  color: red;
  font-size: 1rem;
  margin-top: 10px;
  box-shadow: 0px 0px;
}

.credit-card {
  font-size: 1.3rem;
  font-weight: bold;
  justify-self: left;
  position: relative;
  text-wrap: none;
}

.date {
  font-size: 0.8rem;
}

.column {
  display: grid;
  grid-auto-flow: column;
}

.image {
  width: 50px;
  margin: auto auto auto 0;
  justify-self: left;
}
.master {
  margin-right: 10px;
}

@media only screen and (max-width: 1150px) {
  .card {
    width: 300px;
  }
  .button {
    left: 75%;
  }
}

</style>