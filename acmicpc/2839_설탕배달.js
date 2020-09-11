const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', function (line) {
    let SUGAR = line;
    const BIG = 5;
    const SMALL = 3;

    let bigMax = Math.floor(SUGAR / BIG);
    while(bigMax >= 0) {
        let tempSugar = SUGAR - bigMax * BIG;
        if(tempSugar % 3 === 0) {
            console.log(bigMax + tempSugar / SMALL);
            return;
        } else {
            bigMax--;
        }
    }
    console.log(-1);
    rl.close();
}).on("close", function () {
    process.exit();
});