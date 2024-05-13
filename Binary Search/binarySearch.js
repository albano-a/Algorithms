let binarySearch = function (A, T) {
  let L = 0;
  let R = A.length - 1;

  while (L <= R) {
    let m = Math.floor((L + R) / 2);
    if (A[m] < T) {
      L = m + 1;
    } else if (A[m] > T) {
      R = m - 1;
    } else {
      return m;
    }
  }
  return null;
};

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
let target = 4;
let result = binarySearch(numbers, target)

console.log(`Found ${target} in position ${result}`)
