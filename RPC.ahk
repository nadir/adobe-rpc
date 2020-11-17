;----------------------------------------------------------------------------------------------------------------------------
;----------------------------------------------------------------------------------------------------------------------------

#NoTrayIcon  ;Used for removing icon in the Taskbar System tray.
#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

;----------------------MAIN CODE STARTS HERE--------------------------------

DetectHiddenWindows, On  ;For detecting hidden windows

Run, C:\Discord-Rich Presence\RP-Adobe\rpc.exe, ,Hide  ;Run .exe file in hidden mode.

Loop  ;Loops till the file itself is not externally terminated.
	{
		WinWait, ahk_exe rpc.exe  ;Waits for the .exe file to exist.
		WinWaitClose, ahk_exe rpc.exe  ;Waits for the .exe file to close.
		Sleep, 2500  ;Sleep for 2.5 seconds.
		Run, C:\Discord-Rich Presence\RP-Adobe\rpc.exe, ,Hide  ;Runs the .exe file again in hidden mode.
	}
	
;----------------------------------------------------------------------------------------------------------------------------
;----------------------------------------------------------------------------------------------------------------------------

;THE CODE WONT WORK WITHOUT INSTALLING AUTOHOTKEY (AHK)
