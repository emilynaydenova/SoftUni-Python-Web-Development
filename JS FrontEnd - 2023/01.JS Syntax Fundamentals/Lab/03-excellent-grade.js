function testGrade(num) {
    num = Number(num);
    if (num >= 5.50) {
        console.log("Excellent");
    } else {
        console.log("Not excellent");
    }
}

testGrade(5.50);
testGrade(4.35);