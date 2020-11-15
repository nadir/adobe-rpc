#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

^!+`::
WinShow, ahk_exe rpc.exe
WinKill, ahk_exe rpc.exe
WinWaitClose, ahk_exe rpc.exe
Run, C:\Discord-Rich Presence\RP-Adobe\rpc.exe, ,Hide
MsgBox, failsafe activated
return