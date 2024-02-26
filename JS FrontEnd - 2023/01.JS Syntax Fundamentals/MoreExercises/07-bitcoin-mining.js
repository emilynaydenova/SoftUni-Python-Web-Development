function bitcoin(shifts) {
    let count = 0;
    let currentDay = 0;
    let day = 0;
    const oneBitcoin = 11949.16;
    const oneGramGold = 67.51;
    let money = 0;


    for (let shift of shifts) {
        currentDay += 1;
        if (currentDay % 3 == 0) {
            shift *= 0.7;
        }
        money += shift * oneGramGold;
        if (money >= oneBitcoin) {
            let currentCount = Math.floor(money / oneBitcoin);
            count += currentCount;
            if (day==0) {
                day = currentDay;
            }
            money -= currentCount * oneBitcoin;
        }
    }

    console.log(`Bought bitcoins: ${count}`);
    if (count > 0) {
        console.log(`Day of the first purchased bitcoin: ${day}`)
    }
    console.log(`Left money: ${money.toFixed(2)} lv.`)
}


bitcoin([100, 200, 300]);
bitcoin([50, 100]);
bitcoin([3124.15, 504.212, 2511.124]);