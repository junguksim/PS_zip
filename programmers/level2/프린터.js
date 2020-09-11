function solution(priorities, location) {
    var answer = 0;
    let tasks = priorities.map((prior, index)=>{
        return {
            char : String.fromCharCode(65+index),
            lo : index==location,
            prior
        }
    })
    while(true) {
        console.log(tasks)
        console.log('================')
        
        let item = (tasks.splice(0,1))[0];
        if(tasks.some((curr)=>curr.prior > item.prior)) {
            tasks.push(item);
        }
        else {
            answer++;
            if(item.lo) return answer;
        }
        console.log(`answer : ${answer}`)
    }
}
