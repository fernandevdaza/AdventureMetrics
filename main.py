from db.connection import get_session
from user_interface.main_menu import main_menu
with get_session() as session:
    main_menu(session)