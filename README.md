# sshcracker
ssh弱密码破解。支持自定义目标ip和弱口令。每个ip都使用一个单独的线程破解。

## 安装依赖

执行 `pip install paramiko`

## 操作步骤：

1） 在 `IpText.txt` 中配置目标ip

2） 在 `Accounts.txt` 中配置要检测的用户名和密码。（忽略这步，则使用默认的弱口令）

3） 执行 `python run.py`

如果成功，则会打印 `<ip> user is: <username>, password is: <password>`