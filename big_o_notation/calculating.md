###### Calculating Big-O

```
def count_ones(a_list):
    total = 0
    for element in a_list:
        if element == 1:
            total += 1
    return total
```

- The above code is a classic example of an `O(n)` function
- This is b/c we have to loop over every element that we get in order to complete our calculation
- We can trace this by following along the code and counting
- We're doing a few calculations here
    * We're setting `total` to zero
    * We loop through a_list
    * We check if `element` is equal to 1
    * We increment `total` by 1 a few times

- Setting a counter to zero is a constant time operation
    * If you think about what's happening inside of the computer, we're setting a chunk of memeory to some new value
    * B/c we've hard-coded the zero here, it happens in constant time
- There's no way to call this function or alter the global state that we could change the operation
- This is an `O(1)` operation

- Next we loop through th elist
- We have to look at each item in the list
- This number of operations depends on the size of the list
    * If it's a list of 10 things, we do it 10 times
    * List of 75 things, we do it 75 times
- In mathematical terms this means that the time it takes to do something increases `linearly` with it's input
- We use a variable to represent the size of the input, which everyone in the industry calls `n`
- So the `loop over the list` function is `O(n)` where `n` represents the size of `a_list`

- Checking whether an element is equal to 1 is an `O(n)` operation
- `A way to prove to ourselves that this is true is to think about it as a function`
    * If we had an `is_equal_to_one()` function, would it take longer if you passed in more values?
        * is_equal_to_one(4) vs is_equal_to_one([1, 2, 3, 4, 5])
            * `It wouldn't b/c of the fixed number 1 in our comparison`

- Next, we increment the total by 1
- This is like setting total to zero (but you have to do addition first)
- Addition of 1, like equality, is also constant time

- So where are we?
- We have: O(1) + O(n) * (O(1) + O(1))
    * This is b/c we do 1 up front, constant time operation, then (potentially) 2 more constant item things for each item in the list
    * In math terms, that reduces to : O(2n) + O(1)
    * `In big O, we only care about the biggest term`

- So we're only interested in `O(2n)`
- B/c Big-O only deals with approximation, we can drop the `2`
    * Growth is still linear either way
        * 2 would only change the `rate` of growth, not the `type` of growth

- The answer to this problem is `O(n)`
- It runs slower the more things you give it, but that should grow at a predictable way

- The key aspects to determining the Big-O of a function is really just as simple as counting
- Enumberate the different operations that your code does (be careful to understand what happens when you call out into another function) then determine how they relate to your inputs
- From there its just simplifying to the biggest term an dropping the multipliers