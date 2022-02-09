<template>
  <div class="wrapper">
    <div class="container">
      <div class="section"></div>
      <molecule-text-field-with-user-input
        v-model="input.username"
        type="email"
        placeholderText="Email adresse"
        error="Indtast email"
        :helperMethod="tip"
        helperText="Har du glemt mailadressen?"
      />
      <molecule-text-field-with-user-input
        v-model="input.password"
        type="password"
        placeholderText="Adgangskode"
        :helperMethod="tip"
        helperText="Har du glemt adgangskoden?"
      />
      <div class="section">
        <atom-button class="purple-text white btn" @click="login()">Log ind</atom-button>
      </div>
      <div id="alert" class="red-text" hidden>
        Kombinationen af brugernavn og adgangskode blev ikke genkendt.
      </div>
      <div id="error" class="red-text" hidden>
        Indtast brugernavn og adgangskode.
      </div>
    </div>

    <molecule-forgotten text="Har du ikke en konto?" buttonText="Tilmeld dig" @click="$router.push('/register')" />
  </div>
</template>

<script>
import MoleculeForgotten from '../components/molecules/MoleculeForgotten.vue';
import MoleculeTextFieldWithUserInput from '../components/molecules/MoleculeTextFieldWithUserInput.vue';
import AtomButton from '../components/atoms/AtomButton';

export default {
    components: {
      AtomButton,
      MoleculeForgotten,
      MoleculeTextFieldWithUserInput
    },
    data() {
      return {
        input: {
          username: "",
          password: ""
        }
      }
    },
    methods: {
      login() {
        if(this.input.username !== "" && this.input.password !== "") {
          if(this.input.username === this.getUseremail && this.input.password === this.getPassword) {
            this.$router.push("/bikes-near-you")
          } else {
            document.getElementById("error").hidden = true;
            document.getElementById("alert").hidden = false;
          }
        } else {
          document.getElementById("alert").hidden = true;
          document.getElementById("error").hidden = false;
        }
      },
      tip() {
        alert("Denne funktion er ikke tilgængelig - Brug sidefoden til at navigerer eller tilmeld dig igen");
      }
    },
    computed: {
      getUseremail () {
        return this.$store.state.fakeBackend.useremail
      },
      getPassword () {
        return this.$store.state.fakeBackend.password
      }
    }
}
</script>

<style lang="scss" scoped>
.wrapper {
  display: flex;
  flex-direction: column;
  height: 100%;
}

.container {
  flex-grow: 1;
}

.section{
  height: 10vh
}

.btn {
  text-align: left;
  width: 100%;
}

.helper-text {
  cursor: pointer;
}
</style>