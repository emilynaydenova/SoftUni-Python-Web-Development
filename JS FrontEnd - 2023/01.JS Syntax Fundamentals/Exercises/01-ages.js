function person(age) {
    if (age < 0 || age > 122) {
        console.log('out of bounds');
    } else if (age <= 2) {
        console.log('baby');
    } else if (age <= 13) {
        console.log('child');
    } else if (age <= 19) {
        console.log('teenager');
    } else if (age <= 65) {
        console.log('adult');
    } else {
        console.log('elder');

    }
}

person(20);
person(1);
person(100);
person(-1);