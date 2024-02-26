function modernTimes(sentence) {
    let words = sentence.split(' ');
    let regex = /^[A-Za-z]+$/;

    for (let word of words) {
        if (word.startsWith('#') && word.length > 1) {
            let newWord = word.slice(1); // without #

            if (regex.test(newWord)) {
                console.log(newWord);
            }
        }
    }
}

modernTimes('Nowadays everyone #1www uses # to tag a #special word in #socialMedia');

modernTimes('The symbol # is known #variously in English-speaking #regions as the #number sign');


// charCodeAt(idx) -> ASCII num code
// a-z => 97-122 -> make all words in lower case
// A big difference with substring() is that if the 1st argument is greater than the 2nd argument, substring() will swap them. slice() returns an empty string if the 1st argument is greater than the 2nd argument