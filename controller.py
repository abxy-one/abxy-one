import pygame
from pyvjoystick import vigem as vg

import constants as Consts

class XboxGamePad:
    
    def __init__(self):
        try:
            # Initialize VX360Gamepad
            self.gamepad = vg.VX360Gamepad()
            print(f'VX360Gamepad initialized: {self.gamepad}')

            # Initialize pyGame
            self.pygame_init = pygame.init()
            print(f'PyGame initialized: {self.pygame_init}')

        except Exception as e:
            print(f'No gamepad connected {e}')

    def _get_version(self):
        # Get PyGame version
        try:
            version = int(pygame.version.ver[0])
        except Exception as e:
            print(f'Error getting PyGame version {e}')
            
        return version

    def _get_controllers(self):
        try:
            controllers = []
            # List controllers
            for i in range(pygame.joystick.get_count()):
                joystick = pygame.joystick.Joystick(i)
                joystick.init()
                controllers.append(
                    {
                        'id': joystick.get_id(),
                        'name': joystick.get_name(),
                        'guid': joystick.get_guid()
                    }
                )
        except Exception as e:
            print(f'Error getting controllers {e}')
        
        print(f'Controllers found: {controllers}')
        return controllers

    def load_controllers(self):
        try:
            controller_obj = []
            controllers = self._get_controllers()
            for i in controllers:
                
                if i['guid'] == Consts.VIRTUAL_DRIVER_GUID:
                    pass
                else:
                    joystick = pygame.joystick.Joystick(i['id'])
                    joystick.init()
                    
                    controller_obj.append(
                        {
                            'id': i['id'],
                            'name': i['name'],
                            'controller_obj': joystick 
                            }
                        )
        except Exception as e:
            print(f'Error loading controllers {e}')
        
        print(f'Controllers loaded: {controller_obj}')
        return controller_obj
    
    def deadzone_axis(self, axis_x, axis_y):
        try:
            magnitude = (axis_x ** 2 + axis_y ** 2) ** 0.5
            # Apply the deadzone
            if magnitude < Consts.DEADZONE_THRESHOLD:
                axis_x = 0.0
                axis_y = 0.0
            # Normalize the input. Performs division and assignment
            else:
                axis_x /= magnitude
                axis_y /= magnitude
        except Exception as e:
            print(f'Error get deadzone_axis {e}')

        return axis_x, axis_y
