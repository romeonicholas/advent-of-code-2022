# Challenge 1 of 2 for 8.12.2022
# Input: A matrix of integers that represents the height of trees
# Goal: Count how many trees in the matrix are "visible"--they either
# exist on the border of the matrix or they are taller than ALL the trees
# above, below, to the right, OR to the left of it all the way to that edge

challenge_input = open("input.txt", "r")
tree_rows = challenge_input.read().splitlines()

count_visible = 0

count_visible += len(tree_rows[0])    #Top row
count_visible += len(tree_rows[-1])   #Bottom row
count_visible += (len(tree_rows) - 2) #Left column - overlap
count_visible += (len(tree_rows) - 2) #Right column - overlap

#Middle rows and columns, indicies always start at 1 and stop 1 before end
tree_row_index = 1
while tree_row_index < (len(tree_rows) - 1):
    tree_col_index = 1

    while tree_col_index < (len(tree_rows[tree_row_index]) - 1):
        current_tree_height = int(tree_rows[tree_row_index][tree_col_index])

        #look left
        is_visible_from_left = True
        search_index = tree_col_index - 1
        while search_index >= 0:
            if int(tree_rows[tree_row_index][search_index]) >= current_tree_height:
                is_visible_from_left = False
                break
            else:
                search_index -= 1
        
        #look right
        is_visible_from_right = True
        search_index = tree_col_index + 1
        while search_index < len(tree_rows[tree_row_index]):
            if int(tree_rows[tree_row_index][search_index]) >= current_tree_height:
                is_visible_from_right = False
                break
            else:
                search_index += 1

        #look up
        is_visible_from_above = True
        search_index = tree_row_index - 1
        while search_index >= 0:
            if int(tree_rows[search_index][tree_col_index]) >= current_tree_height:
                is_visible_from_above = False
                break
            else:
                search_index -= 1

        #look down
        is_visible_from_below = True
        search_index = tree_row_index + 1
        while search_index < len(tree_rows):
            if int(tree_rows[search_index][tree_col_index]) >= current_tree_height:
                is_visible_from_below = False
                break
            else:
                search_index += 1

        if is_visible_from_left or is_visible_from_right or is_visible_from_above or is_visible_from_below:
            count_visible += 1

        tree_col_index += 1

    tree_row_index += 1

print(count_visible)
