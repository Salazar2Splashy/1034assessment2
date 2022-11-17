import datetime
import json


def search(clients_list, returndest): #the search function
    potential_clients_list = []
    selected = get_number_input("\nWhat would you like to search by?\n"
                                "1. View all clients\n"
                                "2. First Name\n"
                                "3. Last Name\n"
                                "4. Birthday\n"
                                "5. All with Negative Balance\n", 5)
    print("\nClients List:") #this then gets the inputs and searches adding any matches to a list of potential matches
    if selected == 1:
        potential_clients_list = clients_list
    elif selected == 2:
        searchfor = input("Search: ")
        for cl in clients_list:
            if cl.First_Name == searchfor:
                potential_clients_list.append(cl)
    elif selected == 3:
        searchfor = input("Search: ")
        for cl in clients_list:
            if cl.Last_Name == searchfor:
                potential_clients_list.append(cl)
    elif selected == 4:
        searchfor = input("Search: ")
        for cl in clients_list:
            if cl.DOB == searchfor:
                potential_clients_list.append(cl)
    elif selected == 5:
        for cl in clients_list:
            balance = cl.Balance
            balance = int(balance)
            if balance < 0:
                potential_clients_list.append(cl)
    client_number = 0
    for i in potential_clients_list:
        client_number += 1 # each client is given a number so they're identifiable to the user
        print(client_number, "-",
              (', '.join("%s: %s" % item for item in vars(i).items())).replace("_", " "))
    print('\n')
    n = 0
    for i in potential_clients_list:
        n += 1
    if n > 0:
        selected = get_number_input("\nWhich client do you wish to alter?", n)
        selected -= 1
        target = potential_clients_list[selected]
        print((', '.join("%s: %s" % item for item in vars(i).items())).replace("_", " "))
    else:
        print("\nNo clients found.")
        if returndest == "search":
            client_management(2)
        elif returndest == "balance":
            menu()
    return target # returns the client they want


def menu():  # MAIN MENU
    todo = get_number_input("What would you like to do?\n"
                            "1. Manage/View clients/details\n"
                            "2. Edit client balance\n"
                            "3. Save\n"
                            "4. Exit\n", 4)
    function_list(todo)


def get_number_input(message, limit): #this function is used to verify number inputs for menus
    print(message)
    accepted = False
    while not accepted:
        selected = input("Selection: ")
        try:
            selected = int(selected)
            if 0 < selected <= limit:
                accepted = True
            else:
                print(f"Option must be between 1 and {limit}.\n")
        except ValueError:
            print("Please enter an integer value.\n")
    return selected


class Client: # the client class
    def __init__(self, First_Name, Last_Name, Title, Pronouns, DOB, Job, Balance, Overdraft_Limit):
        self.First_Name = First_Name.title()
        self.Last_Name = Last_Name.title()
        self.Title = Title.title()
        self.Pronouns = Pronouns.title()
        self.DOB = DOB.title()
        self.Job = Job.title()
        self.Balance = Balance
        self.Overdraft_Limit = Overdraft_Limit

    def __iter__(self):
        return self

    def __next__(self):
        for i in range(8):
            return str(i)
        raise StopIteration

    def getvalues(self):
        return self.First_Name, self.Last_Name, self.Title, self.Pronouns, self.DOB, self.Job, self.Balance, self.Overdraft_Limit


