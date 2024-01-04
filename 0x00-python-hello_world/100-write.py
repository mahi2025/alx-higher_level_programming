#!/usr/bin/bash/python3
  2 
  3 import sys
  4 
  5 def p_stderr(message):
  6 sys.stderr.write(message + '\n')
  7 
  8 if _name_ == '__main__':
  9         message = 'and that piece of art is useful - Dora K    orpar, 2015-10-19'
 10 p_stderr(message)
 11 sys.exit(1) 
