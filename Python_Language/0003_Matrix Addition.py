m_rows,n_columns = input().split() 
m_rows,n_columns = int(m_rows),int(n_columns) 
matrix_1,matrix_2,matrix_sum = [] ,[] , []
for i in range(2*(m_rows)):  
    a = []
    a = list(map(int, input().split()))
    if i < m_rows:
        matrix_1.append(a)
    elif i <= 2*m_rows:
        matrix_2.append(a)
for i in range(m_rows):
    a = []
    for j in range((n_columns)):
        a.append(matrix_1[i][j] + matrix_2[i][j]) 
    matrix_sum.append(a)
for i in range(m_rows):
    for j in range(n_columns):
        print(matrix_sum[i][j],end=' ')
    print()