<template>
  <div class="container">
    <atom-icon-button class="left center-align action-button" @click="$router.go(-1)">chevron_left</atom-icon-button>
    <atom-title class="centered" :tag="tag" :title="title"/>
    <AtomSaveButton class="right right-align action-button" @click="func">GEM</AtomSaveButton>
  </div>
  <div class="divider"></div>
</template>

<script>
import AtomTitle from "@/components/atoms/AtomTitle";
import AtomIconButton from "@/components/atoms/AtomIconButton";
import AtomSaveButton from "@/components/atoms/AtomSaveButton";

export default {
  name: "MoleculeHeaderWithNavigationAndAccount",
  components: {
    AtomSaveButton,
    AtomTitle,
    AtomIconButton
  },
  props: {
    title: String,
    func: Function,
    tag: {
      type: String,
      default: 'h4'
    },
  }
}
</script>

<style lang="scss" scoped>
.container {
  display: flex;
}

.action-button {
  background-color: white !important;
  margin: auto 0 auto 0;

  :deep(i) {
    color: grey !important;
  }
}

.centered {
  margin: 1rem auto 1rem auto;
}

.material-icons{
  font-size: 40px
}
</style>