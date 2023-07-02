import sdl2
import sdl2.ext

# This hint allows joystick events to be processed even when the window is not in focus or minimized.
# sdl2.ext.HINT_JOYSTICK_ALLOW_BACKGROUND_EVENTS = "1"

# initialize SDL
sdl2.ext.init()

# initialize the SDL2 subsystems
sdl2.SDL_Init(sdl2.SDL_INIT_GAMECONTROLLER | sdl2.SDL_INIT_JOYSTICK)

# create a instance_id and device_index mapping
# format: {instance_id: device_index}
instance_device_index_map = {}

# main loop
running = True
while running:
    events = sdl2.ext.get_events()

    # loop the events
    for event in events:

        # get devices current events instance id (cdevice is now a controllers device event)
        # unlike the controller added event, the controller removed event does not have a device_index
        # see https://metacpan.org/pod/SDL2::joystick#DESCRIPTION
        cdevice = event.cdevice.which

        # sdl2 quit event
        if event.type == sdl2.SDL_QUIT:
            running = False
            break

        # buttons pressed and release event
        elif event.type == sdl2.SDL_JOYBUTTONDOWN or event.type == sdl2.SDL_JOYBUTTONUP:

            # read button values
            print(f'button type {event.type} event:{event.cbutton.button} - instance_id:{cdevice}')

            if event.type == sdl2.SDL_JOYBUTTONDOWN and event.cbutton.button == sdl2.SDL_CONTROLLER_BUTTON_A:

                # print the instance_id and device_index mapping when button A is pressed
                print(f'instance_device_index_map: {instance_device_index_map}')

        # controller added to system
        elif event.type == sdl2.SDL_CONTROLLERDEVICEADDED:

            # get devices index when controller is first connected
            device_index = event.cdevice.which

            # set the devices device_index instance
            # see https://metacpan.org/pod/SDL2::joystick#DESCRIPTION
            # https://metacpan.org/pod/SDL2::joystick#SDL_JoystickGetDeviceInstanceID(-...-)
            instance_id = sdl2.SDL_JoystickGetDeviceInstanceID(device_index)

            sdl2.SDL_GameControllerOpen(device_index)
            print(f'controller added - instance_id:{instance_id}')

            # map instance_id to device_index
            instance_device_index_map[instance_id] = device_index

        # controller removed from system
        elif event.type == sdl2.SDL_CONTROLLERDEVICEREMOVED:

            # https://metacpan.org/pod/SDL2::gamecontroller#SDL_GameControllerFromInstanceID(-...-)
            controller = sdl2.SDL_GameControllerFromInstanceID(cdevice)

            sdl2.SDL_GameControllerClose(controller)
            print(f'controller removed - instance_id:{cdevice}')

            # remove instance_id from map
            del instance_device_index_map[cdevice]

# quit SDL
sdl2.SDL_Quit()
