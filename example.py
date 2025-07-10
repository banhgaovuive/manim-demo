from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello from GitHub Actions!")
        self.play(Write(text))
        self.wait(2)
