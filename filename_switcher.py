import os, re

def switch(filename):
  """
  >>> switch('file.js.coffee')
  'file_spec.js.coffee'
  >>> switch('file_spec.js.coffee')
  'file.js.coffee'
  """
  if is_spec(filename):
    return remove_spec(filename)
  else:
    return add_spec(filename)

def is_spec(filename):
  """
  >>> is_spec('file.spec.js.coffee')
  True
  >>> is_spec('file_spec.js.coffee')
  True
  >>> is_spec('file_spec.coffee')
  True
  >>> is_spec('file.coffee')
  False
  """
  return re.search(r'[\._]spec\b', filename) is not None

def remove_spec(filename):
  """
  >>> remove_spec('file.spec.js.coffee')
  'file.js.coffee'
  >>> remove_spec('file_spec.js.coffee')
  'file.js.coffee'
  >>> remove_spec('file_spec.rb')
  'file.rb'
  """
  return re.sub(r'[\._]spec\b', '', filename)

def add_spec(filename, separator='_'):
  """
  >>> add_spec('file.js')
  'file_spec.js'
  >>> add_spec('file.js.coffee')
  'file_spec.js.coffee'
  >>> add_spec('file.js.coffee', '.')
  'file.spec.js.coffee'
  """
  return re.sub(r'\.', separator + 'spec.', filename, count=1)
