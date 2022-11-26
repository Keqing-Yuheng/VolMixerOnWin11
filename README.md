# VolMixerOnWin11
Put pervious Volume Mixer to system tray on Windows11.  
在Windows11的系统托盘上显示旧版音量合成器  

**Version 1.1**  
简体中文 | [English](https://github.com/Keqing-Yuheng/VolMixerOnWin11/blob/main/README-English.md "README-English.md")

Windows 11移除了音量控制中旧版的"音量合成器"的入口，取而代之的是在"设置"窗口中打开的新版音量合成器，但新版音量合成器不论是响应速度还是直观性都不如旧版。使用VolMixerOnWin11，可以在系统托盘创建图标，以快速调出旧版音量合成器。  

## 使用方法
**运行`VolMixerOnWin11.exe`即可启动主程序**  

**命令行参数**  
`VolMixerOnWin11.exe [stop|help]`  
- 使用`stop`参数将结束所有VolMixerOnWin11.exe  
- 使用`help`参数可显示程序信息  

运行`VolMixerOnWin11Config.exe`可启动配置向导(仅支持简体中文)，其中可执行上述命令行用法  

**设置开机自启动**  
- 方法1: 将VolMixerOnWin11程序组或主程序快捷方式放置在`启动`文件夹中  
  `启动`文件夹可通过在运行中输入`shell:common startup`(系统)或`shell:startup`(用户)打开  
- 方法2: 使用任务计划程序创建计划任务  

**结束运行**  
运行`VolMixerOnWin11.exe stop`，或在配置向导中选择"停止进程"，即可结束运行  
上述方法均通过运行`taskkill /im VolMixerOnWin11.exe /f`实现  
**注意: 若更改主程序名称，对程序运行的检测与停止将失效!**  
*如果没有stop/help参数，程序启动后不会运行主动停止的代码。作为系统功能的替代，程序与系统同时启动、同时关闭是很正常的。此外，为了更好地融入系统，程序中不包含多余的交互(如在菜单中添加"退出"选项)，因此无法实现控制自身停止的功能*  

**设置托盘图标**  
将ico格式的图标命名为`VolMixer.ico`并与主程序置于同一目录即可  
缺失`VolMixer.ico`会在启动时出现故障，并在系统托盘显示透明图标(不影响功能)  

**语言**  
VolMixerOnWin11主程序支持**简体中文(Simplified Chinese)**与**英文(English)**。检测到系统语言为简体中文则显示简体中文，为其他语言则显示英文  
VolMixerOnWin11配置向导仅支持**简体中文(Simplified Chinese)**  

## 原理
旧版音量合成器`SndVol.exe`并未从系统中移除，VolMixerOnWin11通过在系统托盘提供`SndVol.exe`的入口来打开音量合成器  

## 更新内容(v1.1 - 2022.11)
- 主程序优化语言显示  
- 主程序添加命令行`stop`参数  
- 新增VolMixerOnWin11配置向导  

## 备注
- [v1.0]*似乎GitHub上已有其他提供这个功能的存储库，但其功能仍不够完善，且长期未更新。这个项目仍从相似的基础功能着手，但后续将加入更丰富的功能，以解决需要2个音量按钮的问题。*  
- [v1.1]*Windows 11的**Xbox Game Bar**提供了一个极好的音量合成器，且可以通过Windows+G键快速打开，但其仍存在一些缺陷，如首次启动稍慢和无法通过键盘或鼠标滚轮控制，以及和SndVol.exe一样不显示具体音量值*  
- 本程序以GPL协议授权  