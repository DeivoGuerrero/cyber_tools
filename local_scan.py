import nmap

# This script scans the local network for devices and prints their IP and MAC addresses.
def scan_local_network(my_network):
    # nmap scaner object
    nm = nmap.PortScanner()
    # Scan the local network
    nm.scan(hosts=my_network, arguments='-sn')
    return [
        {
            'ip': nm[host]['addresses']['ipv4'], 
            'mac': nm[host]['addresses']['mac'] if nm[host]['addresses'].get('mac') else 'No MAC address'
        } for host in nm.all_hosts()
        ]

# Print the results
def print_results(hosts):
    print("IP Address\tMAC Address")
    print("-" * 40)
    for host in hosts:
        print(f"{host['ip']}\t{host['mac']}")

# Main function to run the script
if __name__ == "__main__":
    # Set default network to scan
    my_network = '192.168.1.0/24'
    # Aks user for network to scan
    user_input = input(f"Enter the network to scan (default: {my_network}): ")
    if user_input:
        my_network = user_input
    # Scan the local network
    hosts = scan_local_network(my_network)
    # Print the results
    print_results(hosts)