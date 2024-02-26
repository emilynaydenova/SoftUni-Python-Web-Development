function pyramid(base, increment) {
    let stone = 0;
    let marble = 0;
    let lapis = 0;
    let gold = 0;
    let height = 0;


    while (base > 2) {
        height++;
        stone += (base - 2) ** 2 * increment;


        if (height % 5 === 0) {
            lapis += 4 * (base - 1) * increment;
        } else {
            marble += 4 * (base - 1) * increment;
        }

        base -= 2;
    }

    gold = base ** 2* increment;
    height++;

    console.log(`Stone required: ${Math.ceil(stone)}`);
    console.log(`Marble required: ${Math.ceil(marble)}`);
    console.log(`Lapis Lazuli required: ${Math.ceil(lapis)}`);
    console.log(`Gold required: ${Math.ceil(gold)}`);
    console.log(`Final pyramid height: ${Math.floor(height * increment)}`);
}

pyramid(11, 1);
pyramid(11, 0.75);
pyramid(12, 1);
pyramid(23, 0.5);

 