import os, sys
import multiprocessing
import time
from random import shuffle

newstdin = os.fdopen(os.dup(sys.stdin.fileno()))

def popup_words(level, stdin = newstdin):
    with open("word-list/%s" %(level)) as f:
        words = f.readlines()
        shuffle(words)
        
        correct_n = 0
        total = 0
        
        for word in words:
            print "%s   %s   %s" %("*" * 10, word.strip(), "*"*10)
            print("Y as CORRECT , Others as SKIP")
            result = stdin.readline()
            if result.strip() == "y":
                correct_n += 1
            total += 1

            with open("temp", "w") as tempf:
                tempf.write("%d / %d" %(correct_n, total))

            word = f.readline()
                
main = multiprocessing.Process(target=popup_words, args = ("easy", ))

main.start()

timeout = 90
time.sleep(timeout)

main.terminate()

with open("temp", "r") as tempf:
    print "Result:"
    print tempf.read()
