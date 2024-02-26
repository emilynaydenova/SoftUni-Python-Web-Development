function login(input) {

    let tries = 0;

    function reverseString(str) {
        let reversed = str.split('').reverse().join('');
        return reversed;
    }
    let username =input[0];
    let pass = reverseString(username);

    for (let i=1; i<input.length; i++){
        if (input[i] === pass) {
            console.log(`User ${username} logged in.`);
            return;
        } 

        tries++;
        if (tries>=4) {
            console.log(`User ${username} blocked!`);
            return;
        } 

        console.log('Incorrect password. Try again.');
    }
 
}

login(['Acer','login','go','let me in','recA']);
login(['momo','omom']);
login(['sunny','rainy','cloudy','sunny','not sunny']);