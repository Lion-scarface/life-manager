import random
import logo
import webbrowser
list_pas = []
def play():
     while 1 == 1:
          what = input("What do you want ( (1)'view', (2)'add' , (3) 'delete'  ,   (4)'Benefits and harms' ,  (5)'Delete everything' ) or 'help': ").lower()
          if what == "add" or what == "2":
               add = open(r"C:\Users\med66\Desktop\Life manager\add.txt", "a")
               enter_add = input("Write something (or lave a space to exit): ")
               while enter_add != "":
                    add.write(f"{enter_add}\n")
                    enter_add = input("Write something (or lave a space to exit): ")
               add.close()
          elif what == "view" or what == "1" :
                add = open(r"C:\Users\med66\Desktop\Life manager\add.txt", "a")
                add = open(r"C:\Users\med66\Desktop\Life manager\add.txt", "r")
                vi = add.read()
                print("\n  ************ TASKS **************\n")
                print(vi)
                print("\n  *********** END TASKS **********\n")
                input("\n Press (ENTER) to return ....")
          elif what == "delete"or what == "3" :
               add = open(r"C:\Users\med66\Desktop\Life manager\add.txt", "a")
               add = open(r"C:\Users\med66\Desktop\Life manager\add.txt", "r")
               vi = add.read()
               print("\n  ************ TASKS ************\n")
               print(vi)
               print("\n  ************ END TASKS *********\n")
               delete = input("Write what you want to delete : ").lower()
               bo = open(r"C:\Users\med66\Desktop\Life manager\add.txt", "a")
               med = vi.splitlines()
               med.remove(delete)
               bo.close()
               bo = open(r"C:\Users\med66\Desktop\Life manager\add.txt", "w")
               bo.write("\n".join(med))
               bo.close()
          elif what == "benefits and harms" or what == "4":
               look = input("What do you want to look for?: ")
               if look:
                    webbrowser.open(f"https://www.google.com/search?q=Pros%20and%20cons%20of%20this%20routine%20{look}&sca_esv=77cf4491859813e6&sxsrf=ANbL-n7BX7b60BVNCB4_9SGboleqBzMOtg%3A1768482824522&ei=COhoafLQH5yqkdUP1eLPoQk&ved=0ahUKEwjy9K_0z42SAxUcVaQEHVXxM5QQ4dUDCBE&uact=5&oq=hhhhhh&gs_lp=Egxnd3Mtd2l6LXNlcnAiBmhoaGhoaEi2HlAAWOUTcAF4AZABAJgB2gGgAc0IqgEFMC40LjK4AQPIAQD4AQGYAgWgAsgHqAIQwgIHECMYJxjqAsICDRAjGIAEGCcYigUY6gLCAhcQABiABBiRAhi0AhjnBhiKBRjqAtgBAcICCxAAGIAEGJECGIoFwgIFEAAYgATCAgsQLhiABBjRAxjHAcICBRAuGIAEwgIKEC4YgAQYQxiKBcICEBAuGIAEGNEDGEMYxwEYigXCAhkQLhiABBhDGIoFGJcFGNwEGN4EGN8E2AEBwgIZEC4YgAQYQxiKBRiXBRjcBBjeBBjgBNgBAZgDNeIDBRIBMSBA8QXQ_W-WmTXPbboGBggBEAEYAZIHBTEuMC40oAfEL7IHAzItNLgHkgfCBwkyLTEuMS4yLjHIB5YBgAgA&sclient=gws-wiz-serp")
          elif what == "delete everything" or what == "5":
               print("\n  ************ TASKS **************\n")
               print("    Everything was deleted      ")
               print("\n  ************ END TASKS ***********\n")
               add = open(r"C:\Users\med66\Desktop\Life manager\add.txt", "w")
               add.close()
          elif what == "help":
               print("""
         **************************** HELP *********************************
          The program specializes in recording daily habits or routines and 
          stores this information in a file that you control. You can then 
                     search for the benefits and drawbacksz
         *******************************************************************
""")
          else:
               print("I don't understand what you'rs saying !!")
def pas_newo():

    pasw = open(r"C:\Users\med66\Desktop\Life manager\password", "a")
    pasw.close()
    pasw = open(r"C:\Users\med66\Desktop\Life manager\password", "r")
    viu_password = pasw.read()
    if viu_password:
        Enter_password = input("Enter the password: ")
        list_pas.append(Enter_password)
        if Enter_password == viu_password:
            print("\n *** Welcome to life manager *** \n")
            play()
        else:
                print("Incorrect password:")
    else:
        Enter_password_newo = input("Enter the newo password: ")
        pasw.close
        pasw = open(r"C:\Users\med66\Desktop\Life manager\password", "w")
        pasw.write(Enter_password_newo)
        pasw.close()
        play()

ff = open(r"C:\Users\med66\Desktop\Life manager\do_password", "a")
ff.close
ff = open(r"C:\Users\med66\Desktop\Life manager\do_password", "r")
hh = ff.read()
print(random.choice(logo.logo))
if hh:
    if hh == "yas":
         pas_newo()
         pasw = open(r"C:\Users\med66\Desktop\Life manager\password", "r")
         if pasw.read() == "".join(list_pas):
              play()
    else:
         print("\n *** Welcome to life manager *** \n")
         play()
else:
    do_password = input("\nDo you want her to have 'life manager' the password? (yas or no ) : ").lower().split(" ")
    ff = open(r"C:\Users\med66\Desktop\Life manager\do_password", "w")
    if  "yas" in do_password  or "yes" in do_password :
        ff.write("yas")
        ff.close()
        pas_newo()
        play()
    elif "no" in do_password  or "no" in do_password :
         ff.write("no")
         ff.close()
         print("We will continue without the password ? :")
         play()
    else:
        print("I don't understand what you're saying !!")

input("")