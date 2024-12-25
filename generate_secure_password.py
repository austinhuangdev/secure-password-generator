#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import platform
import subprocess
import random
import string
import shutil  # 確保 shutil 已被匯入

# 常量設定區
PASSWORD_LENGTH = 16
INCLUDE_SPECIAL = True
SIMPLE_SPECIAL_CHARS = '!@#$%^&*()'
VERSION = "1.0.0"
DEVELOPER = "Austin Huang"
CONTACT = "austinhuangdev@gmail.com"
GITHUB = "https://github.com/austinhuangdev"
LICENSE = "MIT License"

# ANSI 顏色碼
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
RED = '\033[1;31m'
CYAN = '\033[1;36m'
MAGENTA = '\033[1;35m'
NC = '\033[0m'

def display_welcome():
    print(f"{GREEN}✨ 歡迎使用高強度隨機密碼生成工具！✨{NC}\n")

def display_features():
    print(f"{CYAN}功能特色：{NC}")
    print(f"  - 預設生成長度為 {PASSWORD_LENGTH} 的高強度隨機密碼")
    if INCLUDE_SPECIAL:
        print("  - 預設包含特殊字符")
    else:
        print("  - 不包含特殊字符")
    print("  - 使用隨機函式生成高強度密碼")
    print("  - 跨平台支援（Windows、macOS、Linux）")
    print("  - 若環境允許，可自動將密碼複製至剪貼簿")
    print()

def display_developer_info():
    print(f"{CYAN}開發者資訊：{NC}")
    print(f"  - 開發者：{DEVELOPER}")
    print(f"  - 聯絡方式：{CONTACT}")
    print(f"  - GitHub：{GITHUB}")
    print(f"  - 版本：{VERSION}")
    print(f"  - 授權：{LICENSE}\n")

def detect_os():
    osname = platform.system()
    if osname == "Darwin":
        return "macOS"
    elif osname in ["FreeBSD", "OpenBSD", "NetBSD"]:
        return osname
    else:
        return osname

def define_charset():
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    charset = uppercase + lowercase + digits
    if INCLUDE_SPECIAL:
        charset += SIMPLE_SPECIAL_CHARS
    return charset

def copy_to_clipboard(password, osname):
    # 嘗試複製到剪貼簿
    try:
        if osname == "macOS":
            # macOS
            subprocess.run("pbcopy", input=password.encode('utf-8'), check=True)
            print(f"{GREEN}密碼已複製到剪貼簿。{NC}\n")
        elif osname == "Linux":
            # Linux 嘗試 xclip 或 xsel
            if shutil.which("xclip"):
                subprocess.run(["xclip", "-selection", "clipboard"], input=password.encode('utf-8'), check=True)
                print(f"{GREEN}密碼已複製到剪貼簿。{NC}\n")
            elif shutil.which("xsel"):
                subprocess.run(["xsel", "--clipboard", "--input"], input=password.encode('utf-8'), check=True)
                print(f"{GREEN}密碼已複製到剪貼簿。{NC}\n")
            else:
                print(f"{YELLOW}未找到 xclip 或 xsel，無法自動複製到剪貼簿。請手動複製。{NC}\n")
        elif osname == "Windows":
            # Windows 使用 clip.exe
            try:
                process = subprocess.Popen(
                    ["clip.exe"],
                    stdin=subprocess.PIPE,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE
                )
                stdout, stderr = process.communicate(input=password.encode('utf-8'))
                if process.returncode == 0:
                    print(f"{GREEN}密碼已複製到剪貼簿。{NC}\n")
                else:
                    print(f"{YELLOW}複製失敗，請手動複製。{NC}\n")
                    print(f"錯誤訊息：{stderr.decode().strip()}")
            except Exception as e_clip:
                print(f"{YELLOW}複製時發生錯誤，請手動複製。{NC}\n")
                print(f"錯誤詳情：{e_clip}")
        else:
            print(f"{YELLOW}無法自動複製到剪貼簿的 OS：{osname}，請自行複製。{NC}\n")
    except Exception as e:
        print(f"{YELLOW}自動複製到剪貼簿失敗，請手動複製。{NC}\n")
        print(f"錯誤詳情：{e}")

def display_password_details(password):
    length = len(password)
    uppercase = sum(1 for c in password if c.isupper())
    lowercase = sum(1 for c in password if c.islower())
    numbers = sum(1 for c in password if c.isdigit())
    specials = 0
    if INCLUDE_SPECIAL:
        specials = sum(1 for c in password if c in SIMPLE_SPECIAL_CHARS)

    print(f"{CYAN}隨機生成的密碼資訊：{NC}")
    print(f"  - 數字：{numbers} 個")
    print(f"  - 小寫字母：{lowercase} 個")
    print(f"  - 大寫字母：{uppercase} 個")
    print(f"  - 特殊字符：{specials} 個")
    print(f"  - 資料長度：{length} 個\n")

def display_security_tip():
    print(f"{RED}請妥善保管您的密碼，避免洩露或遺失。{NC}")

def generate_password():
    # 必要字符：至少一個大寫、一個小寫、一個數字、一個特殊字符（若有包含）
    uppercase = random.choice(string.ascii_uppercase)
    lowercase = random.choice(string.ascii_lowercase)
    digit = random.choice(string.digits)
    if INCLUDE_SPECIAL:
        special_char = random.choice(SIMPLE_SPECIAL_CHARS)
        base = uppercase + lowercase + digit + special_char
    else:
        base = uppercase + lowercase + digit

    remaining_length = PASSWORD_LENGTH - len(base)
    charset = define_charset()
    extra_chars = ''.join(random.choice(charset) for _ in range(remaining_length))
    password = base + extra_chars
    # 打亂順序
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password

def main():
    # 基本檢查
    if PASSWORD_LENGTH < 4:
        print(f"{YELLOW}錯誤：密碼長度至少需為4字元以容納必要字元類型。{NC}")
        return

    osname = detect_os()
    display_welcome()
    display_features()
    display_developer_info()

    # 顯示目前的作業系統
    print(f"{CYAN}目前的作業系統：{YELLOW}{osname}{NC}\n")

    password = generate_password()
    display_password_details(password)
    print(f"{GREEN}隨機生成的高強度密碼（長度：{PASSWORD_LENGTH}）：{YELLOW}{password}{NC}\n")
    
    # 嘗試自動複製到剪貼簿
    copy_to_clipboard(password, osname)

    display_security_tip()

if __name__ == '__main__':
    main()
