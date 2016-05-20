#!/usr/bin/python3

def pancakes():
  with open("B-large-practice.in") as arq:

    qtd_casos = int(arq.readline())

    for i in range(1, qtd_casos + 1):

      # Each line is a pancake stack
      stack = arq.readline()

      # We must track the number of flips required
      # to make every happy face upwards
      flips = 0

      # The state of the first pancake topping
      first_topping = stack[0]

      # For each subsequent pancake, we must flip the stack
      # If a pancake is different the the top pancake a flip is required
      # and we need to update the topping state
      for idx in range(1, len(stack)):
        if stack[idx] != current:
          flips += 1
          first_topping = stack[idx]
      
      # Finally, if the topping smile face is downwards
      # One more flip is required so that the entire stack is upwards
      if first_topping == "-":
        flips += 1

      logging.info("Case #%d: %d" % (i, flips))


if __name__ == '__main__':

  print("Algorithm output:")
  import logging
  logging.basicConfig(level = logging.DEBUG, format = '%(message)s')
  pancakes()
  
  print("Algorithm execution time in seconds:")
  logging.disable(logging.CRITICAL)
  import timeit
  print(timeit.timeit("pancakes()", setup="from __main__ import pancakes", number = 1000))