use rand::Rng;

use crate::math::{mod_pow, mod_mul};

#[derive(Debug, Default, Clone, Copy)]
pub struct PedersenInitData {
    pub h: u64,
    pub g: u64,
    pub p: u64
}

pub fn gen_data() -> PedersenInitData {
    let mut rng = rand::thread_rng();

    // Ensure the numbers are suffeciently small
    PedersenInitData {
        h: rng.gen::<u32>() as u64,
        g: rng.gen::<u32>() as u64,
        p: rng.gen::<u32>() as u64,
    }
}

fn get_r(r: Option<u64>) -> u64 {
   match r {
       None => rand::random::<u64>(),
       Some(i) => i
   } 
}

pub fn com(m: crate::dice::Dice, data: PedersenInitData, r: Option<u64>) -> (u64, u64) {
    let r = get_r(r);
    let c = mod_mul(mod_pow(data.g, m as u64, data.p), mod_pow(data.h, r, data.p), data.p);

    (r, c)
}
