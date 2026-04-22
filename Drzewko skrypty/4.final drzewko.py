#!/bin/python3
import os
import random
import time


def pr(arg):
    print(arg, end="\t")


class Node:
    def __init__(self, data, level=0, offset=0):
        self.left = None
        self.right = None
        self.data = data
        self.level = level
        self.offset = offset

    def insert_new(self, data):
        current = self
        while True:
            if data < current.data:
                # lewo
                if current.left is None:
                    current.left = Node(data, current.level + 1, current.offset - 1)
                    break
                else:
                    current = current.left
            else:
                # prawo
                if current.right is None:
                    current.right = Node(data, current.level + 1, current.offset + 1)
                    break
                else:
                    current = current.right

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

    def get_sum(self):
        total = self.data
        if self.left is not None:
            total += self.left.get_sum()
        if self.right is not None:
            total += self.right.get_sum()
        return total

    def get_even_sum(self):
        total = self.data if self.data % 2 == 0 else 0
        if self.left is not None:
            total += self.left.get_even_sum()
        if self.right is not None:
            total += self.right.get_even_sum()
        return total

    # NOWA, CZYTELNA FUNKCJA RYSOWANIA DRZEWA (STYL FOLDERÓW)
    def draw_tree_pretty(self, prefix="", is_last=True, is_root=True, side="ROOT"):
        # Wypisywanie korzenia wygląda odrobinę inaczej niż reszta gałęzi
        if is_root:
            print(f"[{self.data}] (L:{self.level}, X:{self.offset})")
            new_prefix = ""
        else:
            # Wybieramy odpowiedni "łącznik" w zależności od tego, czy to ostatnie dziecko węzła
            connector = "└── " if is_last else "├── "
            print(prefix + connector + f"{side}: [{self.data}] (L:{self.level}, X:{self.offset})")
            # Ustalamy przedrostek dla kolejnych poziomów (dodajemy pionową kreskę lub spację)
            new_prefix = prefix + ("    " if is_last else "│   ")

        # Zbieramy dzieci do listy, aby wiedzieć, które jest ostatnie
        children = []
        if self.left is not None:
            children.append((self.left, "L"))
        if self.right is not None:
            children.append((self.right, "R"))

        # Rekurencyjne wywoływanie dla każdego dziecka
        for i, (child, child_side) in enumerate(children):
            is_child_last = (i == len(children) - 1)
            child.draw_tree_pretty(new_prefix, is_child_last, False, child_side)


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

    root = Node(12)
    r = random

    for j in range(0, 10):
        root.insert_new(r.randint(0, 100))

    print("\n--- GRAFICZNA WIZUALIZACJA DRZEWA ---")
    root.draw_tree_pretty()
    print("-" * 50)

    print("\nPosortowane elementy (PrintTree):")
    root.PrintTree()

    print(f"\n\n---> Suma wszystkich wartości w drzewie: {root.get_sum()}")
    print(f"---> Suma elementów parzystych: {root.get_even_sum()}")

    print(flush=True)
    time.sleep(dt * ms)