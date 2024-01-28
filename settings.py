# CONSTANTS
ROOT_DIR = "/Users/abhijitrawool"
# Classes


# Shell Input
class ShellInput:
    @property
    def req(self):
        return self.required

    @property
    def opt(self):
        return self.optional

    def option_check(self, req):
        self.optional = self.args[req:]
        for exception in self.exceptions[len(self.optional) :]:
            self.optional.append(exception)
        return self.required + self.optional

    def shell_input(self, req: int, args: list, exceptions: list = []):
        self.exceptions = exceptions
        self.args = args[1:]
        self.inputs = []
        self.required = self.args[:req]
        if len(self.args) < req:
            raise Exception("You must enter all necessary parameters")
        for arg in self.args:
            self.inputs.append(arg)
        inputs = self.option_check(req)
        return inputs


def get_shell_input(req: int, args: list, exceptions: list = []):
    shell_exec = ShellInput()
    inputs = shell_exec.shell_input(req, args, exceptions)
    return inputs
