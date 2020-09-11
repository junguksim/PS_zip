//여러줄
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];
for(var i = 1000000; i > 0; i--) {
    input.push(i);
}

rl.on('line', function (line) {
    //input.push(Number(line));
})
    .on('close', function () {
        input.shift();
        input.sort((a,b)=>{return a-b;});
        for(var i of input) {
            console.log(i)
        }
        process.exit();
    });