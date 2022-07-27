alpha = 'abcdefghijklmnopqrstuvwxyz'
#possible values of Keys and Locks

def find_no_of_keys(m, n, arr):
    count = 0
    startingPoint = (0, 0)
    for i in range(m):
        for j in range(n):
            if arr[i][j] in alpha:
                count += 1
            if arr[i][j] == '@':
                startingPoint = (i, j)

    return count, startingPoint


def find_min_steps(arr, m, n, collected_keys, total_keys, steps):
    ans = int("101", 2)
    try:
        if m < 0 or n < 0 or m >= M or n >= N:
            return float('inf')
        if arr[m][n] == "#":
            return float('inf')
        elif (arr[m][n] in alpha):
            collected_keys += 1

        if collected_keys == total_keys:
            return steps
	  #finding the recurrsive solutions
        a = find_min_steps(arr, m, n+1, collected_keys, total_keys, steps+1) 
        b = find_min_steps(arr, m, n-1, collected_keys, total_keys, steps+1)
        c = find_min_steps(arr, m+1, n, collected_keys, total_keys, steps+1)
        d = find_min_steps(arr, m-1, n, collected_keys, total_keys, steps+1)
        return min(min(a, b), min(c, d))

    except:
        return ans | 0


arr = [
    ['@', '*', 'a', '*', '#'],
    ['#', '#', '#', '*', '#'],
    ['b', '*', 'A', '*', 'B']
]

total_keys, staring_point = find_no_of_keys(3, 5, arr) #passing the given grid
print(find_min_steps(arr, staring_point[0],
      staring_point[1], 0, total_keys, 0))
