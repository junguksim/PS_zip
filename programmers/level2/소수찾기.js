function solution(numbers) {
    var answer = 0;
    numbers = numbers.split('');
    let possible = [];
    let i =0;
    while(i < numbers.length) {
        let value = numbers[i];
        let temp = JSON.parse(JSON.stringify(numbers));
        temp.splice(i, 1);
        
        console.log(`value = ${value}`)
        console.log(`비교군 : [${temp}]`)
        if(chkPrime(Number(value)) && possible.indexOf(Number(value)) == -1) {
            possible.push(Number(value));
        }
        temp.map((curr)=>{
            if(chkPrime(Number(curr+value)) && possible.indexOf(Number(curr+value)) == -1) {
                possible.push(Number(curr+value));
            }
        })
        let plus_length = 2;
        while(plus_length < temp.length-1) {
            for(var j = 0 ; j < temp.length ; j++) {
                let val = value;
                let cnt = 0;
                while(cnt < plus_length) {
                    val += temp[j];
                    cnt++;
                }
                

            }


            plus_length++;
        }
        console.log(`possible : [${possible}]`)
        i++;
    }
    console.log(possible)
    return answer;
}

function chkPrime(num) {
    if(num == 1 || num == 0) return false;
    for(var i = 2 ; i < num; i++) {
        if(num % i === 0) {
            return false;
        }
    }
    return true;
}
console.log(solution("011"))