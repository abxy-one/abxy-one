import sdl2
import sdl2.ext
import sdl2.gamecontroller as gc
from pyvjoystick import vigem as vg
import binascii

import constants as Consts

'''
GamePad class
'''
class GamePad():
    def __init__(self) -> None:
        super().__init__()
        try:
            print(f'initialize sdl2 {__class__}')
            sdl2.SDL_Init(sdl2.SDL_INIT_GAMECONTROLLER | sdl2.SDL_INIT_JOYSTICK)
        except Exception as e:
            print(f'initialize sdl2 failed {e}')

    '''
    Open game controllers
    @return SDL_GameControllerOpen
    '''
    def open(self, device_index):
        print(f'{__class__}.open(device_index={device_index})')
        if self._joystick_guid(device_index) != Consts.VIGEM_VIRTUAL_DRIVER_GUID_STR:
            if self._is_game_controller(device_index):
                print(f'{__class__} SDL_GameControllerOpen({device_index})')
                return gc.SDL_GameControllerOpen(device_index)
            else:
                return False
        else:
            return False

    '''
    Close game controller
    @return void
    '''
    def close(self, instance_id):
        print(f'{__class__}.close(instance_id={instance_id})')
        instance = self._instance_from_instance_id(instance_id)
        if self._controller_attached(instance) is True:
            gc.SDL_GameControllerClose(instance)

    '''
    Quit SDL
    @return void
    '''
    def quit() -> None:
        print(f'{__class__}.quit()')
        sdl2.ext.quit()

    ''' 
    Get the number of available game controllers
    @return int
    '''
    def _get_number_of_controllers(self) -> int:
        print(f'{__class__}._get_number_of_controllers()')
        return sdl2.SDL_NumJoysticks()

    '''
    Check if any game controllers are connected
    @return bool
    '''
    def _is_game_controller(self, instance_id) -> bool:
        print(f'{__class__}._is_game_controller(instance_id={instance_id})')
        if gc.SDL_IsGameController(instance_id):
            print(f'{__class__} instance_id {instance_id} is a game controller')
        else:
            print(f'{__class__} instance_id {instance_id} is *NOT* a game controller')
        return gc.SDL_IsGameController(instance_id)

    '''
    Get joystick guid
    @return string
    '''
    def _joystick_guid(self, instance_id) -> str:
        print(f'{__class__}._joystick_guid(instance_id={instance_id})')
        joystick_guid_decode = bytes(sdl2.SDL_JoystickGetDeviceGUID(instance_id))
        return binascii.hexlify(joystick_guid_decode).decode()

    '''
    Game controllers name by index
    @return string
    '''
    def _name_by_index(self, device_index) -> str:
        print(f'{__class__}._name_by_index(device_index={device_index})')
        return gc.SDL_GameControllerNameForIndex(device_index)

    '''
    Game controllers name by instance
    @return string
    '''
    def _name_by_instance(self, instance) -> str:
        print(f'{__class__}._name_by_instance(instance={instance})')
        return gc.SDL_GameControllerName(instance)

    '''
    Game controllers type by index
    @return int
    '''
    def _type_by_index(self, instance_id) -> int:
        print(f'{__class__}._type_by_index(instance_id={instance_id})')
        return gc.SDL_GameControllerTypeForIndex(instance_id)

    '''
    Game controllers type by instance
    @return int
    '''
    def _type_by_instance(self, instance) -> int:
        print(f'{__class__}._type_by_instance(instance={instance})')
        return gc.SDL_GameControllerGetType(instance)

    '''
    Game controllers instance by `instance_id`
    @return sdl instance_id
    '''
    def _instance_from_instance_id(self, instance_id):
        print(f'{__class__}._instance_from_instance_id(instance_id={instance_id})')
        return gc.SDL_GameControllerFromInstanceID(instance_id)

    '''
    Game controllers instance by `device_index`
    Normally only called when a controller is attached
    @return sdl instance device_index
    '''
    def _instance_id_from_device_index(self, device_index):
        print(f'{__class__}._instance_id_from_device_index(device_index={device_index})')
        return sdl2.SDL_JoystickGetDeviceInstanceID(device_index)

    '''
    Check if controller is attached
    @return bool
    '''
    def _controller_attached(self, instance) -> bool:
        print(f'{__class__}._controller_attached(instance={instance})')
        return gc.SDL_GameControllerGetAttached(instance)

