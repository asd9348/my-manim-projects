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

class L01S02_bg_knowledge(MovingCameraScene):
    def construct(self):
        # self.add(NumberPlane().set_z_index(1))

        speak(self, title='Scene2', txt=
        '더 진행하기 전에 몇 가지 사전학습을 하고 가겠습니다#1'
        '차례대로 스테이블 코인, 주문, 가격, 슬리피지, 페어에 대해 알아보고 가겠습니다#1'

              , keep_pitch=True, update=0, speed=1.4)

        bg_knowledge = Tex(r'Background\\Knowledge').scale(2)
        stablecoin = Tex(r'Stablecoin').scale(1.5)
        order = Tex(r'Order').scale(1.5)
        price = Tex(r'Price').scale(1.5)
        slippage = Tex(r'Slippage').scale(1.5)
        pair = Tex(r'Pair').scale(1.5)
        topics = VGroup(stablecoin, order, price, slippage, pair).arrange(D,buff= 0.3)
        self.play(Create(bg_knowledge))
        self.wait(1.5)
        self.play(ReplacementTransform(bg_knowledge, topics))
        self.wait(0.5)

        self.play(ApplyWave(stablecoin),run_time=1.8)
        self.play(ApplyWave(order),run_time=0.6)
        self.play(ApplyWave(price),run_time=0.5)
        self.play(ApplyWave(slippage),run_time=0.8)
        self.play(ApplyWave(pair),run_time=0.6)
        self.wait(10)

