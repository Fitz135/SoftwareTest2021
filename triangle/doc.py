md1 = r'''
假设 $1< a, b, c< 100$

基本边界值（最小值、略高于最小值、正常值、略低于最大值、最大值）：1， 2， 50， 99， 100'''

md2 = r'''健壮性边界（略低于最小值、最小值、略高于最小值、正常值、略低于最大值、最大值、略高于最大值）： 0， 1， 2， 50， 99， 100， 101
'''

md3 = r'''根据程序的输出可以划分4个等价类

$$
\begin{aligned}
&\mathrm{R} 1=\{ \langle\mathrm{a}, \mathrm{b}, \mathrm{c}\rangle: \text { 有三条边 } \mathrm{a}, \mathrm{b} \text { 和 } \mathrm{c} \text { 的等边三角形 }\}\\
&\mathrm{R} 2=\{ \langle\mathrm{a}, \mathrm{b}, \mathrm{c}\rangle: \text { 有三条边 } \mathrm{a}, \mathrm{b} \text { 和 } \mathrm{c} \text { 的等腰三角形 }\}\\
&\mathrm{R} 3=\{ \langle\mathrm{a}, \mathrm{b}, \mathrm{c}\rangle: \text { 有三条边 } \mathrm{a}, \mathrm{b} \text { 和 } \mathrm{c} \text { 的不等边三角形 }\}\\
&\mathrm{R} 4=\{ \langle\mathrm{a}, \mathrm{b}, \mathrm{c}\rangle: \text { 三条边 } \mathrm{a}, \mathrm{b}\text { 和 c 不构成三角形 }\}
\end{aligned}
$$

弱一般等价类共有4个测试用例，与强一般等价类的测试用例个数相同。
'''

md4 = r'''在考虑等价类的健壮情况时，需要从输入变量入手。同时需要考虑三条边为0的情况。

额外弱健壮等价类测试用例如下表所示：
'''

md5 = r'''根据额外强健壮等价类设计思想，变量a，b，c可能一个无效，可能两个无效，或者三个都无效。

强健壮等价类测试用例数量：$$C_{3}^{1} C_{2}^{1} + C_{3}^{2} C_{2}^{1} C_{2}^{1} + C_{3}^{2} C_{2}^{1} C_{2}^{1} C_{2}^{1} =26$$

部分额外的强健壮等价类测试用例如下表
'''