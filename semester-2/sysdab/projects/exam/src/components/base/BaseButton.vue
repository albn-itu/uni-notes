<template>
    <a :v-bind="$attrs"><slot /></a>
</template>

<script>
export default {
    name: 'BaseButton'
}
</script>