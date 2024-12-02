const fs = require('fs');

// Read input.txt
let inp = fs.readFileSync('input.txt', 'utf8');

// Part 1
let curr_floor = 0;
for (let i = 0; i < inp.length; i++) {
    let char = inp[i];
    if (char === '(') {
        curr_floor += 1;
    } else if (char === ')') {
        curr_floor -= 1;
    }
}
console.log(curr_floor);

// Part 2
curr_floor = 0;
let index;
for (index = 0; index < inp.length; index++) {
    let char = inp[index];
    if (char === '(') {
        curr_floor += 1;
    } else if (char === ')') {
        curr_floor -= 1;
    }
    if (curr_floor < 0) {
        break;
    }
}
console.log(index + 1);
