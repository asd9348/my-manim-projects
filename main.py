from manim import *
import random as rd
import numpy as np
from math import *
from colour import Color
from custom_manim_utils.custom_consts import *
from custom_manim_utils.custom_functions import *

config.frame_width = 16
config.frame_height = 9


class final(Scene):
    def construct(self):
        pass
        # lec1_s1.construct(self)
        # lec1_s2.construct(self)
        # lec1_s3.construct(self)
        # lec1_s4.construct(self)
        # working.construct(self)


class working2(Scene):
    def construct(self):
        self.add(NumberPlane().set_z_index(1))
        speak(self, title='Scene2', txt=
        '간단하게 오토매틱 마켓 메이커를 통해 덱스가 돌아가는 원리를 배웟는데, 이젠 약간의 수학과 함께 더욱 자세히 알아보겠습니다#1'
        '엑스와이는 케이에서 엑스를 이항시키면 와이는 엑스분의 케이 형태입니다#1'
        '여러분 모두 중학교 때 함수를 배웠을 것이고, 기본적인 와이는 이엑스도 배웠고 와이는 엑스분의 1을 배운 기억이 날겁니다#1'
        '그중에 엑스분의 1함수는 반비례함수라고 배웠고 쌍곡선의 형태를 띄는 함수입니다. 그리고 이 반비레함수는 케이값에 따라서 보이는 것과 같이 원점에서 점점 멀어지는 함수입니다#1'
        '일반적인 오토매틱 마켓메이커는 이 함수를 사용해 가격을 결정합니다. 도대체 어떻게 가격을 결정하는지 알아보겠습니다#1'
        '여기서 엑스는 에이코인의 양, 와이는 비코인의 양입니다#1 '
        '페어라는 것이 원래 양방향이어서 서로 바꿔도 무방하나 앞으로 이해하기 쉽게 풀내부의 베이스에셋의 양이 엑스, 쿼트에셋의 양이 와이라고 하겠습니다#1'

              , keep_pitch=True, update=True, speed=1.4)

        # TODO 7.877 secs간단하게 오토매틱 마켓 메이커를 통해 덱스가 돌아가는 원리를 배웟는데, 이젠 약간의 수학과 함께 더욱 자세히 알아보겠습니다

        # TODO 1.0 secs pause

        amm_text = Tex('AMM').scale(2)
        with_math_text = Tex('with Math').next_to(amm_text, D)

        self.play(Create(amm_text), run_time=2)
        self.wait(1.5)
        self.play(Create(with_math_text), run_time=2)
        self.wait(1)

        self.play(Uncreate(VGroup(amm_text, with_math_text)), run_time=1)
        self.wait(0.5)

        # TODO 4.615 secs엑스와이는 케이에서 엑스를 이항시키면 와이는 엑스분의 케이 형태입니다

        # TODO 1.0 secs pause

        xyk = MathTex('x', r'\times', 'y', '=', 'k').scale(2)
        self.play(Write(xyk), run_time=1)
        self.wait(1)

        xyk_fraction = MathTex('y', '=', r'\frac{k}{x}').scale(2)
        self.play(TransformMatchingShapes(xyk, xyk_fraction), run_time=1.5)
        self.wait(1)

        # TODO 7.84 secs여러분 모두 중학교 때 함수를 배웠을 것이고, 기본적인 와이는 이엑스도 배웠고 와이는 엑스분의 1을 배운 기억이 날겁니다

        # TODO 1.0 secs pause

        self.play(xyk_fraction.animate.scale(0.5).to_edge(U).shift(L * 6), run_time=1)
        self.wait(t)

        ##### 여러분 모두 중학교 때 함수를 배웠을 것이고
        ##### 기본적인  와이는 2엑스도 배웠고 와이는 엑스분의 1을 빼운기억이 날겁니다
        ##### 그중에 엑스분의 1함수는 반비례함수라고 배웠고 쌍곡선의 형태를 띄는 함수입니다
        # 함수여러개 팝업 그중에 엑스부느이 일 강조
        func_1 = MathTex(r'y = 5x').move_to(np.array([ -5, -2, 0 ]))
        func_2 = MathTex(r'y = 2x-1').move_to(np.array([ 3.5, 3, 0 ]))
        func_3 = MathTex(r'y = \frac{1}{x}')
        func_4 = MathTex(r'y = \frac{x}{15}').move_to(np.array([ 0, -3, 0 ]))
        func_5 = MathTex(r'y = -6x+\frac{17}{31}').move_to(np.array([ 5, -2, 0 ]))

        self.play(AnimationGroup(Create(func_1),
                                 Create(func_2),
                                 Create(func_3),
                                 Create(func_4),
                                 Create(func_5),
                                 lag_ratio=0.5), run_time=3)
        self.wait(2)

        self.play(Circumscribe(func_3), run_time=1)
        self.wait(1)

        self.play(AnimationGroup(Uncreate(func_1),
                                 Uncreate(func_2),
                                 Uncreate(func_3),
                                 Uncreate(func_4),
                                 Uncreate(func_5),
                                 lag_ratio=0.5), run_time=1)

        self.wait(0.5)
        # TODO 11.331 secs그중에 엑스분의 1함수는 반비례함수라고 배웠고 쌍곡선의 형태를 띄는 함수입니다. 그리고 이 반비레함수는 케이값에 따라서 보이는 것과 같이 원점에서 점점 멀어지는 함수입니다

        # TODO 1.0 secs pause

        k_var = Variable(1, MathTex("k"), var_type=Integer).next_to(xyk_fraction, R, buff=2)
        k_tracker = k_var.tracker
        k_tracker.set_value(1)
        graph_range = 50

        ax = Axes(x_range=[ 0, graph_range, int(graph_range / 10) ],
                  y_range=[ 0, graph_range, int(graph_range / 10) ],
                  x_length=5,
                  y_length=5,

                  tips=True,
                  axis_config={"include_numbers": True, 'color': WHITE, 'font_size': 20, 'tip_width': 0.1, 'tip_height': 0.1},
                  ).to_edge(L, buff=1.2)

        xyk_graph = ax.plot(lambda x: k_tracker.get_value() / x,
                            x_range=[ 0.00001, 20 ],
                            use_smoothing=False, color=BLUE)

        xyk_graph.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: k_tracker.get_value() / x,
                    x_range=[ k_tracker.get_value() / graph_range, graph_range ],
                    use_smoothing=False, color=BLUE)))

        self.play(Create(k_var))
        self.play(Create(ax))
        self.play(Create(xyk_graph))
        self.wait(1)

        self.play(k_tracker.animate.set_value(300), run_time=7)
        self.wait(1)

        # TODO 7.502 secs일반적인 오토매틱 마켓메이커는 이 함수를 사용해 가격을 결정합니다. 도대체 어떻게 가격을 결정하는지 알아보겠습니다

        # TODO 1.0 secs pause
        self.wait(5)

        self.play(Uncreate(k_var), run_time=0.5)
        self.play(Uncreate(ax), run_time=0.5)
        self.play(Uncreate(xyk_graph), run_time=0.5)
        self.wait(0.5)

        # TODO 3.54 secs여기서 엑스는 에이코인의 양 와이는 비코인의 양입니다

        # TODO 1.0 secs pause

        # TODO 9.351 secs 페어라는 것이 원래 양방향이어서 서로 바꿔도 무방하나 앞으로 이해하기 쉽게 베이스에셋의 양이 풀내부의 엑스코인의 양, 쿼트에셋의 양이 와이라고 하겠습니다

        # TODO 1.0 secs pause

        B_coin_amt = Tex('B coin amount').shift(L * 4.5)
        A_coin_amt = Tex('A coin amount')
        A_coin_base = Tex('Base asset').next_to(A_coin_amt, D)
        B_coin_quote = Tex('Quote asset').next_to(B_coin_amt, D)
        A_coin_BTC = Tex('BTC').next_to(A_coin_base, D)
        B_coin_USDT = Tex('USDT').next_to(B_coin_quote, D)
        A_coin_texts = VGroup(A_coin_amt, A_coin_base, A_coin_BTC)
        B_coin_texts = VGroup(B_coin_amt, B_coin_quote, B_coin_USDT)

        x_arrow = Arrow(end=A_coin_amt.get_top(), start=xyk_fraction[ 2 ].get_bottom())
        y_arrow = Arrow(end=B_coin_amt.get_top(), start=xyk_fraction[ 0 ].get_bottom())

        self.play(GrowArrow(x_arrow),
                  GrowArrow(y_arrow)
                  , run_time=1)
        self.wait(1)

        self.play(Create(A_coin_texts),
                  Create(B_coin_texts), run_time=2)

        self.wait(7)
        self.play(ApplyWave(A_coin_texts))
        self.play(ApplyWave(B_coin_texts))
        self.wait(0.5)

        self.play(Uncreate(A_coin_texts),
                  Uncreate(B_coin_texts),
                  Unwrite(x_arrow),
                  Unwrite(y_arrow)
                  , run_time=1.5)
        self.wait(0.5)

        self.add(Circle(radius=3, fill_color=RED, fill_opacity=1))
        self.wait(5)


