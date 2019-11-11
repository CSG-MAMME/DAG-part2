#!/usr/bin/env python3
import sys
import time

def matroid_or_not(file_path):
    matroid = set() # List of matroids

    file_h = open(file_path, "r")
    for line in file_h:
        if line[0] == '#': # Ignore commented lines
            continue
        # Build mask, and check that all the values
        # in the input are between 0 and 31
        base_mask = 0
        for val_str in line.split():
            val = int(val_str)
            assert(val >= 0 and val < 32)
            base_mask = base_mask + 2**val
        matroid.add(base_mask)

    # Converts from mask to base
    def get_base(mask):
        base = []
        p = 0
        while mask > 0:
            if mask % 2 == 1:
                base.append(p)
            mask = mask//2
            p += 1
        return base

    for mask1 in matroid: # For each B1 (in mask form) of the set of matroids
        for mask2 in matroid: # For each B2 (in mask form) of the set of matroids
            base1 = get_base(mask1) # Get B1 as a base
            base2 = get_base(mask2) # Get B2 as a base
            for x in base1: 
                if x not in base2: # if x belongs to B1 \ B2
                    for y in base2:
                        if y not in base1: # if y belongs to B2 \ B1
                            if mask1 + 2**y - 2**x in matroid: # Check if B1 \ {x} U {y} is a base
                                break
                    else: # If no such y exists, then we do not have a matroid
                        return False
    return True

"""
To solve this problem using Python we use the same masks approach, but being
more careful on how bitwise operations are handled (i.e. we manually play with
the powers of 2.
"""
if __name__ == "__main__":
    path = "../../matroid-or-not/"
    out_str = "\n---------- Python3 ----------\n"
    results = {}
    for line in sys.stdin:
        for file_name in line.split():
            file_path = path + file_name
            info_str = "Opening file {}\n".format(file_name)
            print(info_str, "(be patient, the program might take some time)")
            start = time.time()
            out_str += "{}\n".format(matroid_or_not(file_path))
            elapsed_time = time.time() - start
            out_str += "Checked file {} in {:.3f} s.\n".format(file_name, 
                    elapsed_time)
            results[file_name] = elapsed_time
    with open("results.txt", "a") as f:
        f.write(out_str)
    with open("py3.dat", "w") as f:
        for k,v in [(k, results[k]) for k in sorted(results, key=results.get)]:
            f.write("{} {}\n".format(k, v))
