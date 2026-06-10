@echo off
setlocal

:menu
cls
echo Rotten Potato TCM - Script Runner
echo ---------------------------------
echo 1. Normalize frontmatter
echo 2. Update metadata interactively
echo 3. Generate inventory CSV
echo 4. Run all (normalize + update + generate)
echo Q. Quit
echo.

set /p choice="Select an option (1-4 or Q): "

if /I "%choice%"=="1" (
    python scripts\normalize_frontmatter.py
    goto menu
) else if /I "%choice%"=="2" (
    python scripts\update_testcase_metadata.py
    goto menu
) else if /I "%choice%"=="3" (
    python scripts\generate_inventory.py
    goto menu
) else if /I "%choice%"=="4" (
    python scripts\normalize_frontmatter.py
    python scripts\update_testcase_metadata.py
    python scripts\generate_inventory.py
    goto menu
) else if /I "%choice%"=="Q" (
    echo Exiting Script Runner...
    exit /b
) else (
    echo Invalid choice. Try again.
    pause
    goto menu
)
