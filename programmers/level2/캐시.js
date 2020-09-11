function solution(cacheSize, cities) {
    var answer = 0;
    let cache = [];
    if(cacheSize == 0) {
        return cities.length*5;    
    }
    for (let i = 0; i < cities.length; i++) {
        cities[i] = cities[i].toLowerCase();
        let findObj = cache.find(ele=>ele.name==cities[i]);
        if(findObj === undefined) {
            cache.push({
                name : cities[i],
                idx : i
            });
            answer += 5;
            if(cache.length > cacheSize) {
                cache.shift();
            }
        }
        else {
            let findIdx = cache.indexOf(findObj);
            cache[findIdx].idx = i;
            answer += 1;
        }
        cache.sort((a,b)=>{
            if(a.idx > b.idx) {
                return 1;
            }
            else if(a.idx < b.idx){
                return -1;
            }
        })
    }
    return answer;
}

console.log(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']));
//console.log(solution(3, ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']));