function solution(relation) {
    var answer = 0;
    let studentNo = [];
    let name = [];
    let major = [];
    let grade = [];
    let tuples = [studentNo, name, major, grade];
    for(var i = 0 ; i < relation.length; i++) {
        studentNo.push(relation[i][0]);
        name.push(relation[i][1]);
        major.push(relation[i][2]);
        grade.push(relation[i][3]);
    }
    for(var i = 0 ; i < tuples.length; i++) {
        let tupleSet = new Set(tuples[i]);
        if(tupleSet.size === tuples[i].length) {
            tuples.splice(i,1);
            answer++; //중복 없는 튜플
        }
    }
    for(var i = 0 ; i < tuples.length; i++) {
        let problemIdxArr = tuples[i].filter((value, index)=>tuples[i].indexOf(value)!==index)
        console.log(problemIdxArr)
    }
    
    return answer;
}

console.log(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]));
