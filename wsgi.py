from jaaql.jaaql import create_app
from controller import JAAQLHelloWorldController
import documentation as documentation

# from os.path import join, dirname
# migration_folder = join(dirname(__file__), "migrations")
# migration_project_name = "example"


if __name__ == '__main__':
    port, flask_app = create_app(supplied_documentation=documentation, controllers=[JAAQLHelloWorldController()],
                                 # migration_folder=migration_folder,
                                 # migration_project_name=migration_project_name
                                 )
    flask_app.run(port=port, host="0.0.0.0", threaded=True,)
else:
    def build_app(*args, **kwargs):
        return create_app(is_gunicorn=True, supplied_documentation=documentation,
                          # migration_folder=migration_folder,
                          # migration_project_name=migration_project_name,
                          controllers=[JAAQLHelloWorldController()], **kwargs)