def client_management(option):
    if option == 1:  # ADD NEW CLIENT
        print("\nInsert client details:")
        firstname = input("First name(s):\n").title()
        lastname = input("Surname:\n").title()
        title = input("Title:\n").title()
        usinput = get_number_input("Pronouns:\n"
                                   "1. He/Him\n"
                                   "2.She/Her\n"
                                   "3. They/Them\n", 3)
        usinput -= 1
        pronounlist = ["He/Him", "She/Her", "They/Them"]
        pronouns = pronounlist[usinput]
        accepted = False
        while not accepted:
            dob = input("Date Of Birth (DD/MM/YYYY):\n")
            try:
                reformed = datetime.datetime.strptime(dob, "%d/%m/%Y")
                accepted = True
            except:
                print("Incorrect date entered!\n")
        job = input("Job Title:\n").title()
        accepted = False
        while not accepted:
            starting_balance = input("Starting Balance:\n")
            try:
                starting_balance = float(starting_balance)
                accepted = True
            except:
                print("\nPlease enter a valid float value.\n")
        accepted = False
        while not accepted:
            overdraft_limit = input("Overdraft Limit:\n")
            try:
                overdraft_limit = float(overdraft_limit)
                accepted = True
            except:
                print("\nPlease enter a valid float value.\n")
        if overdraft_limit > 0: # this is done so that if the user enters the limit to be 3000, it is converted to -3000 for usage in withdrawal
            overdraft_limit *= -1
        new_client = Client(firstname, lastname, title, pronouns, dob, job, starting_balance, overdraft_limit)
        print(('\n'.join("%s: %s" % item for item in vars(new_client).items())).replace("_", " ")) # allows a nice print
        confirmation = input("Are the above details correct?\n").title()
        while confirmation != "Y" and confirmation != "N":
            confirmation = input("Please enter either Y or N.\n").title()
        if confirmation == "Y":
            clients_list.append(new_client)
            print("Successfully added client.\n")
            menu()
        else:
            client_management(1)
    elif option == 2:  # SEARCH CLIENT LIST
        target = search(clients_list, "search")
        to_edit = get_number_input("\nWhich value do you wish to alter?\n"
                                   "1. First Name\n"
                                   "2. Surname\n"
                                   "3. Title\n"
                                   "4. Pronouns\n"
                                   "5. DOB\n"
                                   "6. Job\n"
                                   "7. Overdraft Limit\n"
                                   "8. Delete Client", 8)
        target2 = target
        if to_edit == 1:
            newvalue = input("New First Name:\n").title()
            target2.First_Name = newvalue
        elif to_edit == 2:
            newvalue = input("New Surname:\n").title()
            target2.Last_Name = newvalue
        elif to_edit == 3:
            newvalue = input("New Title:\n").title()
            target2.Title = newvalue
        elif to_edit == 4:
            usinput = get_number_input("Pronouns:\n"
                                       "1. He/Him\n"
                                       "2.She/Her\n"
                                       "3. They/Them\n", 3)
            usinput -= 1
            pronounlist = ["He/Him", "She/Her", "They/Them"]
            newvalue = pronounlist[input]
            target2.Pronouns = newvalue
        elif to_edit == 5:
            accepted = False
            while not accepted:
                dob = input("Date Of Birth (DD/MM/YYYY):\n")
                try:
                    reformed = datetime.datetime.strptime(dob, "%d/%m/%Y") #checks for correct formatting
                    accepted = True
                except:
                    print("Incorrect date entered!\n")
            target2.DOB = dob
        elif to_edit == 6:
            newvalue = input("New Job:\n").title()
            target2.Job = newvalue
        elif to_edit == 7:
            accepted = False
            while not accepted:
                overdraft_limit = input("New Overdraft Limit:\n")
                try:
                    overdraft_limit = float(overdraft_limit)
                    accepted = True
                except:
                    print("\nPlease enter a valid float value.\n")
            if overdraft_limit > 0:
                overdraft_limit *= -1
            target2.Overdraft_Limit = overdraft_limit
        if to_edit == 8:
            confirmation = input("Are you sure you wish to delete client?\n").title()
            while confirmation != "Y" and confirmation != "N":
                confirmation = input("Please enter either Y or N.\n").title()
            if confirmation == "Y":
                clients_list.remove(target)
                print("Successfully deleted client.\n")
                menu()
            else:
                client_management(2)
        else:
            clients_list.remove(target)
            clients_list.append(target2)
            menu()
    elif option == 3:  # return to menu
        menu()


def function_list(option):  # OPERATIONS WITHIN EACH CATEGORY
    if option == 1:  # WITHIN CLIENT MANAGEMENT
        todo = get_number_input("\nWhat would you like to do?\n"
                                "1. Add new client\n"
                                "2. View/Edit/Remove clients\n"
                                "3. Return to main\n", 3)
        client_management(todo)
    elif option == 2:
        target = search(clients_list, "balance")
        accepted = False
        while not accepted:
            newbalance = input("Enter amount to add: ")
            try:
                newbalance = float(newbalance)
                accepted = True
            except:
                print("\nPlease enter a valid float value.\n")
        if target.Balance < target.Overdraft_Limit:
            confirmation = input("You will be charged an additional £5 for going below limit. Do you wish to proceed? (Y/N)\n").title()
            while confirmation != "Y" and confirmation != "N":
                confirmation = input("Please enter either Y or N.\n").title()
            if confirmation == "N":
                menu()
            else:
                target.Balance += -5
        target.Balance += newbalance
        menu()
    elif option == 3: #saves clients to file
        jsonString = json.dumps(clients_list, default=vars)
        jsonFile = open("data.json", "w")
        jsonFile.write(jsonString)
        jsonFile.close()
        print("Saved.\n")
        menu()


clients_list = []

try: #tries to load clients from file
    f = open('data.json')
    jsonlist = json.load(f)
    for cli in jsonlist:
        newcli = Client(cli['First_Name'], cli['Last_Name'], cli['Title'], cli['Pronouns'], cli['DOB'], cli['Job'],
                        cli['Balance'], cli['Overdraft_Limit'])
        clients_list.append(newcli)
except:
    print("Warning: No existing clients found!\n")
menu()