class L01S03_flow(MovingCameraScene):
    def construct(self):
        # self.add(NumberPlane().set_z_index(1))

        speak(self, title='Scene2', txt=
        '중앙화 거래소가 어떻게 작동하는지 예를 보겠습니다. 우리가 관심있는 건 크립토니까 일반적인 크립토 거래소를 기준으로 설명하겠습니다#1'

        '에이는 비트코인을 가지고 있습니다#1'
        '비는 현금을 가지고 있습니다#1'
        '에이는 비트코인을 현금으로 바꾸고 싶고, 비는 현금으로 비트코인을 구매하고 싶습니다#1'

        '그리하여 에이와 비는 거래소로 자신의 자산인 비트코인과 현금을 각각 입금합니다#1'
        '거래소는 현금을 받기위해 시중은행 계좌나 결제시스템을 통하고 입금을 확인한 뒤 자신의 데이터베이스에 기록합니다#1'
        '거래소 데이터베이스에 비의 현금 보유액이 업데이트 됐습니다#1'
        '그리고 비트코인을 입금받기 위해서는 에이에게서 비트코인을 받기위한 주소를 에이에게 알려주고 에이가 그 주소로 비트코인을 전송하면 확인한 뒤 거래소의 데이터베이스에 기록합니다#1'
        '거래소 데이터 베이스에 에이의 비트코인 보유액이 업데이트 됐습니다#1'
        '참고로 지갑은 A의 지갑이지만 실제로 이 지갑은 거래소의 하위지갑입니다#1'  #####################################
        '그래서 A는 거래소의 허락없이는 마음대로 다시 코인을 뺄 수 없습니다#1'

        '거래소 앱에서 자신의 재산을 확인한 에이와 비는 이제 거래할 준비가 됐습니다. 이제 둘은 페어로 갑니다#1'

        '이제 실제 에이비가 주문을 넣는것으로 더 자세히 알아보겠습니다#1'
        '에이는 비트코인을 비싸게 팔고 싶어하고, 비는 비트코인을 싸게 사고 싶어합니다#1'
        '현재 거래쌍에 보이는 가격은 100달러이지만 호가창이 그냥 텅 비어있고 실제 시장참여자는 에이와 비만 있다고 가정하겠습니다#1'
        '그래서 에이는 비트코인을 110달러에 판매하는 매도 지정가주문을 넣고 삐는 90달러에 매수 주문을 넣습니다#1'
        '그러나 가격이 지정가까지 올 생각을 안 하자 둘은 현재가에 더 가깝게 주문을 수정해 에이는 103테더에 매도, 비는 97테더에 매수 주문을 넣습니다#1'
        '여전히 가격 안 움직이고 비트코인을 너무 팔고 싶었던 에이는 시장가 주문을 하면서 비에게 비트코인을 판매합니다#1'
        '기분이 좋아진 비는 어디서 들었는지 개인지갑에 비트코인을 보관해야된다는 애기가 기억나 비트코인 지갑 어플을 받아 개인지갑을 만들고 거래소에 그 주소로 출금을 요청합니다#1'
        '거래소는 비의 요청을 확인하고 거래소의 지갑에서 블록체인상으로 비의 요청 주소로 비트코인을 전송하고 거래소 데이터베이스에서 비의 비트코인 보유액을 차감합니다#1'
        '에이는 비트코인을 팔아 마련한 달러로 테슬라를 사기위해 출금을 하려합니다#1'
        '마찬가지로 거래소에 출금을 요청하고 거래소는 에이가 등록한 은행 계좌로 달러를 송금하고 은행 데이터베이스는 새로 업데이트 됩니다. 에이는 이제 은행에서 현금을 출금합니다#1'

              , keep_pitch=True, update=0, speed=1.4)

        # TODO 8.444 secs중앙화 거래소가 어떻게 작동하는지 예를 보겠습니다.
        #  우리가 관심있는 건 크립토니까 일반적인 크립토 거래소를 기준으로 설명하겠습니다
        # TODO 0:00:00.000  ~  0:00:08.444
        # TODO 1.0secs pause
        # TODO 0:00:08.444  ~  0:00:09.444

        cent_ex_text = Tex('Centralized Exchange').scale(2)
        crypto_text = Tex('Crypto').scale(2)

        self.play(Create(cent_ex_text))
        self.wait(3)

        self.play(cent_ex_text.animate.shift(D * 0.5))
        crypto_text.next_to(cent_ex_text, U)
        self.play(Create(crypto_text))

        self.wait(2)
        self.play(Unwrite(VGroup(crypto_text, cent_ex_text)), run_time=1)
        self.wait(0.444)

        # TODO 2.127 secs에이는 비트코인을 가지고 있습니다
        # TODO 0:00:09.444  ~  0:00:11.571
        # TODO 1.0secs pause
        # TODO 0:00:11.571  ~  0:00:12.571
        A = create_entity("A", 0.5, WHITE, "1 BTC", C_BTC, 0.7, 0.3, asset_text_color=WHITE).shift(RIGHT * 4 + UP * 1)
        self.play(Create(A), run_time=2)
        self.wait(1.127)

        # TODO 1.861 secs비는 현금을 가지고 있습니다
        # TODO 0:00:12.571  ~  0:00:14.432
        # TODO 1.0secs pause
        # TODO 0:00:14.432  ~  0:00:15.432

        B = create_entity("B", 0.5, WHITE, "100 $", C1275, 0.7, 0.3, asset_text_color=WHITE).shift(RIGHT * 4 + DOWN * 1)
        self.play(Create(B), run_time=1)
        self.wait(1.861)

        A_asset_btc = A[ 1 ]
        B_asset_usd = B[ 1 ]

        A_asset_btc.set_z_index(3)
        B_asset_usd.set_z_index(3)

        A_asset_pos = A_asset_btc.get_center()
        B_asset_pos = B_asset_usd.get_center()

        # TODO 5.605 secs에이는 비트코인을 현금으로 바꾸고 싶고, 비는 현금으로 비트코인을 구매하고 싶습니다
        # TODO 0:00:15.432  ~  0:00:21.037
        # TODO 1.0secs pause
        # TODO 0:00:21.037  ~  0:00:22.037

        A_spch = Tex("I want USD").next_to(A, LEFT)
        B_spch = Tex("I want BTC").next_to(B, LEFT)

        self.play(AnimationGroup(Write(A_spch),
                                 Write(B_spch),
                                 lag_ratio=1,
                                 run_time=2))

        self.wait(2.605)

        self.play(AnimationGroup(Unwrite(A_spch),
                                 Unwrite(B_spch),
                                 lag_ratio=1,
                                 run_time=2))

        # TODO 5.352 secs그리하여 에이와 비는 거래소로 자신의 자산인 비트코인과 현금을 각각 입금합니다
        # TODO 0:00:22.037  ~  0:00:27.389
        # TODO 1.0secs pause
        # TODO 0:00:27.389  ~  0:00:28.389

        ex_rect = RoundedRectangle(corner_radius=0.5, height=8, width=6)
        ex_rect_text = Tex("Exchange").next_to(ex_rect, UP, buff=0.2).scale(0.8)
        ex = VGroup(ex_rect, ex_rect_text).move_to(ORIGIN).to_edge(LEFT)

        ex_server_rect = RoundedRectangle(width=1.2, height=0.5, corner_radius=0.1)
        ex_server_led_1 = Dot(radius=0.05, fill_color=GREEN).shift(RIGHT * 0.2)
        ex_server_led_2 = Dot(radius=0.05, fill_color=GREEN).shift(RIGHT * 0.4)

        ex_server = VGroup(ex_server_rect, ex_server_led_1, ex_server_led_2).next_to(ex_rect, UP, aligned_edge=UP, buff=-0.5).shift(
            LEFT * 1.5)

        self.play(Create(ex), run_time=0.5)

        self.play(Create(ex_server), run_time=0.5)

        ex_ledger = MathTable(
            [ [ "Ex", r"a " ],
              [ "A", r"aaaaaa " ],
              [ "B", r"a " ] ],
            include_outer_lines=True).scale(0.4).next_to(ex_server, RIGHT).align_to(ex_server, UP).shift(RIGHT)

        ex_ledger[ 0 ][ 5 ].set_color(BLACK)
        ex_ledger[ 0 ][ 1 ].set_color(BLACK)
        ex_ledger[ 0 ][ 3 ].set_color(BLACK)
        ex_ex_ledger = ex_ledger[ 0 ][ 1 ]
        A_ex_ledger = ex_ledger[ 0 ][ 3 ]
        B_ex_ledger = ex_ledger[ 0 ][ 5 ]

        self.play(Create(ex_ledger), run_time=0.5)

        A_wallet_rect = RoundedRectangle(0.1, width=1, height=1)
        A_wallet_text = Tex(r"A wallet").next_to(A_wallet_rect, UP, buff=0.2).scale(0.6)
        A_wallet = VGroup(A_wallet_rect, A_wallet_text)

        B_wallet_rect = RoundedRectangle(0.1, width=1, height=1)
        B_wallet_text = Tex("B wallet").next_to(B_wallet_rect, UP, buff=0.2).scale(0.6)
        B_wallet = VGroup(B_wallet_rect, B_wallet_text)

        ex_wallet_rect = RoundedRectangle(0.1, width=1, height=1)
        ex_wallet_text = Tex("Ex wallet").next_to(ex_wallet_rect, UP, buff=0.2).scale(0.6)
        ex_wallet = VGroup(ex_wallet_rect, ex_wallet_text)

        wallets = VGroup(ex_wallet, A_wallet, B_wallet).arrange(DOWN).next_to(ex_rect, RIGHT, aligned_edge=RIGHT, buff=-1).shift(DOWN)

        self.play(Create(wallets), run_time=0.5)

        # wallet_expl = Text("Wallet means a group of wallets and bank account. it is better to say it is an account")

        bank_rect = RoundedRectangle(corner_radius=0.2, height=1.8, width=4)
        bank_rect_text = Tex("Bank").next_to(bank_rect, UP, buff=0.1).scale(0.8)
        bank_server = ex_server.copy().next_to(bank_rect, UP, aligned_edge=UP, buff=-0.5).shift(LEFT)
        bank = VGroup(bank_rect, bank_rect_text, bank_server).to_edge(UP).shift(RIGHT)

        # B_bank_bal_tracker = ValueTracker(0)

        bank_ledger = MathTable(
            [ [ "Ex", r"a " ],
              [ "A", r"aaaaaa " ],
              [ "B", r"a " ] ],
            include_outer_lines=True).scale(0.4).next_to(bank_server, RIGHT).align_to(bank_server, UP)

        bank_ledger[ 0 ][ 5 ].set_color(BLACK)
        bank_ledger[ 0 ][ 1 ].set_color(BLACK)
        bank_ledger[ 0 ][ 3 ].set_color(BLACK)

        ex_bank_ledger = bank_ledger[ 0 ][ 1 ]
        A_bank_ledger = bank_ledger[ 0 ][ 3 ]
        B_bank_ledger = bank_ledger[ 0 ][ 5 ]

        # self.play(B_bank_bal_tracker.animate.set_value(35))

        self.play(Create(bank), run_time=0.5)
        self.play(Create(bank_ledger), run_time=0.5)

        self.wait(3.352)

        # TODO 7.345 secs거래소는 현금을 받기위해 시중은행 계좌나 결제시스템을 통하고 입금을 확인한 뒤 자신의 데이터베이스에 기록합니다
        # TODO 0:00:28.389  ~  0:00:35.734
        # TODO 1.0secs pause
        # TODO 0:00:35.734  ~  0:00:36.734

        B_100usd_bank = create_entity("B", 0.5, GRAY, "100 $", WHITE, 0.7, 0.3)[ 1 ].move_to(B_bank_ledger)
        B_100usd_ex = create_entity("B", 0.5, WHITE, "100 $", WHITE, 0.7, 0.3)[ 1 ].move_to(B_ex_ledger)

        self.play(B_asset_usd.animate.next_to(bank_server, DOWN), run_time=1.5)
        self.wait(1)
        self.play(FadeIn(B_100usd_bank, target_position=bank_server, scale=0.2), run_time=1.5)
        self.wait(1)
        self.play(B_100usd_bank.animate.move_to(ex_bank_ledger), run_time=1.5)
        self.play(FadeIn(B_100usd_ex, target_position=ex_server, scale=0.2), run_time=1.5)

        self.wait(0.345)

        # TODO 3.806 secs거래소 데이터베이스에 비의 현금 보유액이 업데이트 됐습니다
        # TODO 0:00:36.734  ~  0:00:40.540
        # TODO 1.0secs pause
        # TODO 0:00:40.540  ~  0:00:41.540

        self.play(B_100usd_ex.animate.move_to(B_ex_ledger), run_time=3)
        self.wait(1.806)

        # TODO 10.679 secs그리고 비트코인을 입금받기 위해서는 에이에게서 비트코인을 받기위한 주소를 에이에게 알려주고 에이가 그 주소로 비트코인을 전송하면 확인한 뒤 거래소의 데이터베이스에 기록합니다

        # TODO 0:00:41.540  ~  0:00:52.219

        # TODO 1.0secs pause

        # TODO 0:00:52.219  ~  0:00:53.219

        btc_addr = Tex(r'BTC Address\\n2kQ5L2rdc5rspJvU\\VrN28fejZYhqakFPx').scale(0.7).move_to(ex_rect).shift(L * 0.6)
        self.play(Create(btc_addr), run_time=2.5)
        self.wait(1)

        self.play(FadeOut(btc_addr, target_position=A[ 0 ]), run_time=2)
        self.wait(1)

        chain_elipse = RoundedRectangle(height=0.2, width=0.4, corner_radius=0.1)
        chain_line = Line(ORIGIN, L * 0.4)
        chain = VGroup()
        for i in range(1):
            chain.add(chain_line.copy())
            chain.add(chain_elipse.copy())
        chain.add(chain_line.copy())
        chain.arrange(R, buff=-0.12).rotate(PI / 2)

        blocks = VGroup()
        for i in range(5):
            blocks.add(Square(1.2, fill_color=BLACK, fill_opacity=1, stroke_color=WHITE))

        blocks.arrange(D, buff=chain.height).to_edge(R)

        block_nums = VGroup()

        for i in range(len(blocks)):
            block_nums.add(Tex(f"{format(i, '04b')}").move_to(blocks[ i ]).scale(0.6))

        blockchain = VGroup()

        for i in range(len(blocks)):
            blockchain.add(blocks[ i ])
            blockchain.add(block_nums[ i ])
            blockchain.add(chain.copy().next_to(blocks[ i ], D, buff=0))

        # blockchain_bar = DashedLine(start=blocks[ 0 ].get_top(), end=blocks[ 9 ].get_bottom(), dash_length=0.4, dashed_ratio=0.6,
        #                             stroke_color=WHITE).shift(LEFT)
        self.play(Create(blockchain),
                  run_time=1)
        self.wait(0.4)

        self.play(A_asset_btc.animate.move_to(blocks[ 2 ]),
                  run_time=1.5)
        self.wait(0.5)

        self.play(A_asset_btc.animate.move_to(A_wallet_rect),
                  run_time=1.279)
        self.wait(0.5)

        # TODO 4.144 secs거래소 데이터 베이스에 에이의 비트코인 보유액이 업데이트 됐습니다
        # TODO 0:00:54.440  ~  0:00:58.584
        # TODO 1.0secs pause
        # TODO 0:00:58.584  ~  0:00:59.584

        A_1btc_ex = create_entity("B", 0.5, WHITE, "1 BTC", WHITE, 0.7, 0.3)[ 1 ].move_to(A_ex_ledger)
        self.play(FadeIn(A_1btc_ex, target_position=ex_server, scale=0.2),
                  run_time=3)
        self.wait(2.144)

        # TODO 4.82 secs참고로 지갑은 A의 지갑이지만 실제로 이 지갑은 거래소의 하위지갑입니다
        # TODO 0:00:58.363  ~  0:01:03.183
        # TODO 1.0secs pause
        # TODO 0:01:03.183  ~  0:01:04.183
        AB_wallet = VGroup(A_wallet, B_wallet)

        ex_wallet_rect_incl = RoundedRectangle(0.1, width=1.3, height=4).move_to(AB_wallet)

        self.play(Transform(ex_wallet_rect, ex_wallet_rect_incl),
                  ex_wallet_text.animate.next_to(ex_wallet_rect_incl, UP, buff=0.1),
                  run_time=2)

        self.play(VGroup(wallets, A_asset_btc).animate.shift(UP * 0.8),
                  run_time=2)
        self.wait(1.82)

        # TODO 4.421 secs그래서 A는 거래소의 허락없이는 마음대로 다시 코인을 뺄 수 없습니다
        # TODO 0:01:05.067  ~  0:01:09.488
        # TODO 1.0secs pause
        # TODO 0:01:09.488  ~  0:01:10.488

        A_withdrawal_spch = Tex('I want my BTC back!').scale(0.7).next_to(A[ 0 ], LEFT)
        self.play(Create(A_withdrawal_spch))

        self.play(A_asset_btc.animate(rate_func=there_and_back_with_pause, run_time=2).move_to(
            get_halfway(A[ 0 ].get_center(), A[ 1 ].get_center())))

        A_emotion = Tex(':(').rotate(-PI / 2).scale(2).next_to(A[ 0 ], LEFT)

        self.play(ReplacementTransform(A_withdrawal_spch, A_emotion), run_time=0.5)
        self.wait(0.921)
        self.play(Uncreate(A_emotion))

        # TODO 6.331 secs거래소 앱에서 자신의 재산을 확인한 에이와 비는 이제 거래할 준비가 됐습니다. 이제 둘은 페어로 갑니다

        # TODO 0:01:09.604  ~  0:01:15.935

        # TODO 1.0secs pause

        # TODO 0:01:15.935  ~  0:01:16.935

        # market_rect = RoundedRectangle(corner_radius=0.5, height=ex_rect.height - bank_rect.height - 1.5, width=bank_rect.width)
        # market_rect_text = Tex("Market").next_to(market_rect, UP, buff=0.2).scale(0.8)
        # market = VGroup(market_rect, market_rect_text).align_to(bank_rect, R).align_to(ex_rect, D)
        #
        # self.play(Create(market),
        #           run_time=2)
        #
        # A[ 0 ].save_state()
        # B[ 0 ].save_state()
        # self.play(VGroup(A[ 0 ], B[ 0 ]).animate().arrange(R, buff=0.7).move_to(market_rect),
        #           run_time=2)
        # self.wait(1.397)
        # self.play(A[ 0 ].animate.restore(),
        #           B[ 0 ].animate.restore(), run_time=1.243)
        # self.wait(2)

        pair_rect = RoundedRectangle(corner_radius=0.1, height=ex_wallet_rect.height, width=3)
        pair_rect_text_1 = Tex("BTC/USD").scale(0.5).next_to(pair_rect, UP, buff=0.1)
        pair = VGroup(pair_rect, pair_rect_text_1).next_to(ex_rect, LEFT, aligned_edge=LEFT, buff=-2).align_to(ex_wallet_rect, DOWN)

        # self.play(Create(pair, run_time=q))

        self.play(
            Create(pair),
            run_time=3)

        pair_rect_text_2 = Tex("BTC/USD Pair").scale(0.5).move_to(pair_rect_text_1)

        self.play(ReplacementTransform(pair_rect_text_1, pair_rect_text_2),
                  run_time=1.426)
        self.wait(2.905)

        # TODO 3.95 secs이제 실제 에이비가 주문을 넣는것으로 더 자세히 알아보겠습니다
        # TODO 0:01:16.935  ~  0:01:20.885
        # TODO 1.0secs pause
        # TODO 0:01:20.885  ~  0:01:21.885
        def create_personal_order_only(self, entity, place_or_cancel, buy_or_sell, px, qty, asset):
            target_pos = ex_server
            start_from = entity

            order_paper = Rectangle(height=1.5, width=1.2)
            order_text_1 = Tex(f"{place_or_cancel}").scale(0.4)
            order_text_2 = Tex(rf"{buy_or_sell} ").scale(0.4)
            order_text_3 = Tex(rf"{qty} {asset}").scale(0.4)
            order_text_4 = Tex(rf"at {px}\$").scale(0.4)
            order_text = VGroup(order_text_1, order_text_2, order_text_3, order_text_4).arrange(DOWN, buff=0.1).move_to(
                order_paper)
            order = VGroup(order_paper, order_text).scale(0.7).next_to(start_from[ 0 ], LEFT)

            # self.play(Create(order))
            # self.wait(q)
            return order

        init_sell_order = create_personal_order_only(self, A, "Place", 'SELL', r'110\$', 1, 'BTC')
        init_buy_order = create_personal_order_only(self, B, "Place", 'BUY', r'90\$', 1, 'BTC')

        self.play(Create(init_sell_order),
                  run_time=1.5)
        self.play(Create(init_buy_order),
                  run_time=1.5)

        self.wait(1.95)
        # TODO 5.158 secs에이는 비트코인을 비싸게 팔고 싶어하고, 비는 비트코인을 싸게 사고 싶어합니다
        # TODO 0:01:21.885  ~  0:01:27.043
        # TODO 1.0secs pause
        # TODO 0:01:27.043  ~  0:01:28.043

        sell_at_higher = Tex('Sell BTC for more dollars').scale(0.6).next_to(init_sell_order, DL).align_to(init_sell_order, R)
        buy_at_lower = Tex('Buy BTC with less dollars').scale(0.6).next_to(init_buy_order, DL).align_to(init_buy_order, R)

        self.play(Write(sell_at_higher),
                  run_time=1)
        self.play(Write(buy_at_lower),
                  run_time=1)
        self.wait(3)
        self.play(FadeOut(VGroup(sell_at_higher, buy_at_lower)),
                  run_time=1.158)

        # TODO 7.792 secs현재 거래쌍에 보이는 가격은 100달러이지만 호가창이 그냥 텅 비어있고 실제 시장참여자는 에이와 비만 있다고 가정하겠습니다
        # TODO 0:01:28.043  ~  0:01:35.835
        # TODO 1.0secs pause
        # TODO 0:01:35.835  ~  0:01:36.835

        curr_px = Integer(100, unit=r'\$')
        self.play(Create(curr_px.move_to(pair_rect)),
                  run_time=2)

        self.wait(2)
        self.play(Flash(A[ 0 ], flash_radius=0.5))
        self.play(Flash(B[ 0 ], flash_radius=0.5))
        self.wait(2.792)

        # TODO 6.935 secs그래서 에이는 비트코인을 110달러에 판매하는 매도 지정가주문을 넣고 삐는 90달러에 매수 주문을 넣습니다
        # TODO 0:01:36.835  ~  0:01:43.770
        # TODO 1.0secs pause
        # TODO 0:01:43.770  ~  0:01:44.770

        def create_personal_order(self, entity, place_or_cancel, buy_or_sell, px, qty, asset):
            target_pos = ex_server
            start_from = entity

            order_paper = Rectangle(height=1.5, width=1.2)
            order_text_1 = Tex(f"{place_or_cancel}").scale(0.4)
            order_text_2 = Tex(rf"{buy_or_sell} ").scale(0.4)
            order_text_3 = Tex(rf"{qty} {asset}").scale(0.4)
            order_text_4 = Tex(rf"at {px}\$").scale(0.4)
            order_text = VGroup(order_text_1, order_text_2, order_text_3, order_text_4).arrange(DOWN, buff=0.1).move_to(
                order_paper)
            order = VGroup(order_paper, order_text).scale(0.7).next_to(start_from[ 0 ], LEFT)

            self.play(Create(order))
            self.wait(q)
            return FadeOut(order, target_position=target_pos)
            # change_waiting_order(self, target_pos, 3, 2, 1300, 1)

        self.wait(1)
        self.play(FadeOut(init_sell_order, target_position=ex_server),
                  run_time=1)

        self.wait(2)
        self.play(FadeOut(init_buy_order, target_position=ex_server),
                  run_time=1)

        self.wait(1)
        ask_val_track = ValueTracker(110)
        bid_val_track = ValueTracker(90)

        dummy = VGroup(A_1btc_ex, B_100usd_ex).copy().arrange(DOWN, buff=2).move_to(pair_rect).shift(LEFT * 0.5)
        dummy_usd_pos = dummy[ 1 ].get_center()
        dummy_btc_pos = dummy[ 0 ].get_center()
        ask = Tex(rf'SELL at {int(ask_val_track.get_value())}\$').scale(0.4).next_to(A_1btc_ex, RIGHT).set_color(RED)
        bid = Tex(rf'BUY at {int(bid_val_track.get_value())}\$').scale(0.4).next_to(dummy[ 1 ], RIGHT).set_color(GREEN)

        B_10usd_ex = create_entity("B", 0.5, WHITE, "10 $", WHITE, 0.7, 0.3)[ 1 ].move_to(B_ex_ledger)
        B_90usd_ex = create_entity("B", 0.5, WHITE, "90 $", WHITE, 0.7, 0.3)[ 1 ].next_to(B_ex_ledger, D, buff=0.5)
        B_3usd_ex = create_entity("B", 0.5, WHITE, "3 $", WHITE, 0.7, 0.3)[ 1 ].move_to(B_ex_ledger)
        B_97usd_ex = create_entity("B", 0.5, WHITE, "97 $", WHITE, 0.7, 0.3)[ 1 ].move_to(dummy_usd_pos)

        # self.play(VGroup(A_1btc_ex, B_100usd_ex).animate.arrange(DOWN, buff=2).move_to(pair_rect).shift(LEFT * 0.5),
        #           )
        self.play(ReplacementTransform(B_100usd_ex, B_10usd_ex),
                  FadeIn(B_90usd_ex, target_position=B_100usd_ex),
                  run_time=0.5)

        self.play(A_1btc_ex.animate.move_to(dummy_btc_pos),
                  B_90usd_ex.animate.move_to(dummy_usd_pos),
                  run_time=0.5)
        self.play(FadeIn(VGroup(ask, bid)),
                  run_time=1.935, rate_func=smooth)

        ask.add_updater(
            lambda ask: ask.become(Tex(rf'SELL at {int(ask_val_track.get_value())}\$').scale(0.4).set_color(RED).next_to(A_1btc_ex, RIGHT)))
        bid.add_updater(lambda bid: bid.become(
            Tex(rf'BUY at {int(bid_val_track.get_value())}\$').scale(0.4).set_color(GREEN).next_to(dummy[ 1 ], RIGHT)))
        # TODO 9.628 secs그러나 가격이 지정가까지 올 생각을 안 하자 둘은 현재가에 더 가깝게 주문을 수정해 에이는 103테더에 매도, 비는 97테더에 매수 주문을 넣습니다
        # TODO 0:01:44.770  ~  0:01:54.398
        # TODO 1.0secs pause
        # TODO 0:01:54.398  ~  0:01:55.398

        self.play(create_personal_order(self, A, "Cancel", 'SELL', r'110\$', 1, 'BTC'),
                  create_personal_order(self, B, "Cancel", 'BUY', r'90\$', 1, 'BTC'))
        self.play(create_personal_order(self, A, "Place", 'SELL', r'103\$', 1, 'BTC'),
                  create_personal_order(self, B, "Place", 'BUY', r'97\$', 1, 'BTC'))

        self.play(ReplacementTransform(B_10usd_ex, B_3usd_ex),
                  ReplacementTransform(B_90usd_ex, B_97usd_ex)
                  )

        self.play(ask_val_track.animate.set_value(103),
                  bid_val_track.animate.set_value(97), rate_func=linear)

        # self.play(create_personal_order(self, A, "Cancel", 'SELL', r'103\$', 1, 'BTC'),
        #           create_personal_order(self, B, "Cancel", 'BUY', r'97\$', 1, 'BTC'))
        # self.play(create_personal_order(self, A, "Place", 'SELL', r'101\$', 1, 'BTC'),
        #           create_personal_order(self, B, "Place", 'BUY', r'100\$', 1, 'BTC'))

        # self.play(ask_val_track.animate.set_value(97), rate_func=linear)

        # ask.clear_updaters()
        # bid.clear_updaters()

        # self.play(Unwrite(VGroup(ask),VGroup(bid)))
        # TODO 7.079 secs여전히 가격 안 움직이고 비트코인을 너무 팔고 싶었던 에이는 시장가 주문을 하면서 비에게 비트코인을 판매합니다
        # TODO 0:01:55.398  ~  0:02:02.477
        # TODO 1.0secs pause
        # TODO 0:02:02.477  ~  0:02:03.477
        self.play(create_personal_order(self, A, "Cancel", 'SELL', r'103\$', 1, 'BTC'), run_time=1)
        self.play(create_personal_order(self, A, "Place", 'SELL', r'97\$', 1, 'BTC'), run_time=1)

        curr_px_2 = Integer(97, unit=r'\$').move_to(pair_rect)

        self.wait(1.579)
        self.play(CyclicReplace(VGroup(A_1btc_ex), VGroup(B_97usd_ex)),
                  Transform(curr_px, curr_px_2),
                  Unwrite(ask),
                  Unwrite(bid),
                  run_time=2
                  )
        self.play(B_3usd_ex.animate.scale_to_fit_width(0.35).shift(L * (0.35 / 2 + 0.05)),
                  run_time=1)
        self.play(A_1btc_ex.animate.scale_to_fit_width(0.35).next_to(B_3usd_ex, R, buff=0.1),
                  B_97usd_ex.animate.move_to(A_ex_ledger),
                  run_time=1.5
                  )
        # TODO 10.692 secs기분이 좋아진 비는 어디서 들었는지 개인지갑에 비트코인을 보관해야된다는 애기가 기억나 비트코인 지갑 어플을 받아 개인지갑을 만들고 거래소에 그 주소로 출금을 요청합니다
        # TODO 0:02:03.477  ~  0:02:14.169
        # TODO 1.0secs pause
        # TODO 0:02:14.169  ~  0:02:15.169

        B_line = manim.Text("Give my BTC").next_to(B[ 0 ], LEFT).scale(0.6)

        self.play(AnimationGroup(Write(B_line),
                                 lag_ratio=1, run_time=3))
        self.wait(5)
        self.play(AnimationGroup(Unwrite(B_line),
                                 lag_ratio=1, run_time=3))

        self.wait(0.698)
        # self.play(A_asset_btc.animate.move_to(blocks[ 2 ]))

        # self.play(A_asset_btc.animate.move_to(blocks[ 2 ]))

        ex_3usd_bank = create_entity("B", 0.5, WHITE, "3 $", WHITE, 0.7, 0.3)[ 1 ].move_to(ex_bank_ledger)
        A_97usd_bank = create_entity("B", 0.5, WHITE, "97 $", WHITE, 0.7, 0.3)[ 1 ].move_to(A_bank_ledger)
        ex_10usd_bank = create_entity("B", 0.5, WHITE, "10 $", WHITE, 0.7, 0.3)[ 1 ].move_to(B_ex_ledger)
        # TODO 10.088 secs거래소는 비의 요청을 확인하고 거래소의 지갑에서 블록체인상으로 비의 요청 주소로 비트코인을 전송하고 거래소 데이터베이스에서 비의 비트코인 보유액을 차감합니다
        # TODO 0:02:15.169  ~  0:02:25.257
        # TODO 1.0secs pause
        # TODO 0:02:25.257  ~  0:02:26.257

        bs_btc_addr = Tex(r"B's BTC Address\\mg9Jh463xCXLmsYCG\\LnBbsQYtdVxJt8y6T").scale(0.7).next_to(B[ 0 ], L, buff=0.5)
        self.play(Create(bs_btc_addr), run_time=1.5)
        self.play(FadeOut(bs_btc_addr, target_position=ex_server), run_time=2)
        # self.play(A_asset_btc.animate.move_to(ex_server),run_time=1.5)
        self.wait(1)
        self.play(A_asset_btc.animate.move_to(blocks[ 3 ]), run_time=2)
        self.play(A_asset_btc.animate.move_to(B_asset_pos), run_time=2)
        self.wait(1)
        self.play(Uncreate(A_1btc_ex), run_time=1.5)
        self.wait(0.588)

        # TODO 4.434 secs에이는 비트코인을 팔아 마련한 달러로 테슬라를 사기위해 출금을 하려합니다
        # TODO 0:02:26.257  ~  0:02:30.691
        # TODO 1.0secs pause
        # TODO 0:02:30.691  ~  0:02:31.691
        A_line = manim.Text("Give my USD").next_to(A[ 0 ], LEFT).scale(0.6)
        self.play(AnimationGroup(Write(A_line),
                                 lag_ratio=1, run_time=1.5))
        self.wait(2)
        self.play(AnimationGroup(Unwrite(A_line),
                                 lag_ratio=1, run_time=1))

        # self.play(B_100usd_bank.animate.move_to(A_bank_ledger))
        # self.play(Uncreate(B_100usd_ex))
        # self.play(Uncreate(B_100usd_bank))
        # self.play(B_asset_usd.animate.move_to(A_asset_pos))
        # self.play(A_asset_btc.animate.move_to(B_asset_pos))

        self.wait(0.934)

        # TODO 10.884 secs마찬가지로 거래소에 출금을 요청하고 거래소는 에이가 등록한 은행 계좌로 달러를 송금하고 은행 데이터베이스는 새로 업데이트 됩니다. 에이는 이제 은행에서 현금을 출금합니다

        # TODO 0:02:31.691  ~  0:02:42.575

        # TODO 1.0secs pause

        # TODO 0:02:42.575  ~  0:02:43.575

        self.wait(3)
        self.play(ReplacementTransform(B_100usd_bank, ex_3usd_bank),
                  FadeIn(A_97usd_bank, target_position=B_100usd_bank), run_time=1.5)

        cash_3 = create_entity("B", 0.5, WHITE, "3 $", C1275, 0.7, 0.3, asset_text_color=WHITE)[ 1 ].move_to(B_asset_usd)
        cash_97 = create_entity("B", 0.5, WHITE, "97 $", C1275, 0.7, 0.3, asset_text_color=WHITE)[ 1 ].next_to(B_asset_usd, D, buff=1)

        self.play(ReplacementTransform(B_asset_usd, cash_3),
                  FadeIn(cash_97, target_position=B_asset_usd), run_time=1.5)

        self.play(cash_97.animate.move_to(A_asset_pos),
                  FadeOut(A_97usd_bank), run_time=1.5)
        self.wait(4.691)

        self.wait(20)

