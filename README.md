# FFXIV-XianRenWeiCai
最终幻想14-Online 仙人微彩概率计算器。本计算器基于Python3开发完成。

## 什么是“仙人微彩计算器”？
通过已知的四个数字和位置，快速计算出剩余位置可能的数字并算出每行、每列和两条对角线的数字总合，并给出对应的金蝶币数量。贡使用者可以快速得出哪一行最容易中奖。

## 算法
目前采用两种算法：

* 最佳行：计算出各可能性下每一行、每一列和两条对角线所获得的金蝶币数量，求平均数。输出最大平均利润的行。
* 最大利润：计算出各可能性下每一行、每一列和两条对角线获得最多金蝶币（10000、3600、1800）的概率。输出获得10000、3600、1800金蝶币的最大可能性行。

# 如何使用
Windows用户可在[releases](https://github.com/cloudkylin/FFXIV-XianRenWeiCai/releases)中下载使用PyInstaller打包的exe文件。（可能不是最新版本）

或克隆本项目，直接运行Python文件，运行前请安装相关依赖库。

## 依赖 
* CLI：命令行版本。不需要依赖。
* GUI：图形界面版。需要安装Tkinter：
    * Tkinter在某些Python3安装包中已经内置，不需要单独安装。
    * 如未安装或不确定，可执行以下命令：
    * > pip install tkinter
* Web：服务器版。需安装Flask。（如在非本机运行，请先确定您服务器的Web服务可用）
    * > pip install flask

## 使用
在使用目录下执行以下操作：
> git clone https://github.com/cloudkylin/FFXIV-XianRenWeiCai.git

> cd FFXIV-XianRenWeiCai/

Windows用户可以点击页面右上角的`Clone or download`中的`Download ZIP`。


CLI和GUI版本可以执行以下命令启动：
> python3 CLI/Calculator.py

或
> python3 GUI/main.py

Web版请参考下个板块“配置”来配置您的服务器。

## 配置
CLI和GUI版本不需要配置，请看下一部分“使用”。

Web版需将本项目Web文件夹下的文件复制到您服务器的Web文件夹下，请确认可以通过您的域名访问。

修改index.html中第16行`action="http://127.0.0.1:5000"`为您服务器地址。然后执行以下操作来启用Flask监听。
> python3 Web/server.py

## Web版运行Demo：
[CloudKylin - 仙人微彩计算器](http://182.254.210.194/xrwc/)（可能无法访问）
