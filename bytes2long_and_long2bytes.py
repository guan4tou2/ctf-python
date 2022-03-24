def bytes_to_long(byte):
    result = 0
    for b in byte:
        result = result * 256 + int(b)
    return result


def long_to_bytes(long):
    result = ""
    for i in range(len(str(long))):
        result += (chr(long >> (i * 8) & 0xff))
    return result[::-1]
