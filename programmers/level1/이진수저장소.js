function solution(arr) {
    // Write your code here
    let maxArr = [];
    let lenArr = [];
    arr.map((curr)=>{
        maxArr.push(Math.max.apply(null, curr));
        lenArr.push(curr.length);
    })
    let DB = [];
    for(var i = 0 ; i < maxArr.length; i++) {
        DB.push({index : i, value : maxArr[i], len : lenArr[i], arr : arr[i].sort((a,b)=>a-b)});
    }
    console.log(DB)
    DB.sort((a,b)=>{
        if(b.value == a.value) {
            if(b.len == a.len) {
                let aMax = 0;
                let bMax = 0;
                let aSliced = [];
                let bSliced = [];
                while(true) {
                    // (a.arr).sort((a,b)=>a-b);
                    // (b.arr).sort((a,b)=>a-b);
                    console.log((a.arr)[(a.arr).length-1]);
                    console.log((b.arr)[(b.arr).length-1]);
                    
                    if((a.arr)[(a.arr).length-1] != (b.arr)[(b.arr).length-1]) {
                        aMax =(a.arr)[(a.arr).length-1]
                        bMax = (b.arr)[(b.arr).length-1]
                        console.log(`aIndex = ${a.index}, bIndex = ${b.index},aMax = ${aMax}, bMax = ${bMax}`)
                        a.arr =(a.arr).concat(aSliced);
                        b.arr = (b.arr).concat(bSliced);
                        break;
                    }
                    else {
                        aSliced.push((a.arr).pop());
                        bSliced.push((b.arr).pop());
                    }
                }
                return bMax - aMax;
            }
            return b.len-a.len;
        }
        else return b.value - a.value;
    })
    return DB.map((curr)=>curr.index);
}

console.log(solution([
    [44 ,0 ,39 ,47 ,6 ,17, 36, 21 ,30 ,33 ,32 ,43 ,50 ,3 ,9 ,20 ,10 ,1 ,5 ,28, 15, 40, 34, 22, 38, 8 ,18, 13, 12], // 0
    [50 ,31 ,24 ,28 ,29 ,30 ,26 ,18 ,49 ,25 ,37 ,7 ,34, 23, 44, 13, 41, 0 ,40 ,48, 27, 8 ,14 ,11 ,47 ,2 ,36, 1, 15 ], // 4
    [10 ,48 ,28 ,36 ,39 ,21 ,41 ,40 ,13 ,6 ,37 ,43 ,35, 32, 12, 49, 3 ,26 ,27, 16, 17, 15, 34, 0 ,50 ,38, 18, 33, 24] // 22
    
]))