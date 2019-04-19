#!/usr/bin/python
from os import system
#system('clear')

# FUNCTION FOR UNIQUE FRIENDS IN LISTS
def friends_of_friends(person,person_friends,all_friends):
  suggestions=[]
  for friends in all_friends[person]:
    if friends in all_friends.keys():
      for friend in all_friends[friends]:
        suggestions.append(friend)
  for items in range(len(suggestions)):
    if person in suggestions:
      suggestions.pop(suggestions.index(person))
    if friend in person_friends:
      if friend in suggestions:
        suggestions.pop(suggestions.index(friend))
  return suggestions

# MAIN FUNCTION
if __name__ == '__main__':

  A = input("Enter A's friends(csv format): ").split(',')
  B = input("Enter B's friends(csv format): ").split(',')
  C = input("Enter C's friends(csv format): ").split(',')
  '''
  A=['B','R','T','J']
  B=['C','A','F','J']
  C=['B','I','P','F']
  '''
  all_friends = {}

  all_friends['A']=[value.strip(' ') for value in A]
  all_friends['B']=[value.strip(' ') for value in B]
  all_friends['C']=[value.strip(' ') for value in C]

  for person in all_friends.keys():
    print('\nFriend suggestions for {}: '.format(person), end='')
    suggestions=friends_of_friends(person,all_friends[person],all_friends)
    print(suggestions)