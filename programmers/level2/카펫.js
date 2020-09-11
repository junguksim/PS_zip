function solution(brown, yellow) {
    let tiles = brown+yellow;
    for(let i = Math.floor(tiles / 2); i >= 0 ; i--) {
        if(tiles % i !== 0) continue;

        let x = i;
        let y = tiles / i;

        if((x-2) * (y-2) == yellow) {
            return [x, y];
        }
    }
}

console.log(solution(8,2000000))