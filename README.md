# Overview
This code registers a talon popping action with behavior determined by several talon settings.

# Settings
The user.fire_chicken_pop_action setting determines what kind of action gets performed, and the other settings determine the details. 

When this is set to 0, the fire chicken pop does nothing. 

When this is set to 1, the pop action presses the key specified by the user.fire_chicken_pop_string setting.

When this is set to 2, the pop action clicks the mouse button specified by the user.fire_chicken_pop_integer setting (0 corresponds to left click and 1 corresponds to right click). The key specified by the user.fire_chicken_pop_string setting is held down during clicking (no key gets held by default).
