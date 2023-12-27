## Stateless code is easier to test

> "One important strategy is to reduce the amount of state in your code. It’s a lot easier to test code that doesn’t rely on state. Any pure function—a bit of code that relies only on its direct inputs, has no side effects, and has predictable results—is easy to test." ([The Rules of Programming, 2. Let Your Code Tell Its Own Story](https://learning.oreilly.com/library/view/-/9781098133108/))

## The longer a bug exists, the more of the codebase will rely on that bug’s behavior

> "Once a bug exists, people will unintentionally write code that relies on that bug. Sometimes that shaky bit of bug-reliant code is nearby, in the same system as the bug. Sometimes it’s not nearby—maybe it’s downstream, in a bit of code that calls your system and depends on the incorrect results your bug causes. Or it’s upstream—a chunk of code that only works because the bug caused you to call it in a particular way." ([The Rules of Programming, 2. Let Your Code Tell Its Own Story](https://learning.oreilly.com/library/view/-/9781098133108/))

## Floating point numbers can might seem the same can be very slightly different

> "Given the inaccuracies inherent in any computation (including converting an input string to a floating-point value), you should never compare two floating-point values to see if they are equal. Different computations that produce the same (mathematical) result may differ in their least significant bits. For example, adding 1.31e0 and 1.69e0 should produce 3.00e0. Likewise, adding 1.50e0 and 1.50e0 should produce 3.00e0. However, were you to compare (1.31e0 + 1.69e0) to (1.50e0 + 1.50e0), you might find that these sums are not equal. Because two seemingly equivalent floating-point computations will not necessarily produce exactly equal results, a straight comparison for equality—which succeeds if and only if all bits (or digits) in the two operands are the same—may fail." ([Write Great Code, Volume 1, 2nd Edition, 4 FLOATING-POINT REPRESENTATION](https://learning.oreilly.com/library/view/-/9781098125646/))

## Floats having a radix point that can float between digits

> "In a floating-point value, the radix point (binary point) can float between digits in the number as needed. So, in a 16-bit binary number that needs only 2 bits of precision for the fractional component, the binary point can float down between bits 1 and 2, leaving bits 2 through 15 for the integer portion. A floating-point format needs one additional field to specify the position of the radix point within the number, equivalent to the exponent in scientific notation." ([Write Great Code, Volume 1, 2nd Edition, 4 FLOATING-POINT REPRESENTATION](https://learning.oreilly.com/library/view/-/9781098125646/))

## It is possible to convert the memory size of a number, at the cost of precision

> "You can also reduce the size of an integer value through saturation, which is useful when you’re willing to live with a possible loss of precision. To convert a value via saturation, you copy the LO bits of the larger object into the smaller object. If the larger value is outside the smaller object’s range, then you clip the larger value by setting the smaller object to the largest (or smallest) value within the smaller value’s range.

For example, when converting a 16-bit signed integer to an 8-bit signed integer, if the 16-bit value is in the range –128 through +127, you simply copy the LO byte into the 8-bit object. If the 16-bit signed value is greater than +127, then you clip the value to +127 and store +127 into the 8-bit object. Likewise, if the value is less than –128, you clip the final 8-bit object to –128. Saturation works the same way when you clip 32-bit values to smaller values." ([Write Great Code, Volume 1, 2nd Edition, 2 NUMERIC REPRESENTATION](https://learning.oreilly.com/library/view/-/9781098125646/))

## Convert from binary to decimal numbering

> "To convert a binary value to decimal, add 2i for each 1 in the binary string, where i is the zero-based position of the binary digit. For example, the binary value 110010102 represents:

1 × 27 + 1 × 26 + 0 × 25 + 0 × 24 + 1 × 23 + 0 × 22 + 1 × 21 + 0 × 2" ([Write Great Code, Volume 1, 2nd Edition, 2 NUMERIC REPRESENTATION](https://learning.oreilly.com/library/view/-/9781098125646/))

## Decimal number system is based on both the character and the position of the character

> "The decimal positional numbering system represents numbers using strings of Arabic numerals, optionally including a decimal point to separate whole and fractional portions of the number representation. The position of a digit in the string affects its meaning: each digit to the left of the decimal point represents a value between 0 and 9, multiplied by an increasing power of 10" ([Write Great Code, Volume 1, 2nd Edition, 2 NUMERIC REPRESENTATION](https://learning.oreilly.com/library/view/-/9781098125646/))

