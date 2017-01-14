# Stack & Queue
from collections import  deque
import math


def help_func(stack):
    min1 = stack[0]
    for i in range(len(stack)):
        min1 = min(min1, stack[i])
    stack.remove(min1)
    return min1


def rearrange(queue, stack):
    while len(stack) is not 0:
        queue.append(help_func(stack))
    while len(queue) is not 0:
        stack.append(queue.popleft())
    return stack


stack = [5, 3, 1, 2, 4]
queue = deque([])
print rearrange(queue, stack)











