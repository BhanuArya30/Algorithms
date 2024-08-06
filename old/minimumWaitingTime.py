# Time O(nlogn) | Space O(n)
def minimumWaitingTime(queries):
    queries.sort()
    wait_counter = 0
    query_wait = []
    for q_idx in range(len(queries)):
        query_wait.append(wait_counter)
        wait_counter += queries[q_idx]
    return sum(query_wait)

arr = [3, 2, 1, 2, 6]
print(minimumWaitingTime(arr))