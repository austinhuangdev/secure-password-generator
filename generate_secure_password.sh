#!/usr/bin/env sh

GREEN='\033[1;32m'
YELLOW='\033[1;33m'
RED='\033[1;31m'
CYAN='\033[1;36m'
NC='\033[0m'

export LC_ALL=C

PASSWORD_LENGTH=16
INCLUDE_SPECIAL="true"
SIMPLE_SPECIAL_CHARS='!@#$%^&*()'

display_welcome() {
    printf "${GREEN}✨ 歡迎使用高強度隨機密碼生成工具！✨${NC}\n\n"
}

display_features() {
    printf "${CYAN}功能特色:${NC}\n"
    printf "  - 預設生成長度為 ${PASSWORD_LENGTH} 的高強度隨機密碼\n"
    printf "  - 預設包含特殊字符\n"
    printf "  - 使用 /dev/urandom 生成高強度隨機密碼\n"
    printf "  - 支援多種 Unix-like 系統 (Linux, macOS, *BSD)\n"
    printf "  - 可自動將密碼複製至剪貼簿（macOS、部分 Linux 系統支援）\n\n"
}

display_developer_info() {
    printf "${CYAN}開發者資訊:${NC}\n"
    printf "  開發者：Austin Huang\n"
    printf "  聯絡方式：austinhuangdev@gmail.com\n"
    printf "  GitHub：https://github.com/austinhuangdev\n"
    printf "  版本：1.7.4\n"
    printf "  授權：MIT License\n\n"
}

detect_os() {
    OSNAME=$(uname -s 2>/dev/null || echo "Unknown")
    case "$OSNAME" in
        Darwin) OS="macOS";;
        Linux) OS="Linux";;
        FreeBSD) OS="FreeBSD";;
        OpenBSD) OS="OpenBSD";;
        NetBSD) OS="NetBSD";;
        *) OS="Unknown";;
    esac
}

define_charset() {
    UPPERCASE='A-Z'
    LOWERCASE='a-z'
    NUMBERS='0-9'
    CHARSET="$UPPERCASE$LOWERCASE$NUMBERS"
    if [ "$INCLUDE_SPECIAL" = "true" ]; then
        CHARSET="$CHARSET$SIMPLE_SPECIAL_CHARS"
    fi
}

copy_to_clipboard() {
    password="$1"
    # 嘗試自動複製
    if [ "$OS" = "macOS" ]; then
        if command -v pbcopy >/dev/null 2>&1; then
            printf "%s" "$password" | pbcopy
            printf "${GREEN}密碼已複製到剪貼簿。${NC}\n\n"
        fi
    elif [ "$OS" = "Linux" ] || [ "$OS" = "FreeBSD" ] || [ "$OS" = "OpenBSD" ] || [ "$OS" = "NetBSD" ]; then
        if command -v xclip >/dev/null 2>&1; then
            printf "%s" "$password" | xclip -selection clipboard
            printf "${GREEN}密碼已複製到剪貼簿。${NC}\n\n"
        elif command -v xsel >/dev/null 2>&1; then
            printf "%s" "$password" | xsel --clipboard --input
            printf "${GREEN}密碼已複製到剪貼簿。${NC}\n\n"
        fi
    fi
}

display_password_details() {
    password="$1"
    length=${#password}

    uppercase=$(printf "%s" "$password" | tr -dc 'A-Z' | wc -c | tr -d ' ')
    lowercase=$(printf "%s" "$password" | tr -dc 'a-z' | wc -c | tr -d ' ')
    numbers=$(printf "%s" "$password" | tr -dc '0-9' | wc -c | tr -d ' ')
    specials=0
    if [ "$INCLUDE_SPECIAL" = "true" ]; then
        specials=$(printf "%s" "$password" | tr -dc "$SIMPLE_SPECIAL_CHARS" | wc -c | tr -d ' ')
    fi

    printf "${CYAN}隨機生成的密碼資訊：${NC}\n"
    printf "  - 數字：%d 個\n" "$numbers"
    printf "  - 小寫字母：%d 個\n" "$lowercase"
    printf "  - 大寫字母：%d 個\n" "$uppercase"
    printf "  - 特殊字符：%d 個\n" "$specials"
    printf "  - 資料長度：%d 個\n\n" "$length"
}

display_security_tip() {
    printf "${RED}請妥善保管您的密碼，避免洩露或遺失。${NC}\n"
}

generate_password() {
    # 顯示目前的作業系統
    printf "${CYAN}目前的作業系統：${YELLOW}%s${NC}\n\n" "$OS"

    # 必要字符：至少一個大寫、一個小寫、一個數字、一個特殊字符
    temp_password="$(tr -dc 'A-Z' < /dev/urandom | head -c 1)"
    temp_password="$temp_password$(tr -dc 'a-z' < /dev/urandom | head -c 1)"
    temp_password="$temp_password$(tr -dc '0-9' < /dev/urandom | head -c 1)"
    temp_password="$temp_password$(tr -dc "$SIMPLE_SPECIAL_CHARS" < /dev/urandom | head -c 1)"

    remaining_length=$((PASSWORD_LENGTH - ${#temp_password}))
    extra_chars=""
    if [ "$remaining_length" -gt 0 ]; then
        extra_chars=$(tr -dc "$CHARSET" < /dev/urandom | head -c "$remaining_length")
    fi

    password="$temp_password$extra_chars"
    display_password_details "$password"

    printf "${GREEN}隨機生成的高強度密碼（長度：${PASSWORD_LENGTH}）：${YELLOW}%s${NC}\n\n" "$password"
    
    copy_to_clipboard "$password"
}

main() {
    # 預設長度檢查（若更改預設長度請一併調整）
    min_len=4
    if [ "$PASSWORD_LENGTH" -lt "$min_len" ]; then
        printf "${YELLOW}錯誤：密碼長度至少需為%d字元以容納必要字元類型。\n${NC}" "$min_len"
        exit 1
    fi

    detect_os
    display_welcome
    display_features
    display_developer_info
    define_charset
    generate_password
    display_security_tip
}

main
