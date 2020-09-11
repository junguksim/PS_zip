function solution(bridge_length, weight, truck_weights) {
    var answer = 0;
    let bridge_queue = new Array(bridge_length);
    bridge_queue.fill(-1);
    answer++;
    let truck = truck_weights.shift();
    let weight_sum = 0;
    weight_sum += truck;
    bridge_queue.unshift(truck);
    bridge_queue.pop();
    while(weight_sum > 0) {
        answer++;
        if(bridge_queue[bridge_queue.length-1] !== -1) {
            weight_sum -= bridge_queue[bridge_queue.length-1];
        }
        bridge_queue.pop();
        if(weight_sum + truck_weights[0] <= weight) {
            truck = truck_weights.shift();
            weight_sum += Number(truck);
            bridge_queue.unshift(truck);
        }
        
        else {
            bridge_queue.unshift(-1);
        }
    }
    return answer;
}

console.log(solution(2, 10 ,[7,4,5,6]));