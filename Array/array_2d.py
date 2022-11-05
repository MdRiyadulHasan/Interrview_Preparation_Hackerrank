def hourglassSum(arr):
    maxsum=-99
    for i in range(4):
        for j in range(4):
            top=sum(arr[i][j:j+3])
            mid=arr[i+1][j+1]
            bottom =sum( arr[i+2][j:j+3])
            hourglass =top+mid+bottom
            maxsum = max(maxsum,hourglass)
    return maxsum 

if __name__ == '__main__':
    arr = [[-9, -9, -9,  1, 1, 1 ],[0, -9,  0,  4, 3, 2],[-9, -9, -9,  1, 2, 3],[0,  0,  8,  6, 6, 0],[ 0,  0,  0, -2, 0, 0],[ 0,  0,  1,  2, 4, 0]]
    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    print(result)