class L01S04_stablecoin(MovingCameraScene):
    def construct(self):
        # self.add(NumberPlane().set_z_index(1))

        speak(self, title='L01S01', txt=
        '잠시 스테이블 코인에 대해서 알아보고 가겠습니다#1'
        '일반적으로 거래소에서 은행계좌가 연동됐다면 원화나 달러같은 법정통화를 사용하고 그렇지 못 하면, 보통 스테이블 코인을 사용하게 됩니다#1'
        '스테이블 코인은 일반적으로 은행을 통해 실제 코인을 보증할 법정통화를 보내면 스테이블 코인 회사에서 발행합니다#1'
        '이제 이 스테이블코인으로 해외 거래소나 탈중앙화 거래소를 마음대로 이용할 수 있습니다#1'
        '스테이블 코인과 달러는 1대 1로 교환될 수 있습니다#1'
        '이번에 큰 이슈가 된 테라나 코인을 담보로 스마트 컨트랙트로 발행되는 다이처럼 법정통화 없이도 스테이블 코인을 만들 수 있습니다#1'
        '그러나 이번 영상의 범위를 벗어나기 때문에 나중에 따로 알아보겠습니다#1'
        '가장 유명한 테더를 예로 들자면 1테더를 발행하기 위해서는 1달러를 담보로 맡겨야하고 테더사는 언제든 사람들에게 돈을 돌려줄 수 있게 지급준비율을 유지하며 받은 달러 일부를 활용해 투자수익을 얻습니다#1'
        '다시 1테더를 가져가면 1테더를 소각시키고 1달러를 돌려받을 수 있습니다#1'
        '이렇게 법정통화를 스테이블 코인으로 만들면 비트코인을 들고 있는 것처럼 변동성에도 노출이 안 되고 현금과 같은 가치를 지닌 자산을 어느나라 거래소든 지갑이든 국경을 자유롭게 이동할 수 있어 많이 사용합니다#1'
              , keep_pitch=True, update=0, speed=1.4)

        # TODO 3.08 secs잠시 스테이블 코인에 대해서 알아보고 가겠습니다
        # TODO 0:00:00.000  ~  0:00:03.080
        # TODO 1.0secs pause
        # TODO 0:00:03.080  ~  0:00:04.080

        stablecoin = Tex('Stablecoin').scale(2)

        self.play(Create(stablecoin))

        self.wait(2.08)
        self.play(Uncreate(stablecoin))

        # TODO 8.734 secs일반적으로 거래소에서 은행계좌가 연동됐다면 원화나 달러같은 법정통화를 사용하고 그렇지 못 하면, 보통 스테이블 코인을 사용하게 됩니다
        # TODO 0:00:04.080  ~  0:00:12.814
        # TODO 1.0secs pause
        # TODO 0:00:12.814  ~  0:00:13.814
        tether_company_rect = RoundedRectangle(height=3, width=4.5, corner_radius=0.5)
        tether_company_text = Tex('Stablecoin Company').next_to(tether_company_rect, UP).align_to(tether_company_rect, L)
        tether_company = VGroup(tether_company_rect, tether_company_text).to_edge(UL, buff=0.5)
        tether_company.set_z_index(1.5)

        investment_rect = RoundedRectangle(height=3, width=4.5, corner_radius=0.5)
        investment_text = Tex('Investment').next_to(investment_rect, UP).align_to(investment_rect, L)
        investment = VGroup(investment_rect, investment_text).to_edge(DL, buff=0.5)
        investment.set_z_index(1.5)

        exchange_rect = RoundedRectangle(height=3, width=4.5, corner_radius=0.5)
        exchange_text = Tex('Exchange').next_to(exchange_rect, UP).align_to(exchange_rect, L)
        exchange = VGroup(exchange_rect, exchange_text).next_to(investment, R, buff=0.5)
        exchange.set_z_index(1.5)

        bank_rect = RoundedRectangle(height=3, width=4.5, corner_radius=0.5)
        bank_text = Tex('Bank').next_to(bank_rect, UP).align_to(bank_rect, L)
        bank = VGroup(bank_rect, bank_text).next_to(tether_company, R, buff=0.5)
        bank.set_z_index(1.5)

        # self.add(index_labels(tether_company[0]))
        self.play(Create(VGroup(tether_company,
                                bank,
                                investment,
                                exchange)))

        def create_entity_tether(person_name, person_radius, person_color, asset_name, how_many, asset_color, asset_width, asset_height,
                                 asset_text_color=WHITE):
            person = LabeledDot(person_name, radius=person_radius, fill_opacity=1.0, color=person_color)

            box = Rectangle(width=asset_width, height=asset_height, fill_color=asset_color, stroke_color=asset_color, fill_opacity=1)
            text = manim.Text(asset_name, color=asset_text_color).scale(asset_height)

            asset = VGroup(box, text).next_to(person, DOWN, buff=0.1)
            assets = VGroup(asset)

            assets = VGroup(*[ asset.copy() for i in range(how_many) ])
            # for i in range(how_many):
            #     VGroup.add(asset.copy())

            assets.arrange(DOWN, buff=0.1).next_to(person, DOWN)

            return VGroup(person, assets)

        A = create_entity_tether("A", 0.5, WHITE, "USD", 20, '#9DC87B', 0.7, 0.3, asset_text_color='#2A5A25').shift(R * 5.5 + U * 3)
        A[ 1 ].arrange_in_grid(rows=4, cols=5, buff=0.1).next_to(A[ 0 ], D)
        self.play(Create(A))

        bank2ex_bridge_arc_1 = ArcBetweenPoints(O, D * 2, radius=-3, color=DARK_GRAY).move_to(get_halfway(bank_rect, exchange_rect)).shift(
            L * 0.5 + R * 1).set_z_index(2)
        bank2ex_bridge_arc_2 = ArcBetweenPoints(O, D * 2, radius=-3, color=DARK_GRAY).flip(axis=U).move_to(
            get_halfway(bank_rect, exchange_rect)).shift(R * 0.5 + R * 1).set_z_index(2)
        usdts_moved2ex = A[ 1 ].copy().move_to(exchange_rect)
        usdts_moved2bank = A[ 1 ].copy().move_to(bank_rect)
        bank2ex_bridge = VGroup(bank2ex_bridge_arc_1, bank2ex_bridge_arc_2)

        bank2ex_path = VMobject()

        A_usdts_list = reversed([ *A[ 1 ] ])
        # for name, age in zip(names, ages):
        #     print(name, age)

        # [ MoveAlongPath(A_usdts_list[ i ], VMobject().set_points_as_corners(
        #     [ usdt.get_center(), bank2ex_bridge.get_top(), bank2ex_bridge.get_bottom(), usdts_moved2bank[ index ].get_center ])) for
        #   usdt, index in zip(A_usdts_list, range(len(usdts_moved2bank))) ]

        # path_list = [ ]
        # for usdt, index in zip(A_usdts_list, range(len(usdts_moved2bank))):
        #     path_list.append(VMobject().set_points_as_corners(
        #         [ usdt.get_center(), bank2ex_bridge.get_top(), bank2ex_bridge.get_bottom(), usdts_moved2bank[ index ].get_center() ]))
        #
        #
        # self.play(Create(VGroup(*path_list)))
        # bank2ex_path.add_cubic_bezier_curve_to(np.array([ last_anchor[ 0 ] - 0.5, -1, 0 ]), np.array([ last_anchor[ 0 ] - 0.5,-1, 0 ]),
        #                                   last_anchor)
        # bank2ex_path.set_style(stroke_width=10, stroke_color=RED)

        self.play(Create(bank2ex_bridge_arc_1),
                  Create(bank2ex_bridge_arc_2))

        self.play(A[ 1 ].animate.move_to(bank_rect))
        # self.play(A[ 1 ].animate(rate_func = there_and_back_with_pause).move_to(exchange_rect))

        self.play(AnimationGroup(*[ MoveAlongPath(usdt, VMobject().set_points_as_corners(
            [ usdt.get_center(), bank2ex_bridge.get_top(), bank2ex_bridge.get_bottom(), usdts_moved2ex[ index ].get_center() ])) for
                                    usdt, index in zip(reversed([ *A[ 1 ] ]), range(len(usdts_moved2ex))) ]
                                 , lag_ratio=0.5), run_time=2)
        self.wait(2)
        self.play(AnimationGroup(*[ MoveAlongPath(usdt, VMobject().set_points_as_corners(
            [ usdt.get_center(), bank2ex_bridge.get_bottom(), bank2ex_bridge.get_top(), usdts_moved2bank[ index ].get_center() ])) for
                                    usdt, index in zip(list(A[ 1 ]), range(len(usdts_moved2bank))) ]
                                 , lag_ratio=0.5), run_time=2)

        self.wait(0.734)

        # [ usdt.animate. for usdt in A_usdts_list ]

        # A_usdts_list =list(A[1])

        # A_usdts_list  =[]
        # for i in range(len(A[1])):
        #     A_usdts_list.append()

        # TODO 7.079 secs스테이블 코인은 일반적으로 은행을 통해 실제 코인을 보증할 법정통화를 보내면 스테이블 코인 회사에서 발행합니다
        # TODO 0:00:13.814  ~  0:00:20.893
        # TODO 1.0secs pause
        # TODO 0:00:20.893  ~  0:00:21.893

        # bridge_arc_1 = ArcBetweenPoints(O, L*2.5)
        bridge_arc_1 = ArcBetweenPoints(O, L * 2, radius=-3, color=DARK_GRAY).move_to(get_halfway(tether_company_rect, bank_rect)).shift(
            U * 1).set_z_index(2)
        bridge_arc_2 = ArcBetweenPoints(O, L * 2, radius=-3, color=DARK_GRAY).flip(axis=L).move_to(
            get_halfway(tether_company_rect, bank_rect)).shift(D * 1).set_z_index(2)

        self.play(Create(bridge_arc_1),
                  Create(bridge_arc_2))
        # self.play(A[ 1 ].animate.move_to(bank_rect))
        self.play(A[ 1 ].animate.move_to(tether_company_rect))
        self.wait(1.079)

        usdts = create_entity_tether("A", 0.5, WHITE, "USDT", 20, C_USDT, 0.7, 0.3)[ 1 ]

        # tethers = VGroup([])
        # for i in range(len(tether_1ea)):
        #     tethers.add(tether_1ea[ i ])
        usdts.arrange_in_grid(4, 5, buff=0.1).move_to(A[ 1 ])

        self.play(Create(usdts))

        last_anchor = usdts.copy().next_to(A[ 0 ], D).get_center()
        my_line = VMobject()
        my_line.set_points_as_corners([ usdts.get_center(), [ usdts.get_x(), -1, 0 ], [ 2, -1, 0 ] ])
        my_line.add_cubic_bezier_curve_to(np.array([ last_anchor[ 0 ] - 0.5, -1, 0 ]), np.array([ last_anchor[ 0 ] - 0.5, -1, 0 ]),
                                          last_anchor)
        my_line.set_style(stroke_width=10, stroke_color=RED)
        # my_line.add_points_as_corners([ 2 * RIGHT + DOWN, 2 * RIGHT + 2 * DOWN ])

        # self.add(my_line)

        self.play(AnimationGroup(VGroup(exchange, investment).animate.shift(D * 2),
                                 AnimationGroup(FadeOut(bank2ex_bridge_arc_1), FadeOut(bank2ex_bridge_arc_2)),
                                 MoveAlongPath(usdts, path=my_line),
                                 lag_ratio=0.5,
                                 run_time=3
                                 )
                  )

        self.play(VGroup(exchange, investment).animate.shift(U * 2),
                  # AnimationGroup(FadeIn(bank2ex_bridge_arc_1), FadeIn(bank2ex_bridge_arc_2)),
                  )

        # TODO 5.014 secs이제 이 스테이블코인으로 해외 거래소나 탈중앙화 거래소를 마음대로 이용할 수 있습니다
        # TODO 0:00:21.893  ~  0:00:26.907
        # TODO 1.0secs pause
        # TODO 0:00:26.907  ~  0:00:27.907

        # self.play(usdts.animate.move_to(exchange_rect),run_time=2)
        # self.wait(4.014)

        # self.play(A[ 1 ].animate.move_to(bank_rect))
        # self.play(A[ 1 ].animate(rate_func = there_and_back_with_pause).move_to(exchange_rect))
        usdts_moved2ex = A[ 1 ].copy().move_to(exchange_rect)
        self.wait(1)
        self.play(AnimationGroup(*[ usdt.animate.move_to(usdts_moved2ex[ index ].get_center()) for
                                    usdt, index in zip([ *usdts[ 10: ] ], range(len(usdts_moved2ex))) ]
                                 , lag_ratio=0.5), run_time=2)

        profit_from_ex = Tex('Users earn Profit', font_size=40).next_to(usdts[ 17 ], D)
        self.wait(1.014)
        self.play(Create(profit_from_ex))
        self.wait(1)

        # TODO 3.383 secs스테이블 코인과 달러는 1대 1로 교환될 수 있습니다
        # TODO 0:00:21.893  ~  0:00:25.276
        # TODO 1.0secs pause
        # TODO 0:00:25.276  ~  0:00:26.276

        usd_1ea = create_entity_tether("A", 0.5, WHITE, "1 USD", 20, '#9DC87B', 1.2, 0.4, asset_text_color='#2A5A25')[ 1 ][ 0 ]
        usdt_1ea = create_entity_tether("A", 0.5, WHITE, "1 USDT", 20, C_USDT, 1.2, 0.4, asset_text_color=WHITE)[ 1 ][ 0 ]
        arrow = MathTex(r'\Leftrightarrow')
        # arrow = MathTex()

        usd_equals_usdt = VGroup(usd_1ea, arrow, usdt_1ea).arrange(R)
        usd_equals_usdt.move_to(get_moved_coor_based_submob(usd_equals_usdt, usd_equals_usdt.get_top(), [ 5.5, -1, 0 ]))

        self.play(Create(usd_equals_usdt), run_time=3)
        self.wait(1.383)

        # TODO 7.901 secs이번에 큰 이슈가 된 테라나 코인을 담보로 스마트 컨트랙트로 발행되는 다이처럼 법정통화 없이도 스테이블 코인을 만들 수 있습니다
        # TODO 0:00:26.276  ~  0:00:34.177
        # TODO 1.0secs pause
        # TODO 0:00:34.177  ~  0:00:35.177
        eth_1ea = create_entity_tether("A", 0.5, WHITE, "ETH", 20, C_ETH, 1.2, 0.4, asset_text_color=WHITE)[ 1 ][ 0 ]
        luna_1ea = create_entity_tether("A", 0.5, WHITE, "LUNC", 20, '#071C4B', 1.2, 0.4, asset_text_color='#FEE834')[ 1 ][ 0 ]
        dai_1ea = create_entity_tether("A", 0.5, WHITE, "DAI", 20, '#DFAF4B', 1.2, 0.4, asset_text_color=WHITE)[ 1 ][ 0 ]
        ustc_1ea = create_entity_tether("A", 0.5, WHITE, "USTC", 20, '#528EED', 1.2, 0.4, asset_text_color='#0B389B')[ 1 ][ 0 ]

        luna_equals_ustc = VGroup(luna_1ea, arrow.copy(), ustc_1ea).arrange(R).move_to([ 5, -2, 0 ]).next_to(usd_equals_usdt, D, buff=0.6)
        eth_equals_dai = VGroup(eth_1ea, arrow.copy(), dai_1ea).arrange(R).move_to([ 5, -2, 0 ]).next_to(luna_equals_ustc, D, buff=0.6)

        self.play(Create(luna_equals_ustc), run_time=2)
        self.play(Create(eth_equals_dai), run_time=2)

        self.wait(4.901)

        # self.play(ReplacementTransform(usd_1ea, colla_1ea))

        # other_stables_1eas = VGroup(dai_1ea,ustc_1ea).arrange(D).move_to(usdt_1ea)

        # self.play(ReplacementTransform(usdt_1ea,other_stables_1eas))

        # TODO 4.24 secs그러나 이번 영상의 범위를 벗어나기 때문에 나중에 따로 알아보겠습니다
        # TODO 0:00:35.177  ~  0:00:39.417
        # TODO 1.0secs pause
        # TODO 0:00:39.417  ~  0:00:40.417

        self.play(Uncreate(eth_equals_dai), run_time=1.5)
        self.play(Uncreate(luna_equals_ustc), run_time=1.5)
        self.wait(2.24)

        # self.play(Uncreate())

        # TODO 12.395 secs가장 유명한 테더를 예로 들자면 1테더를 발행하기 위해서는 1달러를 담보로 맡겨야하고 테더사는 언제든 사람들에게 돈을 돌려줄 수 있게 지급준비율을 유지하며 받은 달러 일부를 활용해 투자수익을 얻습니다

        # TODO 0:00:46.431  ~  0:00:58.826

        # TODO 1.0secs pause

        # TODO 0:00:58.826  ~  0:00:59.826

        self.play(Circumscribe(usd_equals_usdt), run_time=2)
        self.wait(4)

        # self.add(index_labels(A[1]))

        comp2inv_bridge_arc_1 = ArcBetweenPoints(O, D * 2, radius=-3, color=DARK_GRAY).move_to(
            get_halfway(tether_company_rect, investment_rect)).shift(
            L * 0.5 + R * 1).set_z_index(2)
        comp2inv_bridge_arc_2 = ArcBetweenPoints(O, D * 2, radius=-3, color=DARK_GRAY).flip(axis=U).move_to(
            get_halfway(tether_company_rect, investment_rect)).shift(R * 0.5 + R * 1).set_z_index(2)
        usdts_moved2inv = A[ 1 ].copy().move_to(investment_rect)
        usdts_moved2comp = A[ 1 ].copy().move_to(tether_company_rect)
        comp2inv_bridge = VGroup(comp2inv_bridge_arc_1, comp2inv_bridge_arc_2)

        self.play(Create(comp2inv_bridge_arc_1),
                  Create(comp2inv_bridge_arc_2))

        # self.play(A[ 1 ].animate.move_to(bank_rect))
        # self.play(A[ 1 ].animate(rate_func = there_and_back_with_pause).move_to(exchange_rect))

        return2_pos = A[ 1 ][ 12 ].get_center()

        self.play(AnimationGroup(*[ MoveAlongPath(usdt, VMobject().set_points_as_corners(
            [ usdt.get_center(), comp2inv_bridge.get_top(), comp2inv_bridge.get_bottom(), usdts_moved2inv[ index ].get_center() ])) for
                                    usdt, index in zip(reversed([ *A[ 1 ][ -10: ] ]), range(len(usdts_moved2inv))) ]
                                 , lag_ratio=0.5), run_time=3)

        profit_from_inv = Tex('Companies earn Profit', font_size=40).next_to(A[ 1 ][ 12 ], D)
        self.play(Create(profit_from_inv))
        self.wait(2.395)
        # self.play(AnimationGroup(*[ MoveAlongPath(usdt, VMobject().set_points_as_corners(
        #     [ usdt.get_center(), comp2inv_bridge.get_bottom(), comp2inv_bridge.get_top(), usdts_moved2comp[ index ].get_center() ])) for
        #                             usdt, index in zip(list(A[ 1 ]), range(len(usdts_moved2comp))) ]
        #                          , lag_ratio=0.5), run_time=2)

        # TODO 5.086 secs다시 1테더를 가져가면 1테더를 소각시키고 1달러를 돌려받을 수 있습니다
        # TODO 0:00:59.826  ~  0:01:04.912
        # TODO 1.0secs pause
        # TODO 0:01:04.912  ~  0:01:05.912
        # last_anchor = usdts.copy().next_to(A[ 0 ], D).get_center()
        # my_line = VMobject()
        # my_line.set_points_as_corners( [usdts[7].get_center(),usdts[7].get_center()])
        # my_line.add_cubic_bezier_curve_to
        # my_line.add_points_as_corners([ [usdts[7].get_x(), -1, 0] , return2_pos])
        # my_line.set_style(stroke_width=10, stroke_color=RED)

        usdt_return_path = CubicBezier(usdts[ 7 ].get_center(), np.array([ usdts[ 7 ].get_x() - 0.5, -1, 0 ]),
                                       np.array([ usdts[ 7 ].get_x() - 0.5, -1, 0 ]),
                                       np.array([ 2, -1, 0 ]))

        usdt_return_path.add_points_as_corners([ np.array([ A[ 1 ][ 7 ].get_x(), -1, 0 ]), return2_pos ])

        # self.play(Create(bezier))

        # self.play()

        A_asset_row_2 = usdts[ 7 ].get_center()
        # last_anchor = usdts.copy().next_to(A[ 0 ], D).get_center()
        # my_line = VMobject()
        # my_line.set_points_as_corners([ usdts.get_center(), [ usdts.get_x(), -1, 0 ], [ 2, -1, 0 ] ])
        # my_line.add_cubic_bezier_curve_to(np.array([ last_anchor[ 0 ] - 0.5, -1, 0 ]), np.array([ last_anchor[ 0 ] - 0.5, -1, 0 ]),
        #                                   last_anchor)
        # my_line.set_style(stroke_width=10, stroke_color=RED)

        # self.play(MoveAlongPath(usdts[5:10], VMobject().set_points_as_corners(
        #     [ usdts[5:10].get_center(), comp2inv_bridge.get_top(), comp2inv_bridge.get_bottom(), A[1][7].get_bottom()+D*0.1]))

        # self.play(AnimationGroup(VGroup(exchange, investment).animate.shift(D * 2),
        #                          AnimationGroup(FadeOut(bank2ex_bridge_arc_1), FadeOut(bank2ex_bridge_arc_2)),
        #                          MoveAlongPath(usdts, path=my_line),
        #                          lag_ratio=0.5,
        #                          run_time=3
        #                          )
        #           )
        #
        # self.play(VGroup(exchange, investment).animate.shift(U * 2),
        #           # AnimationGroup(FadeIn(bank2ex_bridge_arc_1), FadeIn(bank2ex_bridge_arc_2)),
        #           )

        self.play(AnimationGroup(
            VGroup(investment, exchange, usdts[ 10: ], A[ 1 ][ 10: ], profit_from_inv, profit_from_ex, usd_equals_usdt).animate.shift(
                D * 2),
            FadeOut(VGroup(comp2inv_bridge)),
            MoveAlongPath(usdts[ 5:10 ], usdt_return_path),
            lag_ratio=0.5,
            run_time=2.086))
        # self.play(MoveAlongPath(usdts[ 5:10 ], usdt_return_path))
        self.play(Uncreate(usdts[ 5:10 ], reverse_rate_function=True))
        self.play(A[ 1 ][ 5:10 ].animate.move_to([ bank_rect.get_x(), A[ 1 ][ 5 ].get_y(), 0 ]))
        self.play(A[ 1 ][ 5:10 ].animate.move_to(A_asset_row_2))
        self.play(VGroup(investment, exchange, usdts[ 10: ], A[ 1 ][ 10: ], profit_from_inv, profit_from_ex, usd_equals_usdt).animate.shift(
            U * 2))

        # TODO 13.132 secs이렇게 법정통화를 스테이블 코인으로 만들면 비트코인을 들고 있는 것처럼 변동성에도 노출이 안 되고
        #  현금과 같은 가치를 지닌 자산을 어느나라 거래소든 지갑이든 국경을 자유롭게 이동할 수 있어 많이 사용합니다
        # TODO 0:00:58.487  ~  0:01:11.619
        # TODO 1.0secs pause
        # TODO 0:01:11.619  ~  0:01:12.619
        self.play(usd_equals_usdt.animate.shift(U*2),run_time=2)
        no_vol = Tex('Free from volatility').scale(0.8).next_to(usd_equals_usdt,D*5).align_to(exchange_rect,U)
        no_border = Tex('Money without borders').scale(0.8).next_to(no_vol,D)

        self.play(Create(no_vol),run_time=3)
        self.wait(2)
        self.play(Create(no_border),run_time=3)


        self.wait(20)

