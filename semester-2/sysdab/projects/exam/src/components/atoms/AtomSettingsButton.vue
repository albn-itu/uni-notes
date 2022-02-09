<template>
  <div class="settings-link">
    <base-button class="settings-link-button" :v-bind="$attrs" ><slot /></base-button>
  </div>
</template>

<script>
import BaseButton from '../base/BaseButton.vue'
export default {
    name: 'AtomSettingButton',
    components: {
      BaseButton
    }
}
</script>

<style lang="scss" scoped>
.settings {
  &-link {
    text-align: center;
    border-style: solid;
    border-width: 0 0 1px 0;
    border-color: rgba(0, 0, 0, 0.38);

    &-button {
      font-weight: bold;
      display: block;
      margin: 1em 0 1em 0;
      color: rgba(0, 0, 0, 0.87) 
    }
  }
}
</style>

