function solve(words,sentence) {

    let swords = words.split(', ');
   

    for (let word of swords) {
        let starWord = '*'.repeat(word.length);
        // while (sentence.includes(` ${starWord} `)) {
           sentence = sentence.replace(starWord,word)
        // }   
    }

    console.log(sentence); 
}

solve('great',
'softuni is ***** place for learning new programming languages');

solve('great, learning',
'softuni is ***** place for ******** new programming languages');