let cart_items = 0;

function incrementCartItems() {
    if (cart_items == 99) {
        alert("We currently don't support more than 99 items in our cart");
        return;
    }

    cart_items++;

    element = document.getElementById('cartItems');

    element.innerText = cart_items;
}