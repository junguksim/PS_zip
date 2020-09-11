//한줄
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
let save = [];
let input = 0;
rl.on('line', function (line) {
    input = Number(line);
    save[0] = 0;
    save[1] = 1;
    save[2] = 2;
    for(var i = 3; i < input+1; i++) {
        save[i] = (save[i-1]+save[i-2]) % 15746
    }
    rl.close();
}).on("close", function () {
    console.log(save[input]);
    
    process.exit();
});


/***
 * * 1 -> 1
 * * 2 -> 00, 11
 * * 3 -> 100, 001, 111
 * * 4 -> 1100, 1001, 0011, 0000, 1111
 * * 5 -> 11100, 11001, 10011, 00111, 10000, 00100, 00001, 11111
 * * 6 -> 111100, 111001, 110011, 100111, 001111, 110000, 001100, 000011, 100001 , 001001 ,100100,000000, 111111
 */