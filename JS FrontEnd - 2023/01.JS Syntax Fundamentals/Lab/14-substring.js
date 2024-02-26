function solve(text,startIdx,count) {
    
    let result = text.substring(startIdx,startIdx+count);
    console.log(result);
}

solve('ASentencelllllllllll', 1, 8);
solve('kkkSkipWord', 4, 7);
// The substring() method extracts characters, between two indices (positions), 
// from a string, and returns the substring.