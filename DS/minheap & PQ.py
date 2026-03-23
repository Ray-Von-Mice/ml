import heapq
import queue

def heapsort(iterable):
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for i in range(len(h))]


def main():
    arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0, -1, 20, 15, 12, 11]
    arr2 = arr[:]
    arr3 =[('c', -100), ('a', 2), ('b', 1000)]
    arr4 = arr2[:]
    heapq.heapify(arr)
    heapq.heappush(arr, 2000)
    print(arr)
    heapq.heapify_max(arr)
    print(arr)
    pq = queue.PriorityQueue()
    for num in arr2:
        pq.put(num)
    pq.put(-300)
    print(pq.queue)

    heapsort(arr4)
    print(arr4)
    heapq.heappush(arr4, -1000)
    print(heapq.nsmallest(3, arr4))


if __name__ == "__main__":
    main()