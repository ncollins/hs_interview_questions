// merge sort, in javascript

// Array[Num] -> Array[Num]
function mergeSort(array) {
  if (array.length < 2) {
    // BASE CASE (already sorted)
    return array;
  }
  else {
    // MAIN CASE
    var left, right, middle, sortedLeft, sortedRight,
        winners;

    // STEP 1: split array in half
    middle = Math.floor(array.length/2);
    left = array.slice(0,middle);
    right = array.slice(middle,array.length);

    // STEP 2: recursively sort
    sortedLeft = mergeSort(left);
    sortedRight = mergeSort(right);

    // STEP 3: merge sorted arrays and return
    winners = [];
    while (sortedLeft.length>0 && sortedRight.length>0) {
      if (sortedLeft[0]<sortedRight[0]) {
        winners.push(sortedLeft.shift());
      }
      else if (sortedRight[0]<sortedLeft[0]) {
        winners.push(sortedRight.shift());
      }
    }

    return winners.concat(sortedLeft).concat(sortedRight);
  }
}
