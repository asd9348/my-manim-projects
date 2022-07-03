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



class L01S02_pair(MovingCameraScene):
    def construct(self):
    #     self.add(NumberPlane())

        speak(self, title='Scene2', txt=
        '페어를 표시할 때는 보통 슬래시나 대시를 사용하거나 그냥 티커를 붙여서 표시하기도 합니다#1'
        '그리고 일반적으로 왼쪽의 자산을 베이스 에셋 오른쪽을 쿼트 에셋이라고 부릅니다#1'
        '비티씨 테더 거래쌍의 가격이 현재 100이라면 현재 비티씨는 100테더라는 것입니다#1'
        '심볼처럼 말그대로 1베이스 에셋을 얻으려면 얼마나 많은 쿼트 에셋을 줘야하는지를 표시하는 것입니다#1'
        '여기서 베이스 에셋이 비티씨라고 테더를 가지고 이더를 사기만 할 수 있는게 아니라 당연히 비티씨를 가지고 테더를 살 수도 있습니다#1'
        '우린 이걸 각각 비티씨를 매수한다, 매도한다라고 부릅니다. 비티씨 매수는 테더 매도와 같고, 테더 매수는 비티씨 매도와 같습니다#1'
        '거래 자체가 서로 다른 걸 교환하는 것이기에 내가 비트코인을 들고있는 쪽이 될지 테더를 들고있는 쪽이 될지는 마음대로 정할 수 있습니다 #1'
        '일반적으로 거래쌍의 표기에 있어서는 가격이란 것이 원래 자산의 가치 변동을 표현하기 위한 것이므로 상대적으로 변동성이 큰 자산이 베이스 에셋이 되고 '
        '그에 비해 더 안정적이고 유명한 자산이 가치의 척도가 되기에 용이해 쿼트 에셋으로는 상대적으로 변동성이 작은 스테이블 코인, 법정통화, 비티씨, 이더리움 등이 많이 사용됩니다#1'
        '일반적인 주식 어플에서는 베이스 에셋과 쿼트 에셋을 생각해본 적이 없을 겁니다#1'
        '어차피 전부 쿼트에셋으로 원화만 사용하기 때문에 거래쌍이라는 개념보다는 주식쇼핑같은 느낌입니다#1'
        '하지만 외환시장, 즉 FOREX를 겪어보신 분이면 달러 엔, 유로 달러등의 거래쌍을 보셨을 겁니다#1'
        '크립토 마켓도 특정 코인을 사기위해서 비트코인이나 이더리움을 지불하는 경우도 많고, 스테이블 코인만 해도 종류가 여러가지여서 거래쌍 개념이 더 절실히 다가옵니다#1'
        '주식에서는 1 현대차가 3 삼성전자 이런 식으로 표현하지 않지만 크립토마켓에서는 1이더리움은 0.1비티씨, 1폴카닷은 0.01이더리움과 같은 표현이 많이 나옵니다#1'

              , keep_pitch=True, update=True, speed=1.4)
        # TODO 5.799 secs페어를 표시할 때는 보통 슬래시나 대시를 사용하거나 그냥 티커를 붙여서 표시하기도 합니다
        # TODO 0:00:00.000  ~  0:00:05.799
        # TODO 1.0secs pause
        # TODO 0:00:05.799  ~  0:00:06.799

        BTC_slash_USDT_text = Tex("BTC/USDT").scale(2)
        BTC_dash_USDT_text = Tex("BTC-USDT").scale(2)
        BTC_none_USDT_text = Tex("BTCUSDT", substrings_to_isolate=[ 'BTC', 'USDT' ]).scale(2)
        self.play(Write(BTC_slash_USDT_text))
        self.wait(1.25)
        self.play(TransformMatchingShapes(BTC_slash_USDT_text, BTC_dash_USDT_text))
        self.wait(1.25)
        self.play(TransformMatchingShapes(BTC_dash_USDT_text, BTC_none_USDT_text))
        self.wait(1.299)

        # TODO 5.182 secs그리고 일반적으로 왼쪽의 자산을 베이스 에셋 오른쪽을 쿼트 에셋이라고 부릅니다
        # TODO 0:00:06.799  ~  0:00:11.981
        # TODO 1.0secs pause
        # TODO 0:00:11.981  ~  0:00:12.981

        base_asset = Tex("Base asset").next_to(BTC_none_USDT_text, DL, buff=1.5)
        base_asset_arrow = Arrow(start=base_asset.get_corner(UR), end=BTC_none_USDT_text.get_corner(DL))
        quote_asset = Tex("Quote asset").next_to(BTC_none_USDT_text, DR, buff=1.5)
        quote_asset_arrow = Arrow(start=quote_asset.get_corner(UL), end=BTC_none_USDT_text.get_corner(DR))
        # self.add(index_labels(BTC_none_USDT_text))

        self.play(AnimationGroup(Circumscribe(BTC_none_USDT_text[ 0 ]),
                                 Create(base_asset),
                                 GrowArrow(base_asset_arrow),
                                 lag_ratio=0.7,
                                 run_time=3.091))

        self.play(AnimationGroup(Circumscribe(BTC_none_USDT_text[ 1 ]),
                                 Create(quote_asset),
                                 GrowArrow(quote_asset_arrow),
                                 lag_ratio=0.7,
                                 run_time=3.091))

        # TODO 5.472 secs비티씨 테더 거래쌍의 가격이 현재 100이라면 현재 비티씨는 100테더라는 것입니다
        # TODO 0:00:12.981  ~  0:00:18.453
        # TODO 1.0secs pause
        # TODO 0:00:18.453  ~  0:00:19.453

        expl_text_1 = Tex(r"If price of BTCUSDT is 100, then it means 1 BTC is 100 USDT").shift(DOWN * 3.5)

        self.play(Write(expl_text_1),
                  run_time=1)
        self.wait(4.472)
        self.play(Unwrite(expl_text_1),
                  run_time=1)

        # eth_text = Tex('ETH').move_to(BTC_none_USDT_text[ 0 ]).scale(2)
        # btc_text = Tex('BTC').move_to(BTC_none_USDT_text[ 1 ]).scale(2)
        #
        # self.play(Transform(BTC_none_USDT_text[ 0 ], eth_text))
        # self.play(Transform(BTC_none_USDT_text[ 1 ], btc_text))
        #
        # expl_text_2 = Tex("If price of ETHBTC is 0.1., then it means 1BTC is 0.1BTC").shift(DOWN * 2.5)
        # self.play(Write(expl_text_2))
        # self.play(Unwrite(expl_text_2))
        #
        # self.wait(q)

        # TODO 6.523 secs심볼처럼 말그대로 1베이스 에셋을 얻으려면 얼마나 많은 쿼트 에셋을 줘야하는지를 표시하는 것입니다
        # TODO 0:00:19.453  ~  0:00:25.976
        # TODO 1.0secs pause
        # TODO 0:00:25.976  ~  0:00:26.976

        expl_text_2 = Tex('1 BTC = 100 USDT').move_to(expl_text_1)
        self.play(ReplacementTransform(expl_text_1, expl_text_2), run_time=3)
        self.wait(4.523)

        # TODO 7.72 secs여기서 베이스 에셋이 비티씨라고 테더를 가지고 이더를 사기만 할 수 있는게 아니라 당연히 비티씨를 가지고 테더를 살 수도 있습니다
        # TODO 0:00:26.976  ~  0:00:34.696
        # TODO 1.0secs pause
        # TODO 0:00:34.696  ~  0:00:35.696

        self.play(Uncreate(VGroup(base_asset_arrow,
                                  quote_asset_arrow,
                                  base_asset,
                                  quote_asset,
                                  expl_text_2
                                  )), run_time=3)

        self.wait(1)

        both_arrow = MathTex(r'\Leftrightarrow').scale(2)
        self.play(BTC_none_USDT_text[ 0 ].animate.next_to(both_arrow, L, buff=1),
                  BTC_none_USDT_text[ 1 ].animate.next_to(both_arrow, R, buff=1),
                  Create(both_arrow),
                  run_time=4.72)

        # TODO 8.734 secs우린 이걸 각각 비티씨를 매수한다, 매도한다라고 부릅니다. 비티씨 매수는 테더 매도와 같고, 테더 매수는 비티씨 매도와 같습니다
        # TODO 0:00:35.696  ~  0:00:44.430
        # TODO 1.0secs paus
        # TODO 0:00:44.430  ~  0:00:45.430

        buy_btc_sell_usdt_equal = Tex(r'BUY BTC = SELL USDT').scale(1.3)
        buy_btc_sell_usdt_equal.move_to(
            get_moved_coor_based_submob(buy_btc_sell_usdt_equal, buy_btc_sell_usdt_equal[ 0 ][ 6 ].get_center(),
                                        both_arrow.get_top() + U * 3)
        )
        buy_usdt_sell_btc_equal = Tex(r'SELL BTC = BUY USDT').scale(1.3)
        buy_usdt_sell_btc_equal.move_to(
            get_moved_coor_based_submob(buy_usdt_sell_btc_equal, buy_usdt_sell_btc_equal[ 0 ][ 7 ].get_center(),
                                        both_arrow.get_top() + U * 1.5)
        )
        # self.add(index_labels(buy_usdt_sell_btc_equal[ 0 ]))
        # self.add(index_labels(buy_btc_sell_usdt_equal[ 0 ]))
        buy_btc_sell_usdt_equal[ 0 ][ 0:3 ].set_color(GREEN)
        buy_btc_sell_usdt_equal[ 0 ][ 3:6 ].set_color(C_BTC)
        buy_btc_sell_usdt_equal[ 0 ][ 7:11 ].set_color(RED)
        buy_btc_sell_usdt_equal[ 0 ][ 11:15 ].set_color(C_USDT)
        buy_usdt_sell_btc_equal[ 0 ][ 0:4 ].set_color(RED)
        buy_usdt_sell_btc_equal[ 0 ][ 4:7 ].set_color(C_BTC)
        buy_usdt_sell_btc_equal[ 0 ][ 8:11 ].set_color(GREEN)
        buy_usdt_sell_btc_equal[ 0 ][ 11:15 ].set_color(C_USDT)

        self.play(AnimationGroup(Create(buy_btc_sell_usdt_equal),
                                 Create(buy_usdt_sell_btc_equal)
                                 ), run_time=4)

        self.wait(5.734)

        # TODO 8.106 secs거래 자체가 서로 다른 걸 교환하는 것이기에 내가 비트코인을 들고있는 쪽이 될지 테더를 들고있는 쪽이 될지는 마음대로 정할 수 있습니다
        # TODO 0:00:40.731  ~  0:00:48.837
        # TODO 1.0secs pause
        # TODO 0:00:48.837  ~  0:00:49.837

        BTC_COIN = create_circle_asset(Tex(r'\textbf{BTC}', color=WHITE, font_size=30), fill_color=C_BTC).shift(D * 2 + L * 2)
        USDT_COIN = create_circle_asset(Tex(r'\textbf{USDT}', color=WHITE, font_size=25), fill_color=C_USDT).shift(D * 2 + R * 2)
        swap_arrow_1 = CurvedArrow(start_point=BTC_COIN.get_corner(UR), end_point=USDT_COIN.get_corner(UL), radius=-5)
        swap_arrow_2 = CurvedArrow(start_point=USDT_COIN.get_corner(DL), end_point=BTC_COIN.get_corner(DR), radius=-5)

        self.play(Create(BTC_COIN),
                  Create(USDT_COIN),
                  Create(swap_arrow_1),
                  Create(swap_arrow_2), run_time=3)

        self.play(buy_btc_sell_usdt_equal[ 0 ][ 3:6 ].animate(rate_func=there_and_back_with_pause).scale(1.2),
                  buy_usdt_sell_btc_equal[ 0 ][ 4:7 ].animate(rate_func=there_and_back_with_pause).scale(1.2),
                  Flash(BTC_COIN, color=C_BTC,flash_radius=0.6,line_stroke_width=5),
                  run_time=1.5)
        self.wait(1)
        self.play(buy_usdt_sell_btc_equal[ 0 ][ 11:15 ].animate(rate_func=there_and_back_with_pause).scale(1.2),
                  buy_btc_sell_usdt_equal[ 0 ][ 11:15 ].animate(rate_func=there_and_back_with_pause).scale(1.2),
                  Flash(USDT_COIN, color=C_USDT,flash_radius=0.6,line_stroke_width=5),
                  run_time=1.5)
        self.wait(1.106)

        self.play(Uncreate(buy_btc_sell_usdt_equal),
                  Uncreate(buy_usdt_sell_btc_equal),
                  Uncreate(BTC_COIN),
                  Uncreate(USDT_COIN),
                  Uncreate(swap_arrow_1),
                  Uncreate(swap_arrow_2),
                  run_time=1)

        # TODO 20.912 secs일반적으로 거래쌍의 표기에 있어서는 가격이란 것이 원래 자산의 가치 변동을 표현하기 위한 것이므로 상대적으로 변동성이 큰 자산이 베이스 에셋이 되고
        #  그에 비해 더 안정적이고 유명한 자산이 가치의 척도가 되기에 용이해 쿼트 에셋으로는 상대적으로 변동성이 작은 스테이블 코인, 법정통화, 비티씨, 이더리움 등이 많이 사용됩니다
        # TODO 0:00:49.837  ~  0:01:10.749
        # TODO 1.0secs pause
        # TODO 0:01:10.749  ~  0:01:11.749

        more_volatile = Tex(r'More Volatile Asset\\Base Asset').scale(1.3).move_to([-4, 3.5,0])
        more_volatiles = Tex(r'Stock\\Bitcoin\\Ethereum\\Altcoins').shift(L*5.5+D*2)


        more_stable = Tex(r'More Stable Asset\\Quote Asset').scale(1.3).move_to([4, 3.5,0])
        more_stables = Tex(r'Stablecoin\\Fiat Currency\\Bitcoin\\Ethereum').shift(R*6+D*2)


        volatile_up_arrow = MathTex(r'\Longleftarrow').rotate(-PI/2).next_to(more_volatiles,U)
        volatile_down_arrow = MathTex(r'\Longleftarrow').rotate(PI/2).next_to(more_volatiles,D)
        stable_up_arrow = MathTex(r'\Leftarrow').rotate(-PI/2).next_to(more_stables,U)
        stable_down_arrow = MathTex(r'\Leftarrow').rotate(PI/2).next_to(more_stables,D)
        volatile_arrows= VGroup(volatile_up_arrow,volatile_down_arrow)
        stable_arrows= VGroup(stable_up_arrow,stable_down_arrow)



        self.play(Create(more_volatile))
        self.wait(2)
        self.play(Create(more_volatiles))
        self.wait(2)
        self.play(Create(volatile_arrows))
        self.wait(4)

        self.play(Create(more_stable))
        self.wait(2)
        self.play(Create(more_stables))
        self.wait(2)
        self.play(Create(stable_arrows))
        self.wait(3.912)

        # self.play(Create())

        # TODO 5.182 secs일반적인 주식 어플에서는 베이스 에셋과 쿼트 에셋을 생각해본 적이 없을 겁니다
        # TODO 0:00:26.976  ~  0:00:32.158
        # TODO 1.0secs pause
        # TODO 0:00:32.158  ~  0:00:33.158

        stock_app_rect = RoundedRectangle(width=5, height=4)
        stock_app_text = Tex('Stock App').scale(1.3).next_to(stock_app_rect, U)
        stock_app = VGroup(stock_app_rect, stock_app_text)

        self.play(ReplacementTransform(VGroup(BTC_none_USDT_text,
                                              both_arrow,
                                              expl_text_2,
                                              more_volatile,
                                              more_volatiles,
                                              volatile_arrows,
                                              more_stable,
                                              more_stables,
                                              stable_arrows,
                                              ), stock_app),
                  run_time=3)
        self.wait(3.182)

        # TODO 6.185 secs어차피 전부 쿼트에셋으로 원화만 사용하기 때문에 거래쌍이라는 개념보다는 주식쇼핑같은 느낌입니다
        # TODO 0:00:33.158  ~  0:00:39.343
        # TODO 1.0secs pause
        # TODO 0:00:39.343  ~  0:00:40.343
        krw = Tex(r'Only \textwon').scale(2).next_to(stock_app, D)

        self.play(Create(krw))
        self.wait(2)

        stock_app_buff = 0.4
        pair_text = Tex('Pair').next_to(stock_app[ 0 ].get_corner(UL), DR, buff=stock_app_buff)
        base_text = Tex('Base Asset').next_to(stock_app[ 0 ].get_right(), L, buff=stock_app_buff)
        quote_text = Tex('Quote Asset').next_to(stock_app[ 0 ].get_corner(DL), UR, buff=stock_app_buff)
        pair_text_cross = Cross().scale(0.4).move_to(pair_text)
        base_text_cross = Cross().scale(0.4).move_to(base_text)
        quote_text_cross = Cross().scale(0.4).move_to(quote_text)

        self.play(AnimationGroup(Create(pair_text),
                                 Create(base_text),
                                 Create(quote_text),
                                 lag_ratio=0.6),
                  run_time=2.185)

        pair_text.add(pair_text_cross)
        base_text.add(base_text_cross)
        quote_text.add(quote_text_cross)

        self.play(AnimationGroup(Create(pair_text_cross),
                                 Create(base_text_cross),
                                 Create(quote_text_cross),
                                 lag_ratio=0.6),
                  run_time=1)

        self.wait(1)

        # TODO 7.188 secs하지만 외환시장, 즉 FOREX를 겪어보신 분이면 달러 엔, 유로 달러등의 거래쌍을 보셨을 겁니다
        # TODO 0:00:40.343  ~  0:00:47.531
        # TODO 1.0secs pause
        # TODO 0:00:47.531  ~  0:00:48.531

        currencies = Tex(r'\textwon\  \textyen\  \textdollar\  \texteuro').scale(2).next_to(stock_app, D)

        forex_title = Tex('FOREX').scale(1.3).move_to(stock_app_text)
        self.play(ReplacementTransform(stock_app_text, forex_title))
        self.play(ReplacementTransform(krw, currencies))
        self.wait(1)

        forex_buff = 0.4
        usd_jpy_text = Tex('USD/JPY').next_to(stock_app[ 0 ].get_corner(UL), DR, buff=forex_buff)
        gbp_jpy_text = Tex('GBP/JPY').next_to(stock_app[ 0 ].get_right(), L, buff=forex_buff)
        eur_usd_text = Tex('EUR/USD').next_to(stock_app[ 0 ].get_corner(DL), UR, buff=forex_buff)

        self.play(AnimationGroup(ReplacementTransform(pair_text, usd_jpy_text),
                                 ReplacementTransform(base_text, gbp_jpy_text),
                                 ReplacementTransform(quote_text, eur_usd_text),
                                 lag_ratio=0.6),
                  run_time=3.188)

        self.wait(2)

        # TODO 10.413 secs크립토 마켓도 특정 코인을 사기위해서 비트코인이나 이더리움을 지불하는 경우도 많고,
        #  스테이블 코인만 해도 종류가 여러가지여서 거래쌍 개념이 더 절실히 다가옵니다
        # TODO 0:00:48.531  ~  0:00:58.944
        # TODO 1.0secs pause
        # TODO 0:00:58.944  ~  0:00:59.944

        ex_title = Tex('Crypto Exchange').move_to(stock_app_text)

        ETH_COIN = create_circle_asset(Tex(r'\textbf{ETH}', color=WHITE, font_size=30), fill_color=C_ETH)
        BTC_COIN = create_circle_asset(Tex(r'\textbf{BTC}', color=WHITE, font_size=30), fill_color=C_BTC)
        BNB_COIN = create_circle_asset(Tex(r'\textbf{BNB}', color=C_BNB2, font_size=30), fill_color=C_BNB1)

        self.play(ReplacementTransform(forex_title, ex_title))

        self.play(VGroup(ex_title,
                         stock_app_rect,
                         usd_jpy_text,
                         gbp_jpy_text,
                         eur_usd_text,
                         currencies).animate.to_edge(U))

        self.wait(1)

        cryptos = VGroup(BTC_COIN, ETH_COIN, BNB_COIN).arrange(R).scale(1.2).arrange(R).next_to(stock_app_rect, D)

        stable_coin = Tex('Stable Coin').next_to(cryptos, D)

        cryptos.add(stable_coin)
        self.play(ReplacementTransform(currencies, cryptos), run_time=3)

        left_stable = Tex('USDT', 'USDC', 'BUSD', 'DAI', 'TUSD').scale(1.5).arrange(D, buff=1).to_edge(L)
        left_stable[ 0 ].set_color(C_USDT)
        left_stable[ 1 ].set_color(C_USDC)
        left_stable[ 2 ].set_color(C_BNB2)
        left_stable[ 3 ].set_color('#FAB120')
        left_stable[ 4 ].set_color('#1A5AFF')
        right_stable = Tex('USDP', 'USDN', 'USTC', 'USDD', 'FRAX').scale(1.5).arrange(D, buff=1).to_edge(R)
        right_stable[ 0 ].set_color('#B5D334')
        right_stable[ 1 ].set_color('#00FEB5')
        right_stable[ 2 ].set_color('#216C58')
        right_stable[ 3 ].set_color('#576DC7')
        # right_stable[4].set_color('')

        stables = VGroup(left_stable, right_stable)
        self.wait(2)
        self.play(ReplacementTransform(stable_coin, stables), run_time=1)

        ex_buff = 0.4

        btc_usdt_text = Tex('BTC/USDT', substrings_to_isolate='/').next_to(stock_app[ 0 ].get_corner(UL), DR, buff=ex_buff)
        btc_usdt_text[ 0 ].set_color(C_BTC)
        btc_usdt_text[ 2 ].set_color(C_USDT)
        eth_btc_text = Tex('ETH/BTC', substrings_to_isolate='/').next_to(stock_app[ 0 ].get_right(), L, buff=ex_buff)
        eth_btc_text[ 0 ].set_color(C_ETH)
        eth_btc_text[ 2 ].set_color(C_BTC)

        sol_eth_text = Tex('SOL/ETH', substrings_to_isolate='/').next_to(stock_app[ 0 ].get_corner(DL), UR, buff=ex_buff)
        sol_eth_text[ 0 ].set_color(C_SOL1)
        sol_eth_text[ 2 ].set_color(C_ETH)

        self.play(AnimationGroup(ReplacementTransform(usd_jpy_text, btc_usdt_text),
                                 ReplacementTransform(gbp_jpy_text, eth_btc_text),
                                 ReplacementTransform(eur_usd_text, sol_eth_text),
                                 lag_ratio=0.6),
                  run_time=2.413)

        # TODO 11.259 secs주식에서는 1 현대차가 3 삼성전자 이런 식으로 표현하지 않지만 크립토마켓에서는 1이더리움은 0.1비티씨, 1폴카닷은 0.01이더리움과 같은 표현이 많이 나옵니다
        # TODO 0:00:59.944  ~  0:01:11.203

        long_line = Tex(
            r"We don't say\\1 HYUNDAI MOTORS = 3 SAMSUNG ELECTROINCS\\but we sure say\\1 ETH = 0.1 BTC or 1 DOT = 0.01 ETH",
            substrings_to_isolate=[ 'HYUNDAI MOTORS', 'SAMSUNG ELECTROINCS', '1' ]).next_to(stock_app_rect, D, buff=0.7)

        # 교육 참고용 이해하기 쉽게 색깔 넣고 싶으면 주석해제
        # long_line[0].set_color(RED)
        # long_line[1].set_color(LIGHT_BROWN)
        # long_line[2].set_color(BLUE)
        # long_line[3].set_color(GREEN)
        # long_line[4].set_color(PURPLE)
        # self.add(index_labels(long_line))

        hyundai = SVGMobject('hyundai_logo.svg', fill_color='#3677AE').scale_to_fit_height(long_line[ 1 ].height).next_to(
            long_line[ 4 ].copy().move_to(np.array([ 0, long_line[ 4 ].get_y(), 0 ])), L)
        samsung = SVGMobject('samsung.svg', fill_color='#034A9A').scale_to_fit_height(long_line[ 1 ].height).next_to(
            long_line[ 4 ].copy().move_to(np.array([ 0, long_line[ 4 ].get_y(), 0 ])), R)

        samsung[ 1:8 ].set_fill(color=WHITE, opacity=1)

        self.play(ReplacementTransform(VGroup(stables, cryptos), long_line))
        self.wait(1.5)

        self.play(AnimationGroup(FadeOut(VGroup(long_line[ 3 ], long_line[ 5 ])),
                                 long_line[ 4 ].animate.move_to(np.array([ 0, long_line[ 4 ].get_y(), 0 ])),
                                 AnimationGroup(long_line[ 1 ].animate.next_to(hyundai, L),
                                                DrawBorderThenFill(hyundai),
                                                DrawBorderThenFill(samsung)), lag_ratio=0.3
                                 ))

        self.wait(5)

