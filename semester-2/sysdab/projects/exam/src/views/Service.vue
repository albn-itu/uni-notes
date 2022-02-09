<template>
  <template-help title="Ofte stillede spørgsmål">
    <div class="help-categories">
      <atom-image-with-text class="help-category clickable" img="./images/abonnement.jpg" text="Abonnement" @click="$router.push({name: 'Ofte stillede spørgsmål', params: {faqItem: 'Abonnement'}})"/>
      <atom-image-with-text class="help-category clickable" img="./images/overflytning.jpg" text="Overflytning" @click="$router.push({name: 'Ofte stillede spørgsmål', params: {faqItem: 'Overflytning'}})"/>
      <atom-image-with-text class="help-category clickable" img="./images/reparationer.jpg" text="Reparationer" @click="$router.push({name: 'Ofte stillede spørgsmål', params: {faqItem: 'Reparationer'}})"/>
      <atom-image-with-text class="help-category clickable" img="./images/grønby.jpg" text="Grøn by" @click="$router.push({name: 'Ofte stillede spørgsmål', params: {faqItem: 'Grøn By'}})"/>
    </div>
  </template-help>
</template>
<script>
import AtomImageWithText from "../components/atoms/AtomImageWithText";
import TemplateHelp from '../components/templates/TemplateHelp';

export default {
  components: {
    AtomImageWithText,
    TemplateHelp
  }
}
</script>

<style scoped>
.help-categories {
  display: grid;
  grid-template-columns: auto auto;
  grid-gap: 1rem;
}

.clickable:hover{
  cursor: pointer;
}
</style>