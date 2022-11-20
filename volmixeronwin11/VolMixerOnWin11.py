import wx
import wx.adv
import subprocess
import sys

class FolderBookmarkTaskBarIcon(wx.adv.TaskBarIcon):
    ICON = 'VolMixer.ico' # 图标
    TITLE = 'Volume Mixer' # 标题 会在托盘中显示
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
        menu.Append(self.MENU_ID_MIXER, '打开音量合成器')
        menu.Append(self.MENU_ID_SETTING, '打开声音设置')
        return menu
    # 操作
    def onLeftDown(self, event):
        subprocess.Popen("SndVol.exe")
    # def onRightDown(self, event):
    #     subprocess.Popen("SndVol.exe")
    def onLeftDoubleClick(self, event):
        subprocess.Popen("SndVol.exe")
    def onRightDoubleClick(self, event):
        subprocess.Popen("SndVol.exe")
    def onMenuMixer(self, event):
        subprocess.Popen("SndVol.exe")
    def onMenuSetting(self, event):
        subprocess.Popen(["control.exe","mmsys.cpl"])

class MainFrame(wx.Frame):
    def __init__(self):
        super().__init__()
        if len(sys.argv)>1:
            if sys.argv[1] == "help":
                wx.MessageBox("Volume Mixer On Windows 11\nVersion 1.0\nGitHub Repository: Keqing-Yuheng/VolMixerOnWin11\nURL: https://github.com/Keqing-Yuheng/VolMixerOnWin11 \nThis program is licensed under GPL.\n(C) 2022 Keqing-Yuheng", caption="Volume Mixer On Windows 11")
        FolderBookmarkTaskBarIcon()

class MainApp(wx.App):
    def OnInit(self):
        MainFrame()
        return True

if __name__ == "__main__":
    app = MainApp()
    app.MainLoop()