class L01S02_pair(MovingCameraScene):
    def construct(self):
    #     self.add(NumberPlane())

        speak(self, title='Scene2', txt=
        '페어에 대해 알아보겠습니다#1'
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


class L01S05_order(MovingCameraScene):
    def construct(self):
        # self.add(NumberPlane().set_z_index(1))

        speak(self, title='Scene2', txt=

        '주문의 종류에 대해서 간단히 알아보겠습니다#1'
        '거래소에서 넣는 주문은 주문가격에 따라 크게 두 가지가 있습니다#1'
        '리밋 주문과 마켓 주문이고 한국어로는 지정가 주문 시장가 주문이라고 부릅니다#1'
        '지정가 주문은 말그대로 주문가격을 지정해놓는 주문이고 시장가 주문은 우리가 회를 먹을 때 싯가라고 부르듯이 그냥 그 자리에서 구할 수 있는대로 현재가격으로 즉시 체결하는 주문입니다#1'
        '이전에 들어본 스톱리밋오더, 스톱마켓오더, 트레일링스탑오더 같은 것은 이 가장 기본이 되는 두 종류에 부가적인 기능을 넣은 것입니다#1'


        '리밋 주문은 일반적으로 알고 있듯이 가격을 지정해서 그 가격에 거래하고 싶은 상대측이 나타나면 거래가 체결되는 주문입니다#1'
        '마켓 주문은 원하는 주문량을 입력하면 현재 나와있는 매물 중 가장 유리한 가격대로 주문량이 모두 충족될 때까지 거래를 합니다#1'
        '오더북에서 살펴보겠습니다#1'
        '지금 보시는 건 마켓 주문입니다#1'
        '매수 시장가 주문이면 빨간색 칸 중 가장 아래에 있는 유리한 가격 즉 싸게 팔아줄 판매자에게 구매를 합니다#1'
        '매도 시장가 주문이면 초록색 칸 중 가장 위에 있는 유리한 가격 즉 비싸게 사줄 구매자에게 판매를 합니다#1'
        '지금 보시는 건 리밋 주문입니다#1'
        '매수 지정가 주문이면 초록색 칸 어딘가에 주문을 넣습니다. 즉 지금가격보다 조금이라도 싼 가격에 구매하려고 대기합니다#1'
        '매도 지정가 주문이면 빨간색 칸 어딘가에 주문을 넣습니다. 즉 지금가격보다 조금이라도 비싼 가격에 판매하려고 대기합니다#1'
              , keep_pitch=True, update=1, speed=1.4)

        # TODO 2.851 secs주문의 종류에 대해서 간단히 알아보겠습니다
        # TODO 0:00:00.000  ~  0:00:02.851
        # TODO 1.0secs pause
        # TODO 0:00:02.851  ~  0:00:03.851

        order = Tex('Order').scale(2)
        self.play(Create(order))

        self.wait(2.851)

        # TODO 3.987 secs거래소에서 넣는 주문은 주문가격에 따라 크게 두 가지가 있습니다
        # TODO 0:00:03.851  ~  0:00:07.838
        # TODO 1.0secs pause
        # TODO 0:00:07.838  ~  0:00:08.838
        limit_order_text = Tex(r'Limit Order', '지정가 주문').scale(1.5).arrange(D).shift(L * 4)
        market_order_text = Tex(r'Market Order', '시장가 주문').scale(1.5).arrange(D).shift(R * 4)

        order_type = VGroup(limit_order_text[ 0 ], market_order_text[ 0 ])
        self.play(ReplacementTransform(order, order_type), run_time=2)
        self.wait(2.987)

        # TODO 5.014 secs리밋 주문과 마켓 주문이고 한국어로는 지정가 주문 시장가 주문이라고 부릅니다
        # TODO 0:00:14.176  ~  0:00:19.190
        # TODO 1.0secs pause
        # TODO 0:00:19.190  ~  0:00:20.190
        order_type_KOR = VGroup(limit_order_text[ 1 ], market_order_text[ 1 ])
        self.play(Create(order_type_KOR), run_time=2)
        self.wait(4.014)

        # TODO 10.86 secs지정가 주문은 말그대로 주문가격을 지정해놓는 주문이고 시장가 주문은 우리가 회를 먹을 때 싯가라고 부르듯이
        #  그냥 그 자리에서 구할 수 있는대로 현재가격으로 즉시 체 결하는 주문입니다
        # TODO 0:00:20.190  ~  0:00:31.050
        # TODO 1.0secs pause
        # TODO 0:00:31.050  ~  0:00:32.050

        limit_expl = Tex('Order at a certain price').next_to(limit_order_text, U, buff=0.5)
        market_expl = Tex('Order at the current price').next_to(market_order_text, U, buff=0.5)

        self.play(Create(limit_expl), run_time=3.5)
        self.play(Create(market_expl), run_time=3.5)
        self.wait(4.86)

        # TODO 8.625 secs이전에 들어본 스톱리밋오더, 스톱마켓오더, 트레일링스탑오더 같은 것은 이 가장 기본이 되는 두 종류에 부가적인 기능을 넣은 것입니다
        # TODO 0:00:32.050  ~  0:00:40.675
        # TODO 1.0secs pause
        # TODO 0:00:40.675  ~  0:00:41.675

        stop_limit_order = Tex(r'Stop Limit Order')
        stop_market_order = Tex(r'Stop Market Order')
        trailing_stop_order = Tex(r'Trailing Stop Order')

        other_order_types = VGroup(stop_limit_order, stop_market_order, trailing_stop_order).arrange(R).shift(D * 3)
        stop_limit_order.shift(U * 0.5)
        trailing_stop_order.shift(U * 0.5)
        self.play(FadeIn(stop_limit_order, shift=D), run_time=1.5)
        # self.wait(0.5)
        self.play(FadeIn(stop_market_order, shift=D), run_time=1.5)
        # self.wait(0.5)
        self.play(FadeIn(trailing_stop_order, shift=D), run_time=1.5)

        self.wait(2.5)
        self.play(FadeOut(VGroup(stop_limit_order, stop_market_order, trailing_stop_order), shift=D), run_time=2.625)

        # TODO 7.55 secs리밋 주문은 일반적으로 알고 있듯이 가격을 지정해서 그 가격에 거래하고 싶은 상대측이 나타나면 거래가 체결되는 주문입니다
        # TODO 0:00:41.675  ~  0:00:49.225
        # TODO 1.0secs pause
        # TODO 0:00:49.225  ~  0:00:50.225

        limit_expl_2 = Tex(r'I can wait\\Buy BTC only if it costs less than 99\$').scale(0.8).next_to(limit_expl, U, buff=1)
        self.play(Create(limit_expl_2), run_time=3.5)
        self.wait(5.05)

        # TODO 8.167 secs마켓 주문은 원하는 주문량을 입력하면 현재 나와있는 매물 중 가장 유리한 가격대로 주문량이 모두 충족될 때까지 거래를 합니다
        # TODO 0:00:50.225  ~  0:00:58.392
        # TODO 1.0secs pause
        # TODO 0:00:58.392  ~  0:00:59.392

        market_expl_2 = Tex(r"I can't wait\\Buy BTC at the best possible price NOW").scale(0.8).next_to(market_expl, U, buff=1)
        self.play(Create(market_expl_2), run_time=3.5)
        self.wait(2.667)

        self.play(Uncreate(VGroup(limit_expl_2,
                                  market_expl_2,
                                  limit_expl,
                                  market_expl,
                                  market_order_text,
                                  limit_order_text)),run_time=3)

        # TODO 1.8 secs오더북에서 살펴보겠습니다
        # TODO 0:00:54.054  ~  0:00:55.854
        # TODO 1.0secs pause
        # TODO 0:00:55.854  ~  0:00:56.854

        pair_rect = RoundedRectangle(corner_radius=0.5, height=7, width=4)
        pair_rect_text = Tex("BTCUSD").next_to(pair_rect, UP, buff=0.2).scale(0.8)
        pair = VGroup(pair_rect, pair_rect_text)

        self.play(Create(pair, run_time=q))

        self.wait(q)

        dummy = IntegerTable(
            [
                [ 1000000 ]
            ],
            row_labels=[ Tex(r"105\$") ],
            include_outer_lines=True, arrange_in_grid_config={"cell_alignment": LEFT},
            line_config={'stroke_color': GRAY, 'stroke_width': 2, 'stroke_opacity': 0.5}).scale(0.5)

        # self.play(Create(dummy))
        # self.add(index_labels(dummy))

        curr_px_height = dummy[ 1 ].get_y() - dummy[ 2 ].get_y()
        curr_px_width = dummy[ 4 ].get_x() - dummy[ 3 ].get_x()
        curr_px_rect = Rectangle(width=curr_px_width, height=curr_px_height, color=RED)

        curr_px_valuetracker = ValueTracker(100)
        curr_px_val = str(int(curr_px_valuetracker.get_value()))
        # curr_px_number = Tex(rf'{curr_px_val}\$').move_to(curr_px_rect)
        curr_px_number_100 = Integer(100, unit=r"\$", color=RED).move_to(curr_px_rect)
        curr_px_number_101 = Integer(101, unit=r"\$", color=GREEN).move_to(curr_px_rect)

        # curr_px_number.add_updater(lambda x : x.become(Integer(curr_px_valuetracker.get_value(), unit=r"\$")))

        # curr_px =VGroup(curr_px_rect,curr_px_number_100)

        int_valuetracker = ValueTracker(100)

        my_int = Integer(int_valuetracker.get_value(), unit=r"\$").to_edge(UR)

        # my_int.add_updater()
        self.play(Create(curr_px_rect))
        # self.play(curr_px_valuetracker.animate.set_value(120))

        self.play(FadeIn(curr_px_number_100), run_time=0.01)

        order_book_shrt_table = IntegerTable(
            [ [ 100000 ],
              [ 10000 ],
              [ 1000 ],
              [ 100 ],
              [ 50 ]
              ],
            row_labels=[ Tex(r"105\$"),
                         Tex(r"104\$"),
                         Tex(r"103\$"),
                         Tex(r"102\$"),
                         Tex(r"101\$")
                         ],
            include_outer_lines=True, arrange_in_grid_config={"cell_alignment": LEFT},
            line_config={'stroke_color': GRAY, 'stroke_width': 2, 'stroke_opacity': 0.5}).scale(0.5).next_to(curr_px_rect, UP, buff=0)

        for i in range(1, 6):
            for j in range(1, 3):
                order_book_shrt_table.add_highlighted_cell((i, j), fill_opacity=0.2, color=RED_A)

        order_book_shrt_table.set_row_colors(RED, RED, RED, RED, RED)

        order_book_long_table = IntegerTable(
            [ [ 50 ],
              [ 100 ],
              [ 1000 ],
              [ 10000 ],
              [ 100000 ]
              ],
            row_labels=[ Tex(r"100\$"),
                         Tex(r"99\$"),
                         Tex(r"98\$"),
                         Tex(r"97\$"),
                         Tex(r"96\$")
                         ],
            include_outer_lines=True, arrange_in_grid_config={"cell_alignment": LEFT},
            line_config={'stroke_color': GRAY, 'stroke_width': 2, 'stroke_opacity': 0.5}).scale(0.5).next_to(curr_px_rect, DOWN, buff=0)

        for i in range(1, 6):
            for j in range(1, 3):
                order_book_long_table.add_highlighted_cell((i, j), fill_opacity=0.2, color=GREEN_A)

        # order_book_table.add_highlighted_cell((2,2),fill_opacity=0.2, color=RED_A)
        order_book_long_table.set_row_colors(GREEN, GREEN, GREEN, GREEN, GREEN)

        # order_book_table.add(order_book_table.get_cell((2,2), color=RED))

        # self.add(index_labels(order_book_table))

        def change_waiting_order(self, table, r, c, new_val, run_time):
            a = table.get_entries(pos=(r, c))
            b = Integer(new_val, fill_color=a.fill_color, font_size=a.font_size)
            return Transform(a, b.move_to(a.get_center()).align_to(a, LEFT), run_time=run_time)

        def change_waiting_order_by_perc(self, table, r, c, perc, run_time):
            a = table.get_entries(pos=(r, c))

            new_val = int(a.get_value() * ((100 + perc) / 100))
            b = Integer(new_val, fill_color=a.fill_color, font_size=a.font_size)
            return Transform(a, b.move_to(a.get_center()).align_to(a, LEFT), run_time=run_time)

        self.play(Create(order_book_long_table), Create(order_book_shrt_table))
        self.wait(1)
        # self.play(curr_px_number_100)

        # TODO 2.332 secs지금 보시는 건 마켓 주문입니다
        # TODO 0:00:56.854  ~  0:00:59.186
        # TODO 1.0secs pause
        # TODO 0:00:59.186  ~  0:01:00.186

        # TODO 6.717 secs매수 시장가 주문이면 빨간색 칸 중 가장 아래에 있는 유리한 가격 즉 싸게 팔아줄 판매자에게 구매를 합니다
        # TODO 0:01:00.186  ~  0:01:06.903
        # TODO 1.0secs pause
        # TODO 0:01:06.903  ~  0:01:07.903

        # TODO 6.693 secs매도 시장가 주문이면 초록색 칸 중 가장 위에 있는 유리한 가격 즉 비싸게 사줄 구매자에게 판매를 합니다
        # TODO 0:01:07.903  ~  0:01:14.596
        # TODO 1.0secs pause
        # TODO 0:01:14.596  ~  0:01:15.596

        negative_nums = rd.sample(range(-40, -25, 1), k=8)
        negative_nums.sort(reverse=True)
        # trade_occurred = Tex('A trade has occurred!').scale(0.8).to_corner(UR)
        market_occurred = Tex('Market order!').scale(1.8).next_to(pair_rect, R)

        # self.play(Write(trade_occurred))
        self.play(Write(market_occurred), run_time=2.332)
        self.wait(1)
        repetition = 8
        each_100_101 = [ 1, 1, 1, 1, 0, 0, 0, 0 ]
        each_change = [ -10, -20, -30, -40, -50, -60, -70, -75 ]

        order_book_runtime = 0.2
        for i in range(repetition):

            if_100_or_101 = each_100_101[ i ]
            change = each_change[ i ]

            if if_100_or_101 == 0:
                # self.play(ApplyWave(trade_occurred, amplitude=0.4), run_time=1)
                self.play(ApplyWave(market_occurred, amplitude=0.4), run_time=0.6)
                curr_px_rect.set_color(RED)
                self.play(
                    change_waiting_order_by_perc(self, order_book_long_table, 1, 2, change, order_book_runtime),
                    run_time=order_book_runtime)
                # self.play(FadeIn(curr_px_number_100), FadeOut(curr_px_number_101), run_time=0.1)
                self.add(curr_px_number_100)
                self.remove(curr_px_number_101)

                # self.remove(curr_px_number_101)

                self.wait(1.1)

                # self.play(Uncreate(trade_occurred), run_time=0.01)

                # if i != 7:
                #     self.remove(curr_px_number_100)
                # else:
                curr_px_number = curr_px_number_100


            else:
                # self.play(ApplyWave(trade_occurred, amplitude=0.4), run_time=1)
                self.play(ApplyWave(market_occurred, amplitude=0.4), run_time=0.6)

                # self.play(Uncreate(curr_px_number_100),Uncreate(curr_px_number_101),Create)
                curr_px_rect.set_color(GREEN)
                self.play(
                    change_waiting_order_by_perc(self, order_book_shrt_table, 5, 2, change, order_book_runtime),
                    run_time=order_book_runtime)

                self.add(curr_px_number_101)
                self.remove(curr_px_number_100)

                # self.play(Uncreate(trade_occurred), run_time=0.01)
                # self.play(Uncreate(curr_px_number_101))
                self.wait(1.1)

                # if i != 7:
                #     self.remove(curr_px_number_101)
                # else:
                curr_px_number = curr_px_number_101

        # self.play(ApplyWave(trade_occurred, amplitude=0.4), run_time=1)
        # self.play(ApplyWave(market_occurred, amplitude=0.4), run_time=1)
        self.play(Unwrite(market_occurred), run_time=2)

        # TODO 2.271 secs지금 보시는 건 리밋 주문입니다
        # TODO 0:01:15.596  ~  0:01:17.867
        # TODO 1.0secs pause
        # TODO 0:01:17.867  ~  0:01:18.867

        # TODO 7.55 secs매수 지정가 주문이면 초록색 칸 어딘가에 주문을 넣습니다. 즉 지금가격보다 조금이라도 싼 가격에 구매하려고 대기합니다
        # TODO 0:01:18.867  ~  0:01:26.417
        # TODO 1.0secs pause
        # TODO 0:01:26.417  ~  0:01:27.417

        # TODO 7.683 secs매도 지정가 주문이면 빨간색 칸 어딘가에 주문을 넣습니다. 즉 지금가격보다 조금이라도 비싼 가격에 판매하려고 대기합니다
        # TODO 0:01:27.417  ~  0:01:35.100
        # TODO 1.0secs pause
        # TODO 0:01:35.100  ~  0:01:36.100
        negative_nums = rd.sample(range(-40, -25, 1), k=8)
        negative_nums.sort(reverse=True)
        limit_occured = Tex('Limit order!').scale(1.8).next_to(pair_rect, R)

        self.play(Write(limit_occured), run_time=2.271)
        self.wait(1)

        order_book_runtime = 0.2

        self.play(ApplyWave(limit_occured, amplitude=0.4),
                  run_time=0.6)
        self.play(change_waiting_order_by_perc(self, order_book_long_table, 5, 2, 30, order_book_runtime),
                  run_time=order_book_runtime)
        self.wait(1.1)

        self.play(ApplyWave(limit_occured, amplitude=0.4),
                  run_time=0.6)
        self.play(change_waiting_order_by_perc(self, order_book_long_table, 4, 2, 30, order_book_runtime),
                  run_time=order_book_runtime)
        self.wait(1.1)

        self.play(ApplyWave(limit_occured, amplitude=0.4),
                  run_time=0.6)
        self.play(change_waiting_order_by_perc(self, order_book_long_table, 3, 2, 30, order_book_runtime),
                  run_time=order_book_runtime)
        self.wait(1.1)

        self.play(ApplyWave(limit_occured, amplitude=0.4),
                  run_time=0.6)
        self.play(change_waiting_order_by_perc(self, order_book_long_table, 2, 2, 30, order_book_runtime),
                  run_time=order_book_runtime)
        self.wait(1.1)

        self.play(ApplyWave(limit_occured, amplitude=0.4),
                  run_time=0.6)
        self.play(change_waiting_order_by_perc(self, order_book_shrt_table, 1, 2, 30, order_book_runtime),
                  run_time=order_book_runtime)
        self.wait(1.1)
        self.play(ApplyWave(limit_occured, amplitude=0.4),
                  run_time=0.6)
        self.play(change_waiting_order_by_perc(self, order_book_shrt_table, 2, 2, 30, order_book_runtime),
                  run_time=order_book_runtime)
        self.wait(1.1)
        self.play(ApplyWave(limit_occured, amplitude=0.4),
                  run_time=0.6)
        self.play(change_waiting_order_by_perc(self, order_book_shrt_table, 3, 2, 30, order_book_runtime),
                  run_time=order_book_runtime)
        self.wait(1.1)
        self.play(ApplyWave(limit_occured, amplitude=0.4),
                  run_time=0.6)
        self.play(change_waiting_order_by_perc(self, order_book_shrt_table, 4, 2, 30, order_book_runtime),
                  run_time=order_book_runtime)
        self.wait(1.1)

        self.play(Unwrite(limit_occured), run_time=2)


        self.wait(1)
