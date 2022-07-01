from manim import *
import random as rd
import numpy as np
from math import *
from colour import Color
from custom_manim_utils.custom_consts import *
from custom_manim_utils.custom_functions import *
from custom_manim_utils.custom_color_consts import *

config.frame_width = 16
config.frame_height = 9

BTC = C_BTC
ETH = C_ETH
DOT = C_DOT
SOL2 = C_SOL2
USDT = C_USDT

class final(Scene):
    def construct(self):
        L_02_S_01_dex_pros_and_cons.construct(self)
        L_02_S_02_smart_contract.construct(self)

# class L01S01(MovingCameraScene):
#     def construct(self):
#         speak(self, title='Scene2', txt=
#         '이제 본격적으로 디파이에 대해 알아보겠습니다#1'
#         '디파이의 가장 근간이 되는 것은 탈중앙화 거래소입니다#1'
#         '탈중앙화 거래소는 디센트럴라이즈드 익스체인지로 줄여서 덱스라고 부릅니다#1'
#         '탈중앙화 거래소는 말그대로 중앙화된 주체가 없는 거래소입니다#1'
#         '모든 거래들이 중앙 주체를 거치지 않고 블록체인에 트랜잭션으로 기록되는 것입니다#1'
#         '마치 비트코인 네트워크가 만든사람도 없어진 뒤에 스스로 혼자 계속 작동하듯#1'
#         '덱스도 중앙화된 주체 없이 블록체인상에서 끊임없이 돌아갑니다#1'
#               , keep_pitch=True, update=False, speed=1.4)
#
#         self.wait(5)


