import json

class Load():
    
    def __init__(self, filename) -> None:
        self.filename = filename

    def load(self):
        with open(self.filename, 'r') as file:
            data_read = json.load(file)
        return data_read
    
    def write(self, data):
        with open(self.filename, 'w') as file:
            json.dump(data, file)

class Bindings():
    
    def __init__(self) -> None:
        self.data = Load(filename='files\\bindings.json').load()

    def get_button_data(self, button=None):
        self.button = button
        return self.data[self.button]

    def get_button_bindings(self, button_data=None, action=None):
        self.button_data = button_data
        self.action = action
        bindings = self.button_data['Actions'][self.action]['Bindings']
        return bindings
