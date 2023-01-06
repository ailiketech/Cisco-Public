from netmiko import ConnectHandler # handles our connection
Router = [] # list of routers
port = 9000 #port number of device 1 

for i in range(1,11):
  Router.append({'device_type': 'cisco_ios_telnet',
        'ip': '::1',
        'host': 'R'+ str(i),
        'port': port,
        #'read_timeout_override' : 90
        })
  port = port + 2

for a_device in (Router):
    print ('Initializing Device '+ a_device['host'])
    net_connect = ConnectHandler(**a_device)
    net_connect.enable()
    print(net_connect.send_config_set(['hostname ' + a_device['host'], 'line con 0', 'logging synchronous', 'exec-timeout 0 0', 'no ip domain lookup']))
    net_connect.set_base_prompt()
    print(net_connect.save_config())
    net_connect.disconnect()

print("Done!")