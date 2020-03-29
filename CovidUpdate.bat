@echo off
SET current_path=%~dp0
SET script_path=%current_path%CovidUpdate.py
SET conda_activate_script=%1
SET conda_env=%2
call %conda_activate_script% %conda_env%
py %script_path%
