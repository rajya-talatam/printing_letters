def function(string):
    d=dict()
    for key in string:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1
    a = dict(sorted(d.items(),key=lambda item: item[1],reverse=True))
    #{'i': 4, 's': 4, 'p': 2, 'm': 1}
    for i in a:
        print(i,"=","0",+a[i],end=" ")
function("mississippi")