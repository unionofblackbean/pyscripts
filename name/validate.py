def validate_format(name: str) -> bool:
    name_len = len(name)
    if name_len < 3 or name_len > 16:
        return False

    for ch in name:
        if ch not in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_":
            return False

    return True
