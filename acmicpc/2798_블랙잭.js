const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input.push(line)
})
    .on('close', function () {
        let M = Number((input[0].split(' '))[1]);
        let arr = input[1].split(' ');
        arr = arr.map((curr)=>{return Number(curr)});
        let temp = 0;
        for(let i = 0; i <= arr.length-3; i++) {
            for(let j = i+1; j <= arr.length-2; j++) {
                for(let k = j+1; k <= arr.length-1; k++) {
                    let sum = arr[i]+arr[j]+arr[k];
                    //console.log(`arr[i]=${arr[i]}, arr[j]=${arr[j]}, arr[k]=${arr[k]}, sum = ${sum}`)
                    if((temp < sum) && (sum <= M)) {
                        temp =  sum;
                    }
                }
            }
        }
        console.log(temp);
        process.exit();
    });