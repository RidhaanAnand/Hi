total_slices = 3*8 
print ("total slices", total_slices)
friends = 5 
each_share = total_slices // friends
print("each friend will get", each_share,"slices" )
left_over = total_slices % friends 
print(left_over,"will be leftover")