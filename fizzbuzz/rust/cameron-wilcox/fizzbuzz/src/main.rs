use std::{env, process};

fn main() {
    let args : Vec<String> = env::args().collect();
    if args.len() == 1 {
        println!("Need to have proper amount of arguments!");
        println!("Usage: cargo run {} -- <num>", args[0]);
        process::exit(1);
    }
    let up_to : i32 = args[1].parse::<i32>().unwrap();
    for x in 1..up_to+1 {
        // check for divisibility
        if is_divisible_by_three(x) {
            print!("Fizz");
        }
        if is_divisible_by_five(x) {
            print!("Buzz");
        }
        if !is_divisible_by_five(x) && !is_divisible_by_three(x) { // if not divisible by either, then print number
            print!("{}", x);
        }
        println!();
    }
}


// adding way too many functions because I'm trying rust out for the first time

fn is_divisible_by_three(x : i32) -> bool {
    if x % 3 == 0 {
        true
    }
    else {
        false
    }
}

fn is_divisible_by_five(x : i32) -> bool {
    if x % 5 == 0 {
        true
    }
    else {
        false
    }
}