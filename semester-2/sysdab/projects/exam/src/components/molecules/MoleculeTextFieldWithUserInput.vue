<template>
    <div class="input-field">
      <i v-if="icon" class="material-icons prefix">{{ icon }}</i>
      <input v-bind="$attrs" :id="genId" :type="type" class="validate" :pattern="pattern" :title="title" v-model="model">
      <label v-if="placeholderText" :for="genId" v-text="placeholderText"></label>
      <span class="helper-text" v-if="helperText" :data-error="error" :data-success="success" v-text="helperText" @click="help()"></span>
    </div>
</template>

<script>
import genId from '@/models/Rand';

export default {
  name: "MoleculeTextFieldWithUserInput",
  inheritAttrs: false,
  data() {
    return {
      genId: 0,
      model: '',
    }
  },
  mounted() {
    if (this.id) {
      this.genId = this.id;
    } else {
      this.genId = genId(15);
    }
  },
  props: {
    placeholderText: String,
    type: String,
    helperText: String,
    error: String,
    success: String,
    pattern: String,
    title: String,
    helperMethod: Function,
    icon: String,
    id: String,
  },
  methods: {
    help() {
      if (this.helperMethod) {
        this.helperMethod();
      }
    }
  }
}
</script>

<style scoped>

</style>