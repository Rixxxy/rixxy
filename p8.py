def findTriplets(arr):
    n = len(arr)
    triplet_count = 0
    triplet_set = set()

    # Count frequencies of each element
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    # Handle special case: three zeros
    if freq.get(0, 0) >= 3:
        triplet_set.add((0, 0, 0))
        triplet_count += 1

    # Iterate through unique elements
    unique_elements = list(freq.keys())
    for i in range(len(unique_elements)):
        num1 = unique_elements[i]
        if num1 == 0:
            continue  # Already handled
        for j in range(i + 1, len(unique_elements)):
            num2 = unique_elements[j]
            num3 = -(num1 + num2)
            if num3 in freq:
                if (num1 == num3 and freq[num1] >= 2) or (num2 == num3 and freq[num2] >= 2) or (
                        num1 != num3 and num2 != num3):
                    triplet = tuple(sorted([num1, num2, num3]))
                    triplet_set.add(triplet)
                    triplet_count += 1

    # Print triplets
    for triplet in triplet_set:
        print(list(triplet))

    return triplet_count


# Example usage:
arr = [-1, 0, 1, 2, -1, -4]
findTriplets(arr)
