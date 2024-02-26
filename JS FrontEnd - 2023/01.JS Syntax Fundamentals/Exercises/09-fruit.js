function fruit_calculation(fruit, weight, price) {

    let fruitType = fruit;
    let fruitWeight = weight;
    let pricePerKilo = price;

    let weightInKilos = fruitWeight / 1000;
    let money = weightInKilos * pricePerKilo;

    console.log(`I need $${money.toFixed(2)} to buy ${weightInKilos.toFixed(2)} kilograms ${fruitType}.`);
}



fruit_calculation('orange', 2500, 1.80);
fruit_calculation('apple', 1563, 2.35);


/*
function fruit(type,weightInGrams,pricePerKg){
    let weight = weightInGrams / 1000;
    let money = (weight * pricePerKg).toFixed(2);

    console.log(`I need $${money} to buy ${weight.toFixed(2)} kilograms ${type}.`)
}
*/