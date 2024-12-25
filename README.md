# Secure Password Generator

A cross-platform, high-strength random password generator that provides customizable options for generating secure passwords. Designed for macOS, Linux, Windows, and \*BSD systems.

## Features

- **High-strength random passwords**：Default length of 16 characters (configurable).
- **Special character support**：Includes special characters by default, fully customizable.
- **Secure randomness**：Uses Python's `random` module for generating truly random passwords.
- **Clipboard support**：Automatically copies the generated password to the clipboard (supports `pbcopy` for macOS, `xclip` or `xsel` for Linux/BSD, and `clip.exe` for Windows).
- **Password stats**：Displays details such as the number of uppercase, lowercase, numeric, and special characters.
- **Operating system detection**：Detects and displays the current OS.

## Requirements

- **Python 3.6+**：Ensure Python is installed on your system.
- **macOS**：Supports clipboard copying via `pbcopy`.
- **Linux**：Requires `xclip` or `xsel` for clipboard functionality.
- **BSD Systems**：Compatible, clipboard support depends on `xclip` or `xsel`.
- **Windows**：Supports clipboard copying via `clip.exe` (available in most Windows systems).

## Installation

1. Clone the repository：

   ```shell
   git clone https://github.com/austinhuangdev/secure-password-generator.git
   cd secure-password-generator
   ```

2. (Optional) Set up a virtual environment：

   ```shell
   python3 -m venv venv
   source venv/bin/activate
   ```

## Usage

Run the Python script to generate a secure password：

```bash
python3 generate_secure_password.py
```

## Configuration

要更改預設的密碼長度或包含/排除特殊字符，請編輯 `generate_secure_password.py` 中的以下變數：

- `PASSWORD_LENGTH`：調整密碼的長度。
- `INCLUDE_SPECIAL`：設定為 `True` 或 `False` 以包含/排除特殊字符。
- `SIMPLE_SPECIAL_CHARS`：自定義特殊字符集。

例如：

```python
PASSWORD_LENGTH = 20
INCLUDE_SPECIAL = False
SIMPLE_SPECIAL_CHARS = '!@#$%^&*()_+-=[]{}|;:,.<>?'
```

## Example Output

```plaintext
✨ 歡迎使用高強度隨機密碼生成工具！✨

功能特色：
  - 預設生成長度為 16 的高強度隨機密碼
  - 預設包含特殊字符
  - 使用隨機函式生成高強度密碼
  - 跨平台支援（Windows、macOS、Linux）
  - 若環境允許，可自動將密碼複製至剪貼簿

開發者資訊：
  開發者：Austin Huang
  聯絡方式：austinhuangdev@gmail.com
  GitHub：https://github.com/austinhuangdev
  版本：1.7.4
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

## Author

- **Developer**：Austin Huang
- **Contact**：[austinhuangdev@gmail.com](mailto:austinhuangdev@gmail.com)
- **GitHub**：[https://github.com/austinhuangdev](https://github.com/austinhuangdev)

## License

This project is licensed under the [MIT License](LICENSE).