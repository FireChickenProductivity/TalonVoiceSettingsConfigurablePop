from talon import Module, actions, noise, scope, settings

module = Module()
DISABLED_TAG_NAME = 'fire_chicken_pop_disabled'
module.tag(DISABLED_TAG_NAME)

pop_action_setting_name = 'fire_chicken_pop_action'
pop_action = 'user.' + pop_action_setting_name
module.setting(
    pop_action_setting_name,
    default = 0,
    type = int,
    desc = 'which action to perform on a pop'
)

pop_action_string_setting_name = 'fire_chicken_pop_string'
pop_action_string = 'user.' + pop_action_string_setting_name
module.setting(
    pop_action_string_setting_name,
    default = '',
    type = str,
    desc = 'influences the behavior of many pop actions',
)

pop_action_integer_setting_name = 'fire_chicken_pop_integer'
pop_action_integer = 'user.' + pop_action_integer_setting_name
module.setting(
    pop_action_integer_setting_name,
    type = int,
    default = 0,
    desc = 'influences the behavior of many pop actions'
)

disable_fire_chicken_pop_when_eye_tracker_disabled_setting_name = 'fire_chicken_pop_disabled_by_eye_tracker'
disable_fire_chicken_pop_when_eye_tracker_disabled = 'user.' + disable_fire_chicken_pop_when_eye_tracker_disabled_setting_name
module.setting(
    disable_fire_chicken_pop_when_eye_tracker_disabled_setting_name,
    type = int,
    default = 1,
    desc = 'determines if fire chicken pop should be disabled by the eye tracker'
)

def perform_noise_action(action_number, action_string, action_integer):
    if action_number == 1:
        actions.key(action_string)
    elif action_number == 2:
        hold_key(action_string)
        actions.mouse_click(action_integer)
        release_key(action_string)
    elif action_number == 3:
        action = getattr(actions, action_string)
        action()


def hold_key(key: str):
    if key != '':
        actions.key(key + ':down')

def release_key(key: str):
    if key != '':
        actions.key(key + ':up')

def fire_chicken_pop_enabled():
    tags = scope.get("tag")
    disabling_tag_inactive = 'user.' + DISABLED_TAG_NAME not in tags
    disabled_by_eye_tracker = settings.get(disable_fire_chicken_pop_when_eye_tracker_disabled) != 0 and actions.tracking.control_enabled()
    return disabling_tag_inactive and not disabled_by_eye_tracker

def on_pop(active):
    if fire_chicken_pop_enabled():
        action = settings.get(pop_action)
        action_string = settings.get(pop_action_string)
        action_integer = settings.get(pop_action_integer)
        perform_noise_action(action, action_string, action_integer)
        print(f'pop recognized action: {action}. action string: {action_string}. action integer: {action_integer}')

noise.register('pop', on_pop)
