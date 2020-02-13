class Item:
  def __init__(self, name, description):
    self.name = name
    self.description = description

  def on_take():
    print('item taken')

  def on_drop():
    print('item dropped')