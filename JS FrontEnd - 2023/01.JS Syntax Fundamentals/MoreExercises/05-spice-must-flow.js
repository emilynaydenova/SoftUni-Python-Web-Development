function spiceMine(yield) {
    let spice = 0;
    let days = 0;

    while (yield >= 100) {
        spice += yield;
        if (spice >= 26) {
            spice -=26;
        }
        days++;
        yield -=10;
    }
    if (spice >= 26) {
        spice -=26;
    }

    console.log(days);
    console.log(spice)

}

spiceMine(111);
spiceMine(450);