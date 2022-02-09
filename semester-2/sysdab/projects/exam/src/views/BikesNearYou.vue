<template>
    <molecule-map class="map"></molecule-map>
    <atom-icon-button class="float top-left action-button large-button" @click="$router.back()">chevron_left</atom-icon-button>
    <atom-icon-button class="float top-right action-button large-button" @click="$router.push('/account')">settings</atom-icon-button>
</template>

<script>
// TODO: The settings link above, doesn't work as that page doesn't at the moment exist
import MoleculeMap from '@/components/molecules/MoleculeMap.vue'
import AtomIconButton from '@/components/atoms/AtomIconButton.vue'
export default {
    components: {
        MoleculeMap,
        AtomIconButton
    }
}
</script>
<style lang="scss" scoped>
.map {
  position: fixed;
  width: 100%;
  height: 100%;
  left: 0;
  top: 0;
  z-index: 10;
  background: gray;
}

.float {
    z-index: 11;
}

.top-left, .top-right {
    position: absolute;
    top: 0;
}

.top-left {
    left: 0;
}

.top-right {
    right: 0;
}

.action-button {
    background-color: white !important;
    margin: 2rem;

    :deep(i) {
        color: grey !important;
    }
}

@media only screen and (min-width: 993px) {
    .large-button {
        width: 56px;
        height: 56px;
        padding: 0;
        line-height: 54px;
        font-size: 15px;
        outline: 0;
        text-decoration: none;
        text-align: center;
        letter-spacing: 0.5px;
        border: none;
        text-transform: uppercase;
        box-shadow: 0 2px 2px 0 rgba(0, 0, 0, 0.14), 0 3px 1px -2px rgba(0, 0, 0, 0.12), 0 1px 5px 0 rgba(0, 0, 0, 0.2);
    }

    .large-button :deep(i) {
        font-size: 1.6rem;
        line-height: 56px;
    }   
}


</style>

