''' program to implement min stack
 '''


#this is the implementation with O(n) complexity
"""
class stack:
    def __init__(self):
        self.stack=[]
        self.ss=[]
    def push(self,x):
        if self.ss==[] or x<= self.ss[-1]:
            self.ss.append(x)
            self.stack.append(x)
        else:
            self.stack.append(x)

    def pop(self):
        if self.ss[-1]== self.stack[-1]:
            self.ss.pop(-1)
        self.stack.pop(-1)

    def getMin(self):
        if self.stack==[]:
            print("stack empty")
        else:
            print(self.ss[-1])
st=stack()
st.push(8)
st.push(3)
st.getMin()
st.push(2)
st.getMin()
st.pop()
"""
"""
this is the implementation with O(1) complexity
"""
class stack:
    def __init__(self):
        self.stack=[]
        self.minele="empty"
    def push(self,x):
        if self.minele=="empty" :
            self.minele=x
            self.stack.append(x)
        else:
            if x>=self.minele:
                self.stack.append(x)
            else:
                xx=2*x- self.minele
                self.stack.append(xx)
                self.minele=x
    def pop(self):
        if self.stack[-1]>self.minele:
            self.stack.pop(-1)
        else:
            self.minele=2*self.minele-self.stack[-1]
            self.stack.pop(-1)
    def top(self):
        if self.stack==[]:
            print("empty stack")
        else:
            if self.stack[-1]< self.minele:
                return self.minele
            else:
                return self.stack[-1]
    def getMin(self):
        if self.stack==[]:
            print("stack empty")
        else:
            print(self.minele)

st=stack()
st.push(8)
st.push(3)
st.getMin()
st.push(2)
st.getMin()
st.getMin()
st.pop()
