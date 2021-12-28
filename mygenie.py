from genie.testbed import load

testbed = load('yaml/testbed.yml')
device = testbed.devices['Cisco_ios']
device.connect()
response = device.parse('show version')
print(response)
                        