'''
Virtual Driver Manager class
'''
class VirtualDriverManager(GamePad):

    '''
    Virtual Driver Manager

    Creates a dict to hold the controller instance ids and map to virtual driver objects
    '''
    def __init__(self) -> None:
        super().__init__()
        print(f'{__class__}')
        self.virtual_driver_manager_index = {}

    '''
    Load Virtual Driver - Use the device_index to find the instance_id and
    create a virtual driver object and map to the instance_id
    @return void
    '''
    def load(self, device_index) -> None:
        print(f'{__class__}.load(index_id={device_index})')
        instance_id = self._instance_id_from_device_index(device_index)
        if not instance_id in self.virtual_driver_manager_index:
            self.virtual_driver_manager_index[instance_id] = self._set_virtual_driver(device_index)

    '''
    Unload Virtual Driver - Remove the virtual driver object from the dict
    @return void
    '''
    def unload(self, instance_id) -> None:
        print(f'{__class__}.unload(instance_id={instance_id})')
        try:
            del self.virtual_driver_manager_index[instance_id]
        except Exception as e:
            print(f'{__class__} error unloading virtual driver {e}')

    '''
    Get Virtual Driver
    @return virtual_driver
    '''
    def get_virtual_driver(self, instance_id) -> None:
        print(f'{__class__}.get_virtual_driver(instance_id={instance_id})')
        if instance_id in self.virtual_driver_manager_index:
            return self.virtual_driver_manager_index[instance_id]
        return None

    '''
    Find Virtual Driver and set to the sdl2 instance_id
    @return virtual_driver
    '''
    def _set_virtual_driver(self, device_index):
        print(f'{__class__}._set_virtual_driver(device_index={device_index})')
        instance_id = self._instance_id_from_device_index(device_index)
        controller_type = self._type_by_index(instance_id)
        virtual_driver = None
        if self._joystick_guid(device_index) != Consts.VIGEM_VIRTUAL_DRIVER_GUID_STR:
            if self._is_game_controller(device_index):
                if gc.SDL_CONTROLLER_TYPE_XBOXONE == controller_type \
                    or gc.SDL_CONTROLLER_TYPE_XBOX360 == controller_type:
                        virtual_driver = vg.VX360Gamepad()
                elif gc.SDL_CONTROLLER_TYPE_PS4 == controller_type \
                    or gc.SDL_CONTROLLER_TYPE_PS3 == controller_type \
                    or gc.SDL_CONTROLLER_TYPE_PS5 == controller_type:
                        virtual_driver = vg.VDS4Gamepad()
                else:
                    # use this as the default virtual driver
                    virtual_driver = vg.VX360Gamepad()
        else:
            virtual_driver = None
        return virtual_driver

'''
GamePad Utils class
'''
class GamePadUtils():
    def __init__(self) -> None:
        print(f'{__class__}')

        self.axis_map = {}
        self.device_list = [{
            None: self.axis_map
        }]

    '''
    Get deadzone axis
    '''
    def deadzone(self, axis_x, axis_y):
        print(f'{__class__}.deadzone(axis_x={axis_x}, axis_y={axis_y})')
        try:
            magnitude = (axis_x ** 2 + axis_y ** 2) ** 0.5
            # apply the deadzone
            if magnitude < Consts.DEADZONE_THRESHOLD:
                axis_x = 0.0
                axis_y = 0.0
            # normalize the input. performs division and assignment
            else:
                axis_x /= magnitude
                axis_y /= magnitude
        except Exception as e:
            print(f'{__class__} error get deadzone_axis {e}')

        return axis_x, axis_y
