import virtualbox

class VBoxManager:
    def __init__(self):
        self.vbox = virtualbox.VirtualBox()
        self.options = {
            "1":"Create a VM",
            "2":"List all available VMs",
            "3":"Start a VM",
            "4":"Stop a VM",
            "5":"List Setting of a VM",
            "6":"Delete a VM",
            "7":"End the program"
        }
        self.main()
    
    def prompt(self): 
        print("Options:")
        print("========================")
        for key, value in self.options.items():
            print(f'{key} {value}')
        print("========================")
        selection = input()
        print()
        if selection in ("1", "2", "3", "4", "5", "6", "7"):
            return selection
        return False
    
    def list_machines(self):
        for i, machines in enumerate(self.vbox.machines):
            print(f'[{i + 1}] {machines.name}')
    
    def start_machine(self):
        self.list_machines()
        print()
        machine = input("Select which VM to start: ")
        if machine.isnumeric():
            if int(machine) <= len(self.vbox.machines):
                session = virtualbox.Session()
                progress = self.vbox.machines[int(machine) - 1].launch_vm_process(session, 'gui', [])
                progress.wait_for_completion()
                print(dir(session))
                session.close()
            else:
                print("[-] Machines Index does not exists")
        else:
            print("[-] Invalid Selection")
    
    def stop_machine(self):
        self.list_machines()
        print()
        machine = input("Select which VM to start: ")
        if machine.isnumeric():
            if int(machine) <= len(self.vbox.machines):
                machine = self.vbox.machines[int(machine) - 1]
                if machine.state in (machine.state.powered_off, machine.state.paused):
                    print(f"[+] {machine.name} is already off")
                    return
                else:
                    session = virtualbox.Session()
                    progress = machine.launch_vm_process(session, "gui", [])
                    progress.wait_for_completion()
                    session.console.power_down()
                    session.close()
        else:
            print('[-] Invalid Selection')
    
    def main(self):
        while True:
            selection = self.prompt()
            print(f'[{selection}] {self.options[selection]}')
            print("========================")
            if selection == "1":
                pass
            elif selection == "2":
                self.list_machines()
            elif selection == "3":
                self.start_machine()
            elif selection == "4":
                self.stop_machine()
            elif selection == "5":
                pass
            elif selection == "6":
                pass
            elif selection == "7":
                break 
            else:
                print("[-] Invalid Response")
            print()

VBoxManager()