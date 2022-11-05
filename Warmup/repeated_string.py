def repeatedString(s, n):
    x=n//len(s)
    x1=x*s.count('a')
    x2=s[:n%len(s)].count('a')
    return x1+x2
if __name__ == '__main__':
    s = input()
    n = int(input().strip())
    result = repeatedString(s, n)
    print(result)