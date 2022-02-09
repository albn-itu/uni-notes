<template>
    <link rel="preconnect" href="https://fonts.gstatic.com">
    <link href="https://fonts.googleapis.com/css2?family=Montserrat&display=swap" rel="stylesheet">

    <!-- Probably not the best scaling on this -->
    <header class="landing-page-header">
        <img src="../images/logo.svg" class="logo" alt="Brand logo">
        <atom-button class="button log-ind" @click="onLogIn">LOG IND</atom-button>
    </header>
    <div class="container-box">
        <img src="../images/murillo-de-paula-o2FCfhNSjPo-unsplash.jpg" class="mood-pic" alt="Woman riding a bike">
        <div class="image-box">
            <p class="image-text">You ride, we provide<br> <br>
               Lej cykler fra kun 1kr,- i minuttet med gratis oprettelse
            </p>
          <atom-button class="button sign-up" @click="onSignUp">OPRET KONTO</atom-button>
        </div>
    </div>
    <div class="container-box-guide">
        <p class="guide-text">Så nemt er det</p>
        <!-- <atom-title tag="h2" title="Så nemt er det" class="guide-title"/> -->
        <atom-button class="button sign-up-2" @click="onSignUp">OPRET KONTO</atom-button>
        <p class="arrow-down">&#8595;</p>
        <p class="guide-text">Find en cykel nær dig</p>
        <p class="arrow-down">&#8595;</p>
        <p class="guide-text">Nyd din cykeltur</p>
        <p class="arrow-down">&#8595;</p>
        <p class="guide-text bottom">Stil cyklen og vi henter den</p>
    </div>
</template>

<script>
import AtomButton from '@/components/atoms/AtomButton.vue'

export default {
    components: {
        AtomButton,
    },
    methods: {
      onSignUp() {
        this.$router.replace('/register');
      },
      onLogIn() {
        this.$router.replace('/login');
      }
    }
}
</script>

<style scoped>
  .landing-page-header {
    display: grid;
    grid-auto-flow: column;
  }

  .logo {
    width: 60%;
    height: 10rem;
    padding-top: 3%;
    padding-left: 3%;
    padding-bottom: 3%;
    justify-self: left;
    align-self: center;
  }

  .button {
    position: relative;
    font-family: 'Montserrat', sans-serif;
    text-shadow: 2px 2px #161616;
    background-color: #6200ee;
    text-align: center;
    font-size: 1rem;
    height: fit-content;
    font-weight: bold;
    border-radius: 1rem;
    color: white;
  }

  .log-ind {
    margin-top: 10%;
    margin-bottom: 10%;
    justify-self: right;
    margin-right: 10%;
    padding: 2% 3%;
    top: 2.5rem;
  }

  @media screen and (min-width: 800px) {
    .log-ind {
      font-size: 1rem;
      top: 2rem;
    }
  }

  .mood-pic {
    width: 100%;
  }

  .container-box {
    position: relative;
  }

  .image-box {
    display: grid;
    grid-auto-flow: row;
    position: absolute;
    margin-left: 5%;
    width: 70%;
    height: 70%;
    border: 1px;
    top: 1%;
  }

  .image-text {
    font-family: 'Montserrat', sans-serif;
    font-size: 2rem;
    text-align: center;
    color: white;
    text-shadow: 2px 2px #161616;
  }

  .sign-up {
    margin-top: 10px;
    justify-self: center;
    padding: 1% 3%;
    bottom: 10%;
  }

  .container-box-guide {
    display: grid;
    grid-auto-flow: row;
  }

  .sign-up-2 {
    /*TODO add border color*/
    margin-top: 10px;
    justify-self: center;
    margin-bottom: 1rem;
    top: 5%;
    padding: 1% 2%;
  }

  @media screen and (max-width: 1100px) {
    .sign-up {
      padding: 1% 2%;
    }
    .image-text {
      font-size: 1.8rem;
    }
    .button {
      font-size: 0.85rem;
      margin-bottom: 2%;
    }
  }

  .arrow-down {
    position: relative;
    font-size: 3rem;
    text-align: center;
    color: #5a78ff;
    padding: 0;
    margin: 0;
  }

  .guide-text {
    margin-top: 0.1rem;
    margin-bottom: 0.1rem;
    position: relative;
    font-weight: bold;
    text-align: center;
    font-size: 1.5rem;
  }

  @media screen and (max-width: 900px) {
    .image-text {
      font-size: 1.5rem;
    }
    .sign-up {
      bottom: 30%;
    }
    .guide-text {
      font-size: 1.3rem;
    }
  }
  .bottom {
    margin-bottom: 2rem;
  }
</style>