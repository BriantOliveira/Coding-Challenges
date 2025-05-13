'''
    Each day a quarry-worker is given a pile of stones and told to reduce the larger stones into smaller ones.
    The worker must smash the stones together to reduce them, and is told to always pick up the largest two stones
    and smash them together. If the stones are of equal weight, they both disintegrate entirely. 
    If one is larger, the smaller one is disintegrated and the larger one is reduced by the weight of the smaller one.

    Eventually, there is either one stone left that cannot be broken, or all of the stones have been smashed. 
    Determine the weight of the last stone, or return 0 if there is none.

    Example:
    weights = [1, 2, 3, 6, 7, 7]

    The worker always starts with the two largest stones. In this case, the two largest stones have equal weights of 7 so 
    they both disintegrate when smashed.

    Next, the worker smashes weights 3 and 6. The smaller one is destroyed and the larger weighs 6 - 3 = 3 units.
    Then, weights 3 and 2 are smashed together, which leaves a stone of weight 1. 
    This is smashed with the last remaining stone of weight 1. 
    There are no stones left, so the remaining stone weight is 0.
'''

def lastStoneWeight(weights):
    # Check the size of the array first, if it is 0 just return 0 before even looping
    if len(weights) == 0:
        return 0 
    
    # Loop through the array of weights
    while len(weights) > 1:
        weights.sort() #Sort the stone list
        firstWeight = weights.pop() #Heaviest stone
        secondWeight = weights.pop() #Second heaviest
        
        # Check if they are not the same weight
        if firstWeight != secondWeight:
            # If they are not, subtract the heviest with the second heaviest, and then append the value back to the array.
            weights.append(firstWeight - secondWeight)
    
    # Return the remaining weight in the array if there is any, otherwise return 0.
    return weights[0] if weights else 0;
        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    weights_count = int(input().strip())

    weights = []

    for _ in range(weights_count):
        weights_item = int(input().strip())
        weights.append(weights_item)

    result = lastStoneWeight(weights)

    fptr.write(str(result) + '\n')

    fptr.close()