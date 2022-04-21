from os import popen

class VBoxManager:
    def __init__(self):
        """Initialize all variables for VBoxManager 
        """
        self.options = {
            "1":"Create a VM",
            "2":"List all available VMs",
            "3":"Start a VM",
            "4":"Stop a VM",
            "5":"List Settings of a VM",
            "6":"Delete a VM",
            "7":"End the program"
        }
        self.vms = []
        self.main()
    
    def prompt(self): 
        """Initial Prompt for new selections

        Returns:
            Union[str|bool]: selection or False if user gives invalid selection
        """
        print("Options:")
        print("==========================")
        for key, value in self.options.items():
            print(f'{key} {value}')
        print("==========================")
        selection = input()
        print()
        if selection in ("1", "2", "3", "4", "5", "6", "7"):
            return selection
        return False
    
    def list_machines(self):
        """Lists all current machines
        """
        self.vms = []
        for i, vm in enumerate(popen('vboxmanage list vms')):
            vm = vm.strip()
            self.vms.append(vm.split(' {')[0])
            print(f'[{i + 1}] {vm}')
        
    
    def start_machine(self):
        """Starts a given machines
        """
        self.list_machines()
        print("==========================")
        choice = input("Enter VM to start: ")
        if choice.isnumeric():
            choice = int(choice) - 1
            if choice < len(self.vms):
                print(popen(f'vboxmanage startvm {self.vms[choice]} --type gui').read())
            else:
                print('Out of index for vms')
        else:
            print('Invalid choice for machine')

    
    def stop_machine(self):
        """Stops a given machine
        """
        self.list_machines()
        print("==========================")
        choice = input("Enter VM to start: ")
        if choice.isnumeric():
            choice = int(choice) - 1
            if choice < len(self.vms):
                print(popen(f'vboxmanage controlvm {self.vms[choice]} poweroff --type gui').read())
            else:
                print('Out of index for vms')
        else:
            print('Invalid choice for machine')
    
    def create_vm(self):
        """Create VM and prompts for info to build it
        """
        name = input('Name of VM: ')
        OStype = input('OStype [Debian]: ')
        if OStype.strip() == '': OStype = 'Debian'
        print(popen(f'vboxmanage createvm --name "{name}" --ostype "{OStype}" --register').read())
    
    def list_vm_settings(self):
        """Lists settings of a given vm
        """
        self.list_machines()
        print("==========================")
        choice = input("Enter VM to get info about: ")
        if choice.isnumeric():
            choice = int(choice) - 1
            if choice < len(self.vms):
                print(popen(f'vboxmanage showvminfo {self.vms[choice]}').read())
            else:
                print('Out of index for vms')
        else:
            print('Invalid choice for machine')
    
    def delete_vm(self):
        """Deletes a given VM
        """
        self.list_machines()
        print("==========================")
        choice = input("Enter VM to delete: ")
        if choice.isnumeric():
            choice = int(choice) - 1
            if choice < len(self.vms):
                print(popen(f'vboxmanage unregistervm {self.vms[choice]} --delete').read())
            else:
                print('Out of index for vms')
        else:
            print('Invalid choice for machine')
    
    def main(self):
        """Main function that runs for VBoxManage object
        """
        while True:
            selection = self.prompt()
            print(f'[{selection}] {self.options[selection]}')
            print("========================")
            if selection == "1":
                self.create_vm()
            elif selection == "2":
                self.list_machines()
            elif selection == "3":
                self.start_machine()
            elif selection == "4":
                self.stop_machine()
            elif selection == "5":
                self.list_vm_settings()
            elif selection == "6":
                self.delete_vm()
            elif selection == "7":
                break 
            else:
                print("[-] Invalid Response")
            print()

#Invokes a new VBoxManager object
VBoxManager()