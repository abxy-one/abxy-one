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

            self.gamepad_util = Controller.GamePadUtils()

            self.device_list = {}
            self.axis_map = {
                Consts.AXIS['LEFT_STICK_X']     :0,
                Consts.AXIS['LEFT_STICK_Y']     :0,
                Consts.AXIS['RIGHT_STICK_X']    :0,
                Consts.AXIS['RIGHT_STICK_Y']    :0,
                Consts.AXIS['LEFT_TRIGGER']     :0,
                Consts.AXIS['RIGHT_TRIGGER']    :0
                }

        except Exception as e:
            print(f'Failed Initialize SDL {e}')

    def _button_down(self, vg_button, vg_driver):
        print(f'{__class__}._button_down(vg_button={vg_button},vg_driver={vg_driver})')
        vg_driver.press_button(button=vg_button)
        vg_driver.update()

    def _button_up(self, vg_button, vg_driver):
        print(f'{__class__}._button_up(vg_button={vg_button},vg_driver={vg_driver})')
        vg_driver.release_button(button=vg_button)
        vg_driver.update()

    def _dpad_event(self, hat, vg_driver):
        print(f'{__class__}._dpad_event(hat={hat}, vg_driver={vg_driver})')

    def _joystick_axis_event(self, axis, value, cdevice, vg_driver):
        print(f'{__class__}._jotstick_axis_event(axis={axis}, value={value}, cdevice={cdevice}, vg_driver={vg_driver})')

        self.axis_map[axis] = value
        self.device_list[cdevice] = self.axis_map

        print(self.device_list)

    def run(self):
        try:
            running = True
            while running:
                events = sdl2.ext.get_events()

                for event in events:

                    cdevice = event.cdevice.which

                    virtual_driver = self.virtual_driver_manager.get_virtual_driver(cdevice)
                    print(f'{__class__} virtual_driver: {virtual_driver}')

                    if event.type == sdl2.SDL_QUIT:
                        print(f'{__class__} quit sdl2')
                        self.virtual_driver_manager.quit()
                        running = False
                        break

                    elif event.type == sdl2.SDL_CONTROLLERDEVICEADDED:
                        # get devices index when controller is first connected
                        device_index = event.cdevice.which

                        self.virtual_driver_manager.open(device_index)
                        self.virtual_driver_manager.load(device_index)

                    elif event.type == sdl2.SDL_CONTROLLERDEVICEREMOVED:
                        # del self.device_list[cdevice]
                        self.virtual_driver_manager.close(cdevice)
                        self.virtual_driver_manager.unload(cdevice)

                    elif event.type == sdl2.SDL_JOYAXISMOTION:

                        axis = event.jaxis.axis

                        print(f'{__class__} axis: {axis} - cdevice:{cdevice}')

                        if axis == sdl2.SDL_CONTROLLER_AXIS_LEFTX \
                            or axis == sdl2.SDL_CONTROLLER_AXIS_LEFTY \
                            or axis == sdl2.SDL_CONTROLLER_AXIS_RIGHTX \
                            or axis == sdl2.SDL_CONTROLLER_AXIS_RIGHTY \
                            or axis == sdl2.SDL_CONTROLLER_AXIS_TRIGGERLEFT \
                            or axis == sdl2.SDL_CONTROLLER_AXIS_TRIGGERRIGHT:
                            self._joystick_axis_event(
                                axis=axis,
                                value=event.jaxis.value,
                                cdevice=cdevice,
                                vg_driver=virtual_driver
                            )

                        # deadzone
                        left_deadzone = self.gamepad_util.deadzone(
                            self.axis_map[Consts.AXIS['LEFT_STICK_X']],
                            self.axis_map[Consts.AXIS['LEFT_STICK_Y']]
                            )
                        right_deadzone = self.gamepad_util.deadzone(
                            self.axis_map[Consts.AXIS['RIGHT_STICK_X']],
                            self.axis_map[Consts.AXIS['RIGHT_STICK_Y']]
                            )

                        # # Read triggers axis values
                        # left_trigger = self.gamepad.get_axis(Consts.AXIS['LEFT_TRIGGER'])
                        # right_trigger = self.gamepad.get_axis(Consts.AXIS['RIGHT_TRIGGER'])

                        # Print the joystick values
                        print(f'\n{__class__} {self.axis_map} - cdevice:{cdevice}')
                        print(f'\tleft joystick_X:\t {left_deadzone[0]:.3f}')
                        print(f'\tleft joystick_Y:\t {left_deadzone[1]:.3f}')
                        print(f'\tright joystick_X:\t {right_deadzone[0]:.3f}')
                        print(f'\tright joystick_Y:\t {right_deadzone[1]:.3f}')

                        # if event.caxis.axis == sdl2.SDL_CONTROLLER_AXIS_TRIGGERLEFT:
                        #     print("Left trigger value:", event.caxis.value)

                        # if event.caxis.axis == sdl2.SDL_CONTROLLER_AXIS_TRIGGERRIGHT:
                        #     print("Right trigger value:", event.caxis.value)

                        # # Print the bumper values
                        # print(f'Left Bumper: {left_trigger:.3f}')
                        # print(f'Right Bumper: {right_trigger:.3f}')

                        # # Handle axis values as needed
                        # self.xb_gamepad.gamepad.left_joystick_float(x_value_float=left_deadzone[0], y_value_float=left_deadzone[1])
                        # self.xb_gamepad.gamepad.right_joystick_float(x_value_float=right_deadzone[0], y_value_float=right_deadzone[1])

                        # self.xb_gamepad.gamepad.update()

                    elif event.type == sdl2.SDL_JOYHATMOTION:

                        hat = event.jhat.value
                        print(f'{__class__} hat value :{hat} - cdevice:{cdevice}')

                        if hat == sdl2.SDL_HAT_CENTERED:
                            self._dpad_event(hat=sdl2.SDL_HAT_CENTERED, vg_driver=virtual_driver)

                        elif hat == sdl2.SDL_HAT_UP:
                            self._dpad_event(hat=sdl2.SDL_HAT_UP, vg_driver=virtual_driver)

                        elif hat == sdl2.SDL_HAT_RIGHT:
                            self._dpad_event(hat=sdl2.SDL_HAT_RIGHT, vg_driver=virtual_driver)

                        elif hat == sdl2.SDL_HAT_DOWN:
                            self._dpad_event(hat=sdl2.SDL_HAT_DOWN, vg_driver=virtual_driver)

                        elif hat == sdl2.SDL_HAT_LEFT:
                            self._dpad_event(hat=sdl2.SDL_HAT_LEFT, vg_driver=virtual_driver)

                        elif hat == sdl2.SDL_HAT_RIGHTUP:
                            self._dpad_event(hat=sdl2.SDL_HAT_RIGHTUP, vg_driver=virtual_driver)

                        elif hat == sdl2.SDL_HAT_RIGHTDOWN:
                            self._dpad_event(hat=sdl2.SDL_HAT_RIGHTDOWN, vg_driver=virtual_driver)

                        elif hat == sdl2.SDL_HAT_LEFTUP:
                            self._dpad_event(hat=sdl2.SDL_HAT_LEFTUP, vg_driver=virtual_driver)

                        elif hat == sdl2.SDL_HAT_LEFTDOWN:
                            self._dpad_event(hat=sdl2.SDL_HAT_LEFTDOWN, vg_driver=virtual_driver)

                    elif event.type == sdl2.SDL_JOYBUTTONDOWN:

                        button = event.cbutton.button
                        print(f'{__class__} button down key:{button} - cdevice:{cdevice}')

                        if button == sdl2.SDL_CONTROLLER_BUTTON_A:
                            self._button_down(vg_button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
                                              vg_driver=virtual_driver)

                        if button == sdl2.SDL_CONTROLLER_BUTTON_B:
                            self._button_down(vg_button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
                                              vg_driver=virtual_driver)

                        if button == sdl2.SDL_CONTROLLER_BUTTON_X:
                            self._button_down(vg_button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
                                              vg_driver=virtual_driver)

                        if button == sdl2.SDL_CONTROLLER_BUTTON_Y:
                            self._button_down(vg_button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,
                                              vg_driver=virtual_driver)

                    elif event.type == sdl2.SDL_JOYBUTTONUP:

                        button = event.cbutton.button
                        print(f'{__class__} button up key:{button} - cdevice:{cdevice}')

                        if button == sdl2.SDL_CONTROLLER_BUTTON_A:
                            self._button_up(vg_button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
                                              vg_driver=virtual_driver)

                        if button == sdl2.SDL_CONTROLLER_BUTTON_B:
                            self._button_up(vg_button=vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
                                              vg_driver=virtual_driver)

                        if button == sdl2.SDL_CONTROLLER_BUTTON_X:
                            self._button_up(vg_button=vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
                                              vg_driver=virtual_driver)

                        if button == sdl2.SDL_CONTROLLER_BUTTON_Y:
                            self._button_up(vg_button=vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,
                                              vg_driver=virtual_driver)

        except KeyboardInterrupt as e:
            print(f'{__class__} KeyboardInterrupt: {e}')

        except Exception as e:
            print(f'{__class__}  Exception: {e}')
