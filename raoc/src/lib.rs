use dotenv::dotenv;
use reqwest::header::COOKIE;
use std::{env, fs, io};

pub struct AocInput(String);

impl AocInput {
    pub fn from(input: String) {}
}

pub fn get_local_puzzle_input(path: &String) -> Result<String, io::Error> {
    fs::read_to_string(&path)
}

pub fn save_puzzle_input(input: &String, path: &String) {
    let dir_path: &str = &path.split("/").take(2).collect::<Vec<&str>>().join("/");

    match fs::read_dir(dir_path) {
        Ok(directory) => directory,
        Err(_) => {
            fs::create_dir(dir_path).expect("Input directory can't be created");
            fs::read_dir(dir_path).expect("Input directory can't be created or read")
        }
    };

    fs::write(path, input).unwrap()
}

pub fn get_puzzle_input(year: u16, day: u8) -> Result<AocInput, Box<dyn std::error::Error>> {
    dotenv().ok();

    let input_path = format!("./aoc_inputs/day{}", day);

    if let Ok(input_contents) = get_local_puzzle_input(&input_path) {
        return Ok(AocInput::from(input_contents));
    }

    let token: &str = &["session=", &env::var("TOKEN")?].join("");

    let client = reqwest::blocking::Client::new();
    let input_resp = client
        .get(format!(
            "https://adventofcode.com/{}/day/{}/input",
            year, day
        ))
        .header(COOKIE, token)
        .send()?
        .text()?;

    save_puzzle_input(&input_resp, &input_path);

    Ok(AocInput(input_resp))
}
