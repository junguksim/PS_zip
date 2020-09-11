function solution(s) {
    var answer = s;
    const MAX_CUT_LENGTH = s.length / 2;
    const STR_LENGTH = s.length;
    s = s.split('');
    for(var i = 1 ; i <= MAX_CUT_LENGTH; i++) {
        let temp_str = "";
        
        let standard_str = (s.slice(0, i)).join('');
        let count = 1;
        for(var j = i; j < STR_LENGTH ; j += i) {
            const str = (s.slice(j, j+i)).join('');
            if(str === standard_str) {
                count++;
            }
            else {
                temp_str += (count > 1 ? count + standard_str : standard_str);
                standard_str = str
                count = 1;
            }
        }
        if(standard_str) {
            temp_str += (count > 1 ? count + standard_str : standard_str);
        }
        if(answer.length > temp_str.length) {
            answer = temp_str;
        }
    }
    return answer.length;
}

console.log(solution("aabbaccc"));