<template>
  <div class="wrapper">
    <div class="container">
      <div class="section"></div>
      <molecule-input-with-label
        v-model="input.username"
        type="text"
        label="Kaldenavn"
      />
      <molecule-text-field-with-user-input
        v-model="input.email"
        type="email"
        placeholderText="Email adresse"
        error="Indtast en gyldig email"
      />
      <molecule-text-field-with-user-input
        v-model="input.password"
        type="password"
        placeholderText="Ny adgangskode"
        helperText="Ved at fortsætte accepterer du BriefBikes' servicevilkår og bekræfter, at du har læst BriefBikes' privatlivspolitik."
      />
      <div class="section">
        <atom-button class="purple-text white btn" @click="register()">Opret dig</atom-button>
      </div>
    </div>
    <molecule-forgotten text="Har du allerede en konto?" buttonText="Log ind" @click="$router.push('/login')" />
  </div>
</template>

<script>
import MoleculeForgotten from '../components/molecules/MoleculeForgotten.vue';
import MoleculeInputWithLabel from '../components/molecules/MoleculeInputWithLabel';
import MoleculeTextFieldWithUserInput from '../components/molecules/MoleculeTextFieldWithUserInput.vue';
import AtomButton from '../components/atoms/AtomButton';

export default {
  components: {
    AtomButton,
    MoleculeForgotten,
    MoleculeInputWithLabel,
    MoleculeTextFieldWithUserInput
  },
  data() {
    return {
      input: {
        username: "",
        email: "",
        password: "",
        repeatPassword: ""
      }
    }
  },
  methods: {
    register() {
      if(this.input.email !== "" && this.input.password !== ""){
        this.$store.commit('setName', this.input.username)
        this.$store.commit('setEmail', this.input.email)
        this.$store.commit('setPassword', this.input.password)
        this.$router.push("/login")
      }
    }
  }
}
</script>

<style scoped>
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
  width: 100%
}
</style>