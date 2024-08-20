def validate(ip):
    
    segments = ip.split('.')
    
    if len(segments) != 4:
        return False
    
    for segment in segments:
        if not segment.isdigit():
            return False
        if not 0 <= int(segment) <= 255:
            return False
    
    return True


def main():
    print(validate(input("IPv4 Address: ")))


if __name__ == "__main__":
    main()
