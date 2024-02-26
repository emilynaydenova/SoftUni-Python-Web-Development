function largestNum0(n1,n2,n3) {
    let result = n1;
    if (n2 >=  n1 &&  n2 >= n3) {
        result = n2;
    } else if (n3 >= n1 && n3 >= n2) {
        result = n3;
    } 
    
    console.log(`The largest number is ${result}.`)

};

  

 
function largestNum(n1,n2,n3){
    let result = Math.max(n1,n2,n3); 
    console.log(`The largest number is ${result}.`);
}

 //   console.log('The largest number is '+result+'.');

largestNum(5,-3,16);
largestNum(-3, -5, -22.5);