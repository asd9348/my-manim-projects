from manim import *

import random as rd
import numpy as np
from math import *
from colour import Color
from custom_manim_utils.custom_consts import *
from custom_manim_utils.custom_color_consts import *
from custom_manim_utils.custom_functions import *
from custom_manim_utils.custom_mobs import *

config.frame_width = 16
config.frame_height = 9
background_color = W02
from pprint import pprint


class final(Scene):
    def construct(self):
        self.add(NumberPlane())
        # lec1_s1.construct(self)


class working4(MovingCameraScene):
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


class working2(MovingCameraScene):
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
        '그리고 비트코인을 입금받기 위해서는 에이에게서 비트코인을 받기위한 주소를 에이에게 알려주고 에이가 블록체인을 통해서 그 주소로 비트코인을 전송하면 확인한 뒤 거래소의 데이터베이스에 기록합니다#1'
        '거래소 데이터 베이스에 에이의 비트코인 보유액이 업데이트 됐습니다#1'

        '지갑은 A의 지갑이지만 실제로 이 지갑은 거래소의 하위지갑입니다#1'
        '그래서 A는 거래소의 허락없이는 마음대로 다시 코인을 뺄 수 없습니다#1'

        '거래소 앱에서 자신의 재산을 확인한 에이와 비는 이제 시장으로 갑니다#1'
        '여기서 시장은 물리적인 진짜 시장이 아니라 거래가 일어나는 디지털 공간을 의미합니다#1'
        '보통 이것을 거래쌍 영어로는 짝이라는 뜻의 페어라고 부릅니다#1'
        '페어에 대해서 잠시 알아보고 가겠습니다#1'

        '이제 실제 에이비가 주문을 넣는것으로 더 자세히 알아보겠습니다#1'
        '에이는 비트코인을 비싸게 팔고 싶어하고, 비는 비트코인을 싸게 사고 싶어합니다#1'
        '현재 거래쌍에 보이는 가격은 100테더입니다#1'
        '그래서 에이는 비트코인을 110테더에 판매하는 매도 지정가주문을 넣고 삐는 90테더에 매수 주문을 넣습니다#1'
        '그러나 가격이 지정가까지 올 생각을 안 하자 둘은 현재가에 더 가깝게 주문을 수정해 에이는 103테더에 매도, 비는 97테더에 매수 주문을 넣습니다#1'
        '여전히 가격 안 움직이고 비트코인을 너무 사고 싶었던 비는 시장가 주문을 하면서 에이에게 비트코인을 구매합니다#1'
        '기분이 좋아진 비는 어디서 들었는지 개인지갑에 비트코인을 보관해야된다는 애기가 기억나 비트코인 지갑 어플을 받아 개인지갑을 만들고 거래소에 그 주소로 출금을 요청합니다#1'
        '거래소는 비의 요청을 확인하고 거래소의 지갑에서 블록체인상으로 비의 요청 주소로 비트코인을 전송하고 거래소 데이터베이스에서 비의 비트코인 보유액을 차감합니다#1'
        '에이는 비트코인으로 테슬라를 사려 했지만 구매가 막혀 비트코인을 팔아 마련한 원화로 테슬라를 사기위해 출금을 하려합니다#1'
        '마찬가지로 거래소에 출금을 요청하고 거래소는 에이가 등록한 은행 계좌로 원화를 송금하고 데이터베이스에서 원화 보유액을 차감합니다#1'

              , keep_pitch=True, update=True, speed=1.4)

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
        self.play(Create(B), run_time=2)
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
        ex_wallet_text = Tex("ex wallet").next_to(ex_wallet_rect, UP, buff=0.2).scale(0.6)
        ex_wallet = VGroup(ex_wallet_rect, ex_wallet_text)

        wallets = VGroup(ex_wallet, A_wallet, B_wallet).arrange(DOWN).next_to(ex_rect, RIGHT, aligned_edge=RIGHT, buff=-1).shift(DOWN)

        self.play(Create(wallets), run_time=0.5)

        # wallet_expl = Text("Wallet means a group of wallets and bank account. it is better to say it is an account")

        bank_rect = RoundedRectangle(corner_radius=0.2, height=1.8, width=4)
        bank_rect_text = Tex("Bank").next_to(bank_rect, UP, buff=0.1).scale(0.5)
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

        self.play(B_asset_usd.animate.next_to(bank_server, DOWN), run_time=2)
        self.wait(1)
        self.play(FadeIn(B_100usd_bank, target_position=bank_server, scale=0.2), run_time=2)
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

        # TODO 11.9 secs그리고 비트코인을 입금받기 위해서는 에이에게서 비트코인을 받기위한 주소를 에이에게 알려주고 에이가 블록체인을 통해서 그 주소로 비트코인을 전송하면 확인한 뒤 거래소의 데이터베이스에 기록합니다
        # TODO 0:00:41.540  ~  0:00:53.440
        # TODO 1.0secs pause
        # TODO 0:00:53.440  ~  0:00:54.440

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
                  run_time=2)
        self.wait(0.5)

        self.play(A_asset_btc.animate.move_to(A_wallet_rect),
                  run_time=2)
        self.wait(0.5)

        # TODO 4.144 secs거래소 데이터 베이스에 에이의 비트코인 보유액이 업데이트 됐습니다
        # TODO 0:00:54.440  ~  0:00:58.584
        # TODO 1.0secs pause
        # TODO 0:00:58.584  ~  0:00:59.584

        A_1btc_ex = create_entity("B", 0.5, WHITE, "1 BTC", WHITE, 0.7, 0.3)[ 1 ].move_to(A_ex_ledger)
        self.play(FadeIn(A_1btc_ex, target_position=ex_server, scale=0.2),
                  run_time=3)
        self.wait(2.144)

        # TODO 4.482 secs지갑은 A의 지갑이지만 실제로 이 지갑은 거래소의 하위지갑입니다
        # TODO 0:00:59.585  ~  0:01:04.067
        # TODO 1.0secs pause
        # TODO 0:01:04.067  ~  0:01:05.067
        AB_wallet = VGroup(A_wallet, B_wallet)

        ex_wallet_rect_incl = RoundedRectangle(0.1, width=1.3, height=4).move_to(AB_wallet)

        self.play(Transform(ex_wallet_rect, ex_wallet_rect_incl),
                  ex_wallet_text.animate.next_to(ex_wallet_rect_incl, UP, buff=0.1),
                  run_time=2)

        self.play(VGroup(wallets, A_asset_btc).animate.shift(UP * 0.8),
                  run_time=2)
        self.wait(1.482)

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

        # TODO 4.397 secs거래소 앱에서 자신의 재산을 확인한 에이와 비는 이제 시장으로 갑니다
        # TODO 0:01:10.488  ~  0:01:14.885
        # TODO 1.0secs pause
        # TODO 0:01:14.885  ~  0:01:15.885

        market_rect = RoundedRectangle(corner_radius=0.5, height=ex_rect.height - bank_rect.height - 1.5, width=bank_rect.width)
        market_rect_text = Tex("Market").next_to(market_rect, UP, buff=0.2).scale(0.8)
        market = VGroup(market_rect, market_rect_text).align_to(bank_rect, R).align_to(ex_rect, D)

        self.play(Create(market),
                  run_time=2)

        A[ 0 ].save_state()
        B[ 0 ].save_state()
        self.play(VGroup(A[ 0 ], B[ 0 ]).animate().arrange(R, buff=0.7).move_to(market_rect),
                  run_time=2)
        self.wait(1.397)

        # TODO 5.243 secs여기서 시장은 물리적인 진짜 시장이 아니라 거래가 일어나는 디지털 공간을 의미합니다
        # TODO 0:01:15.885  ~  0:01:21.128
        # TODO 1.0secs pause
        # TODO 0:01:21.128  ~  0:01:22.128

        self.play(A[ 0 ].animate.restore(),
                  B[ 0 ].animate.restore(), run_time=1.243)
        self.wait(2)

        pair_rect = RoundedRectangle(corner_radius=0.1, height=ex_wallet_rect.height, width=3)
        pair_rect_text_1 = Tex("BTC/USD").scale(0.5).next_to(pair_rect, UP, buff=0.1)
        pair = VGroup(pair_rect, pair_rect_text_1).next_to(ex_rect, LEFT, aligned_edge=LEFT, buff=-2).align_to(ex_wallet_rect, DOWN)

        # self.play(Create(pair, run_time=q))

        self.play(ReplacementTransform(market_rect, pair_rect),
                  ReplacementTransform(market_rect_text, pair_rect_text_1),
                  run_time=3)

        # TODO 3.926 secs보통 이것을 거래쌍 영어로는 짝이라는 뜻의 페어라고 부릅니다
        # TODO 0:01:22.128  ~  0:01:26.054
        # TODO 1.0secs pause
        # TODO 0:01:26.054  ~  0:01:27.054

        pair_rect_text_2 = Tex("BTC/USD Pair").scale(0.5).move_to(pair_rect_text_1)

        self.play(ReplacementTransform(pair_rect_text_1, pair_rect_text_2),
                  run_time=1.426)
        self.wait(3.5)

        # TODO 3.95 secs이제 실제 에이비가 주문을 넣는것으로 더 자세히 알아보겠습니다
        # TODO 0:01:30.614  ~  0:01:34.564
        # TODO 1.0secs pause
        # TODO 0:01:34.564  ~  0:01:35.564

        # TODO 5.158 secs에이는 비트코인을 비싸게 팔고 싶어하고, 비는 비트코인을 싸게 사고 싶어합니다
        # TODO 0:01:35.564  ~  0:01:40.722
        # TODO 1.0secs pause
        # TODO 0:01:40.722  ~  0:01:41.722

        # TODO 2.912 secs현재 거래쌍에 보이는 가격은 100테더입니다
        # TODO 0:01:41.722  ~  0:01:44.634
        # TODO 1.0secs pause
        # TODO 0:01:44.634  ~  0:01:45.634

        # TODO 6.983 secs그래서 에이는 비트코인을 110테더에 판매하는 매도 지정가주문을 넣고 삐는 90테더에 매수 주문을 넣습니다
        # TODO 0:01:45.634  ~  0:01:52.617
        # TODO 1.0secs pause
        # TODO 0:01:52.617  ~  0:01:53.617

        # TODO 9.628 secs그러나 가격이 지정가까지 올 생각을 안 하자 둘은 현재가에 더 가깝게 주문을 수정해 에이는 103테더에 매도, 비는 97테더에 매수 주문을 넣습니다
        # TODO 0:01:53.617  ~  0:02:03.245
        # TODO 1.0secs pause
        # TODO 0:02:03.245  ~  0:02:04.245

        # TODO 6.959 secs여전히 가격 안 움직이고 비트코인을 너무 사고 싶었던 비는 시장가 주문을 하면서 에이에게 비트코인을 구매합니다
        # TODO 0:02:04.245  ~  0:02:11.204
        # TODO 1.0secs pause
        # TODO 0:02:11.204  ~  0:02:12.204

        # TODO 10.692 secs기분이 좋아진 비는 어디서 들었는지 개인지갑에 비트코인을 보관해야된다는 애기가 기억나 비트코인 지갑 어플을 받아 개인지갑을만들고 거래소에 그 주소로 출금을 요청합니다
        # TODO 0:02:12.204  ~  0:02:22.896
        # TODO 1.0secs pause
        # TODO 0:02:22.896  ~  0:02:23.896

        # TODO 10.088 secs거래소는 비의 요청을 확인하고 거래소의 지갑에서 블록체인상으로 비의 요청 주소로 비트코인을 전송하고 거래소 데이터베이스에 서 비의 비트코인 보유액을 차감합니다
        # TODO 0:02:23.896  ~  0:02:33.984
        # TODO 1.0secs pause
        # TODO 0:02:33.984  ~  0:02:34.984

        # TODO 7.502 secs에이는 비트코인으로 테슬라를 사려 했지만 구매가 막혀 비트코인을 팔아 마련한 원화로 테슬라를 사기위해 출금을 하려합니다
        # TODO 0:02:34.984  ~  0:02:42.486
        # TODO 1.0secs pause
        # TODO 0:02:42.486  ~  0:02:43.486

        # TODO 8.396 secs마찬가지로 거래소에 출금을 요청하고 거래소는 에이가 등록한 은행 계좌로 원화를 송금하고 데이터베이스에서 원화 보유액을 차감 합니다
        # TODO 0:02:43.486  ~  0:02:51.882
        # TODO 1.0secs pause
        # TODO 0:02:51.882  ~  0:02:52.882

        self.wait(5)


