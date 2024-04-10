# Time O(nlog(n)) | Space O(1)
def optimalFreelancing(jobs):
    profit = 0
    LENGTH_OF_WEEK = 7
    jobs.sort(key = lambda job: job["payment"], reverse=True)
    timeline = [False] * LENGTH_OF_WEEK
    
    for job in jobs:
        maxTime = min(job["deadline"] , LENGTH_OF_WEEK)
        for day in reversed(range(maxTime)):
            if timeline[day] == False:
                timeline[day] = True
                profit += job["payment"]
                break

    return profit
