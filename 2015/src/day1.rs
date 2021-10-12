use raoc_macro::aoc;

#[aoc("test")]
pub fn first(input: String) {
    let mut floor: isize = 0;

    for stair in input.chars() {
        if stair == '(' {
            floor += 1;
            println!("up");
        } else if stair == ')' {
            println!("down");
            floor -= 1;
        }
    }

    println!("{}", floor);
}

#[aoc(2015, 1)]
pub fn second(i: String) {}
