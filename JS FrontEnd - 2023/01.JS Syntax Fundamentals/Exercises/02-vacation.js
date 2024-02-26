function vacation(count, groupType, weekday) {

    let total = 0;

    let groupTypes = {
        'Students': [8.45, 9.80, 10.46],
        'Business': [10.90, 15.60, 16],
        'Regular': [15, 20, 22.50]
    };

    let weekdays = ['Friday', 'Saturday','Sunday'];

    let day = weekdays.indexOf(weekday);
    let price = groupTypes[groupType][day];
      
    total = count * price;
    switch (groupType) { 
        case 'Students':
            if (count >= 30) {
                total *= 0.85;
            }
            break;

        case 'Business':
            if (count >= 100) {
                total -= 10 * price;
            }
            break;

        case 'Regular':
            if (count >= 10 && count <= 20) {
                total *= 0.95;
            }
            break;
      }    
     console.log(`Total price: ${total.toFixed(2)}`)
    }

    vacation(30, "Students", "Sunday");
    vacation(40, "Regular", "Saturday");
