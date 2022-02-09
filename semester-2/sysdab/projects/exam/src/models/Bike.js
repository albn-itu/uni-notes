export default class Bike {
    constructor(id, image, model, price, position) {
        this.id = id;
        this.image = image;
        this.model = model;
        this.price = price;
        this.position = position;
    }

    getImage() {
        return `./bikes/${this.image}`;
    }

    getPrice() {
        return `${this.price} DKK/min`;
    }

    setDistance(distance) {
        this.distance = distance
    }
}