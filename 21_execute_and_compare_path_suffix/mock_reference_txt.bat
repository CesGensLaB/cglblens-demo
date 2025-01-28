@echo off

:: Create directories if they do not exist
if not exist outputs mkdir outputs
if not exist logs mkdir logs

:: Write data to the outputs file
(
echo 1
echo 2
echo 3
) > outputs\cglblens_generated_data.txt

:: Write data to the logs file
echo logs > logs\app.log
