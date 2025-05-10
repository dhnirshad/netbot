from pyats.topology import loader

print("\nLoading the testbed...")
testbed = loader.load('./testbed.yaml')

print("\nFetching device name...")
iosxr1 = testbed.devices["iosxr1"]

print("\nConnecting to the device...")
iosxr1.connect(init_exec_commands=[], init_config_commands=[], log_stdout=False, learn_hostname=True)

print("\nGet running config...")
show_running_config = iosxr1.execute('show running-config')
print("\n -----------------------------")
print(show_running_config)
print("\n -----------------------------")

print("\nDisconnecting from the device...")
iosxr1.disconnect()
print("Bye!!!")


