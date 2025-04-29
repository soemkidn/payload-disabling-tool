// 动态挂钩脚本
Interceptor.attach(Module.getExportByName('ws2_32.dll', 'connect'), {
    onEnter: function(args) {
        var sockaddr = args[1];
        var ip = sockaddr.add(4).readByteArray(4);
        var port = sockaddr.add(2).readU16();
        send(JSON.stringify({
            type: 'c2_config',
            data: {ip: Array.from(ip), port: port}
        }));
    }
});