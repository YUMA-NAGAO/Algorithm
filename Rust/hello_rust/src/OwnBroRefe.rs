fn main(){
    let x= String::from("hello");
    let len=string_length(&x);
    println!("{}",len);
    println!("x is {}",x);
    let test=&len;
    println!("{}",test);

}
fn string_length(s:&String) ->usize{
    let length =s.len();
    length
}