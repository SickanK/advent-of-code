use raoc;
mod day1;

// see if proc macro works with env variables

fn main() {
    match raoc::get_puzzle_input(2015, 1) {
        Ok(t) => day1::day1(t),
        _ => panic!(),
    };
}
