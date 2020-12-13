use std::fs;

fn main() {
    let content = fs::read_to_string("input.txt").expect("Reading input failed");
    let busses = content.lines().skip(1).next().expect("Input file is invalid");
    
    let mut bustimes: Vec<i64> = vec![];

    for bus in busses.split(",") {
        if bus == "x" {
            bustimes.push(-1);
        }
        else {
            bustimes.push(bus.parse().expect("bus line not 'x' nor a number"));
        }
    }

    let mut stepsize: i64 = 0;
    let mut counter: i64 = 0;

    for (i, &time) in bustimes.iter().enumerate() {
        if time < 0 { continue; }
        
        if i == 0 {
            stepsize = time;
        } else {
            while (counter + i as i64) % time != 0 {
                counter += stepsize;
            }
            stepsize *= time;
            println!("Increasing stepsize to {}", stepsize);
        }
    }

    println!("The counter ended on: {:?}", counter);
}
