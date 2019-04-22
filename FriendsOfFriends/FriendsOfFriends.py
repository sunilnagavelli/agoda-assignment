#!/usr/bin/python
from os import system
#system('clear')

class Person():
  # FUNCTION FOR UNIQUE FRIENDS IN LISTS
  def friends_of_friends(self,person,all_friends):
    suggestions=[]
    person_friends = all_friends[person]
    for friend in person_friends:
      if friend in all_friends.keys():
        for second_friend in all_friends[friend]:
          suggestions.append(second_friend)
          if person in suggestions:
            suggestions.pop(suggestions.index(person))
    suggestions = list(set(suggestions) - set(person_friends))
    return suggestions

# MAIN FUNCTION
if __name__ == '__main__':

  A = input("Enter A's friends(csv format): ").split(',')
  B = input("Enter B's friends(csv format): ").split(',')
  C = input("Enter C's friends(csv format): ").split(',')

  all_friends = {
    "A": A,
    "B": B,
    "C": C
  }
  
  person_obj = Person()
  for person in all_friends.keys():
    print('\nFriend suggestions for {}: '.format(person), end='')
    suggestions=person_obj.friends_of_friends(person,all_friends)
    print(suggestions)
