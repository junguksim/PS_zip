function solution(n) {
    var answer = '';
    let r = 0;
    let p = ["4", "1", "2"];

    while (n > 0) {
        r = n % 3;
        n = parseInt(n / 3);

        if (r == 0) {
            n -= 1;
        }
        answer =p[r] + answer;
    }
    return answer;
}

console.log(solution(6));