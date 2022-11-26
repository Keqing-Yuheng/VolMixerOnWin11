#include<cstdio>
#include<cstdlib>
#include<conio.h>
#include<Windows.h>

const char* VER = "Version 1.1";

void taskkill();
void about();

inline void vmc_title()
{
	printf_s(
		"|========================================\n"
		"|\n"
		"|  配置向导 - Windows11音量合成器\n"
		"|  GitHub: Keqing-Yuheng/VolMixerOnWin11\n"
		"|  %s\n"
		"|\n"
		"|========================================\n"
	,VER);
}

int main(int argc, char* argv[])
{
	bool status = 0;
	char in_char = '0';
	SetConsoleTitleA("配置向导 - Windows11音量合成器");
	system("color 0f");
	SetConsoleCP(54936);
	while (true)
	{
		system("cls");
		vmc_title();
		printf_s(
			"|\n"
			"|  状态:\n"
		);
		if (!system("tasklist|findstr /i VolMixerOnWin11.exe"))
			printf_s("|  [运行中]\n");
		else
			printf_s("|  [未运行]\n");
		printf_s(
			"|\n"
			"|========================================\n"
			"|\n"
			"|  键入序号以执行对应操作\n"
			"|\n"
			"|  [1]  停止进程\n"
			"|  [2]  关于程序\n"
			"|  [0]  退出向导\n"
			"|\n"
			"|========================================\n"
		);
		do
		{
			in_char = _getch();
		} while (in_char != '0' && in_char != '1' && in_char != '2');
		switch (in_char)
		{
		case '1':
			taskkill();
			continue;
		case '2':
			about();
			continue;
		case '0':
			return 0;
		}
	}
	return 0;
}

void taskkill()
{
	system("cls");
	vmc_title();
	printf_s(
		"|\n"
		"|  停止中...\n"
	);
	printf_s(
		"|  已执行停止操作\n"
		"|  返回代码: %d\n"
		"|  按任意键返回..."
	,system("taskkill /im VolMixerOnWin11.exe /f"));
	_getch();
}
void about()
{
	system("cls");
	vmc_title();
	printf_s(
		"|\n"
		"|  Volume Mixer On Windows 11\n"
		"|  %s\n"
		"|  在Windows11的系统托盘上显示旧版音量合成器\n"
		"|\n"
		"|  GitHub存储库: Keqing-Yuheng/VolMixerOnWin11\n"
		"|  链接: https://github.com/Keqing-Yuheng/VolMixerOnWin11 \n"
		"|\n"
		"|  本程序以GPL协议授权\n"
		"|  (C) 2022 Keqing-Yuheng\n"
		"|\n"
		"|========================================\n"
		"|\n"
		"|  按任意键返回...\n"
		"|\n"
		"|========================================\n"
	, VER);
	system("start VolMixerOnWin11.exe help");
	_getch();
}