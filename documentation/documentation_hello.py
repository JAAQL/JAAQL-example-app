from jaaql.openapi.swagger_documentation import *

TITLE = "JAAQL Example API"
DESCRIPTION = "Hello World with JAAQL"
FILENAME = "jaaql_example_api"

KEY__name = "name"
KEY__response = "response"

DOCUMENTATION__hello_world = SwaggerDocumentation(
    tags="Greetings",
    security=False,
    methods=SwaggerMethod(
        name="Say Hello",
        description="Asks JAAQL to say hello",
        method=REST__POST,
        body=[
            SwaggerArgumentResponse(
                name=KEY__name,
                description="Who you want this JAAQL application to say hello to",
                arg_type=str,
                example=["Aaron", "Graham"],
                required=True
            )
        ],
        response=SwaggerResponse(
            description="Contains information to setup authenticator app",
            response=[
                SwaggerArgumentResponse(
                    name=KEY__response,
                    description="Response from JAAQL",
                    arg_type=str,
                    example=["Hello Aaron!", "Hello Graham!"],
                    required=True
                )
            ]
        )
    )
)
