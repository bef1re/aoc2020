use std::fs;

fn rotated(direction:usize, delta:i32) -> usize {
    let delta_indexes: i32 = delta / 90;

    return ((direction as i32 + delta_indexes + 4) % 4) as usize;
}

fn main() {
    let mut location = (0i32, 0i32);
    let mut direction: usize = 0;
    let directions = vec!["E", "S", "W", "N"];

    let content = fs::read_to_string("input.txt").expect("Reading input failed");

    for line in content.lines() {
        let (mut letter, num) = line.split_at(1);

        let amount: i32 = num.parse().expect("Second argument is not a number");

        if letter == "F" {
            letter = directions[direction];
        }

        match letter {
            "R" => direction = rotated(direction, amount),
            "L" => direction = rotated(direction, amount * -1),
            "E" => location.0 += amount,
            "W" => location.0 -= amount,
            "N" => location.1 += amount,
            "S" => location.1 -= amount,

            _ => println!("Halp, it's not a letter!")
        }
    }
    
    println!("{}", location.0.abs() + location.1.abs())
}
