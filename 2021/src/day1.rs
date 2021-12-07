use raoc::utils::{to_lines, to_parsed, to_parsed_deep, to_split_deep};

//#[aoc("test")]
#[aoc(2021, 1)]
pub fn first(input: String) -> usize {
    let input = to_parsed::<usize>(&to_lines(&input));

    let mut increase_counter = 0;
    for i in 0..input.len() {
        if i != 0 {
            if input[i] > input[i - 1] {
                increase_counter += 1;
            }
        }
    }

    increase_counter
}

//#[aoc("test")]
#[aoc(2021, 1)]
pub fn second(input: String) -> usize {
    let input = to_parsed::<usize>(&to_lines(&input));

    let mut three_window_sums: Vec<usize> = Vec::new();

    for i in 0..input.len() {
        if (i + 2) < input.len() {
            three_window_sums.push(input[i] + input[i + 1] + input[i + 2]);
        }
    }

    let mut increase_counter = 0;
    for i in 0..three_window_sums.len() {
        if i != 0 {
            if three_window_sums[i] > three_window_sums[i - 1] {
                increase_counter += 1;
            }
        }
    }

    increase_counter
}
