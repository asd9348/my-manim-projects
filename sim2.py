from random import *
import numpy as np
from manim import *

data = np.array([ 50, 80, 20 ])
from manim.opengl import *

from custom_manim_utils.custom_mobs import *
# import manim.utils.space_ops
from manim import *
# from manimlib.imports import *

import random as rd
import numpy as np
# from math import *
from colour import Color
from custom_manim_utils.custom_consts import *
# from custom_manim_utils.custom_color_consts import *
from custom_manim_utils.custom_functions import *
from custom_manim_utils.custom_mobs import *
from custom_manim_utils.custom_mobs import *
from manim_physics import *
from manim_gearbox import *
from pathlib import Path

from pprint import pprint

# UL_pos = map.get_corner(UL)
# DR_pos = map.get_corner(DR)
#
# x_range = [ UL_pos[ 0 ], DR_pos[ 0 ], DR_pos[ 0 ] - UL_pos[ 0 ] ]  # [min, max, len]
# y_range = [ DR_pos[ 1 ], UL_pos[ 1 ], UL_pos[ 1 ] - DR_pos[ 1 ] ]
#
#
# def get_pos_on_map(x_pos, y_pos, x_range, y_range):
#     new_x_pos= x_range[ 2 ]*x_pos + x_range[0]
#     new_y_pos= y_range[ 2 ]*y_pos + y_range[0]
#
#     return [new_x_pos, new_y_pos]
#
#
# map_height = 8
# map_width = 12
#
# default_speed = 1
# default_size = 1
# default_sense = 1

dl_bound = [ -6, -4 ]
ur_bound = [ 6, 4 ]
max_speed = 1

gravity_strength = 1
wall_buffer = 1
wander_step_size = 1
wander_step_duration = 1
dt = 0.1


def update_time(mob, dt):
    mob.time += dt


class Person(VGroup):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.time = 0
        self.last_step_change = -1
        self.change_anims = [ ]
        self.velocity = np.zeros(3)
        # self.infection_start_time = np.inf
        # self.infection_end_time = np.inf
        # self.repulsion_points = []
        # self.num_infected = 0
        self.gravity_strength = 1
        self.gravity_well = np.zeros(3)
        self.wall_buffer = 1
        self.wander_step_size = 1
        self.wander_step_duration = 1
        self.dl_bound = [ -6, -4 ]
        self.ur_bound = [ 6, 4 ]
        self.max_speed = 1

        self.center_point = VectorizedPoint()
        self.add(self.center_point)
        self.add_body()
        # self.add_infection_ring()
        # self.set_status(self.status, run_time=0)

        # Updaters
        self.add_updater(update_time)
        # self.add_updater(lambda m, dt: m.update_position(dt))
        # self.add_updater(lambda m, dt: m.update_infection_ring(dt))
        # self.add_updater(lambda m: m.progress_through_change_anims())

    def add_body(self):
        body = self.get_body()
        body.scale_to_fit_width(0.2)
        body.move_to(self.get_center())
        self.add(body)
        self.body = body

    def get_body(self, status=None):
        person = Triangle()
        person.set_stroke(width=0)
        return person

    def update_position(self, dt):
        center = self.get_center()
        total_force = np.zeros(3)

        # Gravity
        if self.wander_step_size != 0:
            if (self.time - self.last_step_change) > self.wander_step_duration:
                vect = rotate_vector(RIGHT, TAU * random())
                self.gravity_well = center + self.wander_step_size * vect
                self.last_step_change = self.time
                print('fuck')

        if self.gravity_well is not None:
            to_well = (self.gravity_well - center)
            dist = np.linalg.norm(to_well)
            if dist != 0:
                total_force += self.gravity_strength * to_well / (dist ** 3)

        # Avoid walls
        wall_force = np.zeros(3)
        for i in range(2):
            to_lower = center[ i ] - self.dl_bound[ i ]
            to_upper = self.ur_bound[ i ] - center[ i ]

            # Bounce
            if to_lower < 0:
                self.velocity[ i ] = abs(self.velocity[ i ])
                self.set_coord(self.dl_bound[ i ], i)
            if to_upper < 0:
                self.velocity[ i ] = -abs(self.velocity[ i ])
                self.set_coord(self.ur_bound[ i ], i)

            # Repelling force
            wall_force[ i ] += max((-1 / self.wall_buffer + 1 / to_lower), 0)
            wall_force[ i ] -= max((-1 / self.wall_buffer + 1 / to_upper), 0)
        total_force += wall_force

        # Apply force
        self.velocity += total_force * dt

        # Limit speed
        speed = np.linalg.norm(self.velocity)
        if speed > self.max_speed:
            self.velocity *= self.max_speed / speed

        # Update position
        self.shift(self.velocity * dt)

    def get_center(self):
        return self.center_point.get_points()[ 0 ]


