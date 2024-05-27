#  Syntax
  tpl = ('item1', 'item2', 'item3','item4')
  all_items = tpl[0:4]         # all items
  all_items = tpl[0:]         # all items
  middle_two_items = tpl[1:3]  # does not include item at index 3

  fruits = ('banana', 'orange', 'mango', 'lemon')
  all_fruits = fruits[0:4]    # all items
  all_fruits= fruits[0:]      # all items
  orange_mango = fruits[1:3]  # doesn't include item at index 3
  orange_to_the_rest = fruits[1:]


# - Range of Negative Indexes


  # Syntax
  tpl = ('item1', 'item2', 'item3','item4')
  all_items = tpl[-4:]         # all items
  middle_two_items = tpl[-3:-1]  # does not include item at index 3 (-1)

  fruits = ('banana', 'orange', 'mango', 'lemon')
  all_fruits = fruits[-4:]    # all items
  orange_mango = fruits[-3:-1]  # doesn't include item at index 3
  orange_to_the_rest = fruits[-3:]
  