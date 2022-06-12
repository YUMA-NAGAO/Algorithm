A=[]

for _ in range(0,3):
    #備後カードの一行を受け取る
    # これは1次元配列となっている
    row=list(map(int,input().split()))
    # 受け取った一行分の配列をAの末尾に追加する
    # Aは一次元配列を要素とする配列であるため、Aは2次元配列である
    A.append(row)
    
#M=[[False,False,False],[False,False,False],[False,False,False]]
M=[]
for i in range(0,3):
    row=[]
    for j in range(0,3):
        row.append(False)
        
    M.append(row)
    

N=int(input())
# 選ばれた数字が備後カードに書かれているかを確認する

for _ in range(0,N):
    # 選ばれた数字
    b=int(input())
    
    # bが備後カードに書かれているかを調べる
    for i in range(0,3):
        for j in range(0,3):
            if A[i][j]==b:
                
                # もし備後カードのi行目j列目に数字bがあれば、
                #M[i][j]=Trueとして、印をつける
                M[i][j]=True    
                
                
                
# ビンゴが達成しているかを記録する変数
bingo=False

for i in range(0,3):
    #縦でできているかを確認する
    # i行目の3つに印が付いているか調べる
    # 印が付いていたらビンゴ達成となる
    if M[i][0] and M[i][1] and M[i][2]:
        bingo=True
    
for j in range(0,3):
    #横でできているかを確認する
    
    if M[0][j] and M[1][j] and M[2][j]:
        bingo=True
    

if M[0][0] and M[1][1] and M[2][2]:
    #左上から右下へのコピーができているか
    bingo=True

if M[0][2] and M[1][1] and M[2][0]:
    bingo=True

if bingo==True:
    #ここは、bingoだけで良い
    print("Yes") 
else:
    print("No")
    
                

#実際の問題
# https://atcoder.jp/contests/abc157/tasks/abc157_b

    
