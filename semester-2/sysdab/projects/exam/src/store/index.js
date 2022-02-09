import { createStore } from 'vuex'
import { randBike } from '@/constants/bikes';
import Bike from '@/models/Bike';
import CreditCard from "@/models/CreditCard";

export default createStore({
  state: {
    bikes: [],
    creditCards: [new CreditCard(
        "1234123412341234",
        "02/22",
        "691",
        "VISA"
    )],
    fakeBackend: {
      name: "Admin",
      useremail: "admin@mail.dk",
      password: "password"
    },
    payment: {
      bikeId: -1,
      amount: -1
    }
  },
  mutations: {
    addBike(state, bike) {
      state.bikes.push(bike);
    },
    addCreditCard(state, creditCard) {
      state.creditCards.push(creditCard);
    },
    removeCreditCard(state, index) {
      state.creditCards.splice(index, 1);
    },
    setName (state, newName) {
      state.fakeBackend.name = newName
    },
    setEmail (state, newEmail) {
      state.fakeBackend.useremail = newEmail
    },
    setPassword (state, newPassword) {
      state.fakeBackend.password = newPassword
    },
    setBikeId (state, bikeId) {
      state.payment.bikeId = bikeId;
    },
    setAmount (state, amount) {
      state.payment.amount = amount;
    }
  },
  actions: {
    setPayment({ commit }, payload) {
      commit('setBikeId', payload.bikeId);
      commit('setAmount', payload.amount);
    },
    addCreditCard({ commit }, creditCard) {
      commit('addCreditCard', creditCard);
    },
    deleteCreditCard({ commit, state }, creditCardNumber) {
        let creditCard = this.getters.getCreditCardByCardNumber(creditCardNumber);
        if(creditCard == undefined) {
          return;
        }
        let index = state.creditCards.indexOf(creditCard);
        commit('removeCreditCard', index);
    },
    async createBikes({ commit }, payload) {
      for (let i = 0; i < payload.amount; i++) {
        let rand = randBike();
        let bike = new Bike(
          i, 
          rand[1], rand[0], 
          Math.round((Math.random() * (10 - 1) + 1) * 100) / 100, 
          [
            Math.random() * (payload.max[0] - payload.min[0]) + payload.min[0],
            Math.random() * (payload.max[1] - payload.min[1]) + payload.min[1]
          ]
        );

        await commit('addBike', bike);
      }
    },
  },
  getters: {
    getBikesOverId: (state) => (id) => {
      return state.bikes.filter(bike => bike.id > id);
    },
    getBikeById: (state) => (id) => {
      return state.bikes.find(bike => bike.id == id);
    },
    getLargestId: (state) => {
      return Math.max(...(state.bikes.map(x => x.id)));
    },
    getCreditCardByCardNumber: (state) => (cardNumber) => {
      return state.creditCards.find(creditCard => creditCard.cardNumber == cardNumber);
    },
  },
  modules: {
  }
})
