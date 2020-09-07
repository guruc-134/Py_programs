N = int(input())
answer=list()
for i in range(12):
    str=input()
    commands=str.split()
    if commands[0] == "insert":
        answer.insert(int(commands[1]),int(commands[2]))
    elif commands[0] == "print":
        print(answer)
    elif commands[0] == "remove":
        answer.remove(int(commands[1]))
    elif commands[0] == "append":
        answer.append(int(commands[1]))
    elif commands[0] == "sort":
        answer.sort()
    elif commands[0] == "reverse":
        answer.reverse()
    elif commands[0] == "pop":
        answer.pop()
