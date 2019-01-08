// A series of number in which each number 
//(Fibonnacci number) is the sum of the two preceding 
// numbers. The simplest is the series 1,1,2,3,5,8, etc.

// Recursive solution 
function fib(n) {
  if (n < 2) {
    return n;
  }
  return fib(n - 1) + fib(n - 2);
}