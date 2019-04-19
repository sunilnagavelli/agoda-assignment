#!/bin/sh
from os import system
system('clear')

# FUNCTION FOR UNIQUE FRIENDS IN LISTS
def friend_of_friends(*args):
  friend_suggestion = []
  collated_list = []
  for mylist in args:
    collated_list += mylist
  friend_suggestion=set(collated_list)
  return list(friend_suggestion)

def suggest_friends(person):
  suggestion_list = []
  for friend in result:
    if friend not in person:
      suggestion_list.append(friend)
      pop_user=suggestion_list.index(person)
      suggestion_list.pop(int(pop_user))
    print("Suggesting friends for {}: ".format(person))
    print(suggestion_list)

# MAIN FUNCTION
if __name__ == '__main__':

  # LIST OF FRIENDS
  Jack=['James','Bill','Jon']
  Bill=['Jack','DavyJones','Ned']
  Elizebeth=['Bill','Hector','Daenerys']
  
  # LOGIC
  result=friend_of_friends(Jack,Bill,Elizebeth)
  person = Bill
  suggest_friends(person)
  