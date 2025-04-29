from ghidra_bridge import GhidraBridge


class StaticAnalyzer:
    """对应'Ghidra API call'"""

    def __init__(self):
        self.bridge = GhidraBridge()

    def analyze(self, file_path):
        """静态分析入口"""
        return self.bridge.remote_execute(f"""
            for func in currentProgram.getFunctionManager().getFunctions(True):
                if "connect" in func.getName():
                    for ref in getReferencesTo(func):
                        print("调用点:", ref.getFromAddress())
        """)