import os
import os.path
import subprocess
import yaml
import enquiries


def write_rules(data, filename ="/etc/falco/falco_rules.yaml"):     #This function writes the data into the file.
    with open("/etc/falco/falco_rules.yaml", 'w') as f:
        yaml.dump(data, f, indent=4)



def load_data(entries):                                      #This function loads the appended data into the file
    with open("/etc/falco/falco_rules.yaml") as f:
        data = yaml.full_load(f)
        for item in data:
        
            key = "list"
            if key in item.keys():
                if item["list"] == "trusted_images":
                    final = item["items"]
                    final_result = final + entries
                    item["items"] = list(set(final_result))
                    print("Below images are part of the rule after addition")
                    print(final_result)
                    print("--------------------------------------------------------------------------------")
                    write_rules(data)



def remove_data(entries):                                      #This function removes the data from the file
    with open("/etc/falco/falco_rules.yaml") as f:
        data = yaml.full_load(f)
        for item in data:
        
            key = "list"
            if key in item.keys():
                if item["list"] == "trusted_images":
                    final = item["items"]
                    print("Below images are part of the rule")
                    print(final)
                    print("--------------------------------------------------------------------------------")

                    for n in entries:
                        if n in final:
                            final.remove(n)
                    item["items"] = list(set(final))
                    print("Below is the list of images left after the deletion")
                    print(final)
                    print("--------------------------------------------------------------------------------")

                    write_rules(data)



def view_data():                                                            #This funtion gets called by the other functions to view the registry list.
    with open("/etc/falco/falco_rules.yaml") as f:
        data = yaml.full_load(f)
        for item in data:
        
            key = "list"
            if key in item.keys():
                if item["list"] == "trusted_images":
                    final = item["items"]
                    print("Below is the list of images already present in the rule")
                    print(final)
                    print("--------------------------------------------------------------------------------")



def new_rule_cli():                                                         #This function adds a new rule to the list of rules.

    options = ['new_general_rule', 'new_k8s_rule', 'Main_Menu']                     
    choice = enquiries.choose('Choose one of these options: ', options)
    if choice == 'new_general_rule':

        with open("/etc/falco/falco_rules.yaml") as f:
            data = yaml.full_load(f)

            new_rule = {"rule": "", "desc": "", "condition": "", "output": "", "priority": "", "tags": ""}
        
            rule_name = input("Enter the name of the rule: ")
            new_rule["rule"] = rule_name

            description = input("Enter the description for the rule: ")
            new_rule["desc"] = description

            condition = input("Enter the conditions for the rule: ")
            new_rule["condition"] = condition

            output = input("Enter the output for the rule: ")
            new_rule["output"] = output

            priority = input("Enter the priority for the rule: ")
            new_rule["priority"] = priority

            tags = input("Enter the tags for the rule: ")
            new_rule["tags"] = tags
            data.append(new_rule)
            write_rules(data)
           
    elif choice == 'new_k8s_rule':

        print("work in progress")
    
    else:
        main_menu()
        



#def update_file():                                          #This function copies the rule file, and creates a backup
    #if os.path.isfile("/home/vagrant/falco/falco_rules.yaml.bak"):
     #   os.popen('rm /home/vagrant/falco/falco_rules.yaml.bak; cp /etc/falco/falco_rules.yaml /home/vagrant/falco/falco_rules.yaml.bak')
    #else:  
     #   os.popen('cp /etc/falco/falco_rules.yaml /home/vagrant/falco/falco_rules.yaml.bak')



def change_registry():                                         #This function makes changes to existing trusted registries
    options = ['Add_Registry', 'Delete_Registry', 'Main_Menu']
    choice = enquiries.choose('Choose one of these options: ', options)
    entries = []
    
    if choice == "Add_Registry":
        view_data()
        n = int(input("Enter the number of registries you want to enter: "))
        for i in range(0, n):
            reg = input()
            entries.append(reg)
        #print(entries)
        #update_file()
        load_data(entries)

    elif choice == 'Delete_Registry':
        view_data()
        n = int(input("Enter the number of registries you want to delete: "))
        for i in range(0, n):
            reg = input()
            entries.append(reg)
            #update_file()
        remove_data(entries)
    else:
        main_menu()


def list_rules():                                                                               #This function is used to view the rules
    options = ['View_general_rules', 'View_k8s_rules', 'main_menu']                     
    choice = enquiries.choose('Choose one of these options: ', options)
    res = []
    if choice == 'View_general_rules':
        
        with open("/etc/falco/falco_rules.yaml") as f:
            data = yaml.full_load(f)
            print ("Below is the list of rules present:")
            print("--------------------------------------------------------------------------------")
            for item in data:
                key = 'rule'
                if key in item.keys():   
                    print(item[key])
            print("--------------------------------------------------------------------------------")
    elif choice == 'View_k8s_rules':
        print("work in progress")
    else:
        main_menu()

        

def main_menu():                                                                  
    options = ['Add_a_new_rule', 'Change_an_existing_rule', 'list_all_the_rules']                     
    first_choice = enquiries.choose('Choose one of these options: ', options)

    if first_choice == 'Change_an_existing_rule':
        change_registry()

    elif first_choice == 'list_all_the_rules':
        list_rules()

    else:
        options = ['Add_via_cli', 'Add_via_file_upload', 'Main_menu']
        choice = enquiries.choose('Choose one of these options: ', options)

        if choice == "Add_via_cli":
            new_rule_cli()
    
        elif choice == "Add_via_file_upload":
            print("Work in progress")
        else:
            main_menu()
    


main_menu()                                                                     #code starts from here







