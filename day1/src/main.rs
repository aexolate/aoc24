use std::io::{self, BufRead};
use std::path::Path;
use std::fs;

fn main() {
    day1::part1();
}

mod day1 {
    pub fn part1() {
        let input_path = "data/day1.in";

        let contents = std::fs::read_to_string(input_path)
            .expect("Should have been able to read the file");
    
        let mut list1: Vec<i32> = Vec::new();
        let mut list2: Vec<i32> = Vec::new();
    
        for line in contents.lines() {
            let numbers: Vec<i32> = line
                .split_whitespace()
                .filter_map(|s| s.parse::<i32>().ok())
                .collect();
    
                list1.push(numbers[0]);
                list2.push(numbers[1]);
            
        }
    
        assert!(list1.len() == list2.len(), "Lists are not the same length!");
    
        let mut total_distance = 0;
    
        while(!list1.is_empty()) {
            let min1 = *list1.iter().min().unwrap();
            let min2 = *list2.iter().min().unwrap();
    
            total_distance += (min1 - min2).abs();  // Add the distances
    
            if let Some(pos) = list1.iter().position(|&x| x == min1) {
                list1.remove(pos);
            }
            if let Some(pos) = list2.iter().position(|&x| x == min2) {
                list2.remove(pos);
            }
        }
    
        println!("{}", total_distance);
    }
}