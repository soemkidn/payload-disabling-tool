from core.PEParser import PEParser
from core.PEModifier import PEModifier
from core.PEFileViewer import PEFileViewer

def main(input_file, output_file):
    # initialize PE parser
    parser = PEParser(input_file)
    parser.extract_config()
    ip_info = parser.ips[0]     # ip address of attacker
    port_info = parser.ports[0]     # port of attacker
    modifier = PEModifier(input_file, output_file)
    modifier.modify_pe_hex_string(ip_info.start, ip_info.end, b'\x7F\x00\x00\x01')
    modifier = PEModifier(output_file, output_file)
    modifier.modify_pe_hex_string(port_info.start, port_info.end, b'\x00\x50')
    viewer = PEFileViewer(output_file)
    new_ip = viewer.view_hex_range(ip_info.start, ip_info.end)
    new_port = viewer.view_hex_range(port_info.start, port_info.end)
    print(f"New IP: {new_ip}")
    print(f"New Port: {new_port}")
    print("Successfully disabled")




if __name__ == "__main__":
    main("payload.exe", "blocked_payload.exe")