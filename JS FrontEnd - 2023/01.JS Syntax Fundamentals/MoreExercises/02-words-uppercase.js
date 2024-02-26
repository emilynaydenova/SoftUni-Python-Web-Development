function solve(sentence) {
    let re = /[A-Za-z0-9]*/gm;

    let found = filter_array_values(sentence.match(re));
    let arr =[];

    for (let word of found) {
        word = word.toUpperCase();
        arr.push(word);
    }

    function filter_array_values(arr) {
        arr = arr.filter(isEligible);
        return arr;
    }

    function isEligible(value) {
        if (value !== false ||
            value !== null ||
            // value !== 0 ||
            value !== "") {
            return value;
        }
    }
    console.log(arr.join(', '));
}


solve('Hi, how are you?');
solve('hello');
