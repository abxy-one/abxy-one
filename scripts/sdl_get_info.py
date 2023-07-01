import sdl2
# https://github.com/py-sdl/py-sdl2/blob/master/sdl2/gamecontroller.py
import sdl2.gamecontroller as gc
import binascii

# Initialize SDL
sdl2.SDL_Init(sdl2.SDL_INIT_GAMECONTROLLER)

# Get the number of connected game controllers
num_controllers = sdl2.SDL_NumJoysticks()

# Iterate over the connected controllers and retrieve their GUIDs
for i in range(num_controllers):
    
    # https://metacpan.org/pod/SDL2::gamecontroller#SDL_GameControllerOpen(-...-)
    game_controller = gc.SDL_GameControllerOpen(i)

    # https://metacpan.org/pod/SDL2::joystick#SDL_JoystickGetDeviceGUID(-...-)
    joystick_guid = sdl2.SDL_JoystickGetDeviceGUID(i)
    joystick_guid_decode = binascii.hexlify(joystick_guid).decode()
    
    # https://metacpan.org/pod/SDL2::gamecontroller#SDL_GameControllerFromInstanceID(-...-)
    game_controller_instance_id = gc.SDL_GameControllerFromInstanceID(i)
    
    # https://metacpan.org/pod/SDL2::gamecontroller#SDL_GameControllerGetAttached(-...-)
    game_controller_attached = gc.SDL_GameControllerGetAttached(game_controller)
    
    # https://metacpan.org/pod/SDL2::gamecontroller#SDL_IsGameController(-...-)
    is_game_controller = gc.SDL_IsGameController(i)
    
    # https://metacpan.org/pod/SDL2::gamecontroller#SDL_GameControllerNameForIndex(-...-)
    game_controller_name_by_index = gc.SDL_GameControllerNameForIndex(i)

    # https://metacpan.org/pod/SDL2::gamecontroller#SDL_GameControllerName(-...-)
    game_controller_name_by_instance = gc.SDL_GameControllerName(game_controller)
    
    # https://metacpan.org/pod/SDL2::gamecontroller#SDL_GameControllerTypeForIndex(-...-)
    game_controller_type_by_index = gc.SDL_GameControllerTypeForIndex(i)
    
    # https://metacpan.org/pod/SDL2::gamecontroller#SDL_GameControllerGetType(-...-)
    game_controller_type_by_instance = gc.SDL_GameControllerGetType(game_controller)
    
    # https://metacpan.org/pod/SDL2::gamecontroller#SDL_GameControllerGetPlayerIndex(-...-)  
    game_controller_player_index = gc.SDL_GameControllerFromPlayerIndex(i)
    
    # https://metacpan.org/pod/SDL2::gamecontroller#SDL_GameControllerGetVendor(-...-)
    game_controller_vendor = gc.SDL_GameControllerGetVendor(game_controller)
    
    # https://metacpan.org/pod/SDL2::gamecontroller#SDL_GameControllerGetProduct(-...-)
    game_controller_product = gc.SDL_GameControllerGetProduct(game_controller)
    
    # https://metacpan.org/pod/SDL2::gamecontroller#SDL_GameControllerGetProductVersion(-...-)
    game_controller_product_version = gc.SDL_GameControllerGetProductVersion(game_controller)
    
    # https://metacpan.org/pod/SDL2::gamecontroller#SDL_GameControllerGetSerial(-...-)
    game_controller_serial = gc.SDL_GameControllerGetSerial(game_controller)
    
    print("\nController Index: {}".format(i))
    print(f"\tGame Controller Instance ID: {game_controller}")
    print(f"\tJoystick GUID: {joystick_guid_decode}")
    print(f"\tIs Game Controller? {is_game_controller}")
    print(f"\tIs Game Controller Attached? {game_controller_attached}")
    print(f"\tGame Controller Instance by index: {game_controller_instance_id}")
    print(f"\tGame Controller Name by index: {game_controller_name_by_index}")
    print(f"\tGame Controller Name by instance: {game_controller_name_by_instance}")
    print(f"\tGame Controller Type by index: {game_controller_type_by_index}")
    print(f"\tGame Controller Type by instance: {game_controller_type_by_instance}")
    print(f"\tGame Controller Product:Vendor: {game_controller_product}:{game_controller_vendor}")
    print(f"\tGame Controller Product Version: {game_controller_product_version}")
    print(f"\tGame Controller Serial: {game_controller_serial}")
    print(f"\tPlayer Index: {game_controller_player_index}")
    
    # https://metacpan.org/pod/SDL2::gamecontroller#SDL_GameControllerClose(-...-)
    gc.SDL_GameControllerClose(game_controller)

# Controller Type Constants - https://metacpan.org/pod/SDL2::gamecontroller#SDL_GameControllerType
print(f'\n\nController Type Constants:')
print(f'\tUnknown: {gc.SDL_CONTROLLER_TYPE_UNKNOWN}')
print(f'\tXbox 360: {gc.SDL_CONTROLLER_TYPE_XBOX360}')
print(f'\tXbox One: {gc.SDL_CONTROLLER_TYPE_XBOXONE}')
print(f'\tPS3: {gc.SDL_CONTROLLER_TYPE_PS3}')
print(f'\tPS4: {gc.SDL_CONTROLLER_TYPE_PS4}')
print(f'\tNintendo Pro: {gc.SDL_CONTROLLER_TYPE_NINTENDO_SWITCH_PRO}')
print(f'\tVirtual: {gc.SDL_CONTROLLER_TYPE_VIRTUAL}')
print(f'\tPS5: {gc.SDL_CONTROLLER_TYPE_PS5}')    
# Quit SDL
sdl2.SDL_Quit()