class working1(MovingCameraScene):
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
        luna_1ea = create_entity_tether("A", 0.5, WHITE, "LUNA", 20, '#071C4B', 1.2, 0.4, asset_text_color='#FEE834')[ 1 ][ 0 ]
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

        # TODO 13.132 secs이렇게 법정통화를 스테이블 코인으로 만들면 비트코인을 들고 있는 것처럼 변동성에도 노출이 안 되고 현금과 같은 가치를 지닌 자산을 어느나라 거래소든 지갑이든 국경을 자유롭게 이동할 수 있어 많이 사용합니다
        # TODO 0:00:58.487  ~  0:01:11.619
        # TODO 1.0secs pause
        # TODO 0:01:11.619  ~  0:01:12.619

        #
        self.wait(20)


class working3(ThreeDScene):

    def construct(self):
        resolution_fa = 20
        self.set_camera_orientation(phi=0 * DEGREES, theta=0 * DEGREES, gamma=0, zoom=1)
        axes = ThreeDAxes(x_range=(-0.99, 3, 0.11), y_range=(-0.99, 3, 0.11), z_range=(-1, 3, 0.1),
                          x_length=5, y_length=5, z_length=5)

        lab_x = axes.get_x_axis_label(Tex("$x$-label"))
        lab_y = axes.get_y_axis_label(Tex("$y$-label"))
        lab_z = axes.get_z_axis_label(Tex("$z$-label"))
        labs = VGroup(lab_x, lab_y, lab_z)

        imp_loss_graph = Surface(
            lambda u, v: axes.c2p(*self.imp_loss_surface(u, v)),
            v_range=[ -0.99, 3 ],
            u_range=[ -0.99, 3 ],
            fill_color=PINK
        )

        val_graph = Surface(
            lambda u, v: axes.c2p(*self.dollar_val_surface(u, v)),
            v_range=[ -0.99, 3 ],
            u_range=[ -0.99, 3 ],
            resolution=50
            # checkerboard_colors=[C0177, C0134]
        )

        val_graph.set_style(fill_opacity=0.8)
        val_graph.set_fill_by_value(axes=axes, colors=[ (C0193, -0.99), (C0493, -0.5), (C0795, 0), (C1145, 1), (C1195, 3) ], axis=2)

        # imp_loss_surface = Surface(
        #     lambda u, v: axes.c2p(u, v, imp_loss_surface(u, v)),
        #     resolution=(resolution_fa, resolution_fa),
        #     v_range=[-0.9, 4],
        #     u_range=[-0.9, 4],
        #     color=PINK
        #     )
        # dollar_val_surface = Surface(
        #     lambda u, v: axes.c2p(u, v, dollar_val_surface(u, v)),
        #     resolution=(resolution_fa, resolution_fa),
        #     v_range=[-0.9, 4],
        #     u_range=[-0.9, 4],
        #     color=RED
        #     )
        #

        my_graph = axes.plot(lambda x: x, x_range=[ -1, 5 ])
        # my_graph.set_colors_by_gradient([RED,BLUE])
        # surface_plane.set_style(fill_opacity=1)
        # surface_plane.set_fill_by_value(axes=axes, colors=[(RED, -0.5), (YELLOW, 0), (GREEN, 0.5)], axis=2)
        # face = ThreeDVMobject()
        # face.set_points_as_corners([
        #     [ 1, 0, 0 ],
        #     [ 1, 0, 5 ],
        #     [ 0, 1, 5 ],
        #     [ 0, 1, 0 ],
        #     [ 1, 0, 0 ]
        # ])
        #
        # face.set_fill(color=RED, opacity=0.5)
        # face.set_stroke(color=RED_E,width=3,opacity=0.7)
        #

        # surface_plane.set_style(fill_opacity=1)
        # surface_plane.set_fill_by_value(axes=axes, colors=[(RED, -0.5), (YELLOW, 0), (GREEN, 0.5)], axis=2)
        self.add(axes, labs)
        # self.add(imp_loss_graph)
        # self.play(Create(val_graph),run_time=5)
        self.add(val_graph)
        # self.play(Create(my_graph))
        # self.play(my_graph.animate.set_color_by_gradient([RED,BLUE,GREEN]),run_time=3)
        # self.play(my_graph.animate.set_color(RED),run_time=3)
        # self.set_camera_orientation(phi=2 * PI / 5, theta=PI / 5)
        # self.begin_ambient_camera_rotation(rate=0.2, about="theta",run_time=1)
        # self.move_camera(phi=45*DEGREES, about="phi",run_time=3)
        # self.set_camera_orientation(phi=90*DEGREES, theta=45*DEGREES,gamma=0)

        self.move_camera(theta=PI / 2, about="theta", run_time=2)
        self.move_camera(theta=2 * PI / 2, about="theta", run_time=2)
        self.move_camera(theta=3 * PI / 2, about="theta", run_time=2)
        self.move_camera(theta=4 * PI / 2, about="theta", run_time=2)
        self.move_camera(phi=45 * DEGREES, about="phi", run_time=1)
        self.move_camera(theta=4 * PI / 2, about="theta", run_time=2)
        self.move_camera(theta=3 * PI / 2, about="theta", run_time=2)
        self.move_camera(theta=2 * PI / 2, about="theta", run_time=2)
        self.move_camera(theta=PI / 2, about="theta", run_time=2)
        self.move_camera(phi=90 * DEGREES, about="phi", run_time=1)
        self.move_camera(theta=PI / 2, about="theta", run_time=2)
        self.move_camera(theta=2 * PI / 2, about="theta", run_time=2)
        self.move_camera(theta=3 * PI / 2, about="theta", run_time=2)
        self.move_camera(theta=4 * PI / 2, about="theta", run_time=2)
        self.move_camera(phi=135 * DEGREES, about="phi", run_time=1)
        self.move_camera(theta=4 * PI / 2, about="theta", run_time=2)
        self.move_camera(theta=3 * PI / 2, about="theta", run_time=2)
        self.move_camera(theta=2 * PI / 2, about="theta", run_time=2)
        self.move_camera(theta=PI / 2, about="theta", run_time=2)


