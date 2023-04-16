# 1 - Minimum Waiting Time
def minimumWaitingTime(queries):
    queries.sort()
    query_wait = 0
    total_wait = 0

    for query in queries:
        total_wait += query_wait
        query_wait += query 

    return total_wait

def minimumWaitingTime2(queries):
    # multiply the remaining queries by delay time and sum them up 
    queries.sort()
    total = 0
    for i, query in enumerate(queries):
        left = len(queries) - (i+1)
        total += query * left
    
    return total



print(minimumWaitingTime2([3, 2, 1, 2, 6]))