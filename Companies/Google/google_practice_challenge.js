// Helper Function
function isAlphaNumeric(char) { 
    var code = char.charCodeAt(); 
    if ( 
        !(code > 47 && code < 58) && 
        !(code > 64 && code < 91) && 
        !(code > 96 && code < 123) && 
        !(code === 45 || code === 47) 
        ) { 
            return false; 
        } return true; 
    }
    
    /** 
     * Step 1 - Check if string is has continues dashes like "----" and if so, return empty string
     * Step 2 - If the string S contains only 1 character, return that character in uppercase.
     * Step 3 - If the string S doesn’t contain any character, return invalid.
     * Step 4 - Check if string length is equal to 1, and if true check if the value is not a single dash "-" and
     * return string to upperCase
     * Step 5 - If the string S doesn’t consists only of alphanumerical characters (a−z and/or A−Z
     * and/or 0−9) and/or dashes (-), return invalid.
     * Step 6 - Second, I must take all of dashes out of the string S. And I could transform the string to uppercase at this point also
     * Step 7 - Third, loop through the string and add “-” where it should be, depend on variable K
     * Step 8 - Lastly, return the finished String.  
     **/

var licenseKeyFormatting = function(S, K) {

    const exp = ([\-]){${S.length}, ${S.length}} 
    const regex = new RegExp(exp) 
    if (S.search(regex) == 1) { 
        return ""
    }

    if (S.length < 1) return "invalid"; 
    if (S.length == 1 && S[0] !== '-') 
    return S.toUpperCase(); 
    if (K < 0) return "invalid";

    for (let k in S) { 
        if (!isAlphaNumeric(S[k])) return "invalid"; 
    } 
        let key = 0; 
        let strObj = {}; 
        for (let c of S) { 
            if (c != "/" && c != "-") { 
                strObj[key] = c.toUpperCase(); key++; 
            } } 
            let newStr = "";
            let counter = key - 1;

    for (let k in strObj) { 
        newStr += strObj[k]; 
        if (counter !== 0 && counter % K === 0) { 
            newStr += "-"; 
        } 
        counter--; 
    } 
    return newStr; 
};

