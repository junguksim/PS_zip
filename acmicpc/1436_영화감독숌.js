//한줄
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', function (line) {
    let N = Number(line);
    let title = 665;
    let count = 0;
    while(++title) {
        let s = String(title);
        if(s.indexOf("666") != -1) {
            ++count;
        }
        if(count == N) {
            console.log(title);
            break;
        }
    }

    rl.close();
}).on("close", function () {
    process.exit();
});