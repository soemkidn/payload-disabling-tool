from core.PEParser import PEParser


def main(input_file, output_file):
    parser = PEParser(input_file)
    parser.extract_config()
    for ip in parser.ips:
        print(ip.toString())
    for port in parser.ports:
        print(port.toString())


if __name__ == "__main__":
    main("payload.exe", "blocked_payload.exe")