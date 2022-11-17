pub fn mod_pow(base: u64, exp: u64, modulo: u64) -> u64 {
    let mut res: u64 = 1;
    let mut base: u64 = base;
    let mut exp: u64 = exp;
        
    while exp > 0 {
        if exp % 2 == 1 {
            res = (res * base) % modulo;
        }

        exp >>= 1;
        base = (base * base) % modulo;
    }

    res
}

pub fn mod_mul(a: u64, b: u64, modulo: u64) -> u64 {
    ((a % modulo) * (b % modulo)) % modulo
}

#[cfg(test)]
mod tests {
    use super::{mod_pow, mod_mul};

    #[test]
    fn mod_works() {
        let res = mod_pow(214, 400, 12);
        assert_eq!(res, 4);
    }

    #[test]
    fn mul_works() {
        let res = mod_mul(5, 10, 3);
        assert_eq!(res, 2);
    }
}
