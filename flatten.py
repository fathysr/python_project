nestedlist = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flatlist = []
def flatten(n):
    for i in n :
        if isinstance(i,list):
            flatten(i)
        else:
            flatlist.append(i)

flatten(nestedlist)
print(flatlist)