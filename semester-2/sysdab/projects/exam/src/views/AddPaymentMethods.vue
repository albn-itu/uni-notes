<template>
  <link href='https://css.gg/radio-check.css' rel='stylesheet'>
  <link href='https://css.gg/radio-checked.css' rel='stylesheet'>
  <molecule-header-with-navigation-and-save-button title="Tilføj betalingsmetode" :func="validateCreditCard" tag="h5"></molecule-header-with-navigation-and-save-button>
  <atom-card class="card-details column">
    <molecule-text-field-with-user-input icon=" " placeholder-text="Kortnummer" type="text" id="kortnummer" pattern="(\s*\d{4}){4}" title="Kortnummeret skal være på præcis 16 numre" error="Kortnummer ugyldigt" success="Gyldigt kortnummer"></molecule-text-field-with-user-input>
    <i class="gg-check" id="check"></i>
    <div class="column">
      <molecule-text-field-with-user-input icon=" " placeholder-text="Udløbsdato" type="text" id="dato" pattern="\d{2}\/\d{2}" title="Udløbsdatoen skal være på formattet - mm/åå" error="Ugyldig udløbsdato"></molecule-text-field-with-user-input>
      <molecule-text-field-with-user-input icon=" " placeholder-text="Sikkerhedskode" type="text" id="cvc" pattern="\d{3}" title="Sikkerhedskoden skal være 3 tal" error="Ugyldig sikkerhedskode"></molecule-text-field-with-user-input>
    </div>
  <div class="row">
    <img src="../images/paymethods.svg" class="paymethods" alt="Payment methods">
    <div class="button column">
      <i class="gg-radio-check" id="button1" @click="clickedButton('button1')"></i>
      <i class="gg-radio-check" id="button2" @click="clickedButton('button2')"></i>
      <i class="gg-radio-check" id="button3" @click="clickedButton('button3')"></i>
      <i class="gg-radio-check" id="button4" @click="clickedButton('button4')"></i>
    </div>
  </div>
  </atom-card>
</template>

<script>
import AtomCard from "@/components/atoms/AtomCard";
import MoleculeTextFieldWithUserInput from "@/components/molecules/MoleculeTextFieldWithUserInput";
import CreditCard from "@/models/CreditCard";
import MoleculeHeaderWithNavigationAndSaveButton from '@/components/molecules/MoleculeHeaderWithNavigationAndSaveButton'

export default {
  components: { MoleculeTextFieldWithUserInput, AtomCard, MoleculeHeaderWithNavigationAndSaveButton },
  methods: {
    clickedButton(id) {
      this.resetAllButtons();
      document.getElementById(id).className = "gg-radio-checked"
    },
    resetAllButtons() {
      document.getElementById("button1").className = "gg-radio-check";
      document.getElementById("button2").className = "gg-radio-check";
      document.getElementById("button3").className = "gg-radio-check";
      document.getElementById("button4").className = "gg-radio-check";
    },
    validateCreditCard() {
      let cardNumber = document.getElementById("kortnummer").value;
      let expireDate = document.getElementById("dato").value;
      let cvc = document.getElementById("cvc").value;

      let cardNumberRegex = new RegExp("(\\s*\\d{4}){4}");
      let expireDateRegex = new RegExp("\\d{2}\\/\\d{2}");
      let cvcRegex = new RegExp("\\d{3}");

      let cardNumberValid = cardNumberRegex.test(cardNumber);
      let expireDateValid = expireDateRegex.test(expireDate);
      let cvcValid = cvcRegex.test(cvc);

      if(cardNumberValid && expireDateValid && cvcValid && this.validateCardTypeSelected() && !this.cardAlreadyExists(cardNumber)) {
        this.$store.dispatch("addCreditCard",new CreditCard(cardNumber, expireDate, cvc, this.getCardType()));
        this.$router.go(-1);
      } else {
        if(!cardNumberValid || !expireDateValid || !cvcValid) {
          alert("Venligst indtast et gyldigt kort");
        } else if(!this.validateCardTypeSelected()) {
          alert("Venligst vælg kort type");
        } else {
          alert("Kortet findes allerede")
        }
      }

    },
    validateCardTypeSelected() {
      if(document.getElementById("button1").className == "gg-radio-checked"){
        return true;
      }
      if(document.getElementById("button2").className == "gg-radio-checked"){
        return true;
      }
      if(document.getElementById("button3").className == "gg-radio-checked"){
        return true;
      }
      if(document.getElementById("button4").className == "gg-radio-checked"){
        return true;
      }
      return false;
    },
    getCardType() {
      if(document.getElementById("button1").className == "gg-radio-checked"){
        return "DANKORT";
      } else if(document.getElementById("button2").className == "gg-radio-checked" || document.getElementById("button4").className == "gg-radio-checked") {
        return "VISA";
      } else {
        return "MASTERCARD";
      }
    },
    cardAlreadyExists(cardNumber) {
      if(this.$store.getters.getCreditCardByCardNumber(cardNumber) == undefined) {
        return false;
      }
      return true;
    }
  }
}
</script>

<style scoped>
.gg-check {
  display: none;
}
.column {
  display: grid;
  grid-auto-flow: column;
  width: 100%;
}

.card-details {
  margin-top: 50px;
  margin-bottom: 50px;
  width: 100%;
}

.paymethods {
  margin: auto;
  display: block;
  width: 100%;
}

.row {
  display: grid;
  grid-auto-flow: row;
  width: 100%;
}

.button {
  position: relative;
  justify-self: center;
  left: 10%;
}
.gg-radio-check {
  cursor: pointer;
}
@media only screen and (min-width: 1000px) {
  .button {
    left: 11%
  }
}

</style>