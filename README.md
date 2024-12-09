# Secure Password Generator

A cross-platform, high-strength random password generator that provides customizable options for generating secure passwords. Designed for macOS, Linux, and \*BSD systems.

## Features

- **High-strength random passwords**：Default length of 16 characters (configurable).
- **Special character support**：Includes special characters by default, fully customizable.
- **Secure randomness**：Uses `/dev/urandom` for generating truly random passwords.
- **Clipboard support**：Automatically copies the generated password to the clipboard (if supported).
- **Password stats**：Displays details such as the number of uppercase, lowercase, numeric, and special characters.
- **Operating system detection**：Detects and displays the current OS.

## Requirements

- **macOS**：Supports clipboard copying via `pbcopy`.
- **Linux**：Requires `xclip` or `xsel` for clipboard functionality.
- **BSD Systems**：Compatible, clipboard support depends on `xclip` or `xsel`.

## Installation

1. Clone the repository：

   ```bash
   git clone https://github.com/your-username/secure-password-generator.git
   cd secure-password-generator
   ```

2. Make the script executable：

   ```bash
   chmod +x generate_secure_password.sh
   ```

3. Run the script：
   ```bash
   ./generate_secure_password.sh
   ```

## Configuration

- To change the default password length or include/exclude special characters, edit the following variables in `generate_secure_password.sh`：
  - `PASSWORD_LENGTH`：Adjust the length of the password.
  - `INCLUDE_SPECIAL`：Set to `true` or `false` to include/exclude special characters.
  - `SIMPLE_SPECIAL_CHARS`：Customize the set of special characters.

## Example Output

```plaintext
✨ 歡迎使用高強度隨機密碼生成工具！✨

功能特色：
  - 預設生成長度為 16 的高強度隨機密碼
  - 預設包含特殊字符
  - 使用 /dev/urandom 生成高強度隨機密碼
  - 支援多種 Unix-like 系統 (Linux, macOS, *BSD)
  - 可自動將密碼複製至剪貼簿（macOS、部分 Linux 系統支援）

開發者資訊：
  開發者：Austin Huang
  聯絡方式：austinhuangdev@gmail.com
  GitHub：https://github.com/austinhuangdev
  版本：1.7.3
  授權：MIT License

目前的作業系統：macOS

隨機生成的密碼資訊：
  - 數字：3 個
  - 小寫字母：3 個
  - 大寫字母：6 個
  - 特殊字符：4 個
  - 資料長度：16 個

隨機生成的高強度密碼（長度：16）：Mv3)YjIA84IfC&@)

密碼已複製到剪貼簿。

請妥善保管您的密碼，避免洩露或遺失。
```

## License

This project is licensed under the [MIT License](LICENSE).

## Author

- **Austin Huang**
- Contact：[austin@example.com](mailto:austinhuangdev@gmail.com)
- GitHub：[github.com/austinhuang](https://github.com/austinhuangdev)
