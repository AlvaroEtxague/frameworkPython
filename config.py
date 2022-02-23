from environments import Environments as environ


class Config:
    def __init__(self, env):
        self.env = {
            'qa': environ.qa,
            'dev': environ.dev,
        }[env]
