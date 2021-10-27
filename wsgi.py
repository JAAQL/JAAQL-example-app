from jaaql.patch import monkey_patch

if __name__ != '__main__':
    monkey_patch()  # Patch to use async if launched by gunicorn. Important to patch _first_ before anything else

from jaaql.jaaql import create_app
from controller import JAAQLHelloWorldController
import documentation as documentation

if __name__ == '__main__':
    port, flask_app = create_app(supplied_documentation=documentation, controllers=[JAAQLHelloWorldController()])
    flask_app.run(port=port, host="0.0.0.0", threaded=True)
else:
    def build_app(*args, **kwargs):
        return create_app(is_gunicorn=True, supplied_documentation=documentation,
                          controllers=[JAAQLHelloWorldController()], **kwargs)
