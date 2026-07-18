class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        l_row=[set() for x in range(9)]
        l_col=[set() for x in range(9)]
        l_tris=[set() for x in range(9)]
        ind=0
        length=0
        length_tris=0
        
        for row in range(9):
          #  l_row[row]=set()
            for col in range(9):
                if(board[row][col]!="."):
                    ind_r=row//3
                    ind_c=col//3
                    if row<3:
                        ind=ind_r+ind_c
                    elif row<6:
                          ind=ind_r+ind_c+2
                    elif row<9:
                        ind=ind_r+ind_c+4
                    length_tris=len(l_tris[ind])
                    l_tris[ind].add(board[row][col])
                    if(length_tris==len(l_tris[ind])):
                        return False

                    length=len(l_row[row])
                    l_row[row].add(board[row][col])
                    if(length==len(l_row[row])):
                        return False
        
        length=0
        for col in range(9):
          #  l_col[col]=set()
            for row in range(9):
                if(board[row][col]!="."):
                    length=len(l_col[col])
                    l_col[col].add(board[row][col])
                    if(length==len(l_col[col])):
                        return False
                    
        
        return True