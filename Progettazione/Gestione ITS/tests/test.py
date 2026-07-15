class MyClass:

  def __init__(self, v:str):
    self.v = v

  def __hash__(self) -> int:
    return hash(self.v)