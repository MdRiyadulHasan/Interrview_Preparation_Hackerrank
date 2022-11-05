def jumpingOnClouds(c):
    count=0
    i=0
    while i<len(c)-1:
        if i+2<len(c) and c[i+2]==0:
            count+=1
            i+=2
        else:
            count+=1
            i+=1
    return count        
if __name__ == '__main__':
    n = 7 # int(input().strip())
    c = [0,0,1,0,0,1,0] # list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    print(result)
    