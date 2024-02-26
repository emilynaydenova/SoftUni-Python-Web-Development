function roadRadar(speed, area) {

    let vehicleSpeed = Number(speed);

    const areas = {
        "motorway": 130,
        "interstate": 90,
        "city": 50,
        "residential": 20
    };

    let speedLimit = areas[area];
    let difference;
    let status;

    if (vehicleSpeed <= speedLimit) {
        console.log(`Driving ${vehicleSpeed} km/h in a ${speedLimit} zone`);
    } else {
        difference = vehicleSpeed - speedLimit;
        if (difference <= 20) {
            status = 'speeding';
        } else if (difference <= 40) {
            status = 'excessive speeding';
        } else {
            status = 'reckless driving';
        }

        console.log(`The speed is ${difference} km/h faster than the allowed speed of ${speedLimit} - ${status}`);
    }
}

roadRadar(40, 'city');
roadRadar(21, 'residential');
roadRadar(120, 'interstate');
roadRadar(200, 'motorway');
