expression=input()
j=len(expression)-1
def solve(exp,i,j,state):
# state=0 for min 1 for max
    if i>j:
        return 0
    if i==j:
        return int(exp[i])
    if j-i==2:
         if exp[i+1]=='-':
            return int(exp[i])-int(exp[j])
         if exp[i+1]=='+':
            return int(exp[i])+int(exp[j])
         if exp[i+1]=='*':
            return int(exp[i])*int(exp[j])
         if exp[i+1]=='/':
            if exp[j]!=0:
               return int(exp[i])/int(exp[j])

    value=0
    for k in range(i+1,j,2):
        leftMax=solve(exp,i,k-1,1)
        rightMax=solve(exp,k+1,j,1)
        leftMin=solve(exp,i,k-1,0)
        rightMin=solve(exp,k+1,j,0)
        if exp[k]=='-':
            if state==1:
                value+=max(leftMin-rightMax,leftMax-rightMax,leftMin-rightMin,leftMax-rightMin)
            else :
                value+=min(leftMin-rightMax,leftMax-rightMax,leftMin-rightMin,leftMax-rightMin)
        if exp[k]=='+':
            if state==1:
                value+=max(leftMin+rightMax,leftMax+rightMax,leftMin+rightMin,leftMax+rightMin)
            else :
                value+=min(leftMin+rightMax,leftMax+rightMax,leftMin+rightMin,leftMax+rightMin)
        if exp[k]=='*':
                if state==1:
                    value+=max(leftMin*rightMax,leftMax*rightMax,leftMin*rightMin,leftMax*rightMin)
                else :
                    value+=min(leftMin*rightMax,leftMax*rightMax,leftMin*rightMin,leftMax*rightMin)
        if exp[k]=='/':
            if state==1:
                value+=max(leftMin*rightMax,leftMax*rightMax,leftMin*rightMin,leftMax*rightMin)
            else :
                value+=min(leftMin*rightMax,leftMax*rightMax,leftMin*rightMin,leftMax*rightMin)
        return value


print(solve(expression,0,j,1))
