/* Exemple output: 33 (Business owner 42 received three conversations total (1, 2, and 4), but only responded to one conversation (conversation ID 1)).*/

function BuzOwnerinfo(ownerId, messages) {
  var rate = 0
  var ownerResponse = 0 
  var ownerResponseID = []
  var senderID = []
  var onwerInbox = []
  var conversationTotal = 0
  
  // Return 0 if user doesn't have any messages
  if (messages === undefined || messages.length == 0) {
    return 0
  }
  
   // loop through user messages
  for (var i = 0; i < messages.length; i++) {
    var sender = messages[i]["sender"]
    var receiver = messages[i]["recipient"]
    var message = messages[i]["messageId"]
    
   //Check if Owner responded to any messages and store the message id
   if (sender == ownerId) {
      ownerResponse += 1
      ownerResponseID.push(message)
   }
    
    // Check if the owner has received any messages and store message id 
   if (receiver == ownerId) {
     conversationTotal += 1
     onwerInbox.push(message)
   }    
  }
 
  // Sum all the unique messagesID
 var sumOfReceivedMessageId = onwerInbox.reduce((a, b) => a + b, 0)
 
  // subtratct ownerId - total inbox from unique users.
  var result = ownerId - sumOfReceivedMessageId

  // var result = "Business owner " + ownerId + " received " + conversationTotal + " conversation total, but only responded to " + ownerResponse + " (conversation ID " + ownerResponseID + ")."
  return result
}


Allmessages = [
  {sender: 1, recipient: 42, messageId: 1},
  {sender: 42, recipient: 1, messageId: 1},
  {sender: 2, recipient: 42, messageId: 2},
  {sender: 2, recipient: 42, messageId: 2},
  {sender: 3, recipient: 88, messageId: 3},
  {sender: 3, recipient: 42, messageId: 4}]

OwnerBizId = 42 

BuzOwnerinfo(OwnerBizId, Allmessages)