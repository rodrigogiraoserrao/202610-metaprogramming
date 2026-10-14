1. Take a look at `setters.py` and replace the three properties for `r`, `g`, and `b`, with a _single_ descriptor that performs validation on assignment.
 Instead of storing the three components as separate integers in separate attributes, store all components as a hexadecimal string in the attribute `hex`.

2. What if you wanted to have the three components as three “private” attributes? Can you hack something together?