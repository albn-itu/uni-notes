<template>
    <atom-card class="image-with-text card" v-if="loaded">
      <img class="image" :src="bike.getImage()" alt="Bike image">
      <div class="text">
        <p class="model">{{bike.model}}</p>
      </div>
    </atom-card>
  <atom-card class="card">
  <atom-title class="payment-title" tag="h4" title="At betale"></atom-title>
  <p class="amount">{{amount}} DKK</p>
  </atom-card>
  <div class="payment-methods">
    <div class="mobilepay button" @click="paymentConfirm()">
      <img class="normal-image" src="../images/small@2x.png" alt="Mobilepay checkout">
      <img class="large-image" src="../images/medium@2x.png" alt="Mobilepay checkout">
    </div>
    <atom-credit-card class="button" :func="paymentConfirm">
    </atom-credit-card>
   <atom-add-payment-method></atom-add-payment-method>
  </div>
</template>

<script>
import AtomTitle from "@/components/atoms/AtomTitle";
import AtomCard from "@/components/atoms/AtomCard";
import AtomCreditCard from "@/components/molecules/MoleculeCreditCards";
import AtomAddPaymentMethod from "@/components/atoms/AtomAddPaymentMethod";
export default {
    components: {
      AtomAddPaymentMethod,
      AtomCreditCard,
      AtomCard,
      AtomTitle,
    },
  data: () => {
      return{
        loaded: false,
      }
  },
  mounted() {
    if (!this.bikeId || !this.amount || this.bikeId == -1 || this.amount == -1) {
      this.navigateAway();
      return;
    }

    this.loaded = true;
  },
  computed: {
      bikeId() {
        return this.$store.state.payment.bikeId;
      },
      amount() {
        return this.$store.state.payment.amount;
      },
      bike() {
        return this.$store.getters.getBikeById(this.bikeId);
      },

  },
  methods: {
    navigateAway() {
      this.$router.push('/bikes-near-you');
    },
    paymentConfirm() {
      if(confirm("Bekræft betaling")) {
        alert("Betaling fuldført.\nTak fordi du kørte med os!")
        this.navigateAway();
      } else {
        alert("Betaling mislykkedes. Prøv venligst igen");
      }
    },
  }

}
</script>
<style scoped>

.image {
  width: 20rem;
  margin: 2rem auto 10px;
}

.image-with-text {
  margin-left: auto;
  margin-right: auto;
  display: grid;
  grid-auto-flow: row;
  text-align: center;
  font-size: 1.5rem;
  margin-bottom: 4rem;
}

.model {
  max-width: 100%;
  word-wrap: break-word;
}


.amount {
  text-align: center;
  font-size: 30px;
  color: gray;
  margin-bottom: 5rem;
}

.payment-title {
  text-align: center;
}

.payment-methods {
  text-align: center;
}

.button {
  width: 337px;
  height: 64px;
  margin: auto auto 20px;
  background-color: white;
  cursor: pointer;
}

.mobilepay {
  margin-bottom: 20px;
  border: 0;
}

.button:hover {
  opacity: 0.8;
}

.large-image {
  display: none;
}

.card {
  width: 337px;
  margin: 2rem auto;
}

@media only screen and (min-width: 1000px) {
  .normal-image {
    display: none;
  }
  .large-image {
    display: block;
  }
  .button {
    width: 422px;
    height: 80px;
  }
  .card {
    width: 422px;
  }
}
</style>