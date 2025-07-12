from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello, GitHub + Manim!")
        self.play(Write(text))
        self.wait(1)
