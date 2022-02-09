<template>
  <div class="section row"></div>
  <div class="col">
    <MoleculeTextFieldWithUserInput :type="type1" :placeholder-text="placeholderText1" :helper-text="helperText1"></MoleculeTextFieldWithUserInput>
  </div>
  <div class="col">
    <MoleculeTextFieldWithUserInput :type="type2" :placeholder-text="placeholderText2" :helper-text="helperText2"></MoleculeTextFieldWithUserInput>
  </div>
  <div class="col section">
    <a class="waves-effect white purple-text btn" :href="buttonLink" v-text="buttonText"></a>
  </div>
</template>

<script>
import MoleculeTextFieldWithUserInput from "@/components/molecules/MoleculeTextFieldWithUserInput";

export default {
  name: "OrganismTextFieldInGrid",
  components: {
    MoleculeTextFieldWithUserInput,
  },
  props: {
    placeholderText1: String,
    placeholderText2: String,
    type1: String,
    type2: String,
    helperText1: String,
    helperText2: String,
    buttonText: String,
    buttonLink: MimeType,
  }
}
</script>

<style scoped>
.section {
  height: 5vh
}

.btn {
  text-align: left;
  width: 100%
}
</style>