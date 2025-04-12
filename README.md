
# twentykn - 20KN: Twenty Kilo Numeric System (二萬進數)

A unicode-based 20,000-radix numeric encoding system using CJK Unified Ideographs (U+4E00 to U+9FFF).  
Created by **blueradiance** (2025).

---

## 🌐 Description (EN)

**twentykn** is a compression-friendly, unicode-stable, reversible numeric encoding system using exactly 20,000 continuous CJK characters.  
It provides high-density information representation and preserves sortability.

- Supports integer encoding/decoding
- Uses Unicode range U+4E00 to U+9FFF
- Each character represents a value from 0 to 19999
- Sortable by unicode string order
- Fully reversible and system-safe

---

## 🇰🇷 설명 (한국어)

**twentykn**은 유니코드 CJK 한자(U+4E00 ~ U+9FFF) 20,000자를 기반으로 한  
고압축 숫자 인코딩 시스템입니다.  
정렬 가능하며, 100% 복원이 가능한 한자 기반 이만진수(20진수 × 1,000) 체계입니다.

- 정수를 유니코드 한자로 압축
- 유니코드 순서 그대로 정렬 가능
- 모든 OS에서 출력 가능
- 정보량 약 log₂(20000) ≈ 14.3비트/문자

---

## 🇨🇳 中文说明 (简体中文)

**twentykn** 是一个基于 Unicode 的数字编码系统，使用 20,000 个连续的汉字字符（U+4E00 到 U+9FFF）。  
它压缩效率高，可逆性强，字符排序即数字排序，适用于大规模数字存储与传输。

- 每个字符表示 0 ~ 19999 的值
- 使用 Unicode 汉字区段，几乎所有系统支持显示
- 支持整数编码/解码
- 保持可排序性与兼容性

---

## 🔧 Usage

```python
from twentykn import encode, decode

n = 1234567890
s = encode(n)
restored = decode(s)
assert restored == n
```

---

## 📜 License

See `LICENSE.txt` for terms.

Author: **blueradiance**  
