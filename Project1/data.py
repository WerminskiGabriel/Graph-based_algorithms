from pathlib import Path

from testy import *


def read_problem(name):
    path = Path("problems") / name
    items = []

    with Path(path).open() as f:
        solution = int(f.readline().strip())

        while line := f.readline().strip():
            d, luck = map(int, line.split())
            items.append((d, luck))

    return {"arg": [items], "hint": solution}


files = [
    "simple-1",
    "simple-2",
    "primes-const-1",
    "primes-const-2",
    "primes-const-3",
    "primes-rand-close-1",
    "primes-rand-close-2",
    "primes-rand-close-3",
    "primes-rand-close-4",
    "primes-rand-close-5",
    "prime-powers-1",
    "prime-powers-2",
    "prime-powers-3",
    "prime-powers-4",
    *[f"random-{k}" for k in range(1, 43)],
]

problems = {name: read_problem(f"{name}") for name in files}


def printarg(scores):
    print(f"{len(scores)} dzielnikow")


def printhint(hint):
    print("Wynik: {}".format(hint))


def printsol(sol):
    print("Uzyskany wynik: {}".format(sol))


def check(scores, hint, sol):
    if hint == sol:
        print("Test zaliczony")
        return True
    else:
        print("NIEZALICZONY!")
        return False


def runtests(f):
    internal_runtests(printarg, printhint, printsol, check, problems, f)
