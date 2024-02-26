function theatre(dayType, age) {
    let i;
    let j;
    let prices = [
        [12, 18, 12],
        [15, 20, 15],
        [5, 12, 10],
    ]

    if (dayType === 'Weekday') {
        i = 0;
    } else if (dayType === 'Weekend') {
        i = 1;
    } else if (dayType === 'Holiday') {
        i = 2;
    }

    if (age < 0 || age > 122) {
        console.log('Error!');
    } else {
        if (age <= 18) {
            j = 0;
        } else if (age <= 64) {
            j = 1;
        } else {
            j = 2;
        }
        console.log(`${prices[i][j]}$`);
    }
}

theatre('Weekday', 42);
theatre('Holiday', -12);
theatre('Holiday', 15);