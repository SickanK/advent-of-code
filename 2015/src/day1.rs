#[aoc(2015, 1)]
pub fn first(input: String) -> isize {
    let mut floor: isize = 0;

    for stair in input.chars() {
        if stair == '(' {
            floor += 1;
        } else if stair == ')' {
            floor -= 1;
        }
    }

    return floor;
}

//#[aoc("test")]
#[aoc(2015, 1)]
pub fn second(input: String) -> usize {
    let mut floor: isize = 0;
    let mut counter: usize = 0;

    for stair in input.chars() {
        counter += 1;

        if stair == '(' {
            floor += 1;
        } else if stair == ')' {
            floor -= 1;
        }

        if floor == -1 {
            return counter;
        }
    }

    return 0;
}
