<template>
    <div class="input-field">
        <input :id="genId" v-bind="$attrs" v-model="model" class="validate" />
        <label :for="genId">{{ label }}</label>
    </div>
</template>

<script>
import genId from '@/models/Rand';

export default {
    name: 'MoleculeInputWithLabel',
    inheritAttrs: false,
    data() {
        return {
            model: '',
            genId: -1
        }
    },
    props: {
        label: String,
        id: String,
    },
    mounted() {
        if (this.id) {
            this.genId = this.id;
        } else {
            this.genId = genId(15);
        }
    },
}
</script>