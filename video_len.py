def get_time_seconds(len: str) -> int:
    [mins, secs] = list(map(lambda x: int(x), len.split(":")))
    if secs >= 60:
        return -1

    return (60*mins) + secs

if __name__ == "__main__":
    print(get_time_seconds("1:00"))
    print(get_time_seconds("13:56"))
    print(get_time_seconds("10:60"))
    print(get_time_seconds("121:49"))