class working1(MovingCameraScene):
    def construct(self):
        # self.add(NumberPlane().set_z_index(1))

        speak(self, title='L01S01', txt=
        '거래쌍을 다루기에 가격이라는 개념도 정확히 하고 가겠습니다#1'

        '가격은 경제,비즈니스면에서 물건,용역,자산의 금전적 수적가치를 따지는 것이다#1'
        '한 제품 및 서비스의 가격이란 소비자가 그 제품이나 서비스를 한 단위로 구매하기 위해 지불해야 하는 화폐의 양을 말한다#1'

        '비티씨 테더 페어에서 38000테더라고 적혀있다면 있다면 우리는 비티씨의 가격이 얼마일까요#1'
        '38000달러라고 부릅니다. 그러나 이는 엄밀하게 보면 틀린 표현입니다#1'
        '비티씨의 가격은 38000테더입니다. 테더와 달러는 다른 것입니다.다른 스테이블 코인도 마찬가지입니다#1'
        '테더는 실제로 거래해보면 보통 0.999에서 1.001 달러사이를 움직이며 거래되기 때문에 달러와 혼동하기 쉽습니다#1'
        '그러나 달러는 달러 그 자체이고 테더는 이 달러를 담보로 발행했기에 테더 회사가 도망가면 테더는 디지털 쓰레기가 됩니다#1'
        '달러를 옹호하는 건 아닙니다. 미국정부가 망하면 달러는 종이 쓰레기가 됩니다#1'
        '마치 금본위제 시절에 달러가 금이랑 같다고 여기는 것과 같습니다#1'
        '달러는 금이 아니고 금에 대한 보증서 개념이었고 달러가 금이 되기 위해서는 추가적으로 달러지폐를 금으로 교환하는 과정을 거쳐야 했습니다#1'
        '지금까지는 무의식적으로 달러와 테더가 같다고 여겨지는 생각을 없애기 위함이고 이것은 나중에 다른 개념을 이해하는데 도움이 됩니다#1'

        '어쨌든 가격이란것은 단위 화폐에 따라 결정이 되는 것이고, 단위가 없는 무차원 수같은 것이 아닙니다#1'
        '1비트코인은 오천만원 사만달러라고 부르지 오천이나 사만이라고만 부르지 않습니다#1'

        '그렇다면 가격은 어떻게 움직일까요#1'
        '우리가 배우기로는 수요와 공급이 교차하는 지점에서 결정된다고 배웁니다#1'
        '그러나 거래소에서의 가격은 그 말보다는 인내심이 더 부족한 쪽에 의해 결정된다고 하는게 이해하기 쉬울겁니다#1'
        '누구나 더 높은 가격에 팔고 더 낮은 가격에 사고 싶기 때문에 호가창에는 지정가 주문들이 쌓이기 시작합니다#1'
        '그렇게 지정가 주문들이 현재가 위 아래로 계속 쌓이기만 하면 가격은 움직이지 않습니다 #1'
        '실제로 호가창에 100달러과 101달러가 맞닿아 있고 아무도 시장가 주문을 넣지 않으면 가격은 마지막 주문이 100달러에서 매수였으면 100달러 101달러에서 매도였으면 101달러에 정지해있습니다#1'
        '그러다가 누군가 기다림을 참지 못하고 시장가로 구매를 하면 호가창에 쌓여있던 물량이 시장가로 소화되면서 가격은 움직입니다 #1'
        '잘 생각해보면 모든 사람이 지정가 주문만 넣으면 아무 일도 일어나지 않고 모두 기다리기만 합니다#1'

              , keep_pitch=True, update=1, speed=1.4)

        price = Tex('Price').scale(2)

        self.play(Create(price))
        self.wait(2)
        self.play(Uncreate(price))

        price_text = Tex(
            r'A price is the (usually not negative) quantity of payment \\'
            r'or compensation given by one party to another\\in return for goods or services.').shift(D * 2.5)
        self.play(Create(price_text))

        product = Tex('Product', font_size=60)
        service = Tex('service', font_size=60)
        asset = Tex('asset', font_size=60)

        self.play(Create(product))

        self.play(FadeOut(product, shift=U),
                  FadeIn(service, shift=U))
        self.play(FadeOut(service, shift=U),
                  FadeIn(asset, shift=U))

        self.play(Uncreate(price),
                  Uncreate(price_text))


