function solve(sentence) {
    let re = /[A-Z][a-z]*/g;

    let found = sentence.match(re);
    console.log(found.join(', ')); 

}

solve('SplitMeIfYouCanHaHaYouCantOrYouCan');
solve('HoldTheDoor');
solve('ThisIsSoAnnoyingToDoA');