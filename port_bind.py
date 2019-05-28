import paramiko
from sshtunnel import SSHTunnelForwarder

mypkey = paramiko.RSAKey.from_private_key_file('/opt/.ssh/id_rsa')

def set_ssh(name,ip,port,bindport):
    sqlserver = SSHTunnelForwarder(
       ssh_address_or_host=(ip,port),
       ssh_username="root",ssh_pkey=mypkey,
       remote_bind_address=('127.0.0.1', 3306),
       local_bind_address=('127.0.0.1',bindport)
    )
    sqlserver.start()
    return name,bindport
    
data = [
    {'name':'test','params':{'ip':"100.1.1.1",'port':22,'bindport':21001}},
    ]
for i in range(len(data)):
    name = data[i]['name']
    ip = data[i]['params']['ip']
    port = data[i]['params']['port']
    bindport = data[i]['params']['bindport']
    print(set_ssh(name,ip,port,bindport))
    

