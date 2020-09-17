const key = {
    'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,
    'K':11,'L':12,'M':13,'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19, 'T':20,
    'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26
}
let idx = 27;
function solution(msg) {
    let answer = [];
    for(let i = 0 ; i < msg.length; i) {
        let w = msg[i];
        let c = msg[i+1];
        let newW = add(msg,i,w,c,0);
        answer.push(key[newW]);
        i += newW.length;
    }
    return answer;
}

function add(msg, i, w, c, cnt) {
    if(key[w+c] === undefined) {
        key[w+c] = idx++;
        return w;
    }
    else {
        cnt++;
        let newW = w+c;
        let newC = msg[i+1+cnt];
        return add(msg, i, newW, newC, cnt);
    }
}




//console.log(solution('KAKAO'));
//console.log(solution('TOBEORNOTTOBEORTOBEORNOT'))
console.log(solution(`ABABABABABABABAB`));
