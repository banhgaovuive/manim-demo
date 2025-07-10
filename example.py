from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello, Manim on GitHub!")
        self.play(Write(text))
        self.wait(2)
