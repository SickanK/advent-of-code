use dotenv::dotenv;
use reqwest::header::COOKIE;
use std::env;

pub struct Gold {
    year: u16,
    day: u8,
    ops: Box<dyn Fn(AocInput)>,
}

impl Gold {
    pub fn run(&self) -> Result<(), Box<dyn std::error::Error>> {
        (self.ops)(get_puzzle_input(self.year, self.day)?);

        Ok(())
    }
}

pub struct Silver {
    year: u16,
    day: u8,
    ops: Box<dyn Fn(AocInput)>,
}

impl Silver {
    pub fn run(&self) -> Result<(), Box<dyn std::error::Error>> {
        (self.ops)(get_puzzle_input(self.year, self.day)?);

        Ok(())
    }
}

#[derive(Debug)]
pub struct AocInput(String);

pub fn get_puzzle_input(year: u16, day: u8) -> Result<AocInput, Box<dyn std::error::Error>> {
    dotenv().ok();

    let token: &str = &["session=", &env::var("TOKEN")?].join("");

    let client = reqwest::blocking::Client::new();
    let resp = client
        .get(format!(
            "https://adventofcode.com/{}/day/{}/input",
            year, day
        ))
        .header(COOKIE, token)
        .send()?
        .text()?;

    Ok(AocInput(resp))
}
