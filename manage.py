from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Pitch
from flask_migrate import Migrate,MigrateCommand

# Creating app instance

app  = create_app ("production")

#create manage instance
manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(testsg)
@manager.shell
def make_all_shell_context():
    return dict(app = app ,db =db ,User = User, Pitch = Pitch )

if __name__ == '__main__':
    manager.run()