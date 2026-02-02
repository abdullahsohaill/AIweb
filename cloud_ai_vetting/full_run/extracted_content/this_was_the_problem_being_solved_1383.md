# This was the problem being solved.
**URL:** https://atcoder.jp/contests/awtf2025heuristic/tasks/awtf2025heuristic_a
**Page Title:** A - Group Commands and Wall Planning
--------------------

World Tour Finals 2025 Heuristic has begun.
World Tour Finals 2025 Heuristic has ended.
- Top
- Tasks
- Clarifications
- Results All Submissions
- All Submissions
- Standings Standings(Exhibition) Standings Extended Standings Virtual Standings
- Standings(Exhibition)
- Standings
- Extended Standings
- Virtual Standings
- Editorial
Time Limit: 2 sec / Memory Limit: 1024 MiB

### 問題文

N × N N\times N N × N マスの盤面がある。
左上のマスの座標を ( 0 , 0 ) (0, 0) ( 0 , 0 ) とし、下方向に i i i 、右方向に j j j マス進んだ位置の座標を ( i , j ) (i, j) ( i , j ) とする。
一部の隣接マス間には壁が存在する。
盤面上には K K K 台のロボットが存在する。 k k k 番目のロボットの初期位置は ( i k , j k ) (i_k, j_k) ( i k ​ , j k ​ ) で、目的地は ( i k ′ , j k ′ ) (i_k', j_k') ( i k ′ ​ , j k ′ ​ ) である。
高橋くんはこれらのロボットを操作して、すべてのロボットが目的地に到達した状態を達成したい。
まずはじめに、以下の二種類の準備を行う。
- 最初からある壁に加え、任意の隣接マス間に壁を設置できる。
- ロボットをグループに分割する。各ロボットは1つのグループに属し、同じグループのロボットは同時に操作することができる。
これらの準備は最初の操作を行う前に行い、それ以降に新たに壁を設置したりグループを変更することはできない。
次に、以下の2種類の操作を繰り返し行うことでロボットを移動させる。
- グループ命令 : 1つのグループと上下左右の方向を指定し、そのグループに属するすべてのロボットがその方向に1マス移動する。移動先のマスとの間に壁があったり、移動先に他のロボットが存在する場合は移動しない。指定されたグループに属するロボットのうちで、指定した方向に最も進んだ先にあるものから順に移動する。例えば ( 1 , 0 ) (1,0) ( 1 , 0 ) と ( 2 , 0 ) (2,0) ( 2 , 0 ) にロボットがいる状態で上方向を指定した場合、 i i i 座標の小さい順に移動するため、まず ( 1 , 0 ) (1,0) ( 1 , 0 ) のロボットが ( 0 , 0 ) (0,0) ( 0 , 0 ) に移動し、次に ( 2 , 0 ) (2,0) ( 2 , 0 ) のロボットが空いた ( 1 , 0 ) (1,0) ( 1 , 0 ) のマスに移動する。
グループ命令 : 1つのグループと上下左右の方向を指定し、そのグループに属するすべてのロボットがその方向に1マス移動する。移動先のマスとの間に壁があったり、移動先に他のロボットが存在する場合は移動しない。指定されたグループに属するロボットのうちで、指定した方向に最も進んだ先にあるものから順に移動する。例えば ( 1 , 0 ) (1,0) ( 1 , 0 ) と ( 2 , 0 ) (2,0) ( 2 , 0 ) にロボットがいる状態で上方向を指定した場合、 i i i 座標の小さい順に移動するため、まず ( 1 , 0 ) (1,0) ( 1 , 0 ) のロボットが ( 0 , 0 ) (0,0) ( 0 , 0 ) に移動し、次に ( 2 , 0 ) (2,0) ( 2 , 0 ) のロボットが空いた ( 1 , 0 ) (1,0) ( 1 , 0 ) のマスに移動する。
- 個別命令 : 1台のロボットと上下左右の方向を指定し、指定したロボットがその方向に1マス移動する。移動先のマスとの間に壁があったり、移動先に他のロボットが存在する場合は移動しない。
個別命令 : 1台のロボットと上下左右の方向を指定し、指定したロボットがその方向に1マス移動する。移動先のマスとの間に壁があったり、移動先に他のロボットが存在する場合は移動しない。
一度目的地に到達しても、その後の操作によって目的地から離れた場合は、目的地に到達した状態とはみなされない。
操作は最大で K N 2 K N^2 K N 2 回行うことができる。
できるだけ少ない操作回数で、すべてのロボットを目的地へ誘導せよ。
操作回数を T T T 、ロボット k k k の最終位置と目的地とのマンハッタン距離を d k d_k d k ​ としたとき、以下の絶対スコアを獲得する。 T + 100 × ∑ k d k T + 100 \times \sum_k d_k T + 1 0 0 × k ∑ ​ d k ​
絶対スコアは小さければ小さいほど良い。
各テストケース毎に、 r o u n d ( 1 0 9 × 全参加者中の最小絶対スコア 自身の絶対スコア ) \mathrm{round}(10^9\times \frac{全参加者中の最小絶対スコア}{自身の絶対スコア}) r o u n d ( 1 0 9 × 自 身 の 絶 対 ス コ ア 全 参 加 者 中 の 最 小 絶 対 ス コ ア ​ ) の 相対評価スコア が得られ、その和が提出の得点となる。
最終順位はコンテスト終了後に実施されるより多くの入力に対するシステムテストにおける得点で決定される。
暫定テスト、システムテストともに、一部のテストケースで不正な出力や制限時間超過をした場合、そのテストケースの相対評価スコアは0点となり、そのテストケースにおいては「全参加者中の最小絶対スコア」の計算から除外される。
システムテストは CE 以外の結
果を得た一番最後の提出 に対してのみ行われるため、最終的に提出する解答を間違えないよう注意せよ。
- 暫定テスト: 50個
- システムテスト: 2000個、コンテスト終了後に seeds.txt (sha256=063a84b1c0dc9388b0996eed0bc645529c931c139bee6b8e0e84a4faf3e06c40) を公開
暫定テスト、システムテストともに、 CE 以外の結果を得た一番最後の提出のみが順位表に反映される。
相対評価スコアの計算に用いられる各テストケース毎の全参加者中の最小絶対スコアの算出においても、順位表に反映されている最終提出のみが用いられる。
順位表に表示されているスコアは相対評価スコアであり、新規提出があるたびに、相対評価スコアが再計算される。
一方、提出一覧から確認出来る各提出のスコアは各テストケース毎の絶対スコアをそのまま足し合わせたものであり、相対評価スコアは表示されない。
最新以外の提出の、現在の順位表における相対評価スコアを知るためには、再提出が必要である。
不正な出力や制限時間超過をした場合、提出一覧から確認出来るスコアは0となるが、順位表には正解したテストケースに対する相対スコアの和が表示されている。
実行時間には多少のブレが生じます。
また、システムテストでは同時に大量の実行を行うため、暫定テストに比べて数%程度実行時間が伸びる現象が確認されています。
そのため、実行時間制限ギリギリの提出がシステムテストで TLE となる可能性がありま
す。
プログラム内で時間を計測して処理を打ち切るか、実行時間に余裕を持たせるようお願いします。
入力は以下の形式で標準入力から与えられる。
- すべてのテストケースにおいて、 N = 30 N=30 N = 3 0 に固定されている。
- 10 ≤ K ≤ 100 10 \leq K \leq 100 1 0 ≤ K ≤ 1 0 0 を満たす。
- ( i k , j k ) (i_k, j_k) ( i k ​ , j k ​ ) は k k k 台目のロボットの初期位置を表す。
- ( i k ′ , j k ′ ) (i_k', j_k') ( i k ′ ​ , j k ′ ​ ) は k k k 台目のロボットの目的地を表す。
- すべての初期位置、すべての目的地はそれぞれ相異なるが、ロボット k k k の初期位置とロボット k ′ k' k ′ の目的地が等しい可能性はある。
- v i , 0 ⋯ v i , N − 2 v_{i,0} \cdots v_{i,N-2} v i , 0 ​ ⋯ v i , N − 2 ​ は長さ N − 1 N-1 N − 1 の 01 からなる文字列であり、その j j j 文字目 v i , j v_{i,j} v i , j ​ はマス ( i , j ) (i, j) ( i , j ) とマス ( i , j + 1 ) (i, j+1) ( i , j + 1 ) の間に壁がある ( 1 ) かない ( 0 ) かを表す。
- h i , 0 ⋯ h i , N − 1 h_{i,0} \cdots h_{i,N-1} h i , 0 ​ ⋯ h i , N − 1 ​ は長さ N N N の 01 からなる文字列であり、その j j j 文字目 h i , j h_{i,j} h i , j ​ はマス ( i , j ) (i, j) ( i , j ) とマス ( i + 1 , j ) (i+1, j) ( i + 1 , j ) の間に壁がある ( 1 ) かない ( 0 ) かを表す。
- すべてのマスは互いに到達可能であることが保証されている。
まず、設置する壁の情報を以下の形式で標準出力に出力せよ。
- v i , 0 ′ ⋯ v i , N − 2 ′ v_{i,0}' \cdots v_{i,N-2}' v i , 0 ′ ​ ⋯ v i , N − 2 ′ ​ は長さ N − 1 N-1 N − 1 の 01 からなる文字列であり、その j j j 文字目 v i , j ′ v_{i,j}' v i , j ′ ​ はマス ( i , j ) (i, j) ( i , j ) とマス ( i , j + 1 ) (i, j+1) ( i , j + 1 ) の間に壁を設置する（ 1 ）かしない（ 0 ）かを表す。
- h i , 0 ′ ⋯ h i , N − 1 ′ h_{i,0}' \cdots h_{i,N-1}' h i , 0 ′ ​ ⋯ h i , N − 1 ′ ​ は長さ N N N の 01 からなる文字列であり、その j j j 文字目 h i , j ′ h_{i,j}' h i , j ′ ​ はマス ( i , j ) (i, j) ( i , j ) とマス ( i + 1 , j ) (i+1, j) ( i + 1 , j ) の間に壁を設置する（ 1 ）かしない（ 0 ）かを表す。
- 最初から壁が存在する箇所は 0 と 1 のどちらを出力しても構わない。
次に、グループ分けの情報を以下の形式で標準出力に出力せよ。
- g k g_k g k ​ は k k k 番目のロボットの属するグループを表す 0 0 0 以上 K − 1 K-1 K − 1 以下の整数値である。 g k = g k ′ g_k = g_{k'} g k ​ = g k ′ ​ のとき、ロボット k k k と k ′ k' k ′ は同じグループに属する。
最後に、操作列を次の形式で標準出力に出力せよ。
- a t a_t a t ​ は t t t ターン目の操作の種類を指定する1文字である。グループ命令の場合は g 、個別命令の場合は i である。
- b t b_t b t ​ は t t t ターン目の操作対象のグループ番号もしくはロボット番号を表す 0 0 0 以上 K − 1 K-1 K − 1 以下の整数値である。ロボットが1台も属さないグループが指定された場合は、何も起こらない。
- d t d_t d t ​ は t t t ターン目の操作の方向を指定し、以下の1文字である。
- 上: U
- 下: D
- 左: L
- 右: R
例を見る

### 入力生成方法

r a n d ( L , U ) \mathrm{rand}(L, U) r a n d ( L , U ) を、 L L L 以上 U U U 以下の整数値を一様ランダムに生成する関数とする。
ロボットの台数 K K K を K = r a n d ( 10 , 100 ) K = \mathrm{rand}(10, 100) K = r a n d ( 1 0 , 1 0 0 ) により決定する。 ロボットの初期位置は、 N 2 N^2 N 2 個の座標の中から重複しないように一様ランダムに K K K 個選んで生成する。 ロボットの目的地も同様に、 N 2 N^2 N 2 個の座標の中から重複しないように一様ランダムに K K K 個選んで生成する。
壁の線分数 W W W を W = r a n d ( 0 , 2 ) W = \mathrm{rand}(0, 2) W = r a n d ( 0 , 2 ) により生成する。
以下を W W W 回繰り返す。
- 壁を生成する方向を上下左右からランダムに決定する。
- 壁の長さを L = r a n d ( 10 , 20 ) L = \mathrm{rand}(10, 20) L = r a n d ( 1 0 , 2 0 ) により生成する。
- 縦方向の壁の場合、始点 ( i , j ) (i, j) ( i , j ) を i = r a n d ( 5 , N − 5 ) , j = r a n d ( 4 , N − 6 ) i = \mathrm{rand}(5, N-5),\ j = \mathrm{rand}(4, N-6) i = r a n d ( 5 , N − 5 ) , j = r a n d ( 4 , N − 6 ) により選択する。ただし、これまでに生成された縦壁に使用された j j j と絶対値の差が 4 4 4 以下の j j j が選ばれた場合は、方向の選択からやり直す。 上方向の場合は v i − L + 1 , j , ⋯ , v i , j v_{i-L+1, j}, \cdots, v_{i, j} v i − L + 1 , j ​ , ⋯ , v i , j ​ を、下方向の場合は v i , j , ⋯ , v i + L − 1 , j v_{i, j}, \cdots, v_{i+L-1, j} v i , j ​ , ⋯ , v i + L − 1 , j ​ を 1 に設定する。ただし、盤面外にはみ出した部分は無視する。
- 横方向の壁の場合、始点 ( i , j ) (i, j) ( i , j ) を i = r a n d ( 4 , N − 6 ) , j = r a n d ( 5 , N − 5 ) i = \mathrm{rand}(4, N-6),\ j = \mathrm{rand}(5, N-5) i = r a n d ( 4 , N − 6 ) , j = r a n d ( 5 , N − 5 ) により選択する。ただし、これまでに生成された横壁に使用された i i i と絶対値の差が 4 4 4 以下の i i i が選ばれた場合は、方向の選択からやり直す。 左方向の場合は h i , j − L + 1 , ⋯ , h i , j h_{i, j-L+1}, \cdots, h_{i, j} h i , j − L + 1 ​ , ⋯ , h i , j ​ を、右方向の場合は h i , j , ⋯ , h i , j + L − 1 h_{i, j}, \cdots, h_{i, j+L-1} h i , j ​ , ⋯ , h i , j + L − 1 ​ を 1 に設定する。ただし、盤面外にはみ出した部分は無視する。
- 生成した壁に対し、すべてのマスが到達可能であるかを判定する。到達不能な場合は壁を初期化し、 W W W 回の反復をやり直す。

### ツール(入力ジェネレータ・ビジュアライザ)

- Web版 : ローカル版より高性能でアニメーション表示が可能です。
- ローカル版 : 使用するには Rust言語 のコンパイル環境をご用意下さい。 Windows用のコンパイル済みバイナリ : Rust言語の環境構築が面倒な方は代わりにこちらをご利用下さい。
- Windows用のコンパイル済みバイナリ : Rust言語の環境構築が面倒な方は代わりにこちらをご利用下さい。
コンテスト期間中に、ビジュアライズ結果の共有や、解法・考察に関する言及は禁止されています。ご注意下さい。

### 入力例 1 Copy

### 出力例 1 Copy

### Problem Statement

There is an N × N N \times N N × N grid.
The coordinate of the top-left cell is ( 0 , 0 ) (0, 0) ( 0 , 0 ) , and the coordinate of the cell i i i rows down and j j j columns to the right is ( i , j ) (i, j) ( i , j ) .
There are walls between some adjacent cells.
There are K K K robots on the grid.
The initial position of the k k k -th robot is ( i k , j k ) (i_k, j_k) ( i k ​ , j k ​ ) , and its destination is ( i k ′ , j k ′ ) (i_k', j_k') ( i k ′ ​ , j k ′ ​ ) .
Takahashi wants to operate these robots to bring all of them to their respective destinations.
Before making any moves, the following two types of preparations can be made:
- In addition to the existing walls, you may add walls between any adjacent cells.
- Divide the robots into groups. Each robot belongs to exactly one group, and all robots in the same group can be operated simultaneously.
These preparations must be completed before the first move. After that, no additional walls can be placed and the group assignments cannot be changed.
Next, the robots can be moved by repeatedly performing the following two types of operations:
- Group Command : Specify a group and a direction (up, down, left, or right). All robots in that group will attempt to move one cell in the specified direction. If there is a wall between the current and target cells, or if another robot is occupying the target cell, the robot does not move. Among the robots belonging to the group, those farthest in the direction of movement will attempt to move first. For example, if robots are at ( 1 , 0 ) (1, 0) ( 1 , 0 ) and ( 2 , 0 ) (2, 0) ( 2 , 0 ) and the direction is up, the robot at ( 1 , 0 ) (1, 0) ( 1 , 0 ) will move to ( 0 , 0 ) (0, 0) ( 0 , 0 ) first (since it has a smaller i i i coordinate), and then the robot at ( 2 , 0 ) (2, 0) ( 2 , 0 ) will move to the now-empty ( 1 , 0 ) (1, 0) ( 1 , 0 ) .
Group Command : Specify a group and a direction (up, down, left, or right). All robots in that group will attempt to move one cell in the specified direction. If there is a wall between the current and target cells, or if another robot is occupying the target cell, the robot does not move. Among the robots belonging to the group, those farthest in the direction of movement will attempt to move first. For example, if robots are at ( 1 , 0 ) (1, 0) ( 1 , 0 ) and ( 2 , 0 ) (2, 0) ( 2 , 0 ) and the direction is up, the robot at ( 1 , 0 ) (1, 0) ( 1 , 0 ) will move to ( 0 , 0 ) (0, 0) ( 0 , 0 ) first (since it has a smaller i i i coordinate), and then the robot at ( 2 , 0 ) (2, 0) ( 2 , 0 ) will move to the now-empty ( 1 , 0 ) (1, 0) ( 1 , 0 ) .
- Individual Command : Specify a robot and a direction (up, down, left, or right). The specified robot will attempt to move one cell in the specified direction. If there is a wall between the current and target cells, or if another robot is occupying the target cell, the robot does not move.
Individual Command : Specify a robot and a direction (up, down, left, or right). The specified robot will attempt to move one cell in the specified direction. If there is a wall between the current and target cells, or if another robot is occupying the target cell, the robot does not move.
Even if a robot reaches its destination once, if it moves away from the destination due to subsequent operations, it is not considered to have reached its destination.
You may perform at most K N 2 K N^2 K N 2 operations.
Guide all robots to their destinations using as few operations as possible.

### Scoring

Let T T T be the number of operations performed, and let d k d_k d k ​ be the Manhattan distance between the final position and the destination of robot k k k . Then, you obtain the following absolute score: T + 100 × ∑ k d k T + 100 \times \sum_k d_k T + 1 0 0 × k ∑ ​ d k ​
The lower the absolute score, the better.
For each test case, we compute the relative score r o u n d ( 1 0 9 × M I N Y O U R ) \mathrm{round}(10^9\times \frac{\mathrm{MIN}}{\mathrm{YOUR}}) r o u n d ( 1 0 9 × Y O U R M I N ​ ) , where YOUR is your absolute score and MIN is the lowest absolute score among all competitors obtained on that test case. The score of the submission is the sum of the relative scores.
The final ranking will be determined by the system test with more inputs which will be run after the contest is over.
In both the provisional/system test, if your submission produces illegal output or exceeds the time limit for some test cases, only the score for those test cases will be zero, and your submission will be excluded from the MIN calculation for those test cases.
The system test will be performed only for the last submission which received a result other than CE .
Be careful not to make a mistake in the final submission.
- Provisional test: 50
- System test: 2000. We will publish seeds.txt (sha256=063a84b1c0dc9388b0996eed0bc645529c931c139bee6b8e0e84a4faf3e06c40) after the contest is over.
In both the provisional/system test, the standings will be calculated using only the last submission which received a result other than CE .
Only the last submissions are used to calculate the MIN for each test case when calculating the relative scores.
The scores shown in the standings are relative, and whenever a new submission arrives, all relative scores are recalculated.
On the other hand, the score for each submission shown on the submissions page is the sum of the absolute score for each test case, and the relative scores are not shown.
In order to know the relative score of submission other than the latest one in the current standings, you need to resubmit it.
If your submission produces illegal output or exceeds the time limit for some test cases, the score shown on the submissions page will be 0, but the standings show the sum of the relative scores for the test cases that were answered correctly.
Execution time may vary slightly from run to run.
In addition, since system tests simultaneously perform a large number of executions, it has been observed that execution time increases by several percent compared to provisional tests.
For these reasons, submissions that are very close to the time limit may result in TLE in the system test.
Please measure the execution time in your program to terminate the process, or have enough margin in the execution time.

### Input

Input is given from Standard Input in the following format.
- In all test cases, N = 30 N=30 N = 3 0 is fixed.
- 10 ≤ K ≤ 100 10 \leq K \leq 100 1 0 ≤ K ≤ 1 0 0
- ( i k , j k ) (i_k, j_k) ( i k ​ , j k ​ ) represents the initial position of the k k k -th robot.
- ( i k ′ , j k ′ ) (i_k', j_k') ( i k ′ ​ , j k ′ ​ ) represents the destination of the k k k -th robot.
- All initial positions and all destinations are each mutually distinct, but the initial position of robot k k k may coincide with the destination of robot k ′ k' k ′ .
- Each v i , 0 ⋯ v i , N − 2 v_{i,0} \cdots v_{i,N-2} v i , 0 ​ ⋯ v i , N − 2 ​ is a binary string of length N − 1 N-1 N − 1 . The j j j -th character v i , j v_{i,j} v i , j ​ indicates whether there is a wall ( 1 ) or not ( 0 ) between cells ( i , j ) (i, j) ( i , j ) and ( i , j + 1 ) (i, j+1) ( i , j + 1 ) .
- Each h i , 0 ⋯ h i , N − 1 h_{i,0} \cdots h_{i,N-1} h i , 0 ​ ⋯ h i , N − 1 ​ is a binary string of length N N N . The j j j -th character h i , j h_{i,j} h i , j ​ indicates whether there is a wall ( 1 ) or not ( 0 ) between cells ( i , j ) (i, j) ( i , j ) and ( i + 1 , j ) (i+1, j) ( i + 1 , j ) .
- It is guaranteed that all cells are mutually reachable.

### Output

First, output the wall placement information in the following format to Standard Output.
- Each v i , 0 ′ ⋯ v i , N − 2 ′ v_{i,0}' \cdots v_{i,N-2}' v i , 0 ′ ​ ⋯ v i , N − 2 ′ ​ is a binary string of length N − 1 N-1 N − 1 . The j j j -th character v i , j ′ v_{i,j}' v i , j ′ ​ indicates whether a wall is placed ( 1 ) or not ( 0 ) between cells ( i , j ) (i, j) ( i , j ) and ( i , j + 1 ) (i, j+1) ( i , j + 1 ) .
- Each h i , 0 ′ ⋯ h i , N − 1 ′ h_{i,0}' \cdots h_{i,N-1}' h i , 0 ′ ​ ⋯ h i , N − 1 ′ ​ is a binary string of length N N N . The j j j -th character h i , j ′ h_{i,j}' h i , j ′ ​ indicates whether a wall is placed ( 1 ) or not ( 0 ) between cells ( i , j ) (i, j) ( i , j ) and ( i + 1 , j ) (i+1, j) ( i + 1 , j ) .
- For positions where a wall already exists, either 0 or 1 may be output.
Next, output the group assignment information to Standard Output in the following format.
- g k g_k g k ​ is an integer between 0 0 0 and K − 1 K-1 K − 1 representing the group to which the k k k -th robot belongs. If g k = g k ′ g_k = g_{k'} g k ​ = g k ′ ​ , then robot k k k and robot k ′ k' k ′ belong to the same group.
Finally, output the sequence of operations to Standard Output in the following format.
- a t a_t a t ​ is a single character specifying the type of operation on turn t t t . Use g for a group command and i for an individual command.
- b t b_t b t ​ is an integer between 0 0 0 and K − 1 K-1 K − 1 representing the group number or robot number targeted by the operation on turn t t t . If a group with no robots is specified, nothing happens.
- d t d_t d t ​ is a single character indicating the direction of the operation on turn t t t , as follows: Up: U Down: D Left: L Right: R
- Up: U
- Down: D
- Left: L
- Right: R
Show example

### Input Generation

Let r a n d ( L , U ) \mathrm{rand}(L, U) r a n d ( L , U ) be a function that generates a uniformly random integer between L L L and U U U , inclusive.
The number of robots K K K is determined by K = r a n d ( 10 , 100 ) K = \mathrm{rand}(10, 100) K = r a n d ( 1 0 , 1 0 0 ) . The initial positions of the robots are chosen by selecting K K K distinct coordinates uniformly at random from the N 2 N^2 N 2 cells. The destinations of the robots are similarly chosen by selecting K K K distinct coordinates uniformly at random from the N 2 N^2 N 2 cells.
The number of wall segments W W W is determined by W = r a n d ( 0 , 2 ) W = \mathrm{rand}(0, 2) W = r a n d ( 0 , 2 ) .
Repeat the following W W W times:
- Randomly choose the direction of the wall from up, down, left, or right.
- Determine the wall length L = r a n d ( 10 , 20 ) L = \mathrm{rand}(10, 20) L = r a n d ( 1 0 , 2 0 ) .
- For vertical walls, choose the starting point ( i , j ) (i, j) ( i , j ) by i = r a n d ( 5 , N − 5 ) , j = r a n d ( 4 , N − 6 ) i = \mathrm{rand}(5, N-5),\ j = \mathrm{rand}(4, N-6) i = r a n d ( 5 , N − 5 ) , j = r a n d ( 4 , N − 6 ) . If the chosen j j j is within an absolute distance of 4 4 4 from any j j j used in previously generated vertical walls, redo the direction selection. For upward walls, set v i − L + 1 , j , ⋯ , v i , j v_{i-L+1, j}, \cdots, v_{i, j} v i − L + 1 , j ​ , ⋯ , v i , j ​ to 1 . For downward walls, set v i , j , ⋯ , v i + L − 1 , j v_{i, j}, \cdots, v_{i+L-1, j} v i , j ​ , ⋯ , v i + L − 1 , j ​ to 1 . Ignore any part that goes out of bounds.
- For horizontal walls, choose the starting point ( i , j ) (i, j) ( i , j ) by i = r a n d ( 4 , N − 6 ) , j = r a n d ( 5 , N − 5 ) i = \mathrm{rand}(4, N-6),\ j = \mathrm{rand}(5, N-5) i = r a n d ( 4 , N − 6 ) , j = r a n d ( 5 , N − 5 ) . If the chosen i i i is within an absolute distance of 4 4 4 from any i i i used in previously generated horizontal walls, redo the direction selection. For leftward walls, set h i , j − L + 1 , ⋯ , h i , j h_{i, j-L+1}, \cdots, h_{i, j} h i , j − L + 1 ​ , ⋯ , h i , j ​ to 1 . For rightward walls, set h i , j , ⋯ , h i , j + L − 1 h_{i, j}, \cdots, h_{i, j+L-1} h i , j ​ , ⋯ , h i , j + L − 1 ​ to 1 . Ignore any part that goes out of bounds.
- After generating the wall, check whether all cells are still mutually reachable. If not, reset the wall and restart the W W W iterations.

### Tools (Input generator and visualizer)

- Web version : This is more powerful than the local version providing animations and manual play.
- Local version : You need a compilation environment of Rust language . Pre-compiled binary for Windows : If you are not familiar with the Rust language environment, please use this instead.
- Pre-compiled binary for Windows : If you are not familiar with the Rust language environment, please use this instead.
Please be aware that sharing visualization results or discussing solutions/ideas during the contest is prohibited.

### Sample Input 1 Copy

### Sample Output 1 Copy

2026-01-26 (Mon) 03:24:09 +05:00

--------------------