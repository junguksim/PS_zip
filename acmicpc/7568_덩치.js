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
        let N = Number(input[0]);
        input.shift();
        let counts = [];
        input = input.map((curr)=>{
            curr = curr.split(' ');
            return curr.map((curr_)=>{
                return Number(curr_)
            });
        })
        for(var i=0; i <input.length; i++) {
            let count = 1;
            for(var j=0; j <input.length; j++) {
                if(i == j) {
                    continue;
                }
                if(input[i][0] < input[j][0] && input[i][1] < input[j][1]) {
                    count++;
                }
            }
            process.stdout.write(count+" ");
        }
        process.exit();
    });