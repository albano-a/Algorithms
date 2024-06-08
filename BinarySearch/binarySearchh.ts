let BinarySearch = function (A: number[], T: number): number | null {
  let L: number = 0;
  let R: number = A.length - 1;

  while (L <= R) {
    let m: number = Math.floor((L + R) / 2);
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

let num: number[] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
let targ: number = 4;
let resul = BinarySearch(num, targ)

console.log(`Found ${targ} in position ${resul}`)