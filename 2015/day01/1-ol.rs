use std::fs;

fn main() -> std::io::Result<()> {
    println!("{}", fs::read_to_string("input.txt")?
        .chars()
        .map(|c| match c {
            '(' => 1,
            ')' => -1,
            _   => 0,
        })
        .sum::<i32>());

    println!("{}", fs::read_to_string("input.txt")?
        .chars()
        .scan(0, |floor, c| {
            *floor += match c {
                '(' => 1,
                ')' => -1,
                _   => 0,
            };
            Some(*floor)
        })
        .enumerate()
        .find(|&(_, floor)| floor < 0)
        .map(|(i, _)| i + 1)
        .unwrap_or(0));
    Ok(())
}
