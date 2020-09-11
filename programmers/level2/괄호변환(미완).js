let str = "";
function isRight(arr) {
    let left = 0;
    let right = 0;
    let temp = arr;
    if (temp[0] == "(") {
        var i = 1;
        left++;
        while(i < temp.length) {
            //console.log(`left : ${left}, right : ${right}`)
            
            if (temp[i] == "(") {
                left++;
                if(right != 0) {
                    return false;
                }
            }
            else {
                right++;
                if(left == right) {
                    //console.log(`temp after splice : [${temp}]`)
                    left = 0;
                    right = 0;
                }
            }
            i++;
        }
        return true;
    }
    else {
        return false;
    }
}
function split_two(p) {
    if (p == '') return '';
    if(isRight(p)) {
        return {u_queue : p};
    }
    let left_cnt = 0;
    let right_cnt = 0;
    let u_queue = [];
    let v_queue = [];
    for (var i = 0; i < p.length; i++) {
        if (p[i] == "(") {
            left_cnt++;
        }
        else {
            right_cnt++;
        }
        if (left_cnt === right_cnt) {
            u_queue = p.slice(0, i + 1);
            left_cnt = 0;
            right_cnt = 0;
            v_queue = p.slice(i + 1,);
            break;
        }
    }
    //console.log(`u_queue : [ ${u_queue} ], v_queue : [ ${v_queue} ] in split`)
    if(isRight(u_queue)) {
        str += u_queue.join('');
        console.log(`str : ${str}`)
        return split_two(v_queue);
    }
    else {
        return {u_queue, v_queue};
    }
}
function solution(p) {
    var answer = '';
    if (p == '') return answer;
    p = p.split('');
    if (isRight(p)) return p;
    let {u_queue, v_queue} = split_two(p);
    //console.log(`u_queue : [ ${u_queue} ], v_queue : [ ${v_queue} ] in main`)
    if(isRight(u_queue)) {
        return (u_queue.concat(split_two(v_queue).u_queue)).join('');    
    }
    else {
        console.log(`str : ${str}`)
        str += "(";
        console.log(`str : ${str}`)
        str += (split_two(v_queue).u_queue).join('');
        console.log(`str : ${str}`)
        str += ")";
        console.log(`str : ${str}`)
        u_queue.pop();
        u_queue.shift();
        u_queue = u_queue.map((curr)=>{
            if(curr == "(") {
                curr = ")";
            }
            else {
                curr = "(";
            }
            return curr;
        })
        str += u_queue.join('');
        //console.log(`str : ${str}`)
        return str;
    }
}

console.log(solution("(()())()"));
//console.log(solution(")("));
//console.log(solution("()))((()"));