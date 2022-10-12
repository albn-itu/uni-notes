use rand::Rng;

use crate::math::mod_pow;

#[derive(Debug, Default, Clone, Copy)]
pub struct PedersenInitData {
    pub h: u64,
    pub g: u64,
    pub p: u64
}

pub fn gen_data() -> PedersenInitData {
    let mut rng = rand::thread_rng();

    PedersenInitData {
        h: rng.gen_range(1u64..999u64),
        g: rng.gen_range(1u64..999u64),
        p: rng.gen_range(1u64..999u64),
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
    let c = mod_pow(data.g, m as u64, data.p) * mod_pow(data.h, r, data.p);

    (r, c)
}
