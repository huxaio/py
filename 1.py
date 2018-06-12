class FooClass(object):
  """my very first class: FooClass"""
  version = 0.1 # class (data) attribute
  def _init_(self, nm='John Doe'):
    """constructor"""
    self.name = nm # class instance (data)
    print("Created",nm)
fool = FooClass()
print("ok")