#!/bin/python3
import os
import random
import time


def pr(arg):
    print(arg, end="\t")


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    """
    def insert(self, data):
        # Compare the new value with the parent node
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data """ #stary sposób wstawiania danych do drzewa

    def insert_new(self, data):
        current = self
        while True:
            if data < current.data:
                # lewo
                if current.left is None:
                    current.left = Node(data)
                    break
                else:
                    current = current.left
            else:
                # prawo
                if current.right is None:
                    current.right = Node(data)
                    break
                else:
                    current = current.right

    # Print the tree
    def PrintTree(self):
        stack = []
        current = self
        while stack or current:
            while current:
                stack.append(current)
                current = current.left
            current = stack.pop()
            pr(current.data)
            current = current.right

total = 140
abc = 321

ms = 0.001
dt = 100

for i in range(0, total + 1):

    print(os.popen("cls & echo GO:").read())

    print(time.time())
    act_time = time.localtime()
    print(time.strftime('%Y-%m-%d %H:%M:%S', act_time))
    print('_' * i + 'X' + (total - i) * '-')
    print('_' * i + str(i) + (total - i) * '-')
    # print(chr(27) + "[2J")

    root = Node(12)
    r = random

    # Zmieniono 'i' na 'j', aby nie nadpisywać zmiennej z pętli głównej
    for j in range(0, 50):
        root.insert_new(r.randint(0, 100))

    root.PrintTree()
    print(flush=True)
    time.sleep(dt * ms)




