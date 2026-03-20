from ast import Return
import io
import math
import time

def is_prime(a : int):
  if a < 2:
 #   print("small than 2")
    return False
  if a == 2:
      return True
  if (a & 1) == 0:
 #     print("even")
      return False
  if a==3:
     return True
  if sum(int(d) for d in str(a)) % 3 == 0:
 #     print("Mult 3")
      return False

#test the first primes below 100
  prime_list = [5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
  for i in prime_list:
    if a == i:
      return True
    else:
      if a % i == 0:
        return False

  if a > 10609:
    for i in range (103,math.isqrt(a)+1,2):
 #   print(i)
        if a % i == 0:
#      print("found a", a, i)
            return False
  return True

# Re-write a more optimal version of prime detector


def main():
    tim_start = time.process_time()
    print(tim_start)
    value = int(input("Enter a value to check"))
    print ("%d value is prime: %d" % (value, is_prime(value)))
    tim_end = time.process_time()
    print("elapsed time ",tim_end - tim_start)
    print(tim_start, tim_end)

if __name__ == "__main__":
    main()
