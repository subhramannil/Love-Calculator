def calculate_love_score(name1, name2):
    # Combine names: remove spaces and convert to uppercase
    full_name = (name1 + name2).upper().replace(" ", "")
    
    # Define the two groups of letters
    group1 = "TRUE"
    group2 = "LOVE"
    
    total1 = 0
    for char in group1:
        count = full_name.count(char)
        # Use singular "time" for 1 and "times" otherwise
        times_str = "time" if count == 1 else "times"
        #print(f"{char} occurs {count} {times_str}")
        total1 += count
    #print(f"Total = {total1}\n")
    
    total2 = 0
    for char in group2:
        count = full_name.count(char)
        times_str = "time" if count == 1 else "times"
        #print(f"{char} occurs {count} {times_str}")
        total2 += count
    #print(f"Total = {total2}")
    print(str(total1)+str(total2))

# Example usage:
calculate_love_score("Angela Yu", "Jack Bauer")