class mytest(OpenGLVGroup):
    def __init__(self, map_data=None, **kwargs):
        super().__init__(**kwargs)

        self.time = 0
        self.last_step_change = -1
        self.change_anims = [ ]

        self.map_data = map_data

        # self.center_point = VectorizedPoint().move_to([ uniform(map_data[ 'x_range' ][ 'min' ], map_data[ 'x_range' ][ 'max' ]),
        #                                                 uniform(map_data[ 'y_range' ][ 'min' ], map_data[ 'y_range' ][ 'max' ]), 0 ])
        self.center_point = VectorizedPoint().move_to([ -1,-1, 0 ])

        self.change_anims = []

        self.body = None
        if self.get_center()[1]<0:
            self.status = 'below'
        else :
            self.status='above'

        self.color_map = {'below':RED, 'above':BLUE}
        self.ur_bound = map_data['ur_bound']
        self.dl_bound = map_data['dl_bound']
        self.wander_step_size=1
        self.gravity_strength = 1
        self.wall_buffer = 1
        self.wander_step_size = 1
        self.wander_step_duration = 1
        self.max_speed=1
        self.gravity_well= np.zeros(3)
        self.dl_bound = [ -6, -4 ]
        self.ur_bound = [ 6, 4 ]
        self.max_speed = 1
        self.velocity = np.zeros(3)
        self.add_body()
        self.add(self.center_point)
        # Updaters
        self.add_updater(update_time)
        # self.add_updater(lambda m, dt: m.update_pos(dt))
        self.add_updater(lambda m, dt: m.moving_up(dt))
        self.add_updater(lambda m: m.progress_through_change_anims())

        # self.add_updater(lambda m, dt: m.update_infection_ring(dt))
        # self.add_updater(lambda m: m.progress_through_change_anims())

    def add_body(self):
        self.body=Triangle(fill_opacity=1).scale_to_fit_width(0.2).move_to(self.get_center())
        self.add(self.body)

    def get_center(self):
        return self.center_point.get_center()
    def moving_up(self,dt):

        self.shift(0.02 * UP)

        self.change_mob(self)

    def update_pos(self, dt):
        center = self.get_center()
        total_force = np.zeros(3)

        if self.wander_step_size != 0:
            if (self.time - self.last_step_change) > self.wander_step_duration:
                vect = rotate_vector(RIGHT, TAU * random())
                self.gravity_well = center + self.wander_step_size * vect
                self.last_step_change = self.time

        if self.gravity_well is not None:
            to_well = (self.gravity_well - center)
            dist = np.linalg.norm(to_well)
            if dist != 0:
                total_force += self.gravity_strength * to_well / (dist**3)

        # Avoid walls
        wall_force = np.zeros(3)
        for i in range(2):
            to_lower = center[i] - self.dl_bound[i]
            to_upper = self.ur_bound[i] - center[i]

            # Bounce
            if to_lower < 0:
                self.velocity[i] = abs(self.velocity[i])
                self.set_coord(self.dl_bound[i], i)
            if to_upper < 0:
                self.velocity[i] = -abs(self.velocity[i])
                self.set_coord(self.ur_bound[i], i)

            # Repelling force
            wall_force[i] += max((-1 / self.wall_buffer + 1 / to_lower), 0)
            wall_force[i] -= max((-1 / self.wall_buffer + 1 / to_upper), 0)
        total_force += wall_force

        self.velocity += total_force * dt

        speed = np.linalg.norm(self.velocity)
        if speed > self.max_speed:
            self.velocity *= self.max_speed / speed

        self.shift(self.velocity * dt)

        self.change_mob(self)
        # vect = rotate_vector(RIGHT, TAU * random())
        #
        # self.shift(vect*dt)

    def change_mob(self, run_time=1):

        # print(self.status)
        start_color = self.color_map[self.status]
        end_color = self.color_map[self.status]


        if self.get_center()[1]<0:
            curr_state = 'below'
            if self.status==curr_state:
                anims= []
                print('below same')

            else:
                anims = [ UpdateFromAlphaFunc(self.body, lambda m, a: m.rotate(angle=PI*a), run_time=5) ]
                self.status='above'
                print('above to below')

        else:
            curr_state = 'above'
            # print(self.status==curr)
            if self.status==curr_state:
                anims= []
                print('above same')
            else:
                def test(m,a):
                    m.rotate(angle=-PI / 4/30)
                    # m.set_color(RED)
                    print(a)


                anims = [ UpdateFromAlphaFunc(self.body, test, run_time=5, rate_func=linear),
                          UpdateFromAlphaFunc(self.body, lambda m, a: m.set_color(RED), run_time=1, rate_func=linear)]
                # body=self.body.get_center()
                # anims = [ Flash(body) ]
                self.status='above'
                print('below to above')


            # anims = [ UpdateFromAlphaFunc(self.body, lambda m, a: m.rotate(angle=a), run_time=1) ]
        # if self.get_center()[1]<0:
        #     self.status = 'below'
        #     anims= []
        # else:
        #     self.status = 'above'
        #     anims = [ UpdateFromAlphaFunc(self.body, lambda m, a: m.rotate(angle=a), run_time=1) ]

        # anims = [UpdateFromAlphaFunc(self.body,lambda m, a: m.scale_to_fit_width(2),run_time=3)]
        # anims = [
        #     # UpdateFromAlphaFunc(self.body,lambda m, a: m.set_color(interpolate_color(start_color, end_color, a)),run_time=3),
        #     UpdateFromAlphaFunc(self.body,lambda m, a: m.scale_to_fit_width(2),run_time=3),
        #     Rotate(self.body,angle=PI,run_time=5)
        # ]
        for anim in anims:
            self.push_anim(anim)

        # self.status = status

    def push_anim(self, anim):
        anim.suspend_mobject_updating = False
        anim.begin()
        anim.start_time = self.time
        self.change_anims.append(anim)
        return self

    def pop_anim(self, anim):
        anim.update_mobjects(1)
        anim.finish()
        self.change_anims.remove(anim)

    def progress_through_change_anims(self):
        for anim in self.change_anims:
            if anim.run_time == 0:
                alpha = 1
            else:

                alpha = (self.time - anim.start_time) / anim.run_time
                print('alpha is ',alpha)
                print('self.time is ',self.time)
                print('anim.start_time is ',anim.start_time)
                print('anim.run_time is ',anim.run_time)
            anim.interpolate(alpha)
            if alpha >= 1:
                self.pop_anim(anim)
                print('popper')


