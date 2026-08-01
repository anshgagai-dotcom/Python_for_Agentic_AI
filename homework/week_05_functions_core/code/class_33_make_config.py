# Write a function make_config(**settings) that prints all the settings as a dictionary.
# make_config(**settings) jo saari settings ek dict ke roop mein print kare.

#1
def make_config(**settings):
    print(settings)

"""make_config(theme="dark", size=12)"""

make_config(
    theme="light",
    font="Arial",
    size=16
)


