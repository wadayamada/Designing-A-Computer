# Designing-A-Computer
論理ゲートを使ってコンピュータを作ります

## 概要図
<img width="600" alt="スクリーンショット 2023-01-29 3 49 52" src="https://user-images.githubusercontent.com/31792905/215285512-3dde401e-c274-4438-a7f5-0c3d01ab97f6.png">


## 命令セット(TD4)
|  opecode  |  アセンブラ  | 概要　|
| ---- | ---- |----|
|  0001  |  MOV A, B  | A <- B|
|  0100  |  MOV B, A  | B <- A|
|  0011  |  MOV A, IMM | A <- IMM|
|  0111  |  MOV B, IMM | B <- IMM|
|  0010  |  IN A  | A <- IN|
|  0110  |  IN B  | B <- IN|
|  1001  |  OUT B  | OUT <- B|
|  1011  |  OUT IMM  |OUT <- IMM|
|  0000  |  ADD A, IMM  |A <- A+IMM|
|  0101  |  ADD B, IMM  |B <- B+IMM|
|  1111  |  JMP IMM  | IP <- IMM|
|  1110  |  JNC IMM  | if CF==0: JP <-IMM|
|  その他  |  未定義 |　使用禁止|

## お断り
権利的に問題があったらご連絡ください(wada0421514@gmail.com)。修正します。
## 参考
- [The Foundations of Computer Design \| Udemy](https://www.udemy.com/course/the-foundations-of-computer-design/)
- [作ろう！CPU: 基礎から理解するコンピューターのしくみ](https://www.amazon.co.jp/%E4%BD%9C%E3%82%8D%E3%81%86%EF%BC%81CPU-%E4%B8%8A%E5%8E%9F-%E5%91%A8-ebook/dp/B08GP3PPCX/ref=tmm_kin_swatch_0?_encoding=UTF8&qid=&sr=)
