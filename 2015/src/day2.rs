use raoc::utils::{input_lines, parse_split_of_lines, split_lines};
use raoc_macro::aoc;

// split by newline
// split every one of them with "x"
// make those numbers

//#[aoc("test")]
#[aoc(2015, 2)]
pub fn first(input: String) -> usize {
    let split = input_lines(&input);
    println!(
        "{:?}",
        parse_split_of_lines::<usize>(&split_lines("x", &split))
    );
    let split2: Vec<Vec<usize>> = split
        .into_iter()
        .map(|x| x.split("x").map(|x| x.parse::<usize>().unwrap()).collect())
        .collect();

    let mut totalsum: usize = 0;
    for p in split2 {
        let a1 = p[0] * p[1];
        let a2 = p[1] * p[2];
        let a3 = p[0] * p[2];
        totalsum += 2 * (a1 + a2 + a3);

        if a1 < a2 && a1 < a3 {
            totalsum += a1;
        } else if a2 < a3 {
            totalsum += a2
        } else {
            totalsum += a3;
        }
    }

    return totalsum;
}

//#[aoc("test")]
#[aoc(2015, 2)]
pub fn second(input: String) -> usize {
    let split: Vec<&str> = input.lines().collect();
    let split2: Vec<Vec<usize>> = split
        .into_iter()
        .map(|x| x.split("x").map(|x| x.parse::<usize>().unwrap()).collect())
        .collect();

    let mut total_ribbon: usize = 0;
    for p in split2 {
        total_ribbon += p[0] * p[1] * p[2];
        let mut p2 = p.clone();

        if p[0] > p[1] && p[0] > p[2] {
            p2.remove(0);
        } else if p[1] > p[2] {
            p2.remove(1);
        } else {
            p2.remove(2);
        }

        total_ribbon += 2 * (p2[0] + p2[1]);
    }

    return total_ribbon;
}