class working1(MovingCameraScene):
    def construct(self):
        self.add(NumberPlane())
        self.camera.frame.save_state()

        circle = Circle(radius=1)
        x_label = DecimalNumber(33333).next_to(circle, D)
        y_label = DecimalNumber(45645).next_to(circle, L)

        self.play(Create(circle),
                  Create(x_label),
                  Create(y_label))
        self.wait(q)

        scaler = 0.3
        # dist = np.sqrt(circle.get_x() ** 2 + circle.get_y() ** 2)

        circle.add_updater(
            lambda mob: mob.scale_to_fit_height(2 + np.sqrt(circle.get_x() ** 2 + circle.get_y() ** 2) * scaler).set_color(
                Color(hue=1, saturation=np.sqrt(circle.get_x() ** 2 + circle.get_y() ** 2) / 9.17, luminance=0.5)))
        x_label.add_updater(lambda mob: mob.become(DecimalNumber(circle.get_x()).next_to(circle, D)))
        y_label.add_updater(lambda mob: mob.become(DecimalNumber(circle.get_y()).next_to(circle, L)))

        self.play(circle.animate.shift(L * 3))
        self.play(circle.animate.shift(D * 3))
        self.play(circle.animate.shift(U * 3))
        self.play(circle.animate.shift(R * 3))

        self.play(Uncreate(circle))
        ax = Axes(
            x_range=[ 0, 10, 1 ],
            y_range=[ 0, 10, 1 ],
            x_length=5,
            y_length=5
        )
        tracker = ValueTracker(1)

        k_var = Variable(1, 'k', var_type=DecimalNumber, num_decimal_places=2).to_edge(U)
        k_tracker = k_var.tracker
        self.play(Create(k_var))

        x_var = Variable(1, 'x', var_type=DecimalNumber, num_decimal_places=2).to_edge(UR)
        x_tracker = x_var.tracker
        self.play(Create(x_var))

        graph = ax.plot(lambda x: k_tracker.get_value() / x, x_range=[ 0.0001, 10 ], use_smoothing=False)
        graph.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: k_tracker.get_value() / x, x_range=[ k_tracker.get_value() / 10, 10 ], use_smoothing=False)))
        # x_range = [ k_tracker.get_value() / 6000, 16 ]
        self.play(Create(ax),
                  Create(graph))

        dot = Dot().move_to(ax.c2p(x_tracker.get_value(), graph.underlying_function(x_tracker.get_value())))
        dot.add_updater(lambda dot: dot.move_to(ax.c2p(x_tracker.get_value(), graph.underlying_function(x_tracker.get_value()))))
        dot_label = Tex(rf'({x_tracker.get_value():.2f},{graph.underlying_function(x_tracker.get_value()):.2f})').next_to(dot, UR)
        dot_label.add_updater(lambda jot: jot.become(
            Tex(rf'({x_tracker.get_value():.2f},{graph.underlying_function(x_tracker.get_value()):.2f})').next_to(dot, UR)))
        self.play(Create(dot),
                  Create(dot_label))

        self.play(k_tracker.animate.set_value(3),
                  x_tracker.animate.set_value(8))
        self.play(k_tracker.animate.set_value(1))
        # graph.clear_updaters()
        self.play(k_tracker.animate.set_value(5))
        self.play(k_tracker.animate.set_value(5))
        # self.play(k_tracker.animate.set_value(8)
        #
        # def update_curve(mob):
        #     mob.move_to(moving_dot.get_center())
        #
        # self.camera.frame.add_updater(update_curve)
        #



        moving_dummy_tracker = ValueTracker(k_tracker.get_value() / 10)
        # moving_dummy = Dot(color=RED).move_to(ax.c2p(0.5, graph.underlying_function(0.5)))
        moving_dummy = Dot(color=RED).move_to(graph.get_start())
        moving_dummy.add_updater(
            lambda dot: dot.move_to(ax.c2p(moving_dummy_tracker.get_value(), graph.underlying_function(moving_dummy_tracker.get_value()))))
        self.play(Create(moving_dummy))

        # self.play(self.camera.frame.animate.move_to(ORIGIN))
        # def update_curve(mob):
        #     mob.move_to(moving_dummy.get_center())

        self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dummy),run_time=5)

        self.camera.frame.add_updater(lambda camera: camera.move_to(moving_dummy.get_center()))
        # self.camera.frame.add_updater(update_curve)

        # self.play(MoveAlongPath(moving_dummy, graph, rate_func=linear),run_time=5)


        self.play(moving_dummy_tracker.animate.set_value(10),run_time=8)
        # self.play(self.camera.frame.scale(0.5).move_to(tick))
        # circles = VGroup(*[ Circle() for i in range(4) ]).arrange_in_grid(rows=2, cols=2, buff=0)

        # self.play(Create(circle),
        #           Create(circles))
        # self.add(index_labels(circles))
        # self.play(circles.animate.move_to(get_moved_coor_based_submob(circles, circles[ 1 ].get_center(), circle.get_center())))
        self.wait(20)
