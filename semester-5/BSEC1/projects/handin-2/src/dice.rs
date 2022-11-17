pub type Dice = u8;

fn handle_invalid(roll: Dice) -> Dice {
    (roll % 6) + 1
}

pub fn gen() -> Dice {
    handle_invalid(rand::random::<Dice>())
}

pub fn xor(a: Dice, b: Dice) -> Dice {
    handle_invalid(a ^ b)
}

