# Triple Step: a child can hop either 1, 2, or 3 steps at a time. Find the number of ways the child can run up the n stairs

def count_waysdp(n, hops):
    """
        Count the number of ways to the top of the stair case using dynamic programming sequence

        n - total number of steps in staircase
        hops - number of steps child can take

        complexity - Space is 0(n); Time is O(n^2)
    """

    # validate input
    if n <= 0:
        return 1

    # store num of ways to top
    result = [0] * (n+1)
    result[0] = 1

    for hop in hops:
        for i in range(hop, n+1):
            result[i] += result[i - hop]

    # return last result = total num ways to top
    return result[n]

# Double counting results, gives every permutation...
def count_waysmem(n, mem):
    # Simplify recursive approach by using memoization

    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif mem[n] > -1:
        return mem[n]
    else:
        mem[n] = count_waysmem(n - 1, mem) + count_waysmem(n - 2, mem) + count_waysmem(n - 3, mem)
        return mem[n]

def count_ways(n):
    mem = [-1] * (n+1)
    return count_waysmem(n, mem)


if __name__ == '__main__':

    hops = [1, 2, 3]
    print(count_waysdp(5, hops))
    print(count_ways(3))