from flexx import flx

class Calc(flx.Widget):
    def init(self):
        with flx.VSplit():
            self.calc = flx.Label(text="",
                                  style="font-family: Courier New, Lucida Console, monospace;font-size: 12vw; color: white; background: #000000; border-radius: 20px")
            with flx.GridLayout(ncolumns=4):
                self.b7 = flx.Button(text="7", style="background: #cfcfcf")
                self.b8 = flx.Button(text="8", style="background: #cfcfcf")
                self.b9 = flx.Button(text="9", style="background: #cfcfcf")
                self.bback = flx.Button(text=u"\u232B", style="background: #ed3b3b")
                self.b4 = flx.Button(text="4", style="background: #cfcfcf")
                self.b5 = flx.Button(text="5", style="background: #cfcfcf")
                self.b6 = flx.Button(text="6", style="background: #cfcfcf")
                self.bdivide = flx.Button(text=u"\u00F7", style="background: #abb9d6")
                self.b1 = flx.Button(text="1", style="background: #cfcfcf")
                self.b2 = flx.Button(text="2", style="background: #cfcfcf")
                self.b3 = flx.Button(text="3", style="background: #cfcfcf")
                self.bmult = flx.Button(text="*", style="background: #abb9d6")
                self.bdot = flx.Button(text=".", style="background: #cfcfcf")
                self.b0 = flx.Button(text="0", style="background: #cfcfcf")
                self.bplus = flx.Button(text="+", style="background: #abb9d6")
                self.bminus = flx.Button(text="-", style="background: #abb9d6")
                self.beq = flx.Button(text="=", style="background: #229608")
                self.bclr = flx.Button(text="C", style="background: ##ed3b3b")

    @flx.reaction("b7.pointer_click")
    def seven(self, *events):
        self.calc.set_text(self.calc.text + "7")

    @flx.reaction("b8.pointer_click")
    def eight(self, *events):
        self.calc.set_text(self.calc.text + "8")

    @flx.reaction("b9.pointer_click")
    def nine(self, *events):
        self.calc.set_text(self.calc.text + "9")

    @flx.reaction("bback.pointer_click")
    def back(self, *events):
        self.calc.set_text(self.calc.text[:-1])

    @flx.reaction("b4.pointer_click")
    def four(self, *events):
        self.calc.set_text(self.calc.text + "4")

    @flx.reaction("b5.pointer_click")
    def five(self, *events):
        self.calc.set_text(self.calc.text + "5")

    @flx.reaction("b6.pointer_click")
    def six(self, *events):
        self.calc.set_text(self.calc.text + "6")

    @flx.reaction("bdivide.pointer_click")
    def divide(self, *events):
        self.calc.set_text(self.calc.text + "/")

    @flx.reaction("b1.pointer_click")
    def one(self, *events):
        self.calc.set_text(self.calc.text + "1")

    @flx.reaction("b2.pointer_click")
    def two(self, *events):
        self.calc.set_text(self.calc.text + "2")

    @flx.reaction("b3.pointer_click")
    def three(self, *events):
        self.calc.set_text(self.calc.text + "3")

    @flx.reaction("bmult.pointer_click")
    def mult(self, *events):
        self.calc.set_text(self.calc.text + "*")

    @flx.reaction("bdot.pointer_click")
    def dot(self, *events):
        self.calc.set_text(self.calc.text + ".")

    @flx.reaction("b0.pointer_click")
    def zero(self, *events):
        self.calc.set_text(self.calc.text + "0")

    @flx.reaction("bplus.pointer_click")
    def plus(self, *events):
        self.calc.set_text(self.calc.text + "+")

    @flx.reaction("bminus.pointer_click")
    def minus(self, *events):
        self.calc.set_text(self.calc.text + "-")

    @flx.reaction("beq.pointer_click")
    def solve(self, *events):
        self.calc.set_text(eval(self.calc.text))

    @flx.reaction("bclr.pointer_click")
    def clear(self, *events):
        self.calc.set_text("")


app = flx.App(Calc)
app.serve("calc")
flx.start()

app.export("calc.html", link=0)  # Export to single file
app.launch("browser")  # show it now in a browser
flx.run()  # enter the mainloop


