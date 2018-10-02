# ichw
**1.	用你的语言描述图灵为什么要证明停机问题, 其证明方法和数学原理是什么.**

图灵的停机问题为了证明：不存在一个算法，能够判断任意图灵机在运行某程序时是否停机。它由第三次数学危机罗素悖论引起，进一步阐释了高阶逻辑的不自洽性和不完备性。

证明过程如下：
如果存在一个算法可以判断任意一个图灵机在任意一个输入上是否停机，那么就可以设计这样一台图灵机：让它首先执行该算法判断自己在输入上是否停机。如果得出结论是停机，则让它进入一个死循环永不停机；如果结论是不停机，则让它立即停机。这样这台图灵机就在它停机的输入上不停机，在它不停机的输入上停机，产生悖论。结论是，不存在这样的算法。
运用的证明方法和数学原理是反证法；用一个高级的命令去控制图灵机完成一个于原本动作相矛盾的动作，使图灵机无法正确评估结果，以此找到假设中的矛盾。

**2.	你在向中学生做科普，请向他们解释二进制补码的原理.**

二进制补码是计算机的一种有符号整数表示法。相比于原码、反码的表示方法，它有诸多优势：1、它解决了计算机中对0不唯一表达的问题；2、它可将负数转化为正数，使减法转换为加法，从而使正负数的加减运算转换为单纯的正数相加运算，简化了判断过程，提高了计算机运行速度。因此补码成为最广泛的一种机器数表示方法。

若码长为N，

（1）对于正数X，第一位为0，后N-1位为该正数X本身。取值范围为0≤X≤2^(N-1)-1
  
（2）对于负数X，第一位为1，后N-1位为2^N-|X|=2^N+X.取值范围为-2^(N-1)≤X<0

**3.	某基于 IEEE 754浮点数格式的 16 bit 浮点数表示, 有 8 个小数位, 请给出 ±0, ±1.0, 最大非规范化数, 最小非规范化数, 最小规范化浮点数, 最大规范化浮点数,±∞, NaN 的二进制表示(表示形式请参照讲义).**

+0	0000000000000000

-0	1000000000000000

+1.0	0011111100000000

-1.0	1011111100000000

最大非规范化数	0000000011111111

最小非规范化数	1000000000000001

最小规范化浮点数	1000000100000000

最大规范化浮点数	0111111011111111

+∞	0111111100000000

-∞	1111111100000000

NaN	*1111111（Frac non zero）