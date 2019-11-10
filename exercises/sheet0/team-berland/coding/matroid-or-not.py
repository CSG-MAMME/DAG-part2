import sys
import time

def matroid_or_not(file_path):
  matroid = set() # List of matroids

  file = open(file_path, "r")
  for line in file:
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

  for mask1 in matroid:
    for mask2 in matroid:
      base1 = get_base(mask1)
      base2 = get_base(mask2)

      for x in base1:
        if x not in base2:
          for y in base2:
            if y not in base1:
              if mask1 + 2**y - 2**x in matroids:
                break
          else:
            return False
  return True

path = "../../matroid-or-not/"

if __name__ == "__main__":
  for line in sys.stdin:
    for file in line.split():
      file_path = path + file
      print("Opening file ", file)
      start = time.time()
      print(matroid_or_not(file_path))
      print("Checked file", file, "in", time.time() - start, "s.")
