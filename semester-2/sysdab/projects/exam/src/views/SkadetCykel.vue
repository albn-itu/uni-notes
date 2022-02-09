<template>
  <template-help title="Ofte stillede spørgsmål">
      <ol>
        <li>
          <p>Hvis din cykel går i stykker, sørger vi for, at have en cykel der fungerer klar til dig, inden for 48 timer</p>
        </li>

        <li>
          <p>Din cykel kan til hver en tid blive repareret i vores butikker inden for åbningstiderne.</p>
        </li>

        <li>
          <p>Vi er klar til at hjælpe dig døgnet rundt, og vi garanterer god service. </p>
        </li>
      </ol>
  </template-help>
</template>
<script>
import TemplateHelp from '../components/templates/TemplateHelp';

export default {
  components: {
    TemplateHelp
  }
}

</script>

<style scoped>
ol{
  color: #6200ee;
  font-weight: bold;
}

li > p{
  color: black;
  font-weight: normal;
  padding: .5rem;
}
</style>