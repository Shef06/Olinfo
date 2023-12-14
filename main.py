import string

T = int(input())

for i in range(T):
    N = str(input())
    min = 0
    temp = 0
    if(int(N)%25!=0):
        if(N.count('2')>=1):
            if(N.count('5')>=1):
                if(N[len(N)-2] != '2'):
                    temp+=1
                else:
                    if (N[len(N) - 1] != '5'):
                        temp+=1

                if (N[len(N) - 1] != '5'):
                    temp+=1
            else:
              min = -1
            if (min != 0):
                if (temp<min):
                  min = temp
                if(min == -1):
                  min = temp
            elif(min == 0):
                min = temp
        if(N.count('7') >= 1):
            if (N.count('5') >= 1):
                if (N[len(N) - 2] != '7'):
                    temp += 1
                else:
                    if (N[len(N) - 1] != '5'):
                        temp += 1
            else:
                min = -1
            if (N[len(N) - 1] != '5'):
                temp += 1
            if (min != 0):
                if (temp < min):
                  min = temp
                if(min == -1):
                   min = temp
            elif (min == 0):
                min = temp
            else:
                min = -1
        if(N.count('0') >= 1):
            if (N.count('5') >= 1):
                if (N[len(N) - 2] != '5'):
                    temp += 1
                else:
                    if (N[len(N) - 1] != '0'):
                        temp += 1
                if (N[len(N) - 1] != '5'):
                    temp += 1
            elif(N.count('0')>=2):
                if (N[len(N) - 2] != '0'):
                    temp += 1
                else:
                    if (N[len(N) - 1] != '0'):
                        temp += 1
                if (N[len(N) - 1] != '0'):
                    temp += 1
            else:
              min = -1
            if (min != 0):
              if(min == -1):
                  min = temp
              if (temp < min):
                  min = temp
            elif (min == 0):
                min = temp
            else:
                min = -1

    print(min)