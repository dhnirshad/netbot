from pyats.topology import loader
from genie import testbed


def main():
    print("Welcome to the Network Automation Script!")

    # Load the testbed
    print("\nLoading the testbed...")
    testbed = loader.load('./testbed.yaml')

    # Fetch the device name
    print("\nFetching device name...")
    iosxr1 = testbed.devices["iosxr1"]

    # Connect to the device
    print("\nConnecting to the device...")
    iosxr1.connect(init_exec_commands=[], init_config_commands=[], log_stdout=False, learn_hostname=True)

    # Fetch interface brief
    print("\nFetching interface brief...")
    show_interface = iosxr1.parse('show ip interface brief')

    # Display the available interfaces and their IP addresses
    print("\nAvailable interfaces and their IP addresses:")
    for interface in show_interface['interface']:
        print(f"{interface} -- {show_interface['interface'][interface]['ip_address']}")

    # Ask the user to select an interface
    print("\nEnter the name of the interface you want to update the description for:")
    selected_interface = input("Interface name: ").strip()

    # Verify if the selected interface exists
    if selected_interface not in show_interface['interface']:
        print(f"Error: The interface '{selected_interface}' does not exist on the device.")
    else:
        # Prompt the user to enter a new description
        print(f"\nEnter a new description for {selected_interface}:")
        new_description = input("New description: ").strip()

        if not new_description:
            print("Error: Description cannot be empty.")
        else:
            # Update the interface description
            print(f"\nUpdating the description of {selected_interface}...")
            try:
                iosxr1.configure([
                    f"interface {selected_interface}",
                    f"description {new_description}"
                ])
                print(f"Successfully updated the description of {selected_interface} to '{new_description}'.")
            except Exception as e:
                print(f"Error: Failed to update interface description. {str(e)}")

    # Disconnect from the device
    print("\nDisconnecting from the device...")
    iosxr1.disconnect()
    print("Goodbye!")


if __name__ == "__main__":
    main()