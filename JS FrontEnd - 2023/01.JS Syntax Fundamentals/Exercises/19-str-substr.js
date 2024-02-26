function solve(word, text) {
    let wordLower = word.toLowerCase();
    let textLower = text.toLowerCase().split(' ');


    if (textLower.includes(wordLower)) {
        console.log(word);
        return;
    }
    console.log(`${word} not found!`);
}

solve('javascript',
    'JavaScript is the best programming language'
);

solve('python',
    'JavaScript is the best programming language'
);