# testy.py
# from signal import signal, alarm, SIGALRM

import sys
import time
from copy import deepcopy

# TIMER = False
TIMER = False
# RERAISE = False
RERAISE = True
ALLOWED_TIME = 1

if TIMER:
    from signal import SIGALRM, alarm, signal


# format testów
# problems = [ {"arg":arg0, "hint": hint0}, {"arg":arg1, "hint": hint1}, ... ]


def list2str(L):
    s = ""
    for x in L:
        s += str(x) + ", "
    s = s.strip()
    if len(s) > 0:
        s = s[:-1]
    return s


def limit(L, lim=120):
    x = str(L)
    if len(x) < lim:
        return x
    else:
        return x[:lim] + "[za dlugie]..."


class TimeOut(Exception):
    def __init__(self):
        pass


def timeout_handler(signum, frame):
    raise TimeOut()


def internal_runtests(printarg, printhint, printsol, check, problems, f):
    passed = 0
    wrong = 0
    timed_out = 0

    total = len(problems)
    total_time = 0

    for i, (name, data) in enumerate(problems.items(), start=1):
        print("-----------------")
        print(f"Test {i} - {name}")
        arg = deepcopy(data["arg"])
        hint = deepcopy(data["hint"])
        printarg(*arg)
        printhint(hint)
        try:
            if TIMER:
                signal(SIGALRM, timeout_handler)
                alarm(ALLOWED_TIME + 1)

            time_s = time.time()
            sol = f(*arg)
            time_e = time.time()

            if TIMER:
                alarm(0)

            printsol(sol)
            if check(*arg, hint, sol):
                passed += 1
            else:
                wrong += 1

            time_spent = float(time_e - time_s)
            print(f"Orientacyjny czas: {time_spent:.2f} sek.")
            total_time += time_spent
        except TimeOut:
            print("!!!!!!!! PRZEKROCZONY DOPUSZCZALNY CZAS")
            timed_out += 1
        except KeyboardInterrupt:
            print("Obliczenia przerwane przez operatora")
        except Exception as e:
            print("WYJATEK:", e)
            if RERAISE:
                raise e

    print("-----------------")
    print(
        f"Liczba zaliczonych testów: {passed}/{total} "
        f"(zle: {wrong}, timeout: {timed_out})"
    )
    print(f"Orientacyjny łączny czas : {total_time:.2f} sek.")

    solution_name = sys.argv[0].replace("_", " ").replace(".py", "")

    print(f"{solution_name} {passed} {total} {total_time:.2f}", file=sys.stderr)
