from os import system

system('clear')

def color_code(color_name):
  param='\033[0;'
  colors={'red':param+"31m",'green':param+"32m",'yellow':param+"33m",
    'blue':param+"34m",'magenta':param+"35m",'cyan':param+"36m",'none':param+"m"}
  return colors[color_name]

def check_palindrome(input):
  input = input.replace(" ","").lower()
  result = True
  length = len(input)
  left = 0
  right = length - 1
  while(left < right):
    if input[left] in special_chars:
      left = left + 1
    if input[right] in special_chars:
      right = right - 1
    if input[left] in special_chars or input[right] in special_chars:
      continue
    if input[left] != input[right]:
      result = False
      return result
    left += 1
    right -= 1
  return result

def main():
  print(color_code('yellow')+"Enter a string: "+color_code('none'), end='')
  input_str = input()
  if len(input_str) > 1:
    result = check_palindrome(input_str)
    print(color_code('green')+"Palindrome"+color_code('none') if result else color_code('red')+"Not a Palindrome"+color_code('none'))
  else:
    count = 1
    while(count <= 3):
      print("Try again, Enter a string: ", end='')
      input_str = input()
      if len(input_str) > 1:
        result = check_palindrome(input_str)
        print("Palindrome" if result else "Not a Palindrome")
        break
      count += count
  quit_program()

def quit_program():
  Ans = input("Do you want check another string? (y/n) ")
  if (Ans == 'y'):
    main()
  else:
    exit()

if __name__ == '__main__':
  global special_chars 
  special_chars = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789"
  main()
        
#print(check_palindrome("Delia's debonair dahlias, poor, drop, or droop. Sail, Hadrian; Obed sailed"))
