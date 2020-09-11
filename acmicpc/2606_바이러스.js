const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];
let visited = new Array(101);
visited.fill(false);
let graph = Array.from(Array(101), ()=>[]);
let answer = 0;

function dfs(node) {
    answer++;
    visited[node] = true;
    //console.log(graph[node])
    for(var k = 0 ; k < graph[node].length; k++) {
        if(!visited[graph[node][k]]) {
            dfs(graph[node][k]);
        }
    }
    return;
}

rl.on('line', function (line) {
    input.push(line)
})
    .on('close', function () {
        const COMPUTER_COUNT = Number(input[0]);
        const PAIRS_COUNT = Number(input[1]);
        
        for(var i = 2; i < input.length; i++) {
            let from = Number((input[i].split(" "))[0]);
            let to = Number((input[i].split(" "))[1]);
            graph[from].push(to);
            graph[to].push(from);
        }
        dfs(1);
        console.log(answer-1)
        process.exit();
    });

`
100
7
1 100
1 90
55 56
57 59
60 55
56 59
90 55
`