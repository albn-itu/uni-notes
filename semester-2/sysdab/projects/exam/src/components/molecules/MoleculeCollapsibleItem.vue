<template>
    <li :id="title">
        <div class="collapsible-header">
            <i class="material-icons">{{ icon }}</i>
            {{ title }}
        </div>
        <div class="collapsible-body">
            <span>
                {{ body }}
            </span>
        </div>
    </li>
</template>

<script>
export default {
    name: 'MoleculeCollapsibleItem',
    props: {
        title: String,
        body: String,
        icon: String
    }
}
</script>