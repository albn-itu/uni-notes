<template>
  <div class="section container">
    <MoleculeReceiptCard date="apr. 28, 2021" price="17"></MoleculeReceiptCard>
    <MoleculeReceiptCard date="okt 19, 2020" price="61"></MoleculeReceiptCard>
    <MoleculeReceiptCard date="mar. 13, 2020" price="53"></MoleculeReceiptCard>
    <MoleculeReceiptCard date="jan. 10, 2020" price="8"></MoleculeReceiptCard>
  </div>
</template>

<script>
import MoleculeReceiptCard from "@/components/molecules/MoleculeReceiptCard";

export default {
  components: {
    MoleculeReceiptCard,
  },
  methods: {
    createReceipt() {
      //TODO: Dynamically add MoleculeReceiptCard HTML elements.
      const tag = document.createElement("MoleculeReceiptCard");
      const text = document.createTextNode("Why is this not a card");
      tag.appendChild(text);
      const element = document.getElementById("new");
      element.appendChild(tag);
    }
  }
}
</script>

<style scoped>

</style>