# SYSDAB exam - Group K
## Members
TODO

## Branch structure
| Name      | Purpose                       | Limitations                                   |
|-----------|-------------------------------|-----------------------------------------------|
| Master    | Stable releasable code        | At least 2 approvals, only merge from develop |
| Develop   | Unstable or untested code     | At least 1 approval                           |
| fix/*     | Bugfixes, and smaller changes |                                               |
| feature/* | New features                  |                                               |

## Dependencies
TODO: Links
Vue.js for JS functionality, components and routing

Materialize for appearance

SASS for custom styling of materialize

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
