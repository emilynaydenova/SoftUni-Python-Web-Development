function arrayRotation(nums,rotations) {
    rotations %= nums.length;
     
    while (rotations > 0) {
        nums.push(nums.shift());
        rotations--;
    }

    console.log(...nums);
}

arrayRotation([51, 47, 32, 61, 21], 2);
arrayRotation([32, 21, 61, 1], 4);
arrayRotation([2, 4, 15, 31], 5);