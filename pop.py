from talon import Module, actions, noise, scope

module = Module()
DISABLED_TAG_NAME = 'fire_chicken_pop_disabled'
module.tag(DISABLED_TAG_NAME)

pop_action = module.setting(
    'fire_chicken_pop_action',
    default = 0,
    type = int,
    desc = 'which action to perform on a pop'
)

pop_action_string = module.setting(
    'fire_chicken_pop_string',
    default = '',
    type = str,
    desc = 'influences the behavior of many pop actions',
)

pop_action_integer = module.setting(
    'fire_chicken_pop_integer',
    type = int,
    default = 0,
    desc = 'influences the behavior of many pop actions'
)

def perform_noise_action(action_number, action_string, action_integer):
    if action_number == 1:
        actions.key(action_string)
    elif action_number == 2:
        hold_key(action_string)
        actions.mouse_click(action_integer)
        release_key(action_string)

def hold_key(key: str):
    if key != '':
        actions.key(key + ':down')

def release_key(key: str):
    if key != '':
        actions.key(key + ':up')

def fire_chicken_pop_enabled():
    tags = scope.get("tag")
    enabled = 'user.' + DISABLED_TAG_NAME not in tags
    return enabled

def on_pop(active):
    if fire_chicken_pop_enabled():
        action = pop_action.get()
        action_string = pop_action_string.get()
        action_integer = pop_action_integer.get()
        perform_noise_action(action, action_string, action_integer)
        print(f'pop recognized action: {action}. action string: {action_string}. action integer: {action_integer}')

noise.register('pop', on_pop)
