from time import sleep
from replit import clear
from DataChecker import DataChecker

class Menu(DataChecker):
    def __init__(self) -> None:
        super().__init__()
        self.main=self.config["main_menu"]
        self.create= self.config["create_menu"]
        self.show = self.config["show_menu"]
        self.main_menu()

    def main_menu(self):
        userinput = self.menu_parser(self.main, "Main-Menu")
        if userinput == 0:
            self.save_csv()
        elif userinput == 1:
            self.show_menu()
        elif userinput == 2:
            self.edit_menu()
        elif userinput == 666:
            self.save_csv()
        else:
            print("Something went wrong")

    def edit_menu(self):
        clear()
        userinput = self.menu_parser(self.create, "Edit-Menu")
        if userinput == 0:
            self.save_csv()
        elif userinput == 1:
            self.main_menu()
        elif userinput == 2:
            self.create_item()
        elif userinput == 3:
            self.change_item()
        elif userinput == 4: 
            self.delete_item()
        elif userinput == 666:
            self.main_menu()
        else:
            print("Something went wrong")

    def show_menu(self):
        clear()
        userinput = self.menu_parser(self.show, "Show-Menu")
        if userinput == 0:
            self.quit_and_save()
        elif userinput == 1:
            self.main_menu()
        elif userinput == 2:
            self.print_csv()
        elif userinput == 3:
            self.search_by_index()
        elif userinput == 4:
            self.status_filter()
        elif userinput == 5:
            self.sort_after()
        elif userinput == 666:
            self.main_menu()
        else:
            print("Something went wrong")

    def menu_parser(self, menu, title):
        clear()
        userinput = 0
        print("{}\nChoose Entry:\n".format(title))
        for item in menu:
            print("{}: {}".format(menu.index(item),item))
        userinput = input()
        try: 
            userinput = int(userinput)
        except ValueError:
            print("Only Int-Allowed - Programm Exit")
            exit()
        if userinput < 0 or userinput > len(menu)-1:
            clear()
            print("Not Available, back to Main menu")
            sleep(2)
            return 666
        return userinput

if __name__ == "__main__":
    programm = Menu()
