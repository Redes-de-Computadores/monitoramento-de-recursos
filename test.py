import time


def resource_request():
    while True:     
        time.sleep(1) 

        print('''
        For a server resource checking choose:

        1.RAM Memory
        2.CPU
        3.GPU
        0.Exit
        ''')
        chosen_resource_option = int(input('What\'s ur choice? '))
        
        if(chosen_resource_option > 0 and chosen_resource_option < 3):
            info_type(chosen_resource_option)
        elif(chosen_resource_option == 0):
            exit()
            break
        else:
            err()

def info_type(chosen_resource_option):
    resource = ''
    while True:
        time.sleep(1)
        if(chosen_resource_option == 1):
            resource = 'RAM Memory'
        elif (chosen_resource_option == 2):
            resource = 'CPU'
        elif (chosen_resource_option == 3):
            resource = 'GPU'
        print(f'''
            What type information u want to see:

            1.Total of {resource}
            2.{resource} available
            3.{resource} usage percent
            4.{resource} used
            5.{resource} free
            0.Voltar
            ''')
        chosen_type = int(input('What\'s ur choice? '))
        print('\n')

        print(f'Ur choice was: {chosen_type}')

        if(chosen_type > 0 and chosen_type < 4):
            info_type(chosen_resource_option)
        elif(chosen_type == 0):
            print('Getting back to the Menu...')
            break
        else:
            err()

def err():
    print('''
    ===================
      Invalid Option!
    ===================
    ''')
    time.sleep(1)

def exit():
    print('''
    ============
      Bye Bye!
    ============
    ''')
    time.sleep(1)

def start():
    print('''
    =====================================
    Welcome to Server Resources Monitorer
    =====================================
    ''')
    resource_request()

start()