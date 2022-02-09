<template>
  <template-help title="Mine spørgsmål handler om:" contactText="Andre problemer med din cykel? Kontakt os:">
    <ul class="collapsible popout" ref="faqcollapsible">
      <molecule-collapsible-item title="Generelt" body="Lorem ipsum dolor sit amet" icon="description" />
      <molecule-collapsible-item title="Betaling" body="Lorem ipsum dolor sit amet." icon="attach_money" />
      <molecule-collapsible-item title="Registrer" body="Lorem ipsum dolor sit amet." icon="assignment_ind" />
      <molecule-collapsible-item title="Afmelding" body="Lorem ipsum dolor sit amet." icon="error_outline" />
      <molecule-collapsible-item title="Abonnement" body="Lorem ipsum dolor sit amet." icon="account_circle" />
      <molecule-collapsible-item title="Overflytning" body="Lorem ipsum dolor sit amet." icon="low_priority" />
      <molecule-collapsible-item title="Reparationer" body="Lorem ipsum dolor sit amet." icon="build" />
      <molecule-collapsible-item title="Grøn By" body="Lorem ipsum dolor sit amet." icon="location_city" />
    </ul>
  </template-help>
</template>

<script>
import M from 'materialize-css'
import TemplateHelp from '../components/templates/TemplateHelp';
import MoleculeCollapsibleItem from '../components/molecules/MoleculeCollapsibleItem.vue';

export default {
  components: {
    TemplateHelp,
    MoleculeCollapsibleItem,
  },
  data() {
    return {
      instance: null,
    }
  },
  mounted() {
   this.instance = M.Collapsible.init(this.$refs['faqcollapsible'], {});
    if (this.$route.params && this.$route.params.faqItem) {
     this.openElementById(this.$route.params.faqItem);
    }
  },
  methods: {
    openElementById(id) {
      let element = document.getElementById(id);

      if (element == null || element == undefined) {
        return;
      }
      let children = Array.prototype.slice.call(this.$refs['faqcollapsible'].children);
      let index = children.indexOf(element);
      this.instance.open(index);
    }
  }
}
</script>
