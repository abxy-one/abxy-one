import sdl2
import sdl2.ext
import sdl2.gamecontroller as gc
from pyvjoystick import vigem as vg
import binascii

import constants as Consts
  
class GamePad:
    def __init__(self) -> None:
        super().__init__()
        try:
            print(f'initialize sdl2 {__class__}')
            sdl2.SDL_Init(sdl2.SDL_INIT_GAMECONTROLLER)
        except Exception as e:
            print(f'initialize sdl2 failed {e}')

    '''
    Open game controllers
    @return void
    '''
    def open(self, index):
        print(f'{__class__}.open(index={index})')
        return gc.SDL_GameControllerOpen(index)

    '''
    Close game controller
    @return void
    '''
    def close(self, index):
        print(f'{__class__}.close(index={index})')
        if self._controller_attached(self._instance_by_index(index)) is True:
            gc.SDL_GameControllerClose(self._instance_by_index(index))

    '''
    Quit SDL
    @return void
    '''
    def quit() -> None:
        sdl2.ext.quit()
    
    ''' 
    Get the number of available game controllers 
    @return int
    '''
    def _get_controllers(self) -> int:
        return sdl2.SDL_NumJoysticks()
    
    '''
    Check if any game controllers are connected
    @return bool
    '''
    def _is_game_controller(self, index) -> bool:
        return gc.SDL_IsGameController(index) 
    
    '''
    Get joystick guid
    @return string
    '''
    def _joystick_guid(self, index) -> str:
        joystick_guid_decode = bytes(sdl2.SDL_JoystickGetDeviceGUID(index))
        return binascii.hexlify(joystick_guid_decode).decode()
    
    '''
    Game controllers name by index
    @return string
    '''
    def _name_by_index(self, index) -> str:
        return gc.SDL_GameControllerNameForIndex(index)

    '''
    Game controllers name by instance
    @return string
    '''
    def _name_by_instance(self, instance) -> str:
        return gc.SDL_GameControllerName(instance)

    '''
    Game controllers type by index
    @return int
    '''
    def _type_by_index(self, index) -> int:
        return gc.SDL_GameControllerTypeForIndex(index)
    
    '''
    Game controllers type by instance
    @return int
    '''
    def _type_by_instance(self, instance) -> int:
        return gc.SDL_GameControllerGetType(instance)
    
    '''
    Game controllers instance by index
    @return sdl existing controller instance
    '''
    def _instance_by_index(self, index):
        return gc.SDL_GameControllerFromInstanceID(index)
    
    '''
    Check if controller is attached
    @return bool
    '''
    def _controller_attached(self, index) -> bool:
        return gc.SDL_GameControllerGetAttached(index)

    '''
    Initialize game controller
    @return void
    '''
    # def _initialize_controller(self, index):
    #     print(f'{__class__}._initialize_controller(index={index})')
    #     virtual_driver = None
    #     if self._joystick_guid(index) == Consts.VIGEM_VIRTUAL_DRIVER_GUID_STR:
    #         instance = None
    #         name = "VX360 Gamepad Virtual Driver"
    #         virtual_driver = None
    #     else:
    #         instance = gc.SDL_GameControllerOpen(index)
    #         name = self._name_by_instance(instance)
    #         # virtual_driver = self._get_virtual_driver(index)

    #     self.game_controllers.append({
    #         "index": index,
    #         "jdevice": index,
    #         "guid": self._joystick_guid(index),
    #         "name": name,
    #         "type": self._type_by_instance(instance),
    #         "virtual_driver": virtual_driver,
    #         "instance_id": instance
    #         })
    
    # def initialize_gamepads(self) -> None:
    #     try:
    #         for device_index in range(self._get_controllers()):
    #             virtual_driver = None
    #             controller_instance = self.open(device_index)
    #             controller_type = self._type_by_instance(controller_instance)
    #             controller_name = self._name_by_instance(controller_instance)
                
    #             self.get_virtual_driver(index=device_index)
                
    #             self.physical_controllers.append({
    #                     "device_index": device_index,
    #                     "name": controller_name,
    #                     "type": controller_type,
    #                     "virtual_driver": virtual_driver,
    #                     "instance_id": controller_instance
    #                 })
    #         if not self.physical_controllers:
    #             print("Failed to open game controller.")
    #             quit()
    #     except Exception as e:
    #         print(f'Error loading controllers {e}')

    #     return self.physical_controllers

class VirtualDriverManager(GamePad):
    
    '''
    Virtual Driver Manager
    
    Creates a dict to hold the controller objects and map to virtual drivers
    '''
    def __init__(self) -> None:
        super().__init__()
        print(f'{__class__}')
        self.virtual_driver_manager = {}
    
    def check(self, device_id) -> None:
        print(f'{__class__}.check(device_id={device_id})')
        if not device_id in self.virtual_driver_manager:
            self.virtual_driver_manager[device_id] = self._set_virtual_driver(device_id)
        
    def get_virtual_driver(self, device_id) -> None:
        print(f'{__class__}.get_virtual_driver(device_id={device_id})')
        if device_id in self.virtual_driver_manager:
            return self.virtual_driver_manager[device_id]
        return None
    
    def unload(self, device_id) -> None:
        print(f'{__class__}.unload(device_id={device_id})')
        self.virtual_driver_manager[device_id].reset()
        del self.virtual_driver_manager[device_id]
    
    '''
    Get Virtual Driver
    @return virtual_driver
    '''
    def _set_virtual_driver(self, device_id):
        print(f'{__class__}._set_virtual_driver(device_id={device_id})')
        controller_type = self._type_by_index(device_id)
        virtual_driver = None
        if self._joystick_guid(device_id) != Consts.VIGEM_VIRTUAL_DRIVER_GUID_STR:
            if self._is_game_controller(device_id):
                if gc.SDL_CONTROLLER_TYPE_XBOXONE == controller_type \
                    or gc.SDL_CONTROLLER_TYPE_XBOX360 == controller_type:
                        virtual_driver = vg.VX360Gamepad()
                elif gc.SDL_CONTROLLER_TYPE_PS4 == controller_type \
                    or gc.SDL_CONTROLLER_TYPE_PS3 == controller_type \
                    or gc.SDL_CONTROLLER_TYPE_PS5 == controller_type:
                        virtual_driver = vg.VDS4Gamepad()
                else:
                    # Use this as the default virtual driver
                    virtual_driver = vg.VX360Gamepad()
        else:
            virtual_driver = None
        return virtual_driver

class GamePadUtils():
    def __init__(self) -> None:
        pass

    def deadzone(self, axis_x, axis_y):
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
