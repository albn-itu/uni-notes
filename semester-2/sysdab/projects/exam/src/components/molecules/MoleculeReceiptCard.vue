<template>
  <atom-card class="bold" title="Cykel leje">
    <h5 class="right-align">{{formattedPrice}}</h5>
    <div class="dateText" v-text="date"></div>
  </atom-card>
</template>

<script>
import AtomCard from "@/components/atoms/AtomCard";

export default {
  name: 'MoleculeReceiptCard',
  components: {
    AtomCard,
  },
  props: {
    date: String,
    price: String
  },
  computed: {
    formattedPrice(){
      return this.price + " DKK."
    }
  }
}
</script>

<style scoped>
h5 {
  margin-top: 0;
  margin-bottom: 0;
}

.dateText {
  margin-top: 0;
  margin-bottom: 0;
}

.bold > :deep(div > span) {
  font-weight: bold;
}
</style>