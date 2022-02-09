<template>
  <base-button :v-bind="$attrs" class="save-button waves-effect waves-purple btn-flat"><slot /></base-button>
</template>

<script>
import BaseButton from '../base/BaseButton.vue'

export default {
    name: 'AtomSaveButton',
    components: { 
        BaseButton
    }
}
</script>

<style lang="scss" scoped>
@import '@/scss/components/variables.scss';

.save-button {
    border-color: #979797;
    border: 1px solid rgba(0, 0, 0, 0.20);
    border-radius: 4px;
    color: $primary-color;
    font-weight: 500;
}

</style>