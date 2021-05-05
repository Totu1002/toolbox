@echo off

:MainSequence
echo Please select a batch file to execute
echo =======================================
echo [1]:static-ip.bat
echo;
echo [2]:dynamic-ip.bat
echo;
echo [q]:Cancel selection
echo =======================================
echo please enter the target value:
set /p num=

if "%num%"=="" (
	echo === ERROR:please fill in the value ! ===
	echo;
	goto MainSequence
	)
	
if %num%==1 (
	call :static-ip_seting
	) else if %num%==2 (
	call :dynamic-ip_seting
	) else if /i %num%==q (
	echo Processing has been canceled.
	timeout /t 3 > nul
	exit
	) else (
	echo === ERROR:Please enter the correct value ! ===
	echo;
	goto MainSequence
	)

rem subroutine
:static-ip_seting
call static-ip.bat
goto end


:dynamic-ip_seting
call dynamic-ip.bat
goto end


:end
rem ipconfig
rem ipconfig > ipconfig_%date%.txt
echo Processing is complete !
pause
exit
