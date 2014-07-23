Writing Own Square Root Function
================================

> Depending on you needs, a simple divide-and-conquer strategy can be used. It won't converge as fast as some other methods but it may be easier for a novice to understand. In addition, since it's an O(log n) algorithm (halving the search space each iteration), the worst case for a 32-bit float will be 32 iterations.

> Let's say you want the square root of 62.104. You pick a value halfway between 0 and that and square it. If the square is higher than your number, you need to concentrate on numbers less than the midpoint. If it's too low, concentrate on those higher.

> With real math, you could keep dividing the search space in two forever (if it doesn't have a rational square root). In reality, computers will eventually run out of precision and you'll have your approximation. The following C program illustrates the point:

[Source](http://stackoverflow.com/a/1623500)
