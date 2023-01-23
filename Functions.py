def say_hi():
    global s
    s = "I'm Varun I have started to learn coding"
    print(s)


s = " This is outside the function"
say_hi()

print(s)