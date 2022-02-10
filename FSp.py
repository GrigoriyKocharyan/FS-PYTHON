def run():
    if "print(" in code1:
        if code1[-1] == ')':
            for i in range(6,len(code1)-1,1):
                print((code1[i]),end='')
    if "input(" in code1:
        if code1[-1] == ')':
            for s in range(6,len(code1) - 1,1):
                print((code1[s]),end='')
            print('')
            a = input()
            print(a)


while True:
    code1 = input(">>> ")
    run()
    print('')