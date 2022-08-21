import heapq

def solution(food_times, k):
    answer = -1
    heap = []
    for i in range(len(food_times)):
        heapq.heappush(heap, (food_times[i], i+1))
    food_num = len(food_times)
    previous = 0

    while heap:
        t = (heap[0][0] - previous) * food_num
        if k >= t:
            k -= t
            previous, _ = heapq.heappop(heap)
            food_num -= 1
        
        else:
            idx = k % food_num
            heap.sort(key=lambda x: x[1])
            answer = heap[idx][1]
            break
    return answer

food_times = [3, 1, 2]
k = 5
print(solution([1, 5, 5, 5, 5, 6, 7], 31)) 