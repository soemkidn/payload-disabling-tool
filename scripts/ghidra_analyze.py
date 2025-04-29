# Ghidra脚本，通过bridge调用,未定义的对象通过Ghidra上下文注入
def find_c2_references():
    for ref in getReferencesTo(findBytes(currentProgram, b'\xC0\xA8')):
        print(f"在 {ref.getFromAddress()} 发现C2引用")