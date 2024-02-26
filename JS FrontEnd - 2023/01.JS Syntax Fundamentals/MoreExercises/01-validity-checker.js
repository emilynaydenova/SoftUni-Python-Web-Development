function solve(x1, y1, x2, y2) {

    function sqrt(a1, b1, a2, b2) {

        let result = Math.sqrt((a2 - a1) ** 2 + (b2 - b1) ** 2);

        if (Number.isInteger(result)) {
            console.log(`{${a1}, ${b1}} to {${a2}, ${b2}} is valid`);
        } else {
            console.log(`{${a1}, ${b1}} to {${a2}, ${b2}} is invalid`);
        }
    }

    sqrt(x1, y1, 0, 0);
    sqrt(x2, y2, 0, 0);
    sqrt(x1, y1, x2, y2);

}


solve(3, 0, 0, 4);
solve(2, 1, 1, 1);

// Number.isInteger(value)