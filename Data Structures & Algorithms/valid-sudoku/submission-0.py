class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=set()
        col=set()
        box=set()
        for r in range(9):
            for c in range(9):
                val=board[r][c]
                if val==".":
                    continue
                check_cols=(c,val)
                check_rows=(r,val)
                check_boxes=(r//3,c//3,val)
                if check_cols in col or check_rows in row or check_boxes in box:
                    return False
                else:
                    row.add(check_rows)
                    col.add(check_cols)
                    box.add(check_boxes)
        return True
        