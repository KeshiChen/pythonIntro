# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
#
# fib(6);

def fib_generator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'

g = fib_generator(6);

x = next(g);
print(x)
x = next(g);
print(x);
x = next(g);
print(x);
x = next(g);
print(x);
x = next(g);
print(x);
