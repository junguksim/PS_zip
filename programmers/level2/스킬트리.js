function solution(skill, skill_trees) {
    var answer = 0;
    let skill_arr = skill.split('');
    skill_trees = skill_trees.map((curr)=>{
        curr = curr.split('');
        curr = curr.filter((val)=>{
            if(skill_arr.includes(val)) return val;
        })
        return curr;
    });
    for(var i in skill_trees) {
        let queue = [];
        console.log(`skill_trees[${i}] : ` + skill_trees[i])
        if(skill_trees[i].length === 0) {
            answer++;
            console.log(`answer : ${answer}`)
            continue;
        }
        for(var j=0; j < skill_trees[i].length ; j++) {
            let idx = skill_arr.indexOf(skill_trees[i][j]);
            if(queue.length === 0 && idx != 0) {
                break;
            }
            if(queue.length === 0 || queue[queue.length-1] + 1 == idx) {
                queue.push(idx);
                if(j == skill_trees[i].length - 1) {
                    answer++;
                    console.log(`answer : ${answer}`)
                }
            }
            else {
                queue = [];
                break;
            }
        }
        console.log(`queue ${i} 번째 : ` + queue)
    }
    return answer;
}

console.log(solution('CBD', ['CXF','ASF','BDF', 'CEFD']));