# Minecraftpy
A minecraft-like game written in python, in the early stage of development.

## Play It
Typing the following lines of commands to play the game:
```bash
# Create a venv environment is a good choice!
python -m venv .
./bin/activate
# Then run the game.
pip install -r requirments.txt
python -m minecraft --player <name>:<uuid>
```

Notice that `name` and `uuid` should always be provided when start the game.

## Short-term Goal

- [ ] Support i18n
  - [x] [#908](https://github.com/pyglet/pygley/pull/908) was created for pyglet
  - [ ] Waiting for a new release of pyglet
- [ ] A simple 3D scene
