function solution(s) {
    let answer = 0;
    let aObj = {};
    for(var i = 65; i <= 90; i++) {
        aObj[String.fromCharCode(i)] = i - 65;
    }
    let point = 'A'
    console.log(aObj)
    s = s.split('');
    for(var i = 0 ; i < s.length; i++) {
        console.log(`현재 위치 : ${point}, target : ${s[i]}`)
        let goRight = Math.abs(aObj[s[i]] - aObj[point]);
        let goLeft = Math.abs(26 - Math.abs(aObj[s[i]] - aObj[point]));
        console.log(`오른쪽으로 걷는 거리 : ${goRight}`);
        console.log(`왼쪽으로 걷는 거리 : ${goLeft}`);
        if(goRight > goLeft) answer += goLeft;
        else answer += goRight;
        point = s[i];
        console.log(`answer = ${answer}`)
    }
    return answer;
}


console.log(solution("ZNMD"));