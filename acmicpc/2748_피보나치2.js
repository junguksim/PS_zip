//한줄
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});
let input = 0;
let arr = new Array(91);
arr.fill(0);
arr[0] = 0;
arr[1] = 1;

rl.on('line', function (line) {
    input = Number(line);
    rl.close();
}).on("close", function () {
    console.log((String(fibonacci(input))));
    process.exit();
});



function fibonacci(n) {
    if (n <= 1) return n;
    if (arr[n] != 0) {
        return arr[n];
    }
    arr[n] = BigInt(fibonacci(n - 1))+ BigInt(fibonacci(n - 2));
    return arr[n];
}