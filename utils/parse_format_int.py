import re

def parse_numeric_value(raw_value: str):
    print(f"[DEBUG] Valor bruto recebido para parse: {raw_value}")
    if not isinstance(raw_value, str):
        return raw_value
    clean = raw_value.replace(",", ".")
    matches = re.findall(r"\d+(?:\.\d+)?", clean)
    nums = [float(m) if "." in m else int(m) for m in matches]
    if nums:
        return sum(nums)
    return 0
