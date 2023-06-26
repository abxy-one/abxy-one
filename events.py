import pygame
from pyvjoystick import vigem as vg

import constants as Consts
import controller as Controller

class Events():
    def __init__(self):
        self.gamepad = None
        self.gamepads = None
        self.xb_gamepad = None

    def initialize_gamepad(self):
        try:
            # Initialize VX360Gamepad
            self.xb_gamepad = Controller.XboxGamePad()
            
            # Get joystick instance
            self.gamepad = pygame.joystick.Joystick(0)
            self.gamepad.init()
            
            # Get list of controllers
            self.gamepads = self.xb_gamepad.load_controllers()
            # Get single controller object
            self.gamepad = self.gamepads[0]['controller_obj']
            print(self.gamepad.get_name())
            
        except Exception as e:
            print(f'No gamepad connected {e}')

    async def run(self):
        try:
            while True:
                # pygame.init()
                for event in pygame.event.get():
                    print(self.xb_gamepad.pygame_init)
                    if event.type == pygame.QUIT:
                        print('Quit event received. Stopping the thread...')
                        self.stop()

                    print(event.type)
                    
                    # Handle joystick events
                    if event.type == pygame.JOYAXISMOTION:
                
                        # Read joystick axis values
                        axis_lx = self.gamepad.get_axis(Consts.AXIS['LEFT_STICK_X'])
                        axis_ly = self.gamepad.get_axis(Consts.AXIS['LEFT_STICK_Y'])
                        axis_rx = self.gamepad.get_axis(Consts.AXIS['RIGHT_STICK_X'])
                        axis_ry = self.gamepad.get_axis(Consts.AXIS['RIGHT_STICK_Y'])
                        
                        # Deadzone
                        left_deadzone = self.xb_gamepad.deadzone_axis(axis_lx, axis_ly)
                        right_deadzone = self.xb_gamepad.deadzone_axis(axis_rx, axis_ry)
                        
                        # Read triggers axis values
                        left_trigger = self.gamepad.get_axis(Consts.AXIS['LEFT_TRIGGER'])
                        right_trigger = self.gamepad.get_axis(Consts.AXIS['RIGHT_TRIGGER'])
                        
                        # Print the joystick values
                        print(f'Left Joystick   -   X: {left_deadzone[0]:.3f}')
                        print(f'Right Joystick  -   X: {right_deadzone[0]:.3f}')
                        print(f'Left Joystick   -   Y: {left_deadzone[1]:.3f}')
                        print(f'Right Joystick  -   Y: {right_deadzone[1]:.3f}')
                        # Print the bumper values
                        print(f'Left Bumper: {left_trigger:.3f}')
                        print(f'Right Bumper: {right_trigger:.3f}')
                        
                        # Handle axis values as needed
                        self.xb_gamepad.gamepad.left_joystick_float(x_value_float=left_deadzone[0], y_value_float=left_deadzone[1])
                        self.xb_gamepad.gamepad.right_joystick_float(x_value_float=right_deadzone[0], y_value_float=right_deadzone[1])

                        self.xb_gamepad.gamepad.update()

                    elif event.type == pygame.JOYBUTTONDOWN:
                        
                        # Read button values
                        button = event.button
                        print(f'Button Down Key:{button}')
                        
                        # Handle button presses as needed
                        if button == Consts.GAMEPAD['A']:
                            print(f'A Button pressed - reMapped:{hex(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)}')
                            self.xb_gamepad.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
                            self.xb_gamepad.gamepad.update()
                        
                        if button == Consts.GAMEPAD['B']:
                            print(f'A Button pressed - reMapped:{hex(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)}')
                            self.xb_gamepad.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                            self.xb_gamepad.gamepad.update()
                        
                        if button == Consts.GAMEPAD['X']:
                            print(f'A Button pressed - reMapped:{hex(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)}')
                            self.xb_gamepad.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
                            self.xb_gamepad.gamepad.update()
                        
                        if button == Consts.GAMEPAD['Y']:
                            print(f'A Button pressed - reMapped:{hex(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)}')
                            self.xb_gamepad.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
                            self.xb_gamepad.gamepad.update()
                        
                    elif event.type == pygame.JOYHATMOTION:
                        
                        dpad = event.value
                        print(dpad)
                        # # Check for D-pad button presses
                        # if button == pygame.JOY_HATDOWN:
                        #     print("D-pad down button pressed")
                        # elif button == pygame.JOY_HATUP:
                        #     print("D-pad up button pressed")
                        # elif button == pygame.JOY_HATLEFT:
                        #     print("D-pad left button pressed")
                        # elif button == pygame.JOY_HATRIGHT:
                        #     print("D-pad right button pressed")
                            
                    elif event.type == pygame.JOYBUTTONUP:
                        # Read button values
                        button = event.button
                        print(f'Button Up Key:{button}')
                        # Handle button releases as needed
                        if button == Consts.GAMEPAD['A']:
                            print(f'A Button pressed - reMapped:{hex(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)}')
                            self.xb_gamepad.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
                            self.xb_gamepad.gamepad.update()
                        
                        if button == Consts.GAMEPAD['B']:
                            print(f'B Button pressed - reMapped:{hex(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)}')
                            self.xb_gamepad.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                            self.xb_gamepad.gamepad.update()
                        
                        if button == Consts.GAMEPAD['X']:
                            print(f'X Button pressed - reMapped:{hex(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)}')
                            self.xb_gamepad.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
                            self.xb_gamepad.gamepad.update()
                        
                        if button == Consts.GAMEPAD['Y']:
                            print(f'Y Button pressed - reMapped:{hex(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)}')
                            self.xb_gamepad.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
                            self.xb_gamepad.gamepad.update()
        
        except KeyboardInterrupt as e:
            print(f'Error: {e}')
            await self.stop()
            
    async def stop(self):
        print(f"Stopping thread ...")
        try:
            pygame.quit()
            exit()
        except Exception as e:
            print(f'Error: {e}')
