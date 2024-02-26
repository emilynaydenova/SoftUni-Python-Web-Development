function solve(text, word) {
    let newText = text.replaceAll(word,'8888');
    console.group(newText);
    let censored = text.replace(word,'*'.repeat(word.length));
    
    while (censored.includes(word)) {
        censored = censored.replace(word,'*'.repeat(word.length));
    }
    console.log(censored);
}

solve('A small sentence with some small words', 'small');
solve('Find the hidden word', 'hidden');

// string.replace(searchValue, newValue)
// The replace() method searches a string for a value or a regular expression.

// The replace() method returns a new string with the value(s) replaced.

// The replace() method does not change the original string.