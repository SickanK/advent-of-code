use std::fmt;
use std::str::FromStr;

pub fn input_lines(input: &str) -> Vec<String> {
    let lines: Vec<&str> = input.lines().collect();
    let owned_lines: Vec<String> = lines.into_iter().map(|x| x.to_owned()).collect();

    owned_lines
}

pub fn split_lines<'a>(pat: &'a str, input: &Vec<String>) -> Vec<Vec<String>> {
    let split_input: Vec<Vec<&str>> = input
        .iter()
        .map(|x| x.split(pat).collect::<Vec<&str>>())
        .collect();

    let owned_split_input: Vec<Vec<String>> = split_input
        .into_iter()
        .map(|x| x.into_iter().map(|y| y.to_owned()).collect::<Vec<String>>())
        .collect();

    owned_split_input
}

pub fn parse_lines<P>(input: &Vec<String>) -> Vec<P>
where
    P: FromStr,
    <P as FromStr>::Err: fmt::Debug,
{
    let parsed_lines: Vec<P> = input
        .into_iter()
        .map(|y: &String| (&y).parse::<P>().unwrap())
        .collect::<Vec<P>>();

    parsed_lines
}

pub fn parse_split_of_lines<P>(input: &Vec<Vec<String>>) -> Vec<Vec<P>>
where
    P: FromStr,
    <P as FromStr>::Err: fmt::Debug,
{
    let parsed_split_of_lines: Vec<Vec<P>> = input
        .iter()
        .map(|x: &Vec<String>| {
            x.iter()
                .map(|y: &String| (&y).parse::<P>().unwrap())
                .collect::<Vec<P>>()
        })
        .collect();

    parsed_split_of_lines
}
