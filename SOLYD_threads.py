# # Código sem threading

# def inst1():
#     x = 0
#     while x < 10:
#         print('X: ', x)
#         x += 1

# def inst2():
#     y = 0
#     while y < 10:
#         print('Y: ', y)
#         y += 1
    
# inst1()
# inst2()

# Código com threading

import threading

def inst1():
    x = 0
    while x < 10:
        print('X: ', x)
        x += 1

def inst2():
    y = 0
    while y < 10:
        print('Y: ', y)
        y += 1
    
ast = threading.Thread(target=inst1).start()
inst2()