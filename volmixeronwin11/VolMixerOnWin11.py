import wx
import wx.adv
import subprocess
import sys
import locale

global chs
chs = False; # chs==True----Simplified Chinese; chs==False----English

class FolderBookmarkTaskBarIcon(wx.adv.TaskBarIcon):
    # 设置语言
    lang = locale.getdefaultlocale()
    if lang[0] == "zh_CN":
        global chs
        chs = True
    # 图标
    ICON = 'VolMixer.ico'
    # 标题
    if chs:
        TITLE = '音量'
    else:
        TITLE = 'Volume'

    MENU_ID_MIXER, MENU_ID_SETTING = wx.NewIdRef(count=2)

    def __init__(self):
        super().__init__()
        self.SetIcon(wx.Icon(self.ICON), self.TITLE)
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.onLeftDown)
        # self.Bind(wx.adv.EVT_TASKBAR_RIGHT_DOWN, self.onRightDown)
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DCLICK, self.onLeftDoubleClick)
        self.Bind(wx.adv.EVT_TASKBAR_RIGHT_DCLICK, self.onRightDoubleClick)
        self.Bind(wx.EVT_MENU, self.onMenuMixer, id=self.MENU_ID_MIXER)
        self.Bind(wx.EVT_MENU, self.onMenuSetting, id=self.MENU_ID_SETTING)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        # 菜单项目名称
        if chs:
            menu.Append(self.MENU_ID_MIXER, '打开音量合成器')
            menu.Append(self.MENU_ID_SETTING, '打开声音设置')
        else:
            menu.Append(self.MENU_ID_MIXER, 'Volume Mixer')
            menu.Append(self.MENU_ID_SETTING, 'Volume Settings')
        return menu
    # 操作
    # 左键点击
    def onLeftDown(self, event):
        subprocess.Popen("SndVol.exe")
    # 右键点击(不使用以避免弹出菜单同时出现窗口)
    # def onRightDown(self, event):
    #     subprocess.Popen("SndVol.exe")
    # 左键双击
    def onLeftDoubleClick(self, event):
        subprocess.Popen("SndVol.exe")
    # 右键双击
    def onRightDoubleClick(self, event):
        subprocess.Popen("SndVol.exe")
    # 菜单
    def onMenuMixer(self, event):
        subprocess.Popen("SndVol.exe")
    # 菜单
    def onMenuSetting(self, event):
        subprocess.Popen(["control.exe","mmsys.cpl"])

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__()
        if len(sys.argv)>1: # 参数
            if sys.argv[1] == "help": # help 显示信息
                global chs
                if chs:
                    wx.MessageBox("Volume Mixer On Windows 11\n"
                                  "Version 1.1\n"
                                  "在Windows11的系统托盘上显示旧版音量合成器\n"
                                  "GitHub存储库: Keqing-Yuheng/VolMixerOnWin11\n"
                                  "链接: https://github.com/Keqing-Yuheng/VolMixerOnWin11 \n"
                                  "本程序以GPL协议授权\n"
                                  "(C) 2022 Keqing-Yuheng\n", caption = "Volume Mixer On Windows 11")
                else:
                     wx.MessageBox("Volume Mixer On Windows 11\n"
                                   "Version 1.1\n"
                                   "Put pervious Volume Mixer to system tray on Windows11\n"
                                   "GitHub Repository: Keqing-Yuheng/VolMixerOnWin11\n"
                                   "URL: https://github.com/Keqing-Yuheng/VolMixerOnWin11 \n"
                                   "This program is licensed under GPL.\n"
                                   "(C) 2022 Keqing-Yuheng\n", caption = "Volume Mixer On Windows 11")
                exit()
            if sys.argv[1] == "stop": # stop 停止所有的VolMixerOnWin11.exe
                subprocess.Popen(["taskkill.exe","/im","VolMixerOnWin11.exe","/f"])
                exit()
        FolderBookmarkTaskBarIcon()

class MainApp(wx.App):
    def OnInit(self):
        MainFrame()
        return True

if __name__ == "__main__":
    app = MainApp()
    app.MainLoop()