import frida


class DynamicHooker:
    """对应'Frida script injection'"""

    def __init__(self, target_process):
        self.session = frida.attach(target_process)

    def inject(self):
        """注入挂钩脚本"""
        script = """
        Interceptor.attach(Module.getExportByName('ws2_32.dll', 'connect'), {
            onEnter: function(args) {
                var sockaddr = args[1];
                var ip = sockaddr.add(4).readByteArray(4);
                var port = sockaddr.add(2).readU16();
                send({type: 'c2_config', data: {ip: ip, port: port}});
            }
        });
        """
        self.script = self.session.create_script(script)
        self.script.on('message', self.on_message)
        self.script.load()

    def on_message(self, message, _):
        if message['type'] == 'c2_config':
            print("[*] 捕获动态配置:", message['data'])