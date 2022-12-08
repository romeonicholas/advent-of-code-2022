# Challenge 2 of 2 for 8.12.2022
# Input: A matrix of integers that represents the height of trees
# Goal: Find highest scenic score, derived from multiplying the view
# in all directions from a tree. The view score for each direction is
# calculated as how many trees in that direction are its height or shorter
# (stopping after a tree of the same height or higher, or the edge of the matrix)

challenge_input = open("input.txt", "r")
tree_rows = challenge_input.read().splitlines()

greatest_scenic_score = 0

tree_row_index = 0
while tree_row_index < (len(tree_rows)):
    tree_col_index = 0

    while tree_col_index < (len(tree_rows[tree_row_index])):
        current_tree_height = int(tree_rows[tree_row_index][tree_col_index])
        

        #look left
        left_view_score = 0
        search_index = tree_col_index - 1
        while search_index >= 0:
            left_view_score += 1
            if int(tree_rows[tree_row_index][search_index]) < current_tree_height:
                search_index -= 1
            else:
                break
        
        #look right
        right_view_score = 0
        search_index = tree_col_index + 1
        while search_index < len(tree_rows[tree_row_index]):
            right_view_score += 1
            if int(tree_rows[tree_row_index][search_index]) < current_tree_height:
                search_index += 1
            else:
                break

        #look up
        above_view_score = 0
        search_index = tree_row_index - 1
        while search_index >= 0:
            above_view_score += 1
            if int(tree_rows[search_index][tree_col_index]) < current_tree_height:
                search_index -= 1
            else:
                break

        #look down
        below_view_score = 0
        search_index = tree_row_index + 1
        while search_index < len(tree_rows):
            below_view_score += 1
            if int(tree_rows[search_index][tree_col_index]) < current_tree_height:
                search_index += 1
            else:
                break

        total_scenic_score = left_view_score * right_view_score * above_view_score * below_view_score
        if total_scenic_score > greatest_scenic_score:
            greatest_scenic_score = total_scenic_score

        tree_col_index += 1

    tree_row_index += 1

print(greatest_scenic_score)
