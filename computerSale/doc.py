description = r'''Given a computer sales system, main unit (25 ¥ unit price, the maximum monthly sales volume is 70),
monitor (30 ¥ unit price, the maximum monthly sales volume is 80), peripherals (45 ¥ unit price, the maximum monthly
sales volume is 90); each salesperson sells at least one complete machine every month. When the variable of the host
of the system receives a value of -1, the system automatically counts the salesperson's total sales this month. When
the sales volume is less than or equal to 1000 (including 1000), a 10% commission is charged; when the sales volume is
between 1000-1800 (including 1800), the commission is 15%, and when the sales volume is greater than 1800, the
commission is charged according to 20%. Use the boundary value method to design test cases.'''


md1 = r'''边界值法：37个测试用例

x主机的边界值（健壮性边界）：1， 2，35，69，70，0，71，-1

y显示器的边界值（健壮性边界）：1，2，40，79，80，0，81，-1

z外设的值边界（健壮性边界）：1，2，45，89，90，0，91，-1

佣金——设备基本边界值测试用例：13个'''


md2 = r'''健壮性边界的测试用例：9个'''


md3 = r'''直接根据设备销售数量基本边界值计算出的销售额都只在(1800,8200] 区间内，无法覆盖到其他的两个区间，所以以下对每个区间都设置了基本边界值用例，来测试销售额在不同区间内的佣金

销售额：$25x+30y+45z$

销售额区间：[100, 1000],  (1000,1800], (1800,8200] 

三个区间的基本边界值：

- [100, 1000]：100， 125，500，970，1000
- (1000,1800]：1005，1030,1400，1775，1800
- (1800,8200]：1805，1830，5000，8155，8200

佣金——销售额基本边界值测试用例:15个
'''


md4 = r'''所以总共的测试用例为：$13+9+15 = 37$ 个'''

md5 = r'''

x(主机)：单价25元，每月最多销量70台  ;  y(显示器)：单价30元，每月最多销量80台

z(外设)：单价45元，每月最多销量90台  ;  每个销售员每月至少销售一台完整的机器

commission(佣金)：当销售额<=1000按照10%提佣金，当销售额在1000-1800之间（包括1800）按照15%提佣金，当销售额>1800时按照20%提佣金

输入测试用例格式：x,y,z:commission


'''