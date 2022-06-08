fn main() {
    let name = "heel";
    let age:i32 = 30;

    println!("{}",name);
    println!("{}",age);
    println!("{0},{1}",name,age);

    fn add(x:i32,y:i32) -> i32{
        x+y
    
    }
        
    println!("{}",add(age,age));
}
