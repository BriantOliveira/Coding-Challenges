// Runtime: O(n^2)
function findBiz(business, location) {
  var bizDict = {}
  
  // Loop through the business and create a dictionary with number
  // of occurances for each business name
  for (var i = 0; i < business.length; i++) {
    var biz = business[i].name
   
    // if it's already in the dict add 1  
    if (biz in bizDict) {
      bizDict[biz] += 1
    }
    // if it's not in the dict set it to 1
    else {
      bizDict[biz] = 1
    }
  }
  
  var bizArr = []
  // Loop through bizDict and create sorted array
  for (var key in bizDict) {
    var value = bizDict[key]
    
    // if array is empty add item
    if (bizArr.length == 0) {
      bizArr.push([key, value])
    } else {
      //Iterate through array and insert the item at the right index
      for (var x = 0; x < bizArr.length; x++) {
        let item = bizArr[x]
        // Sort bussiness by occurances 
        if (item[1] < value) {
          bizArr.splice(x, 0, [key, value])
          break
        // Sort bussiness by name
        } else if (value == item[1] && item[0] > key) {
          bizArr.splice(x, 0, [key, value])
          break
        // if we reach the end of the array push the business
        } else if (x == bizArr.length) {
          bizArr.push([key, value])
        }
      }
    }    
  }
  return bizArr
}

businessArr = [
  {
  "name": "Whole Foods",
  "location" : "Seattle",
  "id": 123
  },
  {
  "name": "Walmart",
  "location": "Tampa",
  "id": 122
  },
  {
    "name": "HEB",
    "location": "Texas",
    "id": 1234
  },
  {
    "name": "Peets",
    "location": "San Francisco",
    "id": 12344
  },
  {
    "name": "HEB",
    "location": "Texas",
    "id": 1234
  }
]

findBiz(businessArr, "Texas")