def classify(number):
    # Check for invalid input
    if not isinstance(number, int) or number < 1:
        raise ValueError("Classification is only possible for positive integers.")
   
    # Calculate aliquot sum
    aliquot_sum = 0
   
    for i in range(1, number):
        if number % i == 0:
            aliquot_sum += i
   
    # Classification
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"