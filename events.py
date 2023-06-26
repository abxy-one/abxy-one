import pygame
from pyvjoystick import vigem as vg

import constants as Consts
import controller as Controller

# Initialize VX360Gamepad
xb_gamepad = Controller.XboxGamePad()
# Get list of controllers 
gamepads = xb_gamepad.load_controllers()
# Get single controller object
gamepad = gamepads[0]['controller_obj']

# Main loop
while True:
    # Process events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # Handle joystick events
        if event.type == pygame.JOYAXISMOTION:
    
            # Read joystick axis values
            axis_lx = gamepad.get_axis(Consts.AXIS['LEFT_STICK_X'])
            axis_ly = gamepad.get_axis(Consts.AXIS['LEFT_STICK_Y'])
            axis_rx = gamepad.get_axis(Consts.AXIS['RIGHT_STICK_X'])
            axis_ry = gamepad.get_axis(Consts.AXIS['RIGHT_STICK_Y'])
            
            # Deadzone
            left_deadzone = xb_gamepad.deadzone_axis(axis_lx, axis_ly)
            right_deadzone = xb_gamepad.deadzone_axis(axis_rx, axis_ry)
            
            # Read triggers axis values
            left_trigger = gamepad.get_axis(Consts.AXIS['LEFT_TRIGGER'])
            right_trigger = gamepad.get_axis(Consts.AXIS['RIGHT_TRIGGER'])
            
            # Print the joystick values
            print(f'Left Joystick   -   X: {left_deadzone[0]:.3f}')
            print(f'Right Joystick  -   X: {right_deadzone[0]:.3f}')
            print(f'Left Joystick   -   Y: {left_deadzone[1]:.3f}')
            print(f'Right Joystick  -   Y: {right_deadzone[1]:.3f}')
            # Print the bumper values
            print(f'Left Bumper: {left_trigger:.3f}')
            print(f'Right Bumper: {right_trigger:.3f}')
            
            # Handle axis values as needed
            xb_gamepad.gamepad.left_joystick_float(x_value_float=left_deadzone[0], y_value_float=left_deadzone[1])
            xb_gamepad.gamepad.right_joystick_float(x_value_float=right_deadzone[0], y_value_float=right_deadzone[1])

            xb_gamepad.gamepad.update()

        elif event.type == pygame.JOYBUTTONDOWN:
            
            # Read button values
            button = event.button
            print(f'Button Down Key:{button}')
            
            # Handle button presses as needed
            if button == Consts.GAMEPAD['A']:
                print(f'A Button pressed - reMapped:{hex(vg.XUSB_BUTTON.XUSB_GAMEPAD_A)}')
                xb_gamepad.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
                xb_gamepad.gamepad.update()
            
            if button == Consts.GAMEPAD['B']:
                print(f'A Button pressed - reMapped:{hex(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)}')
                xb_gamepad.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                xb_gamepad.gamepad.update()
            
            if button == Consts.GAMEPAD['X']:
                print(f'A Button pressed - reMapped:{hex(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)}')
                xb_gamepad.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
                xb_gamepad.gamepad.update()
            
            if button == Consts.GAMEPAD['Y']:
                print(f'A Button pressed - reMapped:{hex(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)}')
                xb_gamepad.gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
                xb_gamepad.gamepad.update()
            
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
                xb_gamepad.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B)
                xb_gamepad.gamepad.update()
            
            if button == Consts.GAMEPAD['B']:
                print(f'B Button pressed - reMapped:{hex(vg.XUSB_BUTTON.XUSB_GAMEPAD_B)}')
                xb_gamepad.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
                xb_gamepad.gamepad.update()
            
            if button == Consts.GAMEPAD['X']:
                print(f'X Button pressed - reMapped:{hex(vg.XUSB_BUTTON.XUSB_GAMEPAD_X)}')
                xb_gamepad.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X)
                xb_gamepad.gamepad.update()
            
            if button == Consts.GAMEPAD['Y']:
                print(f'Y Button pressed - reMapped:{hex(vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)}')
                xb_gamepad.gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y)
                xb_gamepad.gamepad.update()
