# encoding:gbk
#!/usr/bin/env python
from fractions import Fraction


def print_matrix(info, A):  #��ʽ���������
    print info
    for i in range(len(A)):
        for j in range(len(A[i])):
            if j == len(A[i]):
                print "|",
            print '%6.4f' % A[i][j], 
        print
    print


def swap_line(A,line1, line2):
    for i in range(len(A[line1])):
        A[line1][i],A[line2][i] = A[line2][i],A[line1][i]


  
  
def gauss(A):
    rown = len(A)
    if rown == 0:
        return False
    coln = len(A[0])
    cur_row, cur_col = 0, 0

    while cur_row < rown and cur_col < coln-1:
        #ѡ��Ԫ
        pivot = A[cur_row][cur_col]
        pindex = cur_row

        for i in range(cur_row, len(A)):
            if abs(A[i][cur_col]) > abs(pivot):
                pivot = A[i][cur_col]
                pindex = i
        print_matrix("ѡ��Ԫ", A)


        if pivot == 0: #��һ�������Ѿ�ȫ��
            cur_col += 1
            continue


        #����Ԫ������ǰ��
        if pindex != cur_row:
            swap_line(A,pindex,cur_row)
        print_matrix("����Ԫ����ǰ�к�", A)

       
        #��Ԫ
        temp = Fraction(A[cur_row][cur_col])
        for col in range(cur_col,coln):
            A[cur_row][col] = Fraction(A[cur_row][col]) / temp

        for i in range(0,rown):
            if i == cur_row:
                continue
            temp = Fraction(A[i][cur_col])
            for col in range(cur_col,coln):
                A[i][col] = Fraction(A[i][col]) - temp*A[cur_row][col]
        print_matrix("��Ԫ��", A)
        cur_row += 1
        cur_col += 1

    if cur_row < cur_col:
        return False
    if cur_row < rown:
        for i in range(cur_row,rown):
            if A[i][coln-1] != 0:
                return False
    return True
        
if __name__ == "__main__":
    A =  [[2.0,   3.0,   1.0,    16.0],   
          [1.0,   5.0,   2.0,    23.0],   
          [3.0,   4.0,   5.0,    33.0],
          [6.0,   8.0,  10.0,    66.0]]

    if gauss(A):
        print A
    else:
        print "no solution or many solutions"
    










            
