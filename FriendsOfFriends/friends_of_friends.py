#!/usr/bin/python
import yaml
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
  with open('friends_list.yml','r') as stream:
    try:
      all_friends=yaml.safe_load(stream)
      all_friends=all_friends['friends_list']
    except yaml.YAMLError as ex:
      print(ex)
  person_name = input("Enter the name of person: ")
  if person_name in all_friends.keys():
    person_obj = Person()
    print('Friend suggestions for {}: '.format(person_name), end='')
    suggestions=person_obj.friends_of_friends(person_name,all_friends)
    print(suggestions)   
  else:
    print('Person does not exist in the list.')