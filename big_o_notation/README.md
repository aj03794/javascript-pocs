###### Intro to Big-O Notation

- Big-O notation is how programmers talk about their algorithms
    * An algorithm is basically a function in your program
- `A function's Big-O notation is determined by how it responds to different inputs`
    * How much slower is it if we give it a 1000 inputs instead of 1?

```
def item_in_list(to_check, the_list):
    for item in the_list:
        if to_check == True:
            return True
    return False
```

- The `complexity` of this function is `O(n)`
    - `O(n)` is read `Order of N` b/c the `O` function is also know as the `Order function`

- `Orders of Magnitude` is another mathematical term which basically tells the difference btwn classes of numbers
- In approximation, as long as you're within an order of magnitude, you're pretty close

- `O(n)` says that if we were to graph the time it takes to run this function w/ different sized inputs, we'd see that it approximately corresponds to the number of items in the array
    * The line is basically straight if we were to graph it

- Big-O is all about approximate worst-case performance of doing something
    * The worst case for the code above is that the thing we're searching for isn't in the list at all (`upper bound`)


- Consider this function

```
def all_combinations(the_list):
    results = []
    for item in the_list:
        for inner_item in the_list:
            results.append((item, inner_item))
    return results
```

- This matches every item in the list with every other item in the list
    * If we gave an array of `[1, 2, 3]`, we'd get back `[(1, 1), (1, 2), (1, 3), (2, 1), (2,2), (2, 3), (3, 1), (3, 2), (3, 3)]`
- This function is considered `O(n^2)`
    * This is b/c for every item in the list (aka `n` the input size), we have to do `n` more operations
        * So n * n == n^2
