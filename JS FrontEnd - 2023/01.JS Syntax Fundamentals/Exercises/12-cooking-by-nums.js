function cooking(num, ...choices) {

    let result = Number(num);
 
    choices.forEach( (choice) => {
        switch (choice) {
            case 'chop':
                result /= 2;
                break;
            case 'dice':
                result = Math.sqrt(result);
                break;
            case 'spice':
                result += 1;
                break;
            case 'bake':
                result *= 3;
                break;
            case 'fillet':
                result *= 0.8;
                break;
            default:
                break;
        }
        console.log(result);
     }
    )
      
 }

 

// function cooking(num, ...choices) {

//     let result = Number(num);

//     const parser ={
//         chop() {result /= 2;},
//         dice() {result = Math.sqrt(result);},
//         spice() {result += 1;},
//         bake() {result *= 3;},
//         fillet() {result *= 0.8;},
//     }

//     for (let choice of choices) {
//         parser[choice]();
//         console.log(result);
//     }
//   }

cooking('32', 'chop', 'chop', 'chop', 'chop', 'chop');
cooking('9', 'dice', 'spice', 'chop', 'bake', 'fillet');


/*
let chop = function() {
    return result/2;
}

....
case 'chop':
    result = chop(result);
    break;


*/