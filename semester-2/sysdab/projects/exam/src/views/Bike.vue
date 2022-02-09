<template>
    <atom-card class="center-90" v-if="loaded">
        <img class="image z-depth-4" :src="bike.getImage()" />
        <table class="table info-table">
            <tr>
                <td>Model: </td>
                <td>{{ bike.model }}</td>
            </tr>
            <tr>
                <td>Distance fra dig: </td>
                <td>{{ formattedDistance }}</td>
            </tr>
            <tr>
                <td>Pris: </td>
                <td>{{ bike.getPrice() }}</td>
            </tr>
        </table>
    </atom-card>
    <atom-card class="center-90">
        <table class="info-table large-text">
            <tr>
                <td>Brugt tid: </td>
                <td>{{ clock.time }}</td>
            </tr>
        </table>
    </atom-card>
    <atom-card class="center-90">
        <table class="info-table large-text">
            <tr>
                <td>At betale: </td>
                <td>{{ formattedTotal }}</td>
            </tr>
        </table>
    </atom-card>
    <div class="center-90 button-div">
        <atom-button class="action-button report-damage-button" v-if="status.rented && status.handedIn" @click="reportDamage()">Rapporter skade</atom-button>
    </div>
    <div class="center-90 button-div">
        <atom-button class="action-button rent-button" v-if="!status.rented && !status.handedIn" @click="startRent()">Lej</atom-button>
        <atom-button class="action-button handin-button" v-if="status.rented && !status.handedIn" @click="handIn()">Aflever</atom-button>
        <atom-button class="action-button pay-button" v-if="status.rented && status.handedIn" @click="pay()">Betal</atom-button>
    </div>
</template>

<script>
import AtomButton from '../components/atoms/AtomButton.vue';
import AtomCard from '../components/atoms/AtomCard.vue';

export default {
    components: {
        AtomCard,
        AtomButton
    },
    data() {
        return {
            loaded: false,
            bikeId: 0,
            startedRent: 0,
            stoppedRent: 0,
            total: 0,
            status: {
                rented: false,
                handedIn: false
            },
            clock: {
                time: '00:00:00',
                interval: 0,
            }
        }
    },
    mounted() {
        if (!this.$route.params || !this.$route.params.bikeId) {
            this.navigateAway();
            return;    
        }
        
        this.bikeId = this.$route.params.bikeId;
        this.loaded = true;
    },
    beforeUnmount() {
        clearInterval(this.clock.interval);
    },
    computed: {
        bike() {
            return this.$store.getters.getBikeById(this.bikeId);
        },
        formattedTotal() {
           return `${Math.round(this.total * 100) / 100} DKK`
        },
        formattedDistance() {
            let unit = 'meter';
            let dist = this.bike.distance;

            if (dist > 1000) {
                dist = dist / 1000
                unit = 'kilometer'
            }

            return `${Math.round(dist)} ${unit}`;
        }
    },
    methods: {
        navigateAway() {
            this.$router.push('/bikes-near-you');
        },
        formatNum(num) {
            return num.toLocaleString('da-DK', {
                minimumIntegerDigits: 2,
                useGrouping: false
            });
        },
        startRent() {
            this.startedRent = new Date();
            this.status.rented = true;

            this.clock.interval = setInterval(() => {
                this.calcTime();
                this.calcTotal();
            }, 1000);
        },
        handIn() {
            clearInterval(this.clock.interval);
            this.status.handedIn = true;
            this.stoppedRent = new Date();
            
            this.$store.dispatch({
                type: 'setPayment',
                bikeId: this.bikeId,
                amount: this.total
            });
        },
        reportDamage() {
            alert('This feature has not functionality yet. Coming soon');
        },
        pay() {
          this.$router.push({
            name: 'Betaling',
            params: {
              bikeId: this.bikeId,
              total: this.total
            }
          });
        },
        calcTime() {
            if (this.startedRent == 0) {
                this.clock.time = '00:00:00';
            } 

            if (this.status.rented && this.status.handedIn) {
                return;
            }

            let diff = new Date() - this.startedRent;
            let hours = Math.floor(diff / 1000 / 60 / 60);
            diff -= hours * 1000 * 60 * 60;
            let minutes = Math.floor(diff / 1000 / 60);
            diff -= minutes * 1000 * 60;
            let seconds = Math.floor(diff / 1000);

            this.clock.time = `${this.formatNum(hours)}:${this.formatNum(minutes)}:${this.formatNum(seconds)}`
        },
        calcTotal() {
            if (this.startedRent != 0 || this.status.rented && !this.status.handedIn) {
                let diff = new Date() - this.startedRent;
                this.total = this.bike.price * Math.ceil(diff / 1000 / 60);   
            }
        }
    }
}
</script>
<style lang="scss" scoped>
@import '@/scss/components/variables.scss';

.center-90 {
    top: 10;
    width: 90%;
    margin: 1rem auto 2rem auto;
}

.image {
    width: 100%;
}

tr > td:first-child {
    font-weight: bold;
}

tr > td:last-child {
    text-align: right;
}

.action-button {
    font-size: 3rem;
    height: 4rem;
    width: 100%;
    text-align: center;
    line-height: 4rem;
}

.rent-button, .pay-button {
    background-color: $primary-color; 
}

.handin-button, .report-damage-button {
    background-color: $error-color;
}

.report-damage-button {
    font-size: 2rem;
}

.table {
    margin-top: 1rem;
}

td { 
    padding: 0;
}

tr { 
    border:0;
}

.large-text {
    font-size: 2rem;
}
</style>