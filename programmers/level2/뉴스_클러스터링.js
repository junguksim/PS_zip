function solution(str1, str2) {
    var answer = 0;
    str1 = str1.toUpperCase();
    str2 = str2.toUpperCase();
    let arr1 = [];
    let arr2 = [];
    for(let i = 0 ; i < str1.length-1; i++) {
        var temp = str1.slice(i, i+2);
        if(temp.search(/[^A-Z]/g) >= 0) {continue};
        arr1.push(temp);
    }
    for(let i = 0 ; i < str2.length-1; i++) {
        var temp = str2.slice(i, i+2);
        if(temp.search(/[^A-Z]/g) >= 0) {continue};
        arr2.push(temp);
    }
    arr1 = arr1.sort();
    arr2 = arr2.sort();
    let gyo = [];
    let hap = [];
    for(var i = 0 ; i < arr2.length; i++) {
        if(arr1.indexOf(arr2[i]) >= 0) {
            gyo.push(arr1.splice(arr1.indexOf(arr2[i]), 1))
        }
        hap.push(arr2[i]);
    }
    for(var i = 0 ; i < arr1.length; i++) {
        hap.push(arr1[i])
    }
    if(hap.length == 0) return 65536;
    if(gyo.length == 0) return 0;
    answer = Math.floor((gyo.length/hap.length) * 65536)
    return answer;
}

console.log(solution("aa1+aa2", "AAAA12"))
//console.log(solution('handshake', 'shake hands'));
//console.log(solution('E=M*C^2', 'e=m*c^2'));

