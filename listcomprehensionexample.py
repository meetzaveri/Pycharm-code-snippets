rows = range(1,4)
cols = range(1,3)
cells = [(row, col) for row in rows for col in cols]
print (cells)
for cell in cells:
 print(cell)
 break

word = ['letters',212,'letters',212,213]
print(word.count('letters'))