data ={'G':'C','C':'G','T':'A','A':'U'}

res=''

for i in input():
    if i == 'G' or i == 'C' or i == 'T' or i == 'A':
        res = res+data[i]
    else:
        res='Invalid Input'
        break

print(res)