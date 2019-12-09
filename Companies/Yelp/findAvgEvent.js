

function FindAvg(event) {
  var adsOcc = []
  var adsBizId = []
  var pageViewsOcc = []
  var pageViewsBizId = []
  var photoViewsOcc = []
  var photoViewsBizId = []
  var reviewsOcc = []
  var reviewsBizId = []
  
  
    for (var i = 0; i < event.length; i++) {
      var eventType =  event[i][0]
      var occ = event[i][1]
      var bizId = event[i][2]
      
      if (eventType == 'ads') {
        adsOcc.push(occ)
        adsBizId.push(bizId)
      }
       if (eventType == 'page_views') {
        pageViewsOcc.push(occ)
        pageViewsBizId.push(bizId)
      }
        if (eventType == 'photo_views') {
        photoViewsOcc.push(occ)
        photoViewsBizId.push(bizId)
      }
       if (eventType == 'reviews') {
        reviewsOcc.push(occ)
        reviewsBizId.push(bizId)
      }
     }
    
   
    var totalAds = adsOcc.reduce((a, b) => a + b, 0)
    var adsAvg = totalAds/adsOcc.length
    
    var totalpageViews= pageViewsOcc.reduce((a, b) => a + b, 0)
    var pageViewsAvg = totalpageViews/pageViewsOcc.length
    
    var totalphotoView = photoViewsOcc.reduce((a, b) => a + b, 0)
    var photoViewAvg = totalphotoView/photoViewsOcc.length
    
    var totalReviews = reviewsOcc.reduce((a, b) => a + b, 0)
    var reviewsAvg = totalReviews/reviewsOcc.length
    
    var testArr = []
    testArr.push(adsBizId, pageViewsBizId)
    var testArr2 = []
    testArr2.push(photoViewsBizId + reviewsBizId)
    
    // 2 event occurences and occ.length >= 1 
    var res = reviewsBizId.filter(value => -1 !== photoViewsBizId.indexOf(value)).sort()
    var res1 = adsBizId.filter(value => -1 !== pageViewsBizId.indexOf(value)).sort()
    var finalResult = [res + res1]
    
    return  finalResult
    
  }


  input = [
    ['ads', 7, 3], 
    ['ads', 8, 2], 
    ['ads', 5, 1],
    ['page_views', 11, 2],
    ['page_views', 12, 3],
    ['photo_views', 10, 3],
    ['reviews', 17, 2],
   ]

FindAvg(input)   