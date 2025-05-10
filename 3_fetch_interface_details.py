from pyats.topology import loader
from genie import testbed


def main():
    print("\nLoading the testbed...")
    testbed = loader.load('./testbed.yaml')

    print("\nFetching device name...")
    iosxr1 = testbed.devices["iosxr1"]

    print("\nConnecting to the device...")
    iosxr1.connect(init_exec_commands=[], init_config_commands=[], log_stdout=False, learn_hostname=True)

    print("\nFetching interface brief...")
    show_interface = iosxr1.parse('show ip interface brief')

    print("\nExtracting interface name and IP...")
    for interface in show_interface['interface']:
        print(f"{interface} -- {show_interface['interface'][interface]['ip_address']}")

    print("\nDisconnecting from the device...")
    iosxr1.disconnect()
    print("Bye!!!")


if __name__ == "__main__":
    print("Welcome to the Network Automation Script!")
    main()

