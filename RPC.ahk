;#NoTrayIcon
#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

DetectHiddenWindows, On

Run, C:\Discord-Rich Presence\RP-Adobe\rpc.exe, ,Hide

Loop
	{
		WinWait, ahk_exe rpc.exe
		WinWaitClose, ahk_exe rpc.exe
		Sleep, 2500
		Run, C:\Discord-Rich Presence\RP-Adobe\rpc.exe, ,Hide
	}