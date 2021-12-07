use raoc::utils::{to_lines, to_parsed, to_parsed_deep, to_split_deep};

//#[aoc("test")]
#[aoc(2021, 2)]
pub fn first(input: String) -> isize {
    let input: Vec<Vec<String>> = to_split_deep(" ", &to_lines(&input));

    let mut coordinates: (isize, isize) = (0, 0);
    for i in input {
        let value: isize = i[1].parse::<isize>().unwrap();

        match i[0].as_str() {
            "forward" => coordinates.0 += value,
            "down" => coordinates.1 += value,
            "up" => coordinates.1 -= value,
            _ => (),
        }
    }

    coordinates.0 * coordinates.1
}

//#[aoc("test")]
#[aoc(2021, 2)]
pub fn second(input: String) -> isize {
    let input: Vec<Vec<String>> = to_split_deep(" ", &to_lines(&input));

    let mut coordinates: (isize, isize) = (0, 0);
    let mut aim: isize = 0;
    for i in input {
        let value: isize = i[1].parse::<isize>().unwrap();

        match i[0].as_str() {
            "forward" => {
                coordinates.0 += value;
                coordinates.1 += value * aim;
            }
            "down" => aim += value,
            "up" => aim -= value,
            _ => (),
        }
    }

    coordinates.0 * coordinates.1
}
