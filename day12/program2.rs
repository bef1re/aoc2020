use std::fs;

fn rotated(location:(i32, i32), delta:i32) -> (i32, i32) {
    match delta {
        90 =>  return (location.1, location.0 * -1),
        180 => return (location.0 * -1, location.1 * -1),
        270 => return (location.1 * -1, location.0),
        _ => panic!("Tried to rotate by something else than 90, 180 or 270")
    }
}

fn main() {
    let mut location = (10i32, 1i32);
    let mut ship_location = (0i32, 0i32);

    let content = fs::read_to_string("input.txt").expect("Reading input failed");

    for line in content.lines() {
        let (letter, num) = line.split_at(1);

        let amount: i32 = num.parse().expect("Second argument is not a number");

        match letter {
            "F" => {
                ship_location.0 += location.0 * amount;
                ship_location.1 += location.1 * amount;
            }
            "R" => location = rotated(location, amount),
            "L" => location = rotated(location, 360 - amount),
            "E" => location.0 += amount,
            "W" => location.0 -= amount,
            "N" => location.1 += amount,
            "S" => location.1 -= amount,

            _ => panic!("Halp, it's not a letter!")
        }
    }
    
    println!("{}", ship_location.0.abs() + ship_location.1.abs())
}
