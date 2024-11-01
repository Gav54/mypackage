def top_n(items,n):
    """Return the top n items in an array in desc order.

    Args:
        items(array):list or array-like object
        n(int):num of items to return

    Return:
        array:top n items,in desc order
    """ 
    for i in range(n):
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]:
                items[j],items[j+1] = items[j+1],items[j]

    # get last two items
    top_n  = items[-n:]

    # return in descending order
    return top_n[::-1]