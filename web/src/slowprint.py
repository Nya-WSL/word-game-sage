import sys
import time
import random

def slowprint_title(s):
    for c in s + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(random.random() * 0.06)

def slowprint_choose(s):
    for c in s + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(0.8)

def slowprint_text(s):
    for c in s + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(0.2)

def slowprint_1(s):
    for c in s + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(random.random() * 0.8)

def slowprint_a(s):
    for c in s + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(1)

def slowprint_end(s):
    for c in s + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(0.4)

def slowprint_end1(s):
    for c in s + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(random.random() * 2)