from Minecraft.gui.widget.base import Widget

import pyglet
from pyglet.event import EventDispatcher
from pyglet.gl import *
from pyglet.graphics import OrderedGroup
from pyglet.text.caret import Caret
from pyglet.text.layout import IncrementalTextLayout


class TextEntry(Widget):

    def __init__(self, text, color, x, y, widget):
        self._doc = pyglet.text.document.UnformattedDocument(text)
        self._doc.set_style(0, len(self._doc.text), dict(color=(0, 0, 0, 255)))
        font = self._doc.get_font()
        height = font.ascent - font.descent
        pad = 2
        x1 = x - pad
        y1 = y - pad
        x2 = x + width + pad
        y2 = y + height + pad
        self._outline = batch.add(4, pyglet.gl.GL_QUADS, bg_group,
                                  ('v2i', [x1, y1, x2, y1, x2, y2, x1, y2]),
                                  ('c4B', color * 4))
        self._layout = IncrementalTextLayout(self._doc, width, height, multiline=False, batch=batch)
        self._caret = Caret(self._layout)
        self._caret.visible = False
        self._layout.x = x
        self._layout.y = y
        self._focus = False
        super().__init__(x, y, width, height)

    def _check_hit(self, x, y):
        return self._x < x < self._x + self._width and self._y < y < self._y + self._height

    def _set_focus(self, value):
        self._focus = value
        self._caret.visible = value

    def on_mouse_motion(self, x, y, dx, dy):
        if not self._check_hit(x, y):
            self._set_focus(False)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self._focus:
            self._caret.on_mouse_drag(x, y, dx, dy, buttons, modifiers)

    def on_mouse_press(self, x, y, buttons, modifiers):
        if self._check_hit(x, y):
            self._set_focus(True)
            self._caret.on_mouse_press(x, y, buttons, modifiers)

    def on_text(self, text):
        if self._focus:
            if text in ('\r', '\n'):
                self.dispatch_event('on_commit', self._layout.document.text)
                self._set_focus(False)
                return
            self._caret.on_text(text)

    def on_text_motion(self, motion):
        if self._focus:
            self._caret.on_text_motion(motion)

    def on_text_motion_select(self, motion):
        if self._focus:
            self._caret.on_text_motion_select(motion)

    def on_commit(self, text):
        pass


TextEntry.register_event_type('on_commit')