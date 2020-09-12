function solution(files) {
    var answer = [];
    let obj = {};
    for(var i = 0 ; i < files.length; i++) {
        let fileName = files[i].toLowerCase();
        let head = "";
        let number = "";
        let tail = ''
        for(var j = 0; j < fileName.length; j++) {
            if(fileName[j] == " ") {
                if(number.length > 0) {
                    tail += fileName[j];
                }
                else {
                    head += fileName[j];
                }
                continue;
            }
            if(isNaN(Number(fileName[j]))) {
                if(number.length > 0) {
                    tail += fileName[j];
                }
                else {
                    head += fileName[j];
                }
            }
            else {
                if(tail.length == 0 && number.length < 5) {
                    number += fileName[j];
                }
            }
        }
        number = Number(number)
        obj[files[i]] = [i, head,number,tail];
    }
    let values = Object.values(obj);
    values.sort((a,b)=>{
        if(a[1] > b[1]) return 1;
        else if(b[1] > a[1]) return -1;
        else {
            if(a[2] === b[2]) {
                return a[0] - b[0];
            }
            return a[2] - b[2];
        }
    })
    console.log(obj)
    for(var i = 0 ; i < values.length; i++) {
        answer.push(Object.keys(obj).find(key => obj[key] === values[i]));
    }
    return answer;
}

//console.log(solution(['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']))
console.log(solution(['AB CD01110', 'B1', 'BB1', 'abcd01110']))
