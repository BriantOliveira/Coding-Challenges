// You are building an educational website and want to create a simple calculator for students to use. The calculator will only allow addition and subtraction of positive integers.

// Given an expression string using the "+" and "-" operators like "5+16-2", write a function to find the total.


// Sample input/output:
// evaluate("6+9-12")  => 3
// evaluate("1+2-3+4-5+6-7") => -2


var expression1 = "6+9-12"; // = 3
var expression2 = "1+2-3+4-5+6-7"; // = -2


function cal(expression) {
  
  var currentString = ""
  var totalSum = 0
  var lastSymbol ='+'
  
  const arr = expression.split('')
  
  for (let char of arr) {
    if (char != '+' && char != '-') {
      currentString += char
    } else if (currentString != '') {
      if (lastSymbol === '+') {
        totalSum += Number(currentString)
      } else {
        totalSum -= Number(currentString)
      }
      lastSymbol = char
      currentString = ''
    }
  }
  if (lastSymbol === '+') {
    totalSum += Number(currentString)
  } else {
    totalSum -= Number(currentString)
  }
  
  return totalSum
  
}


console.log(cal("1+2-3+4-5+6-7+9342-342"))