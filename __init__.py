import events as Events
# import asyncio

# async def main():
#     event_thread = Events.Events()
#     event_thread.initialize_gamepad()
#     await event_thread.run()

# # Run the event loop
# loop = asyncio.get_event_loop()
# try:
#     loop.run_until_complete(main())
# finally:
#     loop.close()

event_thread = Events.Events()
event_thread.run()
