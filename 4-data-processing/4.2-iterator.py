# test delay of "for loop" and lazy computation
# 
#

import time

def generated_list():
    i = 0 
    while True:
        i += 1
        print("i in generateor:", i)
        yield i 

if __name__ == "__main__":
    generated = generated_list()
    for i in generated:
        print("i in main", i)
        time.sleep(1)
