md = r'''| 状态               | Case1 | Case2 | Case3 | Case4 | Case5 | Case6 | Case7 |
| ------------------ | ----- | ----- | ----- | ----- | ----- | ----- | ----- |
| 空闲               | 1     | 1     | 1     | 1     | 1     | 1     | 1     |
| 等待输入密码       | 2     | 2     | 2     | 2     | 2     | 2     | 2     |
| 等待第二次输入密码 |       | 3     | 3     | 3     | 3     | 3     |       |
| 等待第三次输入密码 |       |       | 4     | 4     | 4     |       |       |
| 进入账户           | 3     | 4     | 5     |       |       |       |       |
| 吞卡               |       |       |       |       | 5     | 4     | 3     |
| 退卡               | 4     | 5     | 6     | 5     |       |       |       |

case对应的操作分别为：

+ Case1: 1.插入银行卡 2.输入密码正确 3. 操作结束
+ Case2: 1.插入银行卡 2.输入密码错误 3.输入密码正确 4.操作结束
+ Case3: 1.插入银行卡 2.输入密码错误 3.输入密码错误 4.输入密码正确  5.操作结束
+ Case4: 1.插入银行卡 2.输入密码错误 3.输入密码错误 4.输入密码错误 
+ Case5: 1.插入银行卡 2.输入密码错误 3.输入密码错误 4.超过2分钟未操作 
+ Case6: 1.插入银行卡 2.输入密码错误 3.超过2分钟未操作 
+ Case7: 1.插入银行卡 2.超过2分钟未操作 '''

md1 = r'''   Build the state transition diagram of ATM system, 
use the state transition testing method to convert it into transition tree, 
and then design test cases based on the path of transition tree, considering the robustness.  '''