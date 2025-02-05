"""
Given names and grades of students in a class, store them in a nested list 
and print the names of any students having the second lowest grade.

If there are multiple students with the second lowest grade, order their names alphabetically.

Input:
- First line: integer N, number of students.
- Next N lines: each contains a student's name and grade.

Constraints:
- There will always be one or more students having the second lowest grade.

Output:
- Print name(s) of students with the second lowest grade, ordered alphabetically.

Sample Input:
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Sample Output:
Berry
Harry
"""



def order_grades(name, score, records):
    
    records.append([name, score])

def get_low_grades(records):
     
    sorted_records = sorted(records, key=lambda x: x[1])
    
    all_scores = [i[1] for i in sorted_records ]
    
    second_lowest_grade = list(set(all_scores))[1]
    
    names = [i[0] for i in sorted_records if i[1] == second_lowest_grade]
    
    names.sort()
    for name in names:
        print(name)
    return
    
    

    

if __name__ == '__main__':
    records = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        order_grades(name,score,records)
        
        
    get_low_grades(records)
    
        
