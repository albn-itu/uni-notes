export const bikes = [
    ['Specced Evolution 2019', '1.jpg'],
    ['Princip Grav 3', '2.jpg'],
    ['Gazze City D12', '3.jpg'],
    ['DMK Via 2020', '4.jpg'],
    ['Bian Clari 20', '5.jpg'],
    ['Prim Gonne 80', '6.jpg'],
    ['Knog Oi Oi Oi 2021', '7.jpg'],
    ['SKOTTY Fixeie 1g', '8.jpg'],
    ['Kilgemo Retro 8g', '9.jpg'],
    ['Bian Sprite 921', '10.jpg'],
    ['Gazze Geni XD', '11.jpg'],
];

export function randBike() {
    return bikes[Math.floor(Math.random() * (bikes.length - 1))];
}
