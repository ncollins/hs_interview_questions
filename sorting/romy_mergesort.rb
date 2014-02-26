def ugly_brainless_merge(left_team, right_team)
  winners = []

  until left_team.empty? || right_team.empty?
    if left_team.first < right_team.first
      winners.push(left_team.shift)
    else
      winners.push(right_team.shift)
    end
  end
  # because Romy was brainless...
  if left_team.empty?
    winners.concat(right_team)
  else
    winners.concat(left_team)
  end
  # yes, i confess this is nasty spaghetti code!  yuck!
end

# Array[Num] -> Array[Array[Num], Array[Num]]
def halve list
  middle = (list.length/2.0).round

  ugly_left = list[0..middle]
  ugly_right = list[(middle + 1)..(list.length)] # "but the math is ugly", quibbles Nick

  left = list.slice(0, middle) # ... "this is neater," he retorts.
  right = list.slice(middle, list.length)

  [left,right]
end

# Array[Num], Array[Num] -> Array[Num]
def merge(left_team, right_team)
  winners = []

  until left_team.empty? || right_team.empty?
    if left_team.first < right_team.first
      winners.push(left_team.shift)
    else
      winners.push(right_team.shift)
    end
  end
  winners.concat(left_team).concat(right_team)
  # or 
  # winners + left_team + right_team
  # either way, it doesn't matter which team is written first! :D
  #
end

# Array[Num] -> Array[Num]
def merge_sort list

# 1st attempt: FUZZY BRAIN STUFF, ignore
#  if base_case
#    return the_stuff
#  elsif
#    recurse the merge_sort (left)

# base case
  if list.length < 2
    list
# main case
  else
    left, right = halve list
    sorted_left = merge_sort left
    sorted_right = merge_sort right
    merge(sorted_left, sorted_right)
  end
end


def mmmerge(sorted_left, sorted_right)
  winners = []
  until sorted_left.empty? || sorted_right.empty?
    if sorted_left.first < sorted_right.first
      winners.push(sorted_left.shift)
    else
      winners.push(sorted_right.shift)
    end
    winners.concat(sorted_left).concat(sorted_right)
end



