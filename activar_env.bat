@echo off
chcp 65001 > nul
REM Script para crear y gestionar el entorno virtual

setlocal enabledelayedexpansion

REM Definir la ruta del entorno virtual
set "ENV_PATH=%~dp0env"

echo.
echo ========================================
echo   GESTOR DE ENTORNO VIRTUAL
echo ========================================
echo Ruta: %ENV_PATH%
echo.

REM Verificar si el entorno virtual ya existe
if exist "%ENV_PATH%\Scripts\activate.bat" (
    echo ✓ El entorno virtual YA EXISTE
    echo.
    cmd /k "%ENV_PATH%\Scripts\activate.bat"
) else (
    echo Creando entorno virtual...
    python -m venv "%ENV_PATH%"
    
    if !errorlevel! equ 0 (
        echo.
        echo ✓✓✓ ENTORNO VIRTUAL CREADO EXITOSAMENTE ✓✓✓
        echo.
        cmd /k "%ENV_PATH%\Scripts\activate.bat"
    ) else (
        echo.
        echo ✗✗✗ ERROR AL CREAR EL ENTORNO VIRTUAL ✗✗✗
        echo Verifique que Python está instalado correctamente
        pause
        exit /b 1
    )
)
endlocal
