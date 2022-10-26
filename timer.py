import time

print('Bem-Vindo ao seu pomodoro!')


# define a condição timer
def countdown(t):

    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1


# escolher intervalos
t = input("Escolha a duração do seu pomodoro: ")

# retornando a função
print('Seu pomodoro começou:')
print("------getTime()--------")
countdown(int(t))
