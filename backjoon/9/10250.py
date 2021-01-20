test = int(input())

for i in range(test):
    h,w,n = map(int,input().split())
    if n%h == 0:
        yy = str(h)
        xx = str(n//h).zfill(2)
    else:
        yy = str(n%h)
        xx = str(n//h+1).zfill(2)
    print(yy+xx)