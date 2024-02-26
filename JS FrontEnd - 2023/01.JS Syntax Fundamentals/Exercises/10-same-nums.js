// String(num)  = num.toString() = '' + num = `${num}`
// value.toString() will cause an error if value is null or
// undefined. String(value) should not.
// https://stackoverflow.com/questions/3945202/whats-the-difference-between-stringvalue-vs-value-tostring
function sameNumbers(num) {
    // convert digit to array
    let myArr = String(num).split('').map((num) => {
        return Number(num)
    })

    let a = myArr[0]
    const len = myArr.length;
    let result = 'true';
    let total = 0;

    for (let item of myArr) {
        if (item != a) {
            result = 'false';
        }
        total += Number(item)
    }
        console.log(result);
        console.log(total);
    }

    //  The map() method creates a new array populated with the results of calling a provided function on every element in the calling array.
    // const map1 = array1.map(x => x * 2);
    sameNumbers(2222222)
    sameNumbers(1234)
    sameNumbers(1)
    