# - Creating an empty set
# syntax
# st = set()


#add new item on set
st = {'item1', 'item2', 'item3', 'item4'}
print(st.add('item5'))

st = {'item1', 'item2', 'item3', 'item4'}
print(st.update(['item5','item6','item7']))


st = {'item1', 'item2', 'item3', 'item4'}
print(st.remove('item2'))

fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits.pop())  # removes a random item from the set



st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
print(st1.update(st2)) # st2 contents are added to st1




### Exercises: Level 2

# 1. Join A and B
# 1. Find A intersection B
# 1. Is A subset of B
# 1. Are A and B disjoint sets
# 1. Join A with B and B with A
# 1. What is the symmetric difference between A and B
# 1. Delete the sets completely