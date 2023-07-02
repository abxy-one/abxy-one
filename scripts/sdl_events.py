import ctypes
import sdl2
import sdl2.ext

# Define a ctypes structure for userdata
class UserData(ctypes.Structure):
    _fields_ = [("controller", ctypes.c_void_p),
                ("controller_name", ctypes.c_char_p)]

# Initialize SDL
sdl2.ext.init()

# Create a list to hold the controller objects
controllers = []

# Initialize the controller subsystem
sdl2.SDL_Init(sdl2.SDL_INIT_GAMECONTROLLER)

# Get the number of available controllers
num_controllers = sdl2.SDL_NumJoysticks()

# Open each controller and add it to the list
for i in range(num_controllers):
    controller = sdl2.gamecontroller.SDL_GameControllerOpen(i)
    controllers.append(controller)

# Custom event filter function
def event_filter(event, userdata):
    # Handle controller connection event
    if event.type == sdl2.SDL_CONTROLLERDEVICEADDED:
        # Get the controller index from the event
        controller_index = event.cdevice.which
        
        # Open the newly connected controller
        controller = sdl2.gamecontroller.SDL_GameControllerOpen(controller_index)

        # Get the name of the connected controller
        controller_name = sdl2.gamecontroller.SDL_GameControllerName(controller)

        # Add the controller to the list
        controllers.append(controller)
        
        # Update the variable with controller info
        userdata.controller = controller
        userdata.controller_name = controller_name

        # Print the controller info
        print("Controller connected:", controller_name)

    # Value will be ignored
    return 0

# Create an instance of UserData
userdata = UserData()

# Set the event filter with userdata
# sdl2.SDL_SetEventFilter(sdl2.SDL_EventFilter(event_filter), ctypes.byref(userdata))

# Main loop
running = True
while running:
    events = sdl2.ext.get_events()
        
    for event in events:
        if event.type == sdl2.SDL_QUIT:
            running = False
            break

# Close the controllers
for controller in controllers:
    sdl2.gamecontroller.SDL_GameControllerClose(controller)

# Quit SDL
sdl2.SDL_Quit()
