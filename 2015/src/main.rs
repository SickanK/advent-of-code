#[macro_use]
extern crate raoc_macro;

mod day1;
mod day2;

// char iterator

fn main() {
    println!("First: {:?}", day2::first());
    println!("Second: {:?}", day2::second());
}
