import re

def parse_numeric_value(raw_value: str):
    if not isinstance(raw_value, str):
        return raw_value
    clean = raw_value.replace(",", ".")
    matches = re.findall(r"\d+(?:\.\d+)?", clean)
    # nums = [float(m) if "." in m else int(m) for m in matches]
    nums = [int(m) for m in matches]
    if len(nums) == 1:
        return nums[0]
    if nums:
        return {"opcoes": nums, "mensagem": f"Mais de um valor em '{raw_value}'."}
    return None
