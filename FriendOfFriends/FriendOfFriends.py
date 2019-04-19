#!/bin
from os import system
system('clear')

# FUNCTION FOR UNIQUE FRIENDS IN LISTS
def friend_of_friends(*args):
  for databag in range(len(args)):
    pass
  return args

# MAIN FUNCTION
if __name__ == '__main__':
  # LIST OF FRIENDS
  '''
  Jack=['James','Barbosa','DavyJones','Gibbs']
  Bill=['Jack','Gibbs','Bootstrap','DavyJones']
  Elizebeth=['Bill','Bootstrap','Speck','Burt']
  '''
  dict1 = {'Jack':['James','Barbosa','DavyJones','Gibbs']}
  dict2 = {'Bill':['Jack','Gibbs','Bootstrap','DavyJones']}
  dict3 = {'Elizebeth':['Bill','Bootstrap','Speck','Burt']}

  result=friend_of_friends(dict1,dict2,dict3)
  print(result)
  '''
  suggest_friends = Bill
  suggestion_list = []
  for friend in result:
    if friend not in suggest_friends:
      suggestion_list.append(friend)
  pop_user=suggestion_list.index('Bill')
  suggestion_list.pop(int(pop_user))
  print("Suggesting friends for Bill: ")
  print(suggestion_list)
  '''