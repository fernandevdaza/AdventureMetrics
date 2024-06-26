from db.connection import get_session
from user_interface.main_menu import main_menu
from user_interface.clear_util import clear
def main():
    with get_session() as session:
        clear()
        main_menu(session)
        session.close()

main()