# class working1(Scene):
#     def construct(self):
#         speak(self, title='L02S05', txt=
#         '간단하게 오토매틱 마켓 메이커를 통해 덱스가 돌아가는 원리를 배웟는데, 이젠 약간의 수학과 함께 더욱 자세히 알아보겠습니다#1'
#         '엑스와이는 케이에서 엑스를 이항시키면 와이는 엑스분의 케이 형태입니다#1'
#         '여러분 모두 중학교 때 함수를 배웠을 것이고, 기본적인 와이는 이엑스도 배웠고 와이는 엑스분의 1을 배운 기억이 날겁니다#1'
#         '그중에 엑스분의 1함수는 반비례함수라고 배웠고 쌍곡선의 형태를 띄는 함수입니다. 그리고 이 반비레함수는 케이값에 따라서 보이는 것과 같이 원점에서 점점 멀어지는 함수입니다#1'
#         '일반적인 오토매틱 마켓메이커는 이 함수를 사용해 가격을 결정합니다. 도대체 어떻게 가격을 결정하는지 알아보겠습니다#1'
#         '여기서 엑스는 에이코인의 양 와이는 비코인의 양입니다#1 '
#         '페어라는 것이 원래 양방향이어서 서로 바꿔도 무방하나 앞으로 이해하기 쉽게 풀내부의 베이스에셋의 양이 엑스, 쿼트에셋의 양이 와이라고 하겠습니다#1'
#               , keep_pitch=True, update=True, speed=1.4)
#
#


class coor(Scene):
    def construct(self):
        dot1 = Dot().shift(U*2)
        dot2 = Dot().shift(U*1)
        dot3 = Dot()

        # self.add(dot1,dot2,dot3)

        dots = VGroup(dot1,dot2,dot3)


        square1= Square()
        square2= Square().scale(1.2)
        square3= Square().scale(1.4)

        squares = VGroup(square1,square2,square3)

        shapes = VGroup(dots,squares)

        self.play(Create(shapes), run_time=15)

        self.play(dots[2].animate.shift(R*1))
        self.play(shapes[1][1].animate.shift(L*4))
