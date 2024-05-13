# String-Utility-Program

## Overview
This Python program provides a menu-driven interface for performing various operations on strings. Users can check if a string is a palindrome, print the reverse of the string, check if one string is present in another, print uncommon words between two strings, and perform right and left rotations on a string.

## Functions

### `space()`
- **Description**: Prints a decorative separator to enhance the readability of the output.

### `palindrome(a)`
- **Description**: Checks if the given string is a palindrome and prints the result.
- **Parameters**:
  - `a` (str): The string to check.

### `reverse(a)`
- **Description**: Prints the reverse order of each word in the given string.
- **Parameters**:
  - `a` (str): The string to reverse.

### `present(a, c)`
- **Description**: Checks if the words in the second string are present in the first string and prints "Present" if all words are found, otherwise prints "Absent".
- **Parameters**:
  - `a` (str): The main string to check against.
  - `c` (str): The string containing words to check for presence in the main string.

### `uncommon(a, c)`
- **Description**: Prints the words that are present in the first string but not in the second string.
- **Parameters**:
  - `a` (str): The main string.
  - `c` (str): The string to compare against.

### `rightrotation(a, d)`
- **Description**: Prints the right rotation of the string by `d` characters.
- **Parameters**:
  - `a` (str): The string to rotate.
  - `d` (int): The number of characters to rotate.

### `leftrotation(a, d)`
- **Description**: Prints the left rotation of the string by `d` characters.
- **Parameters**:
  - `a` (str): The string to rotate.
  - `d` (int): The number of characters to rotate.

## Menu Options

1. **Check Palindrome**:
   - Prompts the user to input a string.
   - Checks if the string is a palindrome and prints the result.

2. **Print Reverse of the String**:
   - Prompts the user to input a string.
   - Prints the reverse of each word in the string.

3. **Check String Presence**:
   - Prompts the user to input two strings.
   - Checks if the words in the second string are present in the first string and prints "Present" or "Absent".

4. **Print Uncommon Words**:
   - Prompts the user to input two strings.
   - Prints the words that are present in the first string but not in the second string.

5. **Print Right and Left Rotation**:
   - Prompts the user to input a string and a number.
   - Prints the right and left rotation of the string by the given number of characters.

6. **Exit the Program**:
   - Exits the program.

## How to Run the Program

1. Run the script.
2. Follow the on-screen menu options.
3. Enter your choice (1-6) and input the required values as prompted.
4. The program will continue to prompt for input until you choose to exit by entering 6.
