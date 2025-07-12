from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("Xin chào từ Manim trên GitHub!")
        self.play(Write(text))
        self.wait(1)
