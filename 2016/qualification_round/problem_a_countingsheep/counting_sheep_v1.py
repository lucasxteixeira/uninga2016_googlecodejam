#!/usr/bin/python3

def counting_sheep():
  with open("A-large-practice.in") as arq:

    qtd_casos = int(arq.readline())

    for i in range(1, qtd_casos + 1):
      n = int(arq.readline())
      vistos = []

      if n == 0:
        logging.info("Case #%d: INSOMNIA" % i)
        continue

      for x in range(1, 100):
        n_str = str(x * n)
        for char in n_str:
          if char not in vistos:
            vistos.append(char)
            if len(vistos) == 10:
              logging.info("Case #%d: %d" % (i, x * n))

      if len(vistos) < 10:
        logging.info("Case #%d: INSOMNIA" % i)


if __name__ == '__main__':

  print("Algorithm output:")
  import logging
  logging.basicConfig(level = logging.DEBUG, format = '%(message)s')
  counting_sheep()
  
  print("Algorithm execution time in seconds:")
  logging.disable(logging.CRITICAL)
  import timeit
  print(timeit.timeit("counting_sheep()", setup="from __main__ import counting_sheep", number = 1000))