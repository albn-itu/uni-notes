<template>
    <base-button :v-bind="$attrs" class="btn-floating waves-effect waves-light">
        <i class="material-icons">
            <slot />
        </i>
    </base-button>
</template>

<script>
import BaseButton from '../base/BaseButton.vue'
export default {
    name: 'AtomIconButton',
    components: {
        BaseButton
    }
}
</script>
