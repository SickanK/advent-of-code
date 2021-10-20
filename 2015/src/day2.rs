use raoc::utils::{to_lines, to_parsed_deep, to_split_deep};

//#[aoc("test")]
#[aoc(2015, 2)]
pub fn first(input: String) -> usize {
    let input = to_parsed_deep::<usize>(&to_split_deep("x", &to_lines(&input)));

    let mut totalsum: usize = 0;
    for p in input {
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
    let input = to_parsed_deep::<usize>(&to_split_deep("x", &to_lines(&input)));

    let mut total_ribbon: usize = 0;
    for p in input {
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
