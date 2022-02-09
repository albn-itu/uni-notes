export default class CreditCard {
    constructor(cardNumber, expireDate, cvc, cardType) {
        this.cardNumber = cardNumber;
        this.expireDate = expireDate;
        this.cvc = cvc;
        this.type = cardType;
    }
}