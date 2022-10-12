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

#[cfg(test)]
mod tests {
    use super::mod_pow;

    #[test]
    fn mod_works() {
        let res = mod_pow(214, 400, 12);
        assert_eq!(res, 4);
    }
}
