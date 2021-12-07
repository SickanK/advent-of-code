#[macro_use]
extern crate raoc_macro;

mod day1;
mod day2;
mod day3;

// char iterator

fn main() {
    println!("First: {:?}", day3::first());
    println!("Second: {:?}", day3::second());
}
