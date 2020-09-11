//한줄
const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.on('line', function (line) {
    let N = Number(line);
    let first = N - 1;
    let arr = [];
    while(true) {
        let sum = String(first).split('').map((curr)=>{
            curr = Number(curr);
            return curr;
        }).reduce((acc,cur)=>{
            return acc+cur;
        })
        //console.log(first, sum);
        if(first+sum == N) {
            arr.unshift(first);
        }
        if(first < 0) {
            break;
        }
        first--;
    }
    if(arr.length == 0) console.log(0);
    else console.log(arr[0]);
    rl.close();
}).on("close", function () {
    process.exit();
});