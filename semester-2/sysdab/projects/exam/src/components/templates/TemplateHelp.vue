<template>
  <div class="container">
    <atom-card class="help-card" title="Hvordan kan vi hjælpe dig?">
      <molecule-text-field-with-user-input placeholder-text="Søg BriefBikes' hjælp" type="search" icon="search" />
    </atom-card>

    <atom-card class="help-card" :title="title">
			<div class="content">
					<slot />
			</div>

      <atom-card class="help-card contact-info-card" :title="contactText">
        <div class="contact-info-container">
          <molecule-contact-info title="Kontakt os" info="+45 00 00 00" img="./images/phone.jpg" />
          <molecule-contact-info title="Facebook" info="Svar indenfor 24 timer" img="./images/fb.jpg" />
          <molecule-contact-info title="Chat" info="Svar indenfor 24 timer" img="./images/msg.jpg" />
          <molecule-contact-info title="Email" info="Svar indenfor 24 timer" img="./images/email.jpg" />
        </div>
      </atom-card>
    </atom-card>
  </div>
</template>
<script>
import AtomCard from "../atoms/AtomCard";
import MoleculeContactInfo from '../molecules/MoleculeContactInfo.vue';
import MoleculeTextFieldWithUserInput from "../molecules/MoleculeTextFieldWithUserInput";

export default {
  components: {
    AtomCard,
    MoleculeContactInfo,
    MoleculeTextFieldWithUserInput,
  },
  props: {
		title: String,
		contactText: {
			type: String,
			default: 'Er dit spørgsmål ikke på listen?'
		}
  }
}
</script>

<style lang="scss" scoped>
:deep(.help-card) span {
  text-align: center;
  padding-bottom: 0.5rem;
}

.contact-info {
  &-container {
    margin-top: 2rem;

    display: grid;
    grid-template-columns: auto auto;
    grid-gap: 1rem;
  }

  &-card {
    margin-top: 2rem;
  }
}
</style>