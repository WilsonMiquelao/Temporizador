import time

t = input("Digite o tempo em segundos: ")

if t.isdigit():
    t = int(t)
else:
    print("Entrada invalida")
    quit()

#120 / 60 = 2
#150 / 60 = 2 /30

while t != 0:   
    minutes, seconds = divmod(t,60)
    timer = "{:02d}:{:02d}".format(minutes, seconds)
    print(timer, end="\r")
    time.sleep(1)
    t = t - 1

print("Tempo acabou!")
