import os
from pyats.topology import loader


def main(device_cmd="show version"):
    print("\nLoading the testbed...")
    testbed = loader.load('./testbed.yaml')

    print("\nFetching device name...")
    iosxr1 = testbed.devices["iosxr1"]

    print("\nConnecting to the device...")
    iosxr1.connect(init_exec_commands=[], init_config_commands=[], log_stdout=False, learn_hostname=True)

    print(f"\nGet {device_cmd}")
    show_running_config = iosxr1.execute(f"{device_cmd}")
    print("\n -----------------------------")
    print(show_running_config)
    print("\n -----------------------------")

    print("\nDisconnecting from the device...")
    iosxr1.disconnect()
    print("Bye!!!")


if __name__ == "__main__":
    print("Welcome to the Network Automation Script!")
    cmd = input("Please enter the command you want to execute (e.g., 'show running-config'): ")
    main(cmd)

