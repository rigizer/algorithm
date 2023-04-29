# [Silver I] Escape Wall Maria - 24819 

[문제 링크](https://www.acmicpc.net/problem/24819) 

### 성능 요약

메모리: 116396 KB, 시간: 164 ms

### 분류

너비 우선 탐색, 그래프 이론, 그래프 탐색

### 문제 설명

<p>Wall Maria has been broken! Eren must evacuate as soon as possible from his house. He must find the fastest route to escape within Wall Maria before the titans rush in. Wall Maria is represented as a $N \times M$ grid in which Eren can move horizontally or vertically.</p>

<p>There are burning houses and buildings which prevent Eren from passing through them. The burning houses and buildings are represented as '<code>1</code>'. Unburned or safe areas are represented as '<code>0</code>'. There are some areas which can be entered but only from a specific direction. These areas can be represented by either '<code>U</code>', '<code>D</code>', '<code>L</code>', or '<code>R</code>'. For example, if there is an '<code>R</code>' that means that area can only be entered from the right neighboring tile within Wall Maria's grid. Similarly, '<code>U</code>' tiles can only be entered from above, '<code>D</code>' tiles can only be entered from below, and '<code>L</code>' tiles can only be entered from the left.</p>

<p>Eren knows the time $t$ at which the titans will rush in. It takes $1$ unit of time to traverse $1$ zone (which corresponds to $1$ tile in the grid). Once he reaches any border of Wall Maria he is safe. </p>

<p>Eren's starting position is represented by the letter '<code>S</code>'. If Eren escapes at or before time $t$, he is safe. Given his position within Wall Maria determine if it is possible to escape. If it is possible determine the number of zones that must be traversed to lead to the quickest escape. </p>

### 입력 

 <p>The input consists of a single test case. The first line contains three integers $t$ ($1 \le t \le 200$) , $N$ ($1 \le N \le 100$) and $M$ ($1 \le M \le 100$). The rest of N lines will be Wall Maria's grid containing characters '<code>1</code>', '<code>0</code>', '<code>S</code>', '<code>U</code>', '<code>D</code>', '<code>L</code>', or '<code>R</code>'. There is exactly one '<code>S</code>' in the input.</p>

### 출력 

 <p>If it is possible to escape Wall Maria, output the minimum number of zones that must be traversed to escape. If it is not possible to escape, print "<code>NOT POSSIBLE</code>"!</p>

