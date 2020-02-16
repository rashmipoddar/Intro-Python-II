class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description

  def on_take(self):
    print(f'item taken - {self.name}')

  def on_drop(self):
    print(f'item dropped - {self.name}')