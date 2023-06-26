import pygame
from pyvjoystick import vigem as vg

import constants as Consts

class XboxGamePad:
    
    def __init__(self):
        # Initialize VX360Gamepad
        self.gamepad = vg.VX360Gamepad()

        # Initialize pyGame
        pygame.init()

    def _get_version(self):
        # Get PyGame version
        version = int(pygame.version.ver[0])
        return version

    def _get_controllers(self):
        controllers = []
        # List controllers
        for i in range(pygame.joystick.get_count()):
            joystick = pygame.joystick.Joystick(i)
            controllers.append(
                {
                    'id': joystick.get_id(),
                    'name': joystick.get_name(),
                    'guid': joystick.get_guid()
                }
            )
        return controllers

    def load_controllers(self):
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
        return controller_obj
    
    def deadzone_axis(self, axis_x, axis_y):
        magnitude = (axis_x ** 2 + axis_y ** 2) ** 0.5
        # Apply the deadzone
        if magnitude < Consts.DEADZONE_THRESHOLD:
            axis_x = 0.0
            axis_y = 0.0
        # Normalize the input. Performs division and assignment
        else:
            axis_x /= magnitude
            axis_y /= magnitude
        
        return axis_x, axis_y
