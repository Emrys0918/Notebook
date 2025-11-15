nvitop #显示显卡运行情况
nvidia-smi #显示显卡信息
ls #显示当前文件夹的内容
pwd #显示当前工作路径
mkdir #创建目录
rm #删除文件
rm -r #递归删除目录及内容
rm -rf #递归并强制删除
cp #复制
cp -r #递归复制
cat #显示文件内容
grep #在文件中搜索指定文本
ps aux #显示当前运行的进程
ps aux | grep xjq #显示含指定文本的进程
kill 进程id #关闭进程
ping #测试连通性
curl #也可以测试
wget URL #从URl下载文件
tar -czvf archive.tar.gz directory_name  # 压缩目录
tar -xzvf archive.tar.gz  # 解压文件
df -h  # 显示磁盘空间使用情况
du -h directory_name  # 显示目录的磁盘使用情况
du -sh # 当前文件夹使用情况
du -sh ./* #显示细节
source ~/.bashrc

    sftp 用户名@远程主机

    连接命令执行后，系统会提示用户输入密码。成功认证后，就可以开始文件传输操作。

    在SFTP会话中，用户可以使用多种命令来管理文件传输：

    pwd 和 lpwd：分别查看远程服务器和本地机器的当前目录。

    ls 和 lls：分别列出远程服务器和本地机器当前目录下的文件列表。

    put 文件名：将本地机器当前目录下的指定文件上传到远程服务器的当前目录。

    get 文件名：将远程服务器当前目录下的指定文件下载到本地机器的当前目录。

    !命令：在本地机器上执行指定的shell命令，例如!ls会列出本地机器当前目录下的文件。

    exit 或 quit：退出SFTP会话，返回到本地机器的shell。

    put 本地文件路径 远程文件路径

    get 远程文件路径 本地文件路径