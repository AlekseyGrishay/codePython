print("Hello, I'm Eva!")
print("And what is your name?")
name = input()
print("Nice to meet you, ", name)
print("How old are you?")
old = int(input())
if old < 18:
    print("Some young :)")
elif 50 > old >= 18:
    print("Adult")
else:
    print("Very old for this game :/")