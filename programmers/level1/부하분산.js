function solution(k, arrival, load) {
    // Write your code here
    let requests = [];
    let answer = [];
    for(var i = 0; i < arrival.length; i++) {
        requests.push({
            idx : i+1,
            arrival : arrival[i],
            load : load[i],
            finishTime : arrival[i]+load[i]-1
        })
    }
    //console.log(requests)
    requests.sort((a,b)=>{
        return a.arrival - b.arrival
    })
    //console.log(requests)
    let server = new Array(k);
    for(var i = 0 ;i < server.length ; i++) {
        server[i] = {
            idx : i+1,
            load : 0,
            usableTime : 0,
            usable : true
        }
    }
    let j = 0;
    while(requests.length > 0) {
        
        for(var idx = 0 ; idx < requests.length; idx++) {
            if(server[j].usable && server[j].usableTime < requests[idx].finishTime) {
                server[j].load += requests[idx].load;
                server[j].usableTime = requests[idx].finishTime;
                server[j].usable = false;
                requests.shift();
                console.log(server)
                console.log('==========================')
                break;
            }
            if(server[j].usableTime >= requests[idx].finishTime) {
                requests.shift();
                //console.log(`${requests.shift().idx} 번째 요청은 버려진다`);
                break;
            }
        }
        
        if(j === server.length-1) {
            j = 0;
            server = server.map((curr)=>{
                curr.usable = true;
                return curr;
            })
            continue;
        }
        j++;
        
    }
    server.sort((a,b)=>{
        return b.load - a.load
    })
    server = server.filter((value,index)=>{
        return value.load == server[0].load;
    })
    for(var i in server) {
        answer.push(server[i].idx);    
    }
    return answer;
}

console.log(solution(10, [
    5659,6123,6257,6364,6742,6941,7027,7117,8268,9165,3000,3000,3000,3000,
], [5000,5000,5000,5000,5000,5000,5000,5000,5000,5000]));