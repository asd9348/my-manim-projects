from manim import *

Text
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
        pass
        # lec1_s1.construct(self)


class working4(MovingCameraScene):
    def construct(self):
        # self.add(NumberPlane())

        speak(self, title='Scene2', txt=
        '페어를 표시할 때는 보통 슬래시나 대시를 사용하거나 그냥 티커를 붙여서 표시하기도 합니다#1'
        '그리고 일반적으로 왼쪽의 자산을 베이스 에셋 오른쪽을 쿼트 에셋이라고 부릅니다#1'
        '비티씨 테더 거래쌍의 가격이 현재 100이라면 현재 비티씨는 100테더라는 것입니다#1'
        '심볼처럼 말그대로 1베이스 에셋을 얻으려면 얼마나 많은 쿼트 에셋을 줘야하는지를 표시하는 것입니다#1'
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
        self.wait(3.523)

        # TODO 5.182 secs일반적인 주식 어플에서는 베이스 에셋과 쿼트 에셋을 생각해본 적이 없을 겁니다
        # TODO 0:00:26.976  ~  0:00:32.158
        # TODO 1.0secs pause
        # TODO 0:00:32.158  ~  0:00:33.158

        stock_app_rect = RoundedRectangle(width=5, height=4)
        stock_app_text = Tex('Stock App').next_to(stock_app_rect, U)
        stock_app = VGroup(stock_app_rect, stock_app_text)

        self.play(ReplacementTransform(VGroup(BTC_none_USDT_text,
                                              base_asset_arrow,
                                              quote_asset_arrow,
                                              base_asset,
                                              quote_asset,
                                              expl_text_2), stock_app),
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

        forex_title = Tex('FOREX').move_to(stock_app_text)
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
        right_stable = Tex('USDP', 'USDN', 'USTC', 'USDD', 'FRAX').scale(1.5).arrange(D, buff=1).to_edge(R)
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
        self.add(NumberPlane().set_z_index(1))

        speak(self, title='L01S01', txt=
        '참고로 거래소에서 은행계좌가 연동됐다면 원화나 달러같은 법정통화를 사용하고 그렇지 못 하면, 보통 스테이블 코인을 사용하게 됩니다#1'
        '스테이블 코인은 일반적으로 실제 코인을 보증하는 법정통화를 바탕으로 발행하고 1대1로 교환될 수 있는 코인을 말합니다#1'
        '이번에 큰 이슈가 된 테라나 코인을 담보로 스마트 컨트랙트로 발행되는 다이처럼 법정통화 없이도 스테이블 코인을 만들 수 있습니다#1'
        '그러나 이번 영상의 범위를 벗어나기 때문에 나중에 따로 알아보겠습니다#1'
        '가장 유명한 테더를 예로 들자면 1테더를 발행하기 위해서는 1달러를 담보로 맡겨야하고 테더사는 언제든 사람들에게 돈을 돌려줄 수 있게 지급준비율을 유지하며 받은 달러 일부를 채권과 같은 자산에 투자하여 수익을 얻습니다'
        '다시 1테더를 가져가면 1테더를 소각시키고 1달러를 돌려받을 수 있습니다#1'
        '이렇게 법정통화를 스테이블 코인으로 만들면 비트코인을 들고 있는 것처럼 변동성에도 노출이 안 되고 현금과 같은 가치를 지닌 자산을 어느나라 거래소든 지갑이든 국경을 자유롭게 이동할 수 있어 많이 사용합니다#1'
              , keep_pitch=True, update=True, speed=1.4)

        # TODO 8.601 secs참고로 거래소에서 은행계좌가 연동됐다면 원화나 달러같은 법정통화를 사용하고 그렇지 못 하면, 보통 스테이블 코인을 사용하게 됩니다
        # TODO 0:00:00.000  ~  0:00:08.601
        # TODO 1.0secs pause
        # TODO 0:00:08.601  ~  0:00:09.601

        # TODO 7.539 secs스테이블 코인은 일반적으로 실제 코인을 보증하는 법정통화를 바탕으로 발행하고 1대1로 교환될 수 있는 코인을 말합니다
        # TODO 0:00:09.601  ~  0:00:17.140
        # TODO 1.0secs pause
        # TODO 0:00:17.140  ~  0:00:18.140

        # TODO 7.901 secs이번에 큰 이슈가 된 테라나 코인을 담보로 스마트 컨트랙트로 발행되는 다이처럼 법정통화 없이도 스테이블 코인을 만들 수 있습니다
        # TODO 0:00:18.140  ~  0:00:26.041
        # TODO 1.0secs pause
        # TODO 0:00:26.041  ~  0:00:27.041

        # TODO 4.24 secs그러나 이번 영상의 범위를 벗어나기 때문에 나중에 따로 알아보겠습니다
        # TODO 0:00:27.041  ~  0:00:31.281
        # TODO 1.0secs pause
        # TODO 0:00:31.281  ~  0:00:32.281

        # TODO 18.097 secs가장 유명한 테더를 예로 들자면 1테더를 발행하기 위해서는 1달러를 담보로 맡겨야하고 테더사는 언제든 사람들에게 돈을 돌려줄 수 있게 지급준비율을 유지하며 받은 달러 일부를 채권과 같은 자산에 투자하여 수익을 얻습니다다시 1테더를 가져가면 1테더를 소각시키고 1달러를  돌려받을 수 있습니다
        # TODO 0:00:32.281  ~  0:00:50.378
        # TODO 1.0secs pause
        # TODO 0:00:50.378  ~  0:00:51.378

        # TODO 13.132 secs이렇게 법정통화를 스테이블 코인으로 만들면 비트코인을 들고 있는 것처럼 변동성에도 노출이 안 되고 현금과 같은 가치를 지닌  자산을 어느나라 거래소든 지갑이든 국경을 자유롭게 이동할 수 있어 많이 사용합니다
        # TODO 0:00:51.378  ~  0:01:04.510
        # TODO 1.0secs pause
        # TODO 0:01:04.510  ~  0:01:05.510        stablecoin = Tex('Stablecoin').scale(2)
        stablecoin = Tex('Stablecoin').scale(2)

        self.play(Create(stablecoin))

        self.wait(q)
        self.play(Uncreate(stablecoin))
        #

        # 기업 혹은 거래소 박스 형성 (중앙ㅇ에 할거고 이건 왼쪽은 은행이나 채권 만들고)
        tether_company_rect = RoundedRectangle(height=8, width=4, corner_radius=0.5)
        tether_company_text = Tex('Company or Exchange').next_to(tether_company_rect, UP)

        tether_company = VGroup(tether_company_rect, tether_company_text).move_to(ORIGIN)

        tether_company.set_z_index(3)

        # self.add(index_labels(tether_company[0]))
        self.play(Create(tether_company))

        #
        # 고객 엔터티 오른 쪽에 생성하고 법정화폐 붙임

        def create_entity_tether(person_name, person_radius, person_color, asset_name, how_many, asset_color, asset_width, asset_height):
            person = LabeledDot(person_name, radius=person_radius, fill_opacity=1.0, color=person_color)

            box = Rectangle(width=asset_width, height=asset_height, fill_color=asset_color, stroke_color=asset_color, fill_opacity=1)
            text = manim.Text(asset_name, color=BLACK).scale(asset_height)

            asset = VGroup(box, text).next_to(person, DOWN, buff=0.1)
            assets = VGroup(asset)

            assets = VGroup(*[ asset.copy() for i in range(how_many) ])
            # for i in range(how_many):
            #     VGroup.add(asset.copy())

            assets.arrange(DOWN, buff=0.1).next_to(person, DOWN)

            return VGroup(person, assets)

        A = create_entity_tether("A", 0.5, WHITE, "USD", 15, GREEN, 0.7, 0.3)
        B = create_entity_tether("B", 0.5, WHITE, "USD", 10, GREEN, 0.7, 0.3)
        C = create_entity_tether("C", 0.5, WHITE, "USD", 3, GREEN, 0.7, 0.3)
        D = create_entity_tether("D", 0.5, WHITE, "USD", 8, GREEN, 0.7, 0.3)


        people_list = [ A, B, C, D ]
        people = VGroup(A, B, C, D).arrange(RIGHT, buff=0.2, aligned_edge=UP).to_edge(UR)

        self.play(Create(people))
        #
        # 그리고 고객들 돈을 기업으로 전송
        each_money = VGroup()
        for person in people_list:
            for i in range(len(person[ 1 ])):
                each_money.add(person[ 1 ][ i ])

        self.play(each_money.animate.arrange_in_grid(9, 4, buff=0.1).move_to(tether_company[ 0 ]))
        #
        # 기업에서 테더 발행 원래 받은 USD는 위로 밀리면서 새로운 USDT 뭉치가 생겨남

        tether_1ea = create_entity_tether("A", 0.5, WHITE, "USDT", 36, BLUE, 0.7, 0.3)[ 1 ]

        tethers = VGroup()
        for i in range(len(tether_1ea)):
            tethers.add(tether_1ea[ i ])
        tethers.arrange_in_grid(9, 4, buff=0.1).move_to(tether_company[ 0 ])
        self.play(GrowFromCenter(tethers))
        # tethers.arrange()
        self.play(VGroup(each_money, tethers).animate.arrange(DOWN, buff=0.25).move_to(tether_company[ 0 ]))

        #
        # 테더는 다시 엔터티에게 전송
        self.play(tethers[ 0:15 ].animate.arrange(DOWN, buff=0.1).next_to(A[ 0 ], DOWN))
        self.play(tethers[ 15:25 ].animate.arrange(DOWN, buff=0.1).next_to(B[ 0 ], DOWN))
        self.play(tethers[ 25:28 ].animate.arrange(DOWN, buff=0.1).next_to(C[ 0 ], DOWN))
        self.play(tethers[ 28:36 ].animate.arrange(DOWN, buff=0.1).next_to(D[ 0 ], DOWN))
        #
        # 그리고 달러 중 일부는 은행이나 채권등으로 투자
        invest = LabeledRectangle('Banks Bonds etc', width=4, height=6, direction=UP, corner_radius=0.5).to_edge(LEFT)

        self.play(Create(invest))

        self.play(each_money[ 0:16 ].animate.arrange_in_grid(4, 4, buff=0.1).move_to(invest))

        #
        # 엔터티 중 한명이 테더를 반납하면 달러로 돌려줌
        self.play(tethers[ 0:15 ].animate.arrange_in_grid(4, 4, buff=0.1).next_to(each_money[ 28:36 ], DOWN, buff=0.25))
        # self.play(VGroup(each_money[16:36],tethers[ 0:15 ]).animate.arrange(DOWN))

        self.play(each_money[ 23:36 ].animate.arrange(DOWN, buff=0.1).next_to(A[ 0 ], DOWN))

        self.play(Uncreate(tethers[ 0:15 ]))
        #
        # 전부 ㅇ벗어지고 알고리드믹 스테이블코인, 코인담보 스테이블 등이 있으나 나중에 알아보자

        self.play(FadeOut(each_money),
                  FadeOut(tethers),
                  FadeOut(tether_company),
                  FadeOut(invest),
                  FadeOut(people),
                  )


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


class working3(MovingCameraScene):

    def construct(self):

        self.camera.frame.save_state()

        numberline = NumberLine(x_range=[ 0, 5.5, 1 ],
                                length=14,
                                include_numbers=True,
                                include_tip=True,
                                stroke_color=RED,
                                stroke_width=6,
                                longer_tick_multiple=3,
                                )

        self.add(index_labels(numberline[ 3 ]).shift(D * 1))

        self.add(numberline)

        i = 0
        for tick in numberline[ 2 ]:
            if i == 0:
                self.play(self.camera.frame.animate(rate_func=linear).scale(0.5).move_to(tick))
                i = i + 1
            else:
                self.play(self.camera.frame.animate(rate_func=linear).move_to(tick))

        self.play(Restore(self.camera.frame, rate_func=linear))

        # self.play(Create(numberline))


class working4(Scene):
    def construct(self):
        screen_verticl_pixel = 100
        screen_horizontal_pixel= 100
        screen = VGroup()

        for l in np.linspace(0,1,screen_horizontal_pixel):
            for h in np.linspace(0,1,screen_verticl_pixel):
                pixel = Square(0.1, fill_color=Color(hsl=(h, 1, l)), fill_opacity=1, stroke_opacity=0)
                screen.add(pixel)

        screen.arrange_in_grid(screen_verticl_pixel,screen_horizontal_pixel,buff=0).scale(0.5)

        self.play(Create(screen))

        self.play(screen.animate.arrange_in_grid(screen_verticl_pixel,screen_horizontal_pixel,buff=0.05))
        self.play(screen.animate.arrange_in_grid(screen_verticl_pixel,screen_horizontal_pixel,buff=0))

        # self.add(screen)








