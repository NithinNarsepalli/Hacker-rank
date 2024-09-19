'''
Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

Function Description

Complete the split_and_join function in the editor below.

split_and_join has the following parameters:

string line: a string of space-separated words
Returns

string: the resulting string
Input Format
The one line contains a string consisting of space separated words.

Sample Input

this is a string   
Sample Output

this-is-a-string

'''
def split_and_join(line):
    # write your code here
    sp = line.split(" ")
    return join(sp)
    
def join(sp):
    res=sp[0]
    for i in range(1, len(sp)):
        res +="-" + sp[i]
    return res
        
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
