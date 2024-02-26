// The typeof operator returns a string indicating 
// the type of an operand
// syntax: typeof operand

const obj ={name: 'Maria', age:18};
console.log(typeof obj); // object


function circleArea(arg) {
    let typeArg = typeof arg
    if (typeArg === 'number'){
        let area = Math.PI * arg ** 2
        console.log(area.toFixed(2))
    } else {
        console.log(`We can not calculate the circle area, because we receive a ${typeArg}.`)
    }
}


circleArea(5);
circleArea('name');

console.log(typeof 'blubber');
console.log(typeof 15);
/*
function circleArea(radius) {
    let typeOfRadius = typeof(radius)
    if (typeOfRadius == 'number'){ 
        let area = Math.PI * radius ** 2;
     
     console.log(`${area.toFixed(2)}`);
    } else {
        console.log(`We can not calculate the circle area, because we receive a ${typeOfRadius}.`)
    }    

*/