from classes.helper import Helper
from classes.store import Store

store_name = 'Blockbuster'

def run():
    store = Store(store_name)
    while True:
        mode = input(Helper.main_menu(store.name))
        if mode == '1':
            Helper.clear_console()
            store.display_inventory()
            input('\nPress any key to return to menu')
        elif mode == '2':
            store.display_all_customers()
            input('\nPress any key to return to menu')
        elif mode == '3':
            store.display_customer_videos()
        elif mode == '4':
            store.add_customer()
        elif mode == '5':
            store.rent()
        elif mode == '6':
            store.return_videos()
        elif mode == '7':
            store.change_customer_account()
        elif mode == '8':
            store.delete_customer_account()
        elif mode == '9':
            store.add_videos()
        elif mode == '10':
            store.remove_videos()
        elif mode == '11':
            store.save()
            return
        else:
            input('Not a valid menu choice. Press any key to try again')

run()