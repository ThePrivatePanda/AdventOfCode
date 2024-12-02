use std::fs;

fn main() -> std::io::Result<()> {
    let inp = fs::read_to_string("input.txt")?;

    // Part 1
    let mut curr_floor = 0;
    for c in inp.chars() {
        if c == '(' {
            curr_floor += 1;
        } else if c == ')' {
            curr_floor -= 1;
        }
    }
    println!("{}", curr_floor);

    // Part 2
    let mut curr_floor = 0;
    for (index, c) in inp.chars().enumerate() {
        if c == '(' {
            curr_floor += 1;
        } else if c == ')' {
            curr_floor -= 1;
        }
        if curr_floor < 0 {
            println!("{}", index + 1);
            break;
        }
    }

    Ok(())
}
