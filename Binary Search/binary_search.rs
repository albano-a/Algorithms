fn binary_search(a: &[i32], t: i32) -> Option<usize> {
    let mut l = 0;
    let mut r = a.len() - 1;

    while l <= r {
        let m = (l + r) / 2;
        if a[m] < t {
            l = m + 1;
        } else if a[m] > t {
            r = m - 1;
        } else {
            return Some(m);
        }
    }
    return None
}

fn main() {
    let arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19];
    let target = 7;

    match binary_search(&arr, target) {
        Some(index) => println!("Found {} at index {}", target, index),
        None => println!("{} not found", target),
    }
}
