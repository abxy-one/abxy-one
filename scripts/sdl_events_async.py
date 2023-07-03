import sdl2
import sdl2.ext
import asyncio
import threading

# This hint allows joystick events to be processed even when the window is not in focus or minimized.
# sdl2.ext.HINT_JOYSTICK_ALLOW_BACKGROUND_EVENTS = "1"

# initialize SDL
sdl2.ext.init()

# initialize the SDL2 subsystems
sdl2.SDL_Init(sdl2.SDL_INIT_GAMECONTROLLER | sdl2.SDL_INIT_JOYSTICK)

# create a instance_id and device_index mapping
# format: {instance_id: device_index}
instance_device_index_map = {}

# When an event occurs, such as a button press or release, the corresponding 
# function (handle_button_up() or handle_button_down()) is awaited using await. 
# This allows the event loop to continue executing other events concurrently 
# while waiting for the awaited function to complete its work asynchronously. 
# Once the awaited function finishes, the event loop resumes the execution 
# of the current coroutine.

class Event:
    def __init__(self, event):
        self.event = event

    async def handle(self):
        event_type = self.event.type

        if event_type == sdl2.SDL_QUIT:
            await self.handle_quit()
        elif event_type == sdl2.SDL_JOYBUTTONDOWN:
            await self.handle_button_down()
        elif event_type == sdl2.SDL_JOYBUTTONUP:
            await self.handle_button_up()
        elif event_type == sdl2.SDL_CONTROLLERDEVICEADDED:
            await self.handle_controller_added()
        elif event_type == sdl2.SDL_CONTROLLERDEVICEREMOVED:
            await self.handle_controller_removed()

    async def handle_quit(self):
        print('Quit event received')
        global running
        running = False

    async def handle_button_down(self):
        print(f'Button down - Thread: {threading.current_thread().name} Event Type: {self.event.type} device: {self.event.cdevice}')
        # await asyncio.sleep(0.1)  # Simulating some asynchronous work

    async def handle_button_up(self):
        print(f'Button up - Thread: {threading.current_thread().name} Event Type: {self.event.type}')
        # await asyncio.sleep(0.1)  # Simulating some asynchronous work

    async def handle_controller_added(self):
        device_index = self.event.cdevice.which
        instance_id = sdl2.SDL_JoystickGetDeviceInstanceID(device_index)

        sdl2.SDL_GameControllerOpen(device_index)
        print(f'Controller added - Instance ID: {instance_id}')

        # map instance_id to device_index
        instance_device_index_map[instance_id] = device_index

    async def handle_controller_removed(self):
        cdevice = self.event.cdevice.which

        controller = sdl2.SDL_GameControllerFromInstanceID(cdevice)
        sdl2.SDL_GameControllerClose(controller)
        print(f'Controller removed - Instance ID: {cdevice}')

        # remove instance_id from map
        del instance_device_index_map[cdevice]


# main loop
running = True

async def event_loop():
    global running

    while running:
        events = sdl2.ext.get_events()

        for event in events:
            event_handler = Event(event)
            await event_handler.handle()

    sdl2.SDL_Quit()

# Run the event loop asynchronously
asyncio.run(event_loop())
