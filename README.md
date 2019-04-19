# [](https://www.agoda.com)<img align="center" width="120" height="40" src="https://cdn6.agoda.net/images/MVC/default/agoda-logo.svg?sanitize=true&raw=true"/> Coding Assignment


## 1. Friend Of Friends

Implement a method in a Person class below to return their friends of friends (or 2nd-degree network -
in LinkedIn terminology).

Example: B is A's friend. C is B's friend. Therefore C is A's friend of friends. (A) --> B --> C
```java
  class Person {
    String name List<Person> friends
    List<Person> friendsOfFriends() {
    //Implement Me
    }
  }
```
Note
* Rewrite the Person class in your language that you choose. And implement the method with test
cases.
* Provide a Dockerfile for your solution.
* Friends are 2 ways relationship. If B is A's friend, then A is also B's friend. Does your
implementation correctly handle this fact?
• A's friends should never be shown up as A's friends of friends. Are there any case in your
implementation that might happen?

### Solution:

The programming language choosen for this solution is Python, The code can be viewed from the following file FriendsOfFriends.py

#### Steps to run

-----

## 2. Modified Palindrome
  A palindrome is a word that read the same in both direction
  * Example (Palindrome): eye, madam, racecar, noon
  * Example (Not Palindrome): test, abc, anything

Implement a modified palindrome, where it is case insensitive and ignore any non-alphanumeric
characters
Example Modified Palindrome:
• _!E#@y#e
• MaDaM!!
• RaCEC@A@R
```java
boolean isPalindrome(String word) {
//Implement Me
}
```
Note
* Rewrite the isPalindrome method in the language that you choose with test cases.
* Provide a Dockerfile for your solution.
* If the string is very long (e.g. 1-billion characters). Is your implementation still efficient?

### Solution:

The programming language choosen for this solution is Python, The code can be viewed from the following file ModifiedPalindrome.py

#### Steps to run

1. Once you check out the repo, Please open the change dir to the Palindrome folder
2. The Dockerfile provided in this folder will help you to create an image and run the container, Below are the commands to do so.
  ```
  docker build --tag sunilnagavelli/modifiedpalindrome:latest

  ```
3. Now run the docker file with below command
```
docker run --tty --interactive --name palindrome-check sunilnagavelli/palindromecheck:latest
```
4. At the prompt, Please enter your string to check if it is a palindrome or not

Example:
```bash
[sunil@macpro]$ docker run -ti --name palindrome-check sunilnagavelli/palindromecheck:latest
root@127d1a956cc3:/usr/src/app# 
Enter a string: De@lia's de*bonair d~ahlias, poor, d%rop, or dr&oop. Sail, H(adrian; Obe#d s$ailed
Palindrome
```
=======
