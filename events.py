import controller as Controller
import sdl2.ext
import sdl2
from pyvjoystick import vigem as vg

import constants as Consts

class Events():
    def __init__(self):
        super().__init__()
        try:
            # This hint allows joystick events to be processed even when the window is not in focus or minimized.
            sdl2.ext.HINT_JOYSTICK_ALLOW_BACKGROUND_EVENTS = "1"

            # Initialize SDL
            sdl2.ext.init()

            self.virtual_driver_manager = Controller.VirtualDriverManager()
            
        except Exception as e:
            print(f'Failed Initialize SDL {e}')

    def run(self):
        try:
            running = True
            while running:
                events = sdl2.ext.get_events()
    
                for event in events:
                    
                    device_id = event.cdevice.which
                    # self.virtual_driver_manager.check(device_id)
                    # self.virtual_driver = self.virtual_driver_manager.get_virtual_driver(device_id)
                    
                    if event.type == sdl2.SDL_QUIT:
                        print(f'\nquit sdl2')
                        self.virtual_driver_manager.quit()
                        running = False
                        break
                    
                    if event.type == sdl2.SDL_CONTROLLERDEVICEREMOVED:
                        print(f'\nclose device: {device_id}')
                        # self.virtual_driver_manager.unload(device_id)
                        self.virtual_driver_manager.close(device_id)
                        
                    if event.type == sdl2.SDL_CONTROLLERDEVICEADDED:
                        print(f'\nopen device: {device_id}')
                        self.virtual_driver_manager.open(device_id)
            
                    # Handle joystick events
                    # if event.type == sdl2.SDL_JOYAXISMOTION:
                
                    #     # Read joystick axis values
                    #     axis_lx = self.gamepad.get_axis(Consts.AXIS['LEFT_STICK_X'])
                    #     axis_ly = self.gamepad.get_axis(Consts.AXIS['LEFT_STICK_Y'])
                    #     axis_rx = self.gamepad.get_axis(Consts.AXIS['RIGHT_STICK_X'])
                    #     axis_ry = self.gamepad.get_axis(Consts.AXIS['RIGHT_STICK_Y'])
                        
                    #     # Deadzone
                    #     left_deadzone = self.xb_gamepad.deadzone_axis(axis_lx, axis_ly)
                    #     right_deadzone = self.xb_gamepad.deadzone_axis(axis_rx, axis_ry)
                        
                    #     # Read triggers axis values
                    #     left_trigger = self.gamepad.get_axis(Consts.AXIS['LEFT_TRIGGER'])
                    #     right_trigger = self.gamepad.get_axis(Consts.AXIS['RIGHT_TRIGGER'])
                        
                    #     # Print the joystick values
                    #     print(f'Left Joystick   -   X: {left_deadzone[0]:.3f}')
                    #     print(f'Right Joystick  -   X: {right_deadzone[0]:.3f}')
                    #     print(f'Left Joystick   -   Y: {left_deadzone[1]:.3f}')
                    #     print(f'Right Joystick  -   Y: {right_deadzone[1]:.3f}')
                    #     # Print the bumper values
                    #     print(f'Left Bumper: {left_trigger:.3f}')
                    #     print(f'Right Bumper: {right_trigger:.3f}')
                        
                    #     # Handle axis values as needed
                    #     self.xb_gamepad.gamepad.left_joystick_float(x_value_float=left_deadzone[0], y_value_float=left_deadzone[1])
                    #     self.xb_gamepad.gamepad.right_joystick_float(x_value_float=right_deadzone[0], y_value_float=right_deadzone[1])

                    #     self.xb_gamepad.gamepad.update()

                    # elif event.type == sdl2.SDL_JOYBUTTONDOWN:
                        
                    #     # Read button values
                    #     button = event.cbutton.button
                    #     print(f'Button Down Key:{button} - Device:{device_id}')
                        
                    #     # Handle button presses as needed
                    #     if button == sdl2.SDL_CONTROLLER_BUTTON_A:
                    #         print(f'A Button pressed - reMapped:{hex(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)}')
                    #         self.virtual_driver.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
                    #         self.virtual_driver.update()
                        
                    #     if button == sdl2.SDL_CONTROLLER_BUTTON_B:
                    #         print(f'A Button pressed - reMapped:{hex(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)}')
                    #         self.virtual_driver.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                    #         self.virtual_driver.update()
                        
                    #     if button == sdl2.SDL_CONTROLLER_BUTTON_X:
                    #         print(f'A Button pressed - reMapped:{hex(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)}')
                    #         self.virtual_driver.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
                    #         self.virtual_driver.update()
                        
                    #     if button == sdl2.SDL_CONTROLLER_BUTTON_Y:
                    #         print(f'A Button pressed - reMapped:{hex(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)}')
                    #         self.virtual_driver.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
                    #         self.virtual_driver.update()
                        
                    # elif event.type == sdl2.SDL_JOYHATMOTION:
                        
                    #     dpad = event.value
                    #     print(dpad)
                    #     # # Check for D-pad button presses
                    #     # if button == pygame.JOY_HATDOWN:
                    #     #     print("D-pad down button pressed")
                    #     # elif button == pygame.JOY_HATUP:
                    #     #     print("D-pad up button pressed")
                    #     # elif button == pygame.JOY_HATLEFT:
                    #     #     print("D-pad left button pressed")
                    #     # elif button == pygame.JOY_HATRIGHT:
                    #     #     print("D-pad right button pressed")
                            
                    # elif event.type == sdl2.SDL_JOYBUTTONUP:
                    #     # Read button values
                    #     button = event.cbutton.button
                    #     print(f'Button Up Key:{button}')
                    #     # Handle button releases as needed
                    #     if button == Consts.GAMEPAD['A']:
                    #         print(f'A Button pressed - reMapped:{hex(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)}')
                    #         self.virtual_driver.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
                    #         self.virtual_driver.update()
                        
                    #     if button == Consts.GAMEPAD['B']:
                    #         print(f'B Button pressed - reMapped:{hex(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)}')
                    #         self.virtual_driver.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                    #         self.virtual_driver.update()
                        
                    #     if button == Consts.GAMEPAD['X']:
                    #         print(f'X Button pressed - reMapped:{hex(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)}')
                    #         self.virtual_driver.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
                    #         self.virtual_driver.update()
                        
                    #     if button == Consts.GAMEPAD['Y']:
                    #         print(f'Y Button pressed - reMapped:{hex(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)}')
                    #         self.virtual_driver.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
                    #         self.virtual_driver.update()
        
        except KeyboardInterrupt as e:
            print(f'Error: {e}')
            
        except Exception as e:
            print(f'Error: {e}')
