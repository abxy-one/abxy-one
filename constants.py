from pyvjoystick import vigem as vg

GAMEPAD = {
    'A'                 : 0,
    'B'                 : 1,
    'X'                 : 2,
    'Y'                 : 3,
    'LEFT_BUMP'         : 4,
    'RIGHT_BUMP'        : 5,
    'BACK'              : 6,
    'START'             : 7,
    'GUIDE'             : 8,
    'LEFT_STICK_BTN'    : 9,
    'RIGHT_STICK_BTN'   : 10
}

AXIS = {
    'LEFT_STICK_X'  : 1,
    'LEFT_STICK_Y'  : 2,
    'RIGHT_STICK_X' : 3,
    'RIGHT_STICK_Y' : 4,
    'LEFT_TRIGGER'  : 7,
    'RIGHT_TRIGGER' : 5,
}

DEADZONE_THRESHOLD = 0.2

VIGEM_VIRTUAL_DRIVER_GUID_STR = "030003f05e0400008e02000000007200"

BUTTON_ACTIONS = {
    'SINGLE_PRESS'      : 0,
    'DOUBLE_PRESS'      : 1,
    'LONG_PRESS'        : 2,
    'HOLD_PRESS'        : 3,
    'RELEASE_PRESS'     : 4,
    'SINGLE_PRESS_HOLD' : 5,
    'DOUBLE_PRESS_HOLD' : 6,
    'LONG_PRESS_HOLD'   : 7,
}

XB_CONTROLLER_BUTTONS = {
    'A'                 : vg.XUSB_BUTTON.XUSB_GAMEPAD_A,
    'B'                 : vg.XUSB_BUTTON.XUSB_GAMEPAD_B,
    'X'                 : vg.XUSB_BUTTON.XUSB_GAMEPAD_X,
    'Y'                 : vg.XUSB_BUTTON.XUSB_GAMEPAD_Y,
    # 'LEFT_BUMP'         : vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_SHOULDER,
    # 'RIGHT_BUMP'        : vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_SHOULDER,
    # 'BACK'              : vg.XUSB_BUTTON.XUSB_GAMEPAD_BACK,
    # 'START'             : vg.XUSB_BUTTON.XUSB_GAMEPAD_START,
    # 'GUIDE'             : vg.XUSB_BUTTON.XUSB_GAMEPAD_GUIDE,
    # 'LEFT_STICK_BTN'    : vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB,
    # 'RIGHT_STICK_BTN'   : vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB,
    # 'DPAD_UP'           : vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_UP,
    # 'DPAD_DOWN'         : vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_DOWN,
    # 'DPAD_LEFT'         : vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_LEFT,
    # 'DPAD_RIGHT'        : vg.XUSB_BUTTON.XUSB_GAMEPAD_DPAD_RIGHT,
    # 'LEFT_TRIGGER'      : vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_TRIGGER,
    # 'RIGHT_TRIGGER'     : vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_TRIGGER,
    # 'LEFT_STICK_X'      : vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB_DEADZONE,
    # 'LEFT_STICK_Y'      : vg.XUSB_BUTTON.XUSB_GAMEPAD_LEFT_THUMB_DEADZONE,
    # 'RIGHT_STICK_X'     : vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB_DEADZONE,
    # 'RIGHT_STICK_Y'     : vg.XUSB_BUTTON.XUSB_GAMEPAD_RIGHT_THUMB_DEADZONE
}

SDL_JOYSTICK_TYPE = {
    'SDL_JOYSTICK_TYPE'         : 0,
    'SDL_GAME_CONTROLLER_TYPE'  : 1,
}

# SDL_CONTROLLER_TYPE_NAMES = {
    
# }
