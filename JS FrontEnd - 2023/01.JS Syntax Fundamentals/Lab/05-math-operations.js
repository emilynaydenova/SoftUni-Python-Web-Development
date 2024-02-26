function operations(a,b,operator){
    let result;
    switch(operator){
        case '+': result = a+b;  break;
        case '-': result = a-b;  break;
        case '*': result = a*b;  break;
        case '/':
            if (b !=0){
               result = a/b;
            }
            else{ result="Can not be devided by 0"}
            break;
        case '%':
            if (b !=0){
                result = a % b;
             }
             else{ result="Can not be devided by 0"}
             break;
        case '**': result=a**b;  break;

    }
    console.log(result)
}

operations(5, 6, '+');
operations(3, 5.5, '*');