class working2(MovingCameraScene):
    def construct(self):
        map = Rectangle(width=12, height=8)

        def get_rect_map_data(map):
            UR_pos = map.get_corner(UR)
            DL_pos = map.get_corner(DL)
            x_range = {'min': DL_pos[ 0 ], 'max': UR_pos[ 0 ], 'len': UR_pos[ 0 ] - DL_pos[ 0 ]}  # [min, max, len]
            y_range = {'min': DL_pos[ 1 ], 'max': UR_pos[ 1 ], 'len': UR_pos[ 1 ] - DL_pos[ 1 ]}

            return {'x_range': x_range, 'y_range': y_range, 'ur_bound':UR_pos, 'dl_bound':DL_pos}

        map_data = get_rect_map_data(map)
        self.add(map)
        tris=OpenGLVGroup(*[mytest(map_data=map_data) for i in range(1)])
        # tri_2=mytest(map_data=map_data)
        # self.add(tri_1)
        # self.add(tri_2)

        # self.play(Flash(tris[0]))

        timer = DecimalNumber(0.05).to_corner(UL)
        timer.add_updater(lambda m, dt: m.set_value(tris[0].time))
        # timer=always_
        # redraw(lambda m, dt: m.set_value(m.get_value()+dt))
        self.add(timer)


        # instances =VGroup(*[mytest() for i in range(10) ])
        # time_tracker = self.time

        self.add(tris)

        # self.play(Create(tris))
        self.wait(100)

        # timer.clear_updaters()



        # self.play(Create(mytest(map_data=map_data)),run_time=3)

        # self.wait(8)
