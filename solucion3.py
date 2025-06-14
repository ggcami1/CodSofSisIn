def calculate(s):
    s = s.replace("plus", "+").replace("minus", "-")
    return str(eval(s))

def duplicate_or_unique(arr):
    total= sum(arr)
    unique_values = set(arr)
    unique_sum = sum(unique_values)
    legth = len(arr)
    
    if legth == len(unique_values) + 1:
        
        return total - unique_sum
    else:
        return 2 * unique_sum -total
