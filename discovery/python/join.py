from kazoo.client import KazooClient

IPAddr = "10.0.12.1" #your ip address
PortNo = 1234
PortNo = bytes(str(PortNo), encoding="ascii") 
import time


zk = KazooClient(hosts='127.0.0.1:2182') #change it to the zookeeper address
zk.start()
zk.add_auth("digest","cmpe:275")


zk.ensure_path("/servers/")
#Store your details in zookeeper
children = zk.create("/servers/"+IPAddr,PortNo,ephemeral=True)

#Print your details
data, stat = zk.get("/servers/"+IPAddr)
print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))

#Keep connection to zookeeper alive
while True:
    time.sleep(200)
zk.stop()