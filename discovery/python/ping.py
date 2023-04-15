from kazoo.client import KazooClient
import os


zk = KazooClient(hosts='127.0.0.1:2181') #change it to the zookeeper address
zk.start()
zk.add_auth("digest","cmpe:275")


#Gets all the servers available
servers = zk.get_children("/servers")
print(servers)

#ping the available servers to see if connectable
if(len(servers)!=0):
    for server in servers:
        print("--------------server---------------")
        data, stat = zk.get("/servers/"+str(server))
        print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))
        hostname = str(server)
        response = os.system("ping -W 2000 -c 1 " + hostname)
        #and then check the response...
        if response == 0:
            print (hostname, 'is up!')
        else:
          print (hostname, 'is down!')
        print("-----------------------------------")
        
else:
     print("No active server")

zk.stop()