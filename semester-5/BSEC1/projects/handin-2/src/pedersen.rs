use crate::math::mod_pow;

#[derive(Debug, Default)]
pub struct PedersenInitData {
    pub h: u64,
    pub g: u64,
    pub p: u64
}

pub fn gen_data() -> PedersenInitData {
    PedersenInitData {
        h: rand::random::<u64>(),
        g: rand::random::<u64>(),
        p: rand::random::<u64>(),
    }
}

fn get_r(r: Option<u64>) -> u64 {
   match r {
       None => rand::random::<u64>(),
       Some(i) => i
   } 
}

pub fn com(m: u64, data: PedersenInitData, r: Option<u64>) -> (u64, u64) {
    let r = get_r(r);
    let c = mod_pow(data.g, m, data.p) * mod_pow(data.h, r, data.p);

    (r, c)
}
