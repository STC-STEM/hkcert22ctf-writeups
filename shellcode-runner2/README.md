# Shellcode Runner 2

詳細視頻解釋： https://youtu.be/Rd-fyE9y6Lw

根據 http://ref.x86asm.net/coder32.html#x00 <br>
我們可以得知 `add` 的 8bits 方法對應的匯編碼為 0x00

根據源碼：

```c
int is_all_upper(char* s) {
    for (int i=0; i<strlen(s); i++)
        if (!isupper(s[i]) && !isdigit(s[i]) && s[i] != ' ')
            return 0;
    return 1;
}
```

`strlen()` 處理的是 `null-terminated string` <br>
只會根據他遇到的第一個 `'\0'` 來判斷字符串長度

因此我們可以通過
```asm
add %al, %al
```
這一匯編代碼製造出開頭為 `0x00` 的 payload <br>
以令 `strlen()` 誤判 payload 長度， 繞過檢查

hkcert22{d41d8cd98f00b204e9800998ecf8427e33a}