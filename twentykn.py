
"""
twentykn - 20KN: Twenty Kilo Numeric system (이만진수)

- 한자 기반 20,000진법 숫자 체계
- 범위: U+4E00 ~ U+9FFF (CJK Unified Ideographs, 20,992자)
- 정렬 가능: 유니코드 순서 = 숫자 크기
- 가독성 & 정보압축 동시 확보
- 설계: blueradiance (2025)
"""

BASE = 20000
OFFSET = 0x4E00  # Unicode starting point for CJK Unified Ideographs

def encode(n: int) -> str:
    """정수를 20KN 문자열로 인코딩"""
    if n == 0:
        return chr(OFFSET)
    result = []
    while n > 0:
        result.insert(0, chr(OFFSET + (n % BASE)))
        n //= BASE
    return ''.join(result)

def decode(s: str) -> int:
    """20KN 문자열을 정수로 복원"""
    total = 0
    for ch in s:
        total = total * BASE + (ord(ch) - OFFSET)
    return total
