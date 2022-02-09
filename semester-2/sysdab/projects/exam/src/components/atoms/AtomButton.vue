<template>
  <base-button :v-bind="$attrs" class="waves-effect waves-light btn"><slot /></base-button>
</template>

<script>
import BaseButton from '../base/BaseButton.vue'
export default {
    name: 'AtomButton',
    components: {
      BaseButton
    }
}
</script>
