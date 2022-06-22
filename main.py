from manim import *
import random as rd
import numpy as np
from math import *
from colour import Color
from custom_manim_utils.custom_consts import *
from custom_manim_utils.custom_color_consts import *
from custom_manim_utils.custom_functions import *

config.frame_width = 16
config.frame_height = 9


class final(Scene):
    def construct(self):
        pass
        # lec1_s1.construct(self)


class working2(MovingCameraScene):
    def construct(self):
        # self.add(NumberPlane().set_z_index(1))

        speak(self, title='Scene2', txt=
        '케이상승 후 가격상승 또는 하락하는 경우를 동영상을 다시 보면서 천천히 곱씹어보시면 더 이해가 잘 될겁니다#1'
              , keep_pitch=True, update=1, speed=1.4)



        rect = RoundedRectangle(width=5,height=3,corner_radius=0.5)
        text = Tex('djfkdj', font_size=20).move_to(rect)


        self.wait(2)


class working1(MovingCameraScene):
    def construct(self):
        self.add(NumberPlane().set_z_index(1))


        speak(self, title='L01S01', txt=
        '안녕하십니까. 디파이를 알아보는 디파이 시리즈 첫번째 에피소드입니다#1'
        '디파이를 제대로 이해하기 위해서는 씨파이부터 이해할 필요가 있습니다#1'
        '씨파이는 센트럴라이즈드 파이낸스의 줄임말이고, 디파이는 아시다시피 디센트럴라이즈드 파이낸스의 줄임말입니다#1'
        '디파이가 나오게 된 배경에는 씨파이에 대한 불만이 있었기 때문입니다#1'
        '중앙화 거래소는 사람들이 원자재나 주식 등 무언가를 편하게 거래하기 위해서 탄생했습니다#1'
        '단순히 개인 대 개인으로 거래를 하려면 거래대상을 직접 찾기 힘들었고, 그 자리에서 일어나는 교환의 형태면 자리에 있는 동안만 상대방을 찾을 수 있고 예약 등의 형태로 거래하기가 어려웠습니다#1'
        '그래서 모두가 통일된 규격으로 거래하고 일방적 계약파기의 위험을 없애고, 내가 자고 있어도 예약된 주문이 가능하게 하는 등 다양한 편의를 위해 거래자 사이에 제3자인 거래소가 등장하고 거래소가 거래를 중개하기 시작했습니다#1'
              , keep_pitch=True, update=True, speed=1.4)
        self.camera.frame.save_state()

        # TODO 4.676 secs안녕하십니까. 디파이를 알아보는 디파이 시리즈 첫번째 에피소드입니다
        # TODO 0:00:00.000  ~  0:00:04.676
        # TODO 1.0secs pause
        # TODO 0:00:04.676  ~  0:00:05.676

        DEFI_lec1_title = Tex(r'DEFI Series\\EP.1').scale(2)
        DEFI_lec1_subtitle = Tex(r'Centralized Finance').next_to(DEFI_lec1_title, D)

        self.play(Create(DEFI_lec1_title),run_time=1)
        self.play(Create(DEFI_lec1_subtitle),run_time=1)
        self.wait(2.676)
        # self.wait(1)
        self.play(Uncreate(VGroup(DEFI_lec1_title, DEFI_lec1_subtitle)),run_time=1)

        # TODO 4.144 secs디파이를 제대로 이해하기 위해서는 씨파이부터 이해할 필요가 있습니다
        # TODO 0:00:05.676  ~  0:00:09.820
        # TODO 1.0secs pause
        # TODO 0:00:09.820  ~  0:00:10.820
        cefi = Tex('CEFI', substrings_to_isolate=['C', 'F']).scale(2)
        centralized_finance = Tex('Centralized Finance', substrings_to_isolate=['C', 'F']).scale(2)

        self.play(Create(cefi))
        self.wait(3)

        # TODO 7.164 secs씨파이는 센트럴라이즈드 파이낸스의 줄임말이고, 디파이는 아시다시피 디센트럴라이즈드 파이낸스의 줄임말입니다
        # TODO 0:00:10.820  ~  0:00:17.984
        # TODO 1.0secs pause
        # TODO 0:00:17.984  ~  0:00:18.984

        self.play(TransformMatchingTex(cefi,centralized_finance),run_time=1)
        self.wait(1)

        decentralized_finance = Tex('Decentralized Finance', substrings_to_isolate=['D', 'F']).scale(2).shift(D*1)
        defi = Tex('DEFI', substrings_to_isolate=['D', 'F']).scale(2).shift(D*1)

        self.play(centralized_finance.animate.shift(U*1))

        self.play(Create(defi))
        self.wait(1)
        self.play(TransformMatchingTex(defi,decentralized_finance))
        self.wait(2.164)

        # TODO 4.096 secs디파이가 나오게 된 배경에는 씨파이에 대한 불만이 있었기 때문입니다
        # TODO 0:00:18.984  ~  0:00:23.080
        # TODO 1.0secs pause
        # TODO 0:00:23.080  ~  0:00:24.080

        defi_spch = Tex("I don't like you CEFI...").next_to(decentralized_finance,D)
        cefi_spch = Tex("Well...").next_to(centralized_finance,U)

        self.play(Create(defi_spch))
        self.wait(1)
        self.play(Create(cefi_spch))
        self.wait(1)

        self.play(Uncreate(VGroup(centralized_finance,
                                  decentralized_finance,
                                  cefi_spch,
                                  defi_spch)))

        # TODO 5.69 secs중앙화 거래소는 사람들은 원자재나 주식 등 무언가를 편하게 거래하기 위해서 탄생했습니다
        # TODO 0:00:24.080  ~  0:00:29.770
        # TODO 1.0secs pause
        # TODO 0:00:29.770  ~  0:00:30.770


        arrow_1 = CurvedArrow(2 * L, 2 * R, radius=-5).shift(U * 1)
        arrow_2 = CurvedArrow(2 * R, 2 * L, radius=-5).shift(D * 1)
        btc = BTC_COIN.copy().scale(1.5).shift(L * 3)
        usdt = USDT_COIN.copy().scale(1.5).shift(R * 3)
        trade_main = VGroup(btc, usdt, arrow_1, arrow_2)

        milk = create_circle_asset(Tex(r'\textbf{Milk}',color=BLACK, font_size =25),  fill_color='#F0F2E8').scale(1.5).shift(L * 3)
        apple = create_circle_asset(Tex(r'\textbf{Apple}',color=WHITE, font_size =20),  fill_color='#C03728').scale(1.5).shift(R * 3)
        ssnlf =create_circle_asset(Tex(r'\textbf{SSNLF}',color=WHITE, font_size =20),  fill_color='#034A9A').scale(1.5).shift(L * 3)
        krw =create_circle_asset(Tex(r'\textbf{KRW}',color=WHITE, font_size =30),  fill_color='#EBBE69').scale(1.5).shift(R * 3)
        block = create_circle_asset(Tex(r'\textbf{Block}',color=WHITE, font_size =20),  fill_color='#CF4D27').scale(1.5).shift(L * 3)
        fish = create_circle_asset(Tex(r'\textbf{Fish}',color='#73C2E8', font_size =25),  fill_color='#4689C4').scale(1.5).shift(R * 3)
        appl =create_circle_asset(Tex(r'\textbf{AAPL}',color=WHITE, font_size =25),  fill_color='#919191').scale(1.5).shift(L * 3)
        usd= create_circle_asset(Tex(r'\textbf{USD}',color='#8AC889', font_size =30),  fill_color='#1E6B34').scale(1.5).shift(R * 3)


        trade_1 = VGroup(milk, apple, arrow_1.copy(), arrow_2.copy()).scale(0.6).to_edge(UR)
        trade_2 = VGroup(ssnlf, krw, arrow_1.copy(), arrow_2.copy()).scale(0.6).to_edge(DL)
        trade_3 = VGroup(block, fish, arrow_1.copy(), arrow_2.copy()).scale(0.6).to_edge(UL)
        trade_4 = VGroup(appl, usd, arrow_1.copy(), arrow_2.copy()).scale(0.6).to_edge(DR)
        # trade_1= trade_main.copy().scale(0.6).shift(R*6+U*3)
        # trade_2= trade_main.copy().scale(0.5).shift(L*6+D*3)
        # trade_3= trade_main.copy().scale(0.4).shift(L*6+U*3)
        # trade_4= trade_main.copy().scale(0.3).shift(R*6+D*3)

        self.play(AnimationGroup(Create(trade_main),
                                 Create(trade_1),
                                 Create(trade_2),
                                 Create(trade_4),
                                 Create(trade_3),
                                 ))

        self.play(AnimationGroup(Swap(btc, usdt),
                                 Swap(trade_1[ 0 ], trade_1[ 1 ]),
                                 Swap(trade_2[ 0 ], trade_2[ 1 ]),
                                 Swap(trade_4[ 0 ], trade_4[ 1 ]),
                                 Swap(trade_1[ 1 ], trade_1[ 0 ]),
                                 Swap(usdt, btc),
                                 Swap(trade_3[ 0 ], trade_3[ 1 ]),
                                 Swap(trade_2[ 1 ], trade_2[ 0 ]), lag_ratio=0.5, run_time=4)
                  )
        exchanges = Tex('Exchanges').scale(2)
        self.play(ReplacementTransform(VGroup(trade_main, trade_1, trade_2, trade_3, trade_4), exchanges))
        self.wait(0.5)
        self.play(Uncreate(exchanges), run_time=1.163)


        # TODO 11.61 secs단순히 개인 대 개인으로 거래를 하려면 거래대상을 직접 찾기 힘들었고, 그 자리에서 일어나는 교환의 형태면 자리에 있는 동안만
        #  상대방을 찾을 수 있고 예약 등의 형태로 거래하기가 어려웠습니다
        # TODO 0:00:30.770  ~  0:00:42.380
        # TODO 1.0secs pause
        # TODO 0:00:42.380  ~  0:00:43.380

        # TODO 13.76 secs그래서 모두가 통일된 규격으로 거래하고 일방적 계약파기의 위험을 없애고, 내가 자고 있어도 예약된 주문이 가능하게 하는 등 다
        #  양한 편의를 위해 거래자 사이에 제3자인 거래소가 등장하고 거래소가 거래를 중개하기 시작했습니다
        # TODO 0:00:43.380  ~  0:00:57.140
        # TODO 1.0secs pause
        # TODO 0:00:57.140  ~  0:00:58.140

        self.wait(5)


