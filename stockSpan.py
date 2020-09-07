stockPrices=list(map(int,input().split()))
st=[]
spanOfDay=[]
count=1
for i in range(len(stockPrices)):
    #print(stockPrices[i])
    count=1
    if st==[]:
        spanOfDay.append(count)
    elif len(st)>0 and  st[-1]> stockPrices[i]:
        spanOfDay.append(count)
    elif st!=[] and st[-1]<= stockPrices[i]:
        while st!=[] and st[-1]<= stockPrices[i]:
            st.pop(-1)
        if st==[]:
            spanOfDay.append(1)
        else:
            spanOfDay.append(i-stockPrices.index(st[-1]))
    st.append(stockPrices[i])
print(spanOfDay)
