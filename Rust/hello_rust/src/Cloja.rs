fn main(){
    let num=10;
    let add_one = |x| {num+x};
    let add_two = |x ,y| {x+y};

    let ans =add_one(1);
    println!("ans is {}",ans);
    let ans =add_two(10,20);
    let hello=ans;
    println!("{}",ans);
}

// 使用していない変数が存在すると、warningになる。
// 理由としては、無駄なメモリを確保しないため。