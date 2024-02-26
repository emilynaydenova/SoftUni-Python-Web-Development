function solve(num, arr) {

    let new_arr = arr.slice(0, num);
    new_arr = new_arr.reverse(); 
    console.log(...new_arr);
     
}

solve(3, [10, 20, 30, 40, 50]);
solve(4, [-1, 20, 99, 5]);
solve(2, [66, 43, 75, 89, 47]);