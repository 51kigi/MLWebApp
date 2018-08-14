from flask_script import Manager
from flask_blog import appa

from flask_blog.scripts.db import InitDB


if __name__ == "__main__":
    manager = Manager(appa)
    manager.add_command('init_db', InitDB())
    manager.run()

