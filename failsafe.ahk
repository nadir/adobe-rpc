;----------------------------------------------------------------------------------------------------------------------------
;----------------------------------------------------------------------------------------------------------------------------

#NoTrayIcon  ;Used for removing icon in the Taskbar System tray.
#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

;----------------------MAIN CODE STARTS HERE--------------------------------

^!+`::  ;Shows the Keypress CTRL(^) + ALT(!) + SHIFT(+) + BACKTICK(`) which executes the command. Can be changed according to the user by applying appropriate custom keypress.
WinShow, ahk_exe rpc.exe  ;Unhides the hidden .exe file.
WinKill, ahk_exe rpc.exe  ;Kills the .exe service.
WinWaitClose, ahk_exe rpc.exe  ;Waits for the .exe file yo close.
Run, C:\Discord-Rich Presence\RP-Adobe\rpc.exe, ,Hide  ;Runs the .exe file again in hidden mode.
MsgBox, failsafe activated  ;Optional msg to confirm the execution of the commands. CAN BE DEACTIVATED BY ADDING A SEMICOLON(;)AT THE START OF THE COMMAND ON THIS LINE (LINE 17)
return

ExitApp

;----------------------------------------------------------------------------------------------------------------------------
;----------------------------------------------------------------------------------------------------------------------------

;THE CODE WONT WORK WITHOUT INSTALLING AUTOHOTKEY (AHK)
