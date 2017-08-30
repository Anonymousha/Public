#!/usr/bin/python
#Author: EITENNE

import random

def main():
  first = random.randint(1,9)
  second = random.randint(1,9)
  third = random.randint(1,9)
  four = random.randint(1,9)
  fith = random.randint(1,9)

  digit = ['601','514','557','526','379','142','590','307','419','216']

  start = random.choice(digit)
  print'Phone number: %s-%s%s-%s%s%s' % (start,first,second,third,four,fith)

main()
