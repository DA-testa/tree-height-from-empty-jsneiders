# python3
# Autors: Kristiāns Šneiders 221RDB042
import sys
import threading
import numpy as np


def compute_height(n, parents):
    parents = np.array(parents)
    depth = np.zeros(n, dtype=int)

    def compute_depth(node):
        if (depth[node] != 0):
            return depth[node]
        if (parents[node] == -1):
            depth[node] = 1
        else:
            depth[node] = 1 + compute_depth(parents[node])
        return depth[node]
    
    for i in range(n):
        compute_depth(i)

    return np.max(depth)
def main():
    choice = input("Enter F or I: ")
    choice = choice.upper()
    if (choice == "I" ):
        n = int(input("Count: "))
        parents = list(map(int, input("Nodes: ").split()))
        height = compute_height(n, parents)
    elif (choice == "F"):
        test_number = input("Enter a number from 1 to 25: ")
        with open(f"test/{test_number}", "r") as file:
            n = int(file.readline().strip())
            parents = list(map(int, file.readline().strip().split()))
            height = compute_height(n, parents)
    else: height = "Error"

    print(height)

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)
threading.Thread(target=main).start()
