# Overview
This code registers a talon popping action with behavior determined by several talon settings.

# Settings
The user.fire_chicken_pop_action setting determines what kind of action gets performed, and the other settings determine the details. 

When this is set to 0, the fire chicken pop does nothing. 

When this is set to 1, the pop action presses the key specified by the user.fire_chicken_pop_string setting.

When this is set to 2, the pop action clicks the mouse button specified by the user.fire_chicken_pop_integer setting (0 corresponds to left click and 1 corresponds to right click). The key specified by the user.fire_chicken_pop_string setting is held down during clicking (no key gets held by default).

When this is set to 3, the pop action calls the action stored in the user.fire_chicken_pop_string setting.

# Examples
Each example shows the code to put in a talon file to get the desired result.
## Press Right With Kindle in Command Mode
```
app: Kindle
mode: command
-
settings():
    user.fire_chicken_pop_action = 1
    user.fire_chicken_pop_string = 'right'
```

## Control Left Click With Google Chrome
```
app: Google Chrome
-
settings():
    user.fire_chicken_pop_action = 2
    user.fire_chicken_pop_string = 'ctrl'
    user.fire_chicken_pop_integer = 0
```

## Repeat last command
```
-
settings():
    user.fire_chicken_pop_action = 3
    user.fire_chicken_pop_string = 'core.repeat_command'
```

# Disabling the Configurable Pop
If you want to disable the configurable pop in specific contexts, you can activate the fire_chicken_pop_disabled tag.
