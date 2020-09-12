function solution(m, musicinfos) {
    var answer = [];
    let obj = {};
    m = m.replace(/(C#)/g, 'c')
        .replace(/(D#)/g, 'd')
        .replace(/(F#)/g, 'f')
        .replace(/(G#)/g, 'g')
        .replace(/(A#)/g, 'a')
    for(var i = 0 ; i < musicinfos.length; i++) {
        var arr = musicinfos[i].split(',');
        var start = arr[0].split(":");
        var end = arr[1].split(":");
        var length = (end[0]-start[0])*60 + (end[1]-start[1])*1;
        var str = '';
        arr[3] = arr[3].replace(/(C#)/g, 'c')
        .replace(/(D#)/g, 'd')
        .replace(/(F#)/g, 'f')
        .replace(/(G#)/g, 'g')
        .replace(/(A#)/g, 'a')
        
        for(var j = 0; j < length; j++) {
            str += arr[3][j % arr[3].length];
        }
        obj[arr[2]] = str;
    }
    for(var key in obj) {
        if(obj[key].indexOf(m) >= 0) {
            if(answer.length == 0) {
                answer = [key, obj[key].length];
            }
            if(obj[key].length > answer[1]) {
                answer = [key, obj[key].length];
            }
        }
    }
    if(answer.length > 0) {
        return answer[0];
    } 
    return '(None)';
}

console.log(solution('CCB', ["03:00,03:05,FOO,C#C#BC#C#B", "04:00,04:08,BAR,CCBCCB"]))
//console.log(solution('CC#BCC#BCC#BCC#B', ['03:00', '03:30', 'FOO', 'CC#B', '04:00', '04:08', 'BAR', 'CC#BCC#BCC#B']))
//console.log(solution('ABC', ['12:00', '12:14', 'HELLO', 'C#DEFGAB', '13:00', '13:05', 'WORLD', 'ABCDEF']))