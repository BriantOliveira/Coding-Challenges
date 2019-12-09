/** Lyft Internship coding question */

// You have an array of two numbers, find the common numbers
// and return it in an array.
// x = [1, 2, 4, 5, 6];
// y = [1, 3, 5]; 

/** Best case O(1) */
// is rare that many items will get hashed to the same key (If chosen a good hash
// function you won't need a bid load balance)

/** Worse case O(n) */
// if too many elements are hashed into the same key: looking inside that given key
// may be O(n) time. 
function findCommonElements(x, y) {
  const common = {};
  
x.forEach((element1) => y.forEach((element2) => {
  if (element1 === element2) {
    // common.push(element1) 
    common[element1] = common[element1] + 1 || 1;
  }
}
));
 console.log(Object.keys(common).map(element => Number(element)));
}

findCommonElements([1, 2, 4, 5, 6], [1, 3, 5])