# handlers/__init__.py
from .start import router as start_router
from .main_menu import router as main_menu_router
from .project_info import router as project_info_router
from .ask_question import router as ask_question_router
from .fill_application import router as fill_application_router


all_routers = [
    start_router,
    main_menu_router,
    project_info_router,
    ask_question_router,
    fill_application_router,
]
