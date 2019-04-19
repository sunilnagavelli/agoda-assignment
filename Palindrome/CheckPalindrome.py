import re

def CheckPalindrome(input):
  #input = input.replace(" ","")
  input = re.sub('[\s+]', '', input)
  result = True
  length = len(input)
  left = 0
  right = length - 1
  while(left < right):
    if input[left] in specialchars:
        left = left + 1
    if input[right] in specialchars:
        right = right - 1
    if input[left].lower() != input[right].lower():
        result = False
        return result
    left += 1
    right -= 1
  return result

def main():
  print("Enter a string: ", end='')
  input_str = input()
  if len(input_str) > 1:
    result = CheckPalindrome(input_str)
    print("Palindrome" if result else "Not a Palindrome")
  else:
    count = 1
    while(count <= 3):
      print("Try again, Enter a string: ", end='')
      input_str = input()
      if len(input_str) > 1:
        result = CheckPalindrome(input_str)
        print("Palindrome" if result else "Not a Palindrome")
        break
      count += count

if __name__ == '__main__':
  global specialchars
  specialchars = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~0123456789"
  main()

#print(CheckPalindrome("Delia's debonair dahlias, poor, drop, or droop. Sail, Hadrian; Obed sailed"))
