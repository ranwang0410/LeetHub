/**
 * @param {string} allowed
 * @param {string[]} words
 * @return {number}
 */
var countConsistentStrings = function(allowed, words) {
    let count=0
    for(let j=0;j<words.length;j++)
   {
     let a=words[j].split('');
     let b=true;
    for(let i of a)
    {
        if(!allowed.includes(i))
        {
           b=false
        }
       
    }
    if(b==true){count++}}
    
    return count
};