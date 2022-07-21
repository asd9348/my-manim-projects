class test_1(Scene):
    def construct(self):
        charge1 = Charge(-4, LEFT * 3.5)
        charge2 = Charge(2, RIGHT * 4 + DOWN * 2)
        charge3_mag_tkr = ValueTracker(8)
        charge3 = redraw(lambda: Charge(charge3_mag_tkr.get_value(), UP * 3))
        charge4 = Charge(-1, RIGHT * 7 + U * 3.5)
        charge5 = Charge(-1, DOWN * 3.5)
        charge6 = Charge(-1, RIGHT * 7 + DOWN * 2)
        charge7 = Charge(-1, L * 7 + DOWN * 3)
        field = redraw(lambda: ElectricField(charge1, charge2, charge3, charge4, charge5, charge6, charge7))
        self.add(field, charge1, charge2, charge3, charge4, charge5, charge6, charge7)
        # self.play(charge3.animate.shift(L * 4), run_time=2)

        # self.play(charge3_mag_tkr.animate.set_value(15),
        #           charge1.animate.shift(D * 1 + L * 1), run_time=1)
        # self.play(charge3_mag_tkr.animate.set_value(1),
        #           charge1.animate.shift(D * 1 + L * 1), run_time=1)
        # self.wait(5)


class test_2(VectorScene):
    def construct(self):
        mag_tracker = ValueTracker(2)
        current1 = Current(LEFT * 4)

        # current2 = redraw(lambda: Current(RIGHT * 2.5, direction=IN, magnitude=mag_tracker.get_value()))
        current2 = Current(RIGHT * 4, direction=IN, magnitude=mag_tracker.get_value())

        def mag_change(current):
            current.magnitude = mag_tracker.get_value()

        current2.add_updater(mag_change)
        magnet = BarMagnet().rotate(PI / 4)

        field = redraw(lambda: MagneticField(current1, current2, magnet))
        # field = MagneticField(current1, current2)

        # sources=[current1, current2]
        # def field_update(field):
        #     field.magnetic_sources = sources
        #
        # field.add_updater(field_update)
        # field = MagneticField(current1, current2,magnet)
        # field.add_updater(lambda x: x.become(MagneticField(current1, current2)))

        # def field_fun(field):
        #     updated_field = MagneticField(current1, current2)
        #
        #     return updated_field
        # field.add_updater(field_update)

        # def redraw(func):
        #     mob = func()
        #     mob.add_updater(lambda m: mob.become(func()))
        #     return mob

        # field = MagneticField(current1, current2)
        # field.add_updater(lambda field:field.become(MagneticField(current1, Current(RIGHT * 2.5, direction=IN, magnitude=mag_tracker.get_value()))))

        # current2.magnitude=15
        # print(current2.magnitude)

        # print(self.mobjects)

        # current(1)
        # self.add(field,  magnet)
        self.add(field, current1, current2, magnet)

        # field.add_updater()
        # self.wait(1)

        # self.play(field.animate.shift(L*1))

        # self.wait(5)

        self.play(current1.animate.shift(L * 2))
        # self.play(current2.animate.become(Current(U * 2.5, direction=IN, magnitude=10)))

        self.play(mag_tracker.animate.set_value(10))

        # self.play()
        self.play(magnet.animate.rotate(PI / 4))
        # self.wait(5)


class test_3(SpaceScene):
    def construct(self):
        circle = Circle().shift(UP)
        circle.set_fill(RED, 1)
        circle.shift(DOWN + RIGHT)

        rect = Square().shift(UP)
        rect.rotate(PI / 4)
        rect.set_fill(YELLOW_A, 1)
        rect.shift(UP * 2)
        rect.scale(0.5)

        ground = Line([ -4, -3.5, 0 ], [ 4, -3.5, 0 ])
        wall1 = Line([ -4, -3.5, 0 ], [ -4, 3.5, 0 ])
        wall2 = Line([ 4, -3.5, 0 ], [ 4, 3.5, 0 ])
        walls = VGroup(ground, wall1, wall2)
        self.add(walls)

        self.play(
            DrawBorderThenFill(circle),
            DrawBorderThenFill(rect),
        )
        self.make_rigid_body(rect, elasticity=2)  # Mobjects will move with gravity
        self.make_rigid_body(circle, elasticity=0.3)  # Mobjects will move with gravity
        self.make_static_body(walls)  # Mobjects will stay in place
        self.wait(5)


class test_4(SpaceScene):
    def construct(self):
        # smaller gear
        gear1 = Gear(12, module=1, profile_shift=0.3, stroke_opacity=0, fill_color=WHITE, fill_opacity=1)
        # larger gear with inner teeth
        gear2 = Gear(36, module=1, inner_teeth=True, profile_shift=0.1, stroke_opacity=0, fill_color=RED, fill_opacity=1)
        gear1.shift(gear1.rp * UP)
        gear2.shift(gear2.rp * UP)
        # mesh with 0.15*module larger distance than default
        # positive_bias param is used to define left or right tooth flank shall engage if there is offset and play
        gear2.mesh_to(gear1, offset=0.15, positive_bias=False)

        self.play(Create(gear1))
        self.play(Create(gear2))
        # self.add(gear1)
        # self.add(gear2)
        # self.add(regular.angry)
        self.play(Rotate(gear1, gear1.pitch_angle * 8, rate_func=linear),
                  Rotate(gear2, gear2.pitch_angle * 8, rate_func=linear),
                  run_time=10)


class test_4(Scene):
    def construct(self):
        lens_style = {"fill_opacity": 0.5, "color": BLUE}
        a = Lens(-5, 1, **lens_style).shift(LEFT)
        a2 = Lens(5, 1, **lens_style).shift(RIGHT)
        b = [
            Ray(LEFT * 5 + UP * i, RIGHT, 8, [ a, a2 ], color=RED)
            for i in np.linspace(-2, 2, 10)
        ]
        self.add(a, a2, *b)
