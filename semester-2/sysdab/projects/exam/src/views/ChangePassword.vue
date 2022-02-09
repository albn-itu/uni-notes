<template>
  <div class="container">
    <molecule-input-with-validation v-model="input.email" type="email" class="validate" label="Email adresse" />
    <molecule-input-with-validation v-model="input.newPassword" type="password" class="validate" label="Ny adgangskode" />
    <molecule-input-with-validation v-model="input.repeatPassword" type="password" class="validate" label="Gentag ny adganskode" />
   <div class="section">
      <a class="waves-effect white purple-text btn" @click="changePassword()">GEM</a>
    </div>
    <div id="missingInputError" class="red-text" hidden>
      Udfyld alle tekstfelter.
    </div>
    <div id="emailError" class="red-text" hidden>
      Email adressen er forkert
    </div>
    <div id="matchError" class="red-text" hidden>
      De nye password matcher ikke.
    </div>
    <div id="success" class="green-text" hidden>
      Success. Password er nu opdateret.
    </div>
    <div class="section"></div>
  </div>
</template>

<script>
import MoleculeInputWithValidation from '../components/molecules/MoleculeInputWithLabel.vue';

export default {
  components: {
    MoleculeInputWithValidation
  },
  data() {
    return {
      input: {
        email: "",
        newPassword: "",
        repeatPassword: ""
      }
    }
  },
  methods: {
    changePassword() {
      if (this.input.email !== "" && this.input.newPassword !== "" && this.input.repeatPassword !== "") {
        if (this.input.email === this.getUseremail) {
          if (this.input.newPassword === this.input.repeatPassword) {
            this.$store.commit('setPassword', this.input.newPassword)
            document.getElementById("missingInputError").hidden = true;
            document.getElementById("emailError").hidden = true;
            document.getElementById("matchError").hidden = true;
            document.getElementById("success").hidden = false;
          } else {
            document.getElementById("missingInputError").hidden = true;
            document.getElementById("emailError").hidden = true;
            document.getElementById("success").hidden = true;
            document.getElementById("matchError").hidden = false;
          }
        } else {
          document.getElementById("missingInputError").hidden = true;
          document.getElementById("success").hidden = true;
          document.getElementById("matchError").hidden = true;
          document.getElementById("emailError").hidden = false;
        }
      }
      else {
        document.getElementById("success").hidden = true;
        document.getElementById("matchError").hidden = true;
        document.getElementById("emailError").hidden = true;
        document.getElementById("missingInputError").hidden = false;
      }
    }
  },
  computed: {
    getUseremail () {
      return this.$store.state.fakeBackend.useremail
    },
  }
}
</script>