class working3(Scene):
    # config.frame_width = 16 * 4
    # config.frame_height = 9 * 4

    def construct(self):

        self.add(NumberPlane().set_z_index(1))

        speak(self, title='L02S05', txt=
        '아#1'
              , keep_pitch=True, update=True, speed=1.4)



class working(Scene):
    def construct(self):
        p1 = np.array([ -4, -2, 0 ])
        p2 = np.array([ 4, -2, 0 ])
        p3 = [ 1, 1, 0 ]
        p4 = [ -1, 1, 0 ]
        # a = Line(p1,p2).append_points(Line(p2,p3).points).append_points(Line(p3,p4).points)
        a = Line(start=p1, end=p2, buff=0.1)
        # point_start= a.get_start()
        # point_end  = a.get_end()
        # point_center = a.get_center()

        # self.add(Dot(a.get_start()).set_color(YELLOW).scale(2))
        # self.add(Dot(a.get_end()).set_color(RED).scale(2))
        # self.add(Dot(a.get_top()).set_color(GREEN_A).scale(2))
        # self.add(Dot(a.get_bottom()).set_color(GREEN_D).scale(2))
        # self.add(Dot(a.get_center()).set_color(BLUE).scale(2))
        # self.add(Dot(a.point_from_proportion(0.5)).set_color(ORANGE).scale(2))
        self.add(*[ Dot(x) for x in a.points ])
        self.add(a)


