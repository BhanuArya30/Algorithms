# # Time O(nlogn) | Space O(1)
# def nonConstructibleChange(coins):
#     coins.sort()
#     current_change = 0
#     for coin in coins:
#         if coin > current_change + 1:
#             return current_change + 1
#         current_change += coin
#     return current_change + 1


# Time O(nlogn) | Space O(1)
def nonConstructibleChange(coins):
    coins.sort()
    minimum_change = 0
    for coin in coins:
        if coin > minimum_change + 1:
            break
        minimum_change += coin
    return minimum_change + 1

"""
Lets say our minimum_change is 7, it basically means that with our current coins we can make from 1,2,3,...,7.

Now, we already have a fact, that we can make any coin from 1 to 7, right?
Then, whatever coin (n) we add to it, we will be able to make n+1, n+2, n+3, ... n+7.

Now, the reason why n must be less than minimum_change + 1 for us to add it to our minimum change is that: 

If n is greater than minimum_change+1, then we can't make minimum_change+1 with our coins.

For example, our new coin is 9. We can make 9+1, 9+2, ..., 9+7, but we can't make 8.
To make 8 we need any coin less than or equal to 8. 

If we have 8 we can just use that coin. If we have 7 we can add 1 to it. If we have 6 we can add 2 to it, and so on.
"""