'''In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints


Each character in the string is an ascii character.

Output Format

Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input

ABCDCDC
CDC
Sample Output

2
'''




def count_substring(string, sub_string):
    ssiz=len(string)
    sub=len(sub_string)
    if 1<=ssiz<= 200:
        co=0
        j=0
        for i in range(ssiz):
            check = string[j:j+sub]
            if check == sub_string:
                co+=1
                j+=1
            else:
                j+=1
    return co

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)


