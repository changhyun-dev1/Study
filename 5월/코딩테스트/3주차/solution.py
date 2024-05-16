# 다리를 지나는 트럭
def solution(bridge_length, weight, truck_weights):
    bridge = [0] * bridge_length    
    onbridge = sum(bridge)         
    answer = 0                   

    while bridge:
        answer += 1
        onbridge -= bridge.pop(0) 
      
        if truck_weights:
            if onbridge + truck_weights[0] <= weight:
                new_truck = truck_weights.pop(0)    
                bridge.append(new_truck)            
                onbridge += new_truck              
            else:
                bridge.append(0)                    

    return answer

# 정수 삼각형
def solution(triangle):

    for i in range(1, len(triangle)): 
        for j in range(i+1): 
            if j == 0: 
                triangle[i][j] += triangle[i-1][j]
            elif j == i: 
                triangle[i][j] += triangle[i-1][-1]
            else: 
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
                
    return max(triangle[-1])
