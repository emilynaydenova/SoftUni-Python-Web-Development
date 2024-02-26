function calculator(a,operator,b) {
    let result=0;
    switch(operator) {
        case '+':
            result= a+ b;
            break;
        case '-':
            result= a-b;
            break;
        case '*':
            result=a * b;
            break;
        case '/':
            if( b!=0) {
            result=a/b;
            }; 
       }
    console.log(`${result.toFixed(2)}`);

}

calculator(5,'+', 10);
calculator(25.5,'-', 3);