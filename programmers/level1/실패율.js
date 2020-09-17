function solution(N, stages) {
    let users = stages.length;
    for(var i = 1 ; i <= N ; i++) {
        const failures = (stages.filter((value)=>value === i)).length;
        if(failures == 0) {
            fails.push({index : i, failRatio : 0});
        }
        else {
            fails.push({index : i, failRatio : (failures / users)});
            users -= failures;
        }
    }
    fails.sort((a,b)=>{
        if(a.failRatio === b.failRatio) {
            return a.index - b.index;
        }
        else {
            return b.failRatio - a.failRatio;
        }
    })
    return fails.map((curr)=>curr.index)
}

console.log(solution(4, [4,4,4,4,4]));