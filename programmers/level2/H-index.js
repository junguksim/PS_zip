function solution(citations) {
    var answer = 0;
    if(citations.length == 0) {
        return citations[0];
    }
    
    let j= 0;
    while(j <= citations.length) {
        
        let bigger = (citations.filter((val)=>{
            return val >= j;
        })).length;
        let smaller = (citations.filter((val)=>{
            return val <= j;
        })).length;
        //console.log(`item : ${j}, bigger : ${bigger}, smaller : ${smaller}, answer : ${answer}`)
        if(bigger >= j && smaller <= j) {
            answer = j;  
        }
        j++;
    }
    return answer;
}

console.log(solution([3,0,6,1,5]))
console.log(solution([31,66]))