''' question:
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

Input Format

The first line contains . The second line contains an array   of  integers each separated by a space.

Constraints

Output Format

Print the runner-up score.

answer:
'''
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split(" "))
    k=list(arr)
    k.sort(reverse=True)
    maxim=max(k)
    i=0
    while True:
        if k[i] == maxim:
            i+=1
        else:
            print(k[i])
            break
