from documentation.documentation_hello import DOCUMENTATION__hello_world, KEY__name, KEY__response
from jaaql.mvc.controller_interface import JAAQLControllerInterface, BaseJAAQLController


class JAAQLHelloWorldController(JAAQLControllerInterface):

    def route(self, base_controller: BaseJAAQLController):

        @base_controller.cors_route('/hello-world', DOCUMENTATION__hello_world)
        def submit(http_inputs: dict):
            return {
                KEY__response: "Hello %s!" % http_inputs[KEY__name]
            }
