l=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        l.append([name,score])
      
    low=min(b for a,b in l)
    for a,b in l:
        l.sort()
        for a,b in l:
            if b==low:
                l.remove([a,b])

        
    seclow=min(b for a, b in l)
    for a,b in l:
        if b==seclow:
            print(a)        
