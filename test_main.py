from main import *

def test_one():
  """ done. """
  assert myfunction('Hello') == 'reversed: olleH'
  assert myfunction(1) == 3
  assert myfunction(6) == 8

def test_two():
  assert myfunction(3) == 5
  assert myfunction('abc123')== 'length: 6'
