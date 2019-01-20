def kth(arr1, m, arr2, n, k):
    if k > (m + n) or k < 1:
        return -1

    if m > n:
        return kth(arr2, n, arr1, m, k)

    if m == 0:
        return arr2[k-1]

    if k == 1:
        return min(arr1[0], arr2[0])

    i = min(m, k//2)
    j = min(n, k//2)

    if arr1[i - 1] > arr2[j - 1]:
        return kth(arr1, m, arr2[j:], n - j, k - j)
    else:
        return kth(arr1[i:], m - i, arr2, n, k - i)

def main():
    arr1 = [2,3,6,7,9]
    arr2 = [1,4,8,10]
    m = len(arr1)
    n = len(arr2)
    k = 5

    ans = kth(arr1,m,arr2,n,k)

    if ans == -1:
        print("Invalid input")
    else:
        print(ans)

    return 0

if __name__ == "__main__":
    main()