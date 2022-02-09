<template>
  <template-help title="Ofte stillede spørgsmål">
    <div class="help-categories">
      <atom-image-with-text class="help-category clickable" img="./images/generelt.jpg" text="Generelt" @click="$router.push({name: 'Ofte stillede spørgsmål', params: {faqItem: 'Generelt'}})"/>
      <atom-image-with-text class="help-category clickable " img="./images/payment.jpg" text="Betaling" @click="$router.push({name: 'Ofte stillede spørgsmål', params: {faqItem: 'Betaling'}})"/>
      <atom-image-with-text class="help-category clickable" img="./images/registrer.jpg" text="Registrer" @click="$router.push('/register')"/>
      <atom-image-with-text class="help-category clickable" img="./images/service.jpg" text="Service" @click="$router.push('/service')"/>
      <atom-image-with-text class="help-category clickable" img="./images/reformedafmeld.jpg" text="Afmelding" @click="$router.push({name: 'Ofte stillede spørgsmål', params: {faqItem: 'Afmelding'}})"/>
      <atom-image-with-text class="help-category clickable" img="./images/skadet cykel.jpg" text="Skadet cykel" @click="$router.push('/SkadetCykel')"/>
    </div>
  </template-help>
</template>
<script>
import AtomImageWithText from "../components/atoms/AtomImageWithText";
import TemplateHelp from '../components/templates/TemplateHelp';

export default {
  components: {
    AtomImageWithText,
    TemplateHelp,
  }
}
</script>
<style lang="scss" scoped>
.help-categories {
  display: grid;
  grid-template-columns: auto auto;
  grid-gap: 1rem;
}

.clickable:hover{
  cursor: pointer;
}
</style>