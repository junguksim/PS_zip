function solution(numbers) {
    var answer = numbers.map((curr)=>{
        curr = curr + '';
        return curr;
    }).sort((a,b)=>{
        return (b+a)-(a+b)
    }).join('');
    return answer[0]==='0'? '0' : answer;
}

console.log(solution([3, 30, 34, 5, 9]));