class L01S01(MovingCameraScene):
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

        self.play(Create(DEFI_lec1_title), run_time=1)
        self.play(Create(DEFI_lec1_subtitle), run_time=1)
        self.wait(2.676)
        # self.wait(1)
        self.play(Uncreate(VGroup(DEFI_lec1_title, DEFI_lec1_subtitle)), run_time=1)

        # TODO 4.144 secs디파이를 제대로 이해하기 위해서는 씨파이부터 이해할 필요가 있습니다
        # TODO 0:00:05.676  ~  0:00:09.820
        # TODO 1.0secs pause
        # TODO 0:00:09.820  ~  0:00:10.820
        cefi = Tex('CEFI', substrings_to_isolate=[ 'C', 'F' ]).scale(2)
        centralized_finance = Tex('Centralized Finance', substrings_to_isolate=[ 'C', 'F' ]).scale(2)

        self.play(Create(cefi))
        self.wait(3)

        # TODO 7.164 secs씨파이는 센트럴라이즈드 파이낸스의 줄임말이고, 디파이는 아시다시피 디센트럴라이즈드 파이낸스의 줄임말입니다
        # TODO 0:00:10.820  ~  0:00:17.984
        # TODO 1.0secs pause
        # TODO 0:00:17.984  ~  0:00:18.984

        self.play(TransformMatchingTex(cefi, centralized_finance), run_time=1)
        self.wait(1)

        decentralized_finance = Tex('Decentralized Finance', substrings_to_isolate=[ 'D', 'F' ]).scale(2).shift(D * 1)
        defi = Tex('DEFI', substrings_to_isolate=[ 'D', 'F' ]).scale(2).shift(D * 1)

        self.play(centralized_finance.animate.shift(U * 1))

        self.play(Create(defi))
        self.wait(1)
        self.play(TransformMatchingTex(defi, decentralized_finance))
        self.wait(2.164)

        # TODO 4.096 secs디파이가 나오게 된 배경에는 씨파이에 대한 불만이 있었기 때문입니다
        # TODO 0:00:18.984  ~  0:00:23.080
        # TODO 1.0secs pause
        # TODO 0:00:23.080  ~  0:00:24.080

        defi_spch = Tex("I don't like you CEFI...").next_to(decentralized_finance, D)
        cefi_spch = Tex("Well...").next_to(centralized_finance, U)

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

        milk = create_circle_asset(Tex(r'\textbf{Milk}', color=BLACK, font_size=25), fill_color='#F0F2E8').scale(1.5).shift(L * 3)
        apple = create_circle_asset(Tex(r'\textbf{Apple}', color=WHITE, font_size=20), fill_color='#C03728').scale(1.5).shift(R * 3)
        ssnlf = create_circle_asset(Tex(r'\textbf{SSNLF}', color=WHITE, font_size=20), fill_color='#034A9A').scale(1.5).shift(L * 3)
        krw = create_circle_asset(Tex(r'\textbf{KRW}', color=WHITE, font_size=30), fill_color='#EBBE69').scale(1.5).shift(R * 3)
        block = create_circle_asset(Tex(r'\textbf{Block}', color=WHITE, font_size=20), fill_color='#CF4D27').scale(1.5).shift(L * 3)
        fish = create_circle_asset(Tex(r'\textbf{Fish}', color='#73C2E8', font_size=25), fill_color='#4689C4').scale(1.5).shift(R * 3)
        appl = create_circle_asset(Tex(r'\textbf{AAPL}', color=WHITE, font_size=25), fill_color='#919191').scale(1.5).shift(L * 3)
        usd = create_circle_asset(Tex(r'\textbf{USD}', color='#8AC889', font_size=30), fill_color='#1E6B34').scale(1.5).shift(R * 3)

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

        A = create_entity(MathTex(r'A', color=BLACK, font_size=55), 1, WHITE, "BTC", C_BTC, 1.4, 0.3, asset_text_color=WHITE).to_edge(L)

        B = create_entity(MathTex(r'B', color=BLACK, font_size=55), 1, WHITE, "ETH", C_ETH, 1.4, 0.3, asset_text_color=WHITE).to_edge(R)

        a_spch = Tex('I want some ETH').next_to(A, DR)
        b_spch = Tex('I want some BTC').next_to(B, DL)
        where_is_A = Tex(r'Where is A?').next_to(b_spch, D, aligned_edge=R)
        where_is_B = Tex(r'Where is B?').next_to(a_spch, D, aligned_edge=L)

        A.add(a_spch)
        B.add(b_spch)

        today = Tex('Today').to_edge(U).scale(2)
        tomorrow = Tex('Tomorrow').to_edge(U).scale(2)

        self.play(Create(A),
                  Create(B))

        self.play(Create(today), run_time=0.5)
        self.play(A.animate.shift(L * 9))
        self.wait(0.5)
        self.play(Create(where_is_A))
        self.wait(1)
        self.play(Uncreate(today),
                  Uncreate(where_is_A))
        self.play(A.animate.shift(R * 9))

        self.play(Create(tomorrow), run_time=0.5)
        self.play(B.animate.shift(R * 9))
        self.wait(0.5)
        self.play(Create(where_is_B))
        self.wait(1)
        self.play(Uncreate(tomorrow),
                  Uncreate(where_is_B))

        self.play(A.animate.shift(L * 9))

        # TODO 13.76 secs그래서 모두가 통일된 규격으로 거래하고 일방적 계약파기의 위험을 없애고, 내가 자고 있어도 예약된 주문이 가능하게 하는 등 다
        #  양한 편의를 위해 거래자 사이에 제3자인 거래소가 등장하고 거래소가 거래를 중개하기 시작했습니다
        # TODO 0:00:43.380  ~  0:00:57.140
        # TODO 1.0secs pause
        # TODO 0:00:57.140  ~  0:00:58.140

        contract_R = Graph([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ],
                           [ (10, 11), (11, 1), (10, 9), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9) ],
                           layout={1: [ 0, 3.5, 0 ],
                                   2: [ -0.5, 3, 0 ],
                                   3: [ 0.5, 2, 0 ],
                                   4: [ -0.5, 1, 0 ],
                                   5: [ 0.5, 0, 0 ],
                                   6: [ -0.5, -1, 0 ],
                                   7: [ 0.5, -2, 0 ],
                                   8: [ -0.5, -3, 0 ],
                                   9: [ 0, -3.5, 0 ],
                                   10: [ 3, -3.5, 0 ],
                                   11: [ 3, 3.5, 0 ]},
                           vertex_type=Dot,
                           vertex_config={'fill_opacity': 0}
                           )
        contract_L = Graph([ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ],
                           [ (10, 11), (11, 1), (10, 9), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9) ],
                           layout={1: [ 0, 3.5, 0 ],
                                   2: [ -0.5, 3, 0 ],
                                   3: [ 0.5, 2, 0 ],
                                   4: [ -0.5, 1, 0 ],
                                   5: [ 0.5, 0, 0 ],
                                   6: [ -0.5, -1, 0 ],
                                   7: [ 0.5, -2, 0 ],
                                   8: [ -0.5, -3, 0 ],
                                   9: [ 0, -3.5, 0 ],
                                   10: [ -3, -3.5, 0 ],
                                   11: [ -3, 3.5, 0 ]},
                           vertex_type=Dot,
                           vertex_config={'fill_opacity': 0}

                           )

        contract_text = Tex(r'Contract').scale(1.8)

        self.add(index_labels(contract_text))
        contract_box = Rectangle(width=6, height=7)
        self.play(Create(contract_box))
        self.play(Create(contract_text))

        self.add(contract_L)
        self.add(contract_R)
        self.remove(contract_box)

        self.play(contract_L.animate.rotate(PI / 8).shift(L * 2),
                  contract_R.animate.rotate(-PI / 8).shift(R * 2),
                  contract_text[ 0 ][ 0:4 ].animate.rotate(PI / 4).shift(L * 3),
                  contract_text[ 0 ][ 4: ].animate.rotate(-PI / 4).shift(R * 3)
                  )
        cross = Cross(stroke_width=35).scale(4)
        self.wait(0.5)
        self.play(Create(cross), run_time=0.5)

        self.play(FadeOut(VGroup(contract_text[ 0 ][ 0:4 ], contract_L), shift=L),
                  FadeOut(VGroup(contract_text[ 0 ][ 4: ], contract_R), shift=R),
                  FadeOut(cross, shift=U),
                  )

        A.remove(a_spch)
        B.remove(b_spch)
        self.play(A.animate.shift(R * 9),
                  B.animate.shift(L * 9))

        exchange_box = RoundedRectangle(width=6, height=3, corner_radius=0.5)
        exchange_text = Tex('Exchange').next_to(exchange_box, U)
        exchange = VGroup(exchange_text, exchange_box)
        self.play(AnimationGroup(Create(exchange),
                                 A[ 1 ].animate.move_to(exchange_box.get_center() + L * 1.5),
                                 B[ 1 ].animate.move_to(exchange_box.get_center() + R * 1.5)
                                 , lag_ratio=0.5))

        self.play(A[ 0 ].animate.shift(U * 1.5))
        z_1 = Tex('Z').next_to(A[ 0 ], UR)
        z_2 = z_1.copy().scale(0.8).next_to(z_1, UR, buff=0.2)
        z_3 = z_1.copy().scale(0.6).next_to(z_2, UR, buff=0.2)
        zzz = VGroup(z_1, z_2, z_3).scale(1.1).next_to(A[ 0 ], UR, buff=0.1)

        self.play(Create(zzz))

        self.play(Swap(A[ 1 ], B[ 1 ]))

        zzz.invert()
        self.play(Uncreate(zzz))
        self.play(A[ 0 ].animate.shift(D * 1.5))

        self.play(A[ 1 ].animate.next_to(B[ 0 ], D),
                  B[ 1 ].animate.next_to(A[ 0 ], D))

        a_spch = Tex(r'Wow. I got it exchanged', 'while I am gone.').arrange(D, aligned_edge=L).next_to(B[ 1 ], D, aligned_edge=L)
        b_spch = Tex(r'Wow. I got it exchanged', 'without dealing with sleeping A').arrange(D, aligned_edge=R).next_to(A[ 1 ], D,
                                                                                                                       aligned_edge=R)

        self.play(Create(a_spch),
                  Create(b_spch))
        self.wait(20)
