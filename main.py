from manim import *
import random as rd
import numpy as np
from math import *
from colour import Color

config.frame_width = 16
config.frame_height = 9

q = 0.3
qq = 2 * q
qqq = 3 * q

L = LEFT
R = RIGHT
U = UP
D = DOWN


class LabeledRectangle(RoundedRectangle):

    def __init__(
            self,
            label: str or SingleStringMathTex or Text or Tex,
            width: float or None = None,
            height: float or None = None,
            corner_radius: float or None = None,
            direction: np.ndarray = UP,
            **kwargs, ) -> None:

        if isinstance(label, str):
            from manim import Tex

            rendered_label = Tex(label, color=WHITE)
        else:
            rendered_label = label

        if width is None:
            width = 0.2 + max(rendered_label.width, rendered_label.height)
        if height is None:
            height = 0.2 + max(rendered_label.height, rendered_label.height)

        if corner_radius is None:
            corner_radius = 0.2

        super().__init__(width=width, height=height, corner_radius=corner_radius, **kwargs)
        rendered_label.next_to(self, direction)
        self.add(rendered_label)


def create_asset_mob(text, width=0.5, height=0.3, fill_color=GREEN, stroke_color=GREEN):
    box = Rectangle(width=width, height=height, fill_color=fill_color, stroke_color=stroke_color, fill_opacity=1)
    text = Text(text, color=BLACK).scale(height)

    return VGroup(box, text)


def create_entity(person_name, person_radius, person_color, asset_name, asset_color, asset_width, asset_height):
    person = LabeledDot(person_name, radius=person_radius, fill_opacity=1.0, color=person_color)

    box = Rectangle(width=asset_width, height=asset_height, fill_color=asset_color, stroke_color=asset_color, fill_opacity=1)
    text = Text(asset_name, color=BLACK).scale(asset_height)

    asset = VGroup(box, text).next_to(person, DOWN, buff=0.1)

    return VGroup(person, asset)


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
        dot = LabeledDot('Fuck')

        self.add(dot[ 0 ][ 0 ])


class working1(Scene):
    def construct(self):
        as5 = 265
        ##### 간단하게 오토매틱 마켓 메이커를 통해 덱스가 돌아가는 원리를 배웟는데
        ##### 이젠 약간의 수학과 함께 더욱 자세히 알아보겠습니다
        amm_text = Tex('AMM').scale(2)
        with_math_text = Tex('with Math').next_to(amm_text, D)

        self.play(Create(amm_text))
        self.play(Create(with_math_text))
        self.play(Uncreate(VGroup(amm_text, with_math_text)))
        #####
        ##### 엑스와이는 케이에서 엑스를 이항시키면
        ##### 와이는 엑스부느이 케이 형태입니다
        # 좌측 상단
        xyk = MathTex('x', r'\times', 'y', '=', 'k').scale(2)
        self.play(Write(xyk))

        xyk_fraction = MathTex('y', '=', r'\frac{k}{x}').scale(2)
        self.play(TransformMatchingShapes(xyk, xyk_fraction))
        self.play(xyk_fraction.animate.scale(0.5).to_edge(U).shift(L * 6))

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
                                 lag_ratio=0.5))

        self.play(Circumscribe(func_3))

        self.play(AnimationGroup(Uncreate(func_1),
                                 Uncreate(func_2),
                                 Uncreate(func_3),
                                 Uncreate(func_4),
                                 Uncreate(func_5),
                                 lag_ratio=0.5))

        ##### 그리고 이 반비레함수는 케이값에 따라서
        ##### 보이는 것과 같이 원점에서 점점 멀어지는 함수입니다
        ##### 일반적인 오토매틱 마켓메이커는 이 함수를 사용해 가격을 결정합니다
        ##### 도대체 어떻게 가격을 결정하는지 알아보겠습니다
        # 케이 바리어블 생성해서 옆에둠
        # 좌표게생성
        # 케이값 변경하면서 그래프 움직임
        # 좌표계 삭제

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
        self.play(k_tracker.animate.set_value(300), run_time=4)
        self.play(Uncreate(k_var))
        self.play(Uncreate(ax))
        self.play(Uncreate(xyk_graph))

        ##### 여기서 엑스는 a코인의 양 와이는 비코인의 양입니다
        ##### 페어라는 것이 원래 양방향이어서 서로 바꿔도 무방하나
        ##### 앞으로 이해하기 쉽게 풀내부의 베이스에셋의 양이 풀내부의 엑스 쿼트에셋의 양이 와이라고
        ##### 우리가 살펴볼 비티씨테더 페어에서는
        ##### 엑스는 풀내부 비티씨의 양
        ##### 왕이는 풀내부 테더의 양입니다
        # 엑스 와이 화살표와 설명
        # 화살표 밑에 설명 추가
        # 화살표 밑에 설명 추가
        A_coin_amt = Tex('A coin amount').shift(L * 4.5)
        B_coin_amt = Tex('B coin amount')
        A_coin_base = Tex('Base asset').next_to(A_coin_amt, D)
        B_coin_quote = Tex('Quote asset').next_to(B_coin_amt, D)
        A_coin_BTC = Tex('BTC').next_to(A_coin_base, D)
        B_coin_USDT = Tex('USDT').next_to(B_coin_quote, D)
        A_coin_texts = VGroup(A_coin_amt, A_coin_base, A_coin_BTC)
        B_coin_texts = VGroup(B_coin_amt, B_coin_quote, B_coin_USDT)

        x_arrow = Arrow(end=A_coin_amt.get_top(), start=xyk_fraction[ 0 ].get_bottom())
        y_arrow = Arrow(end=B_coin_amt.get_top(), start=xyk_fraction[ 2 ].get_bottom())

        self.play(Create(x_arrow),
                  Create(y_arrow)
                  )

        self.play(Create(A_coin_texts),
                  Create(B_coin_texts))
        self.play(Uncreate(A_coin_texts),
                  Uncreate(B_coin_texts),
                  Uncreate(x_arrow),
                  Uncreate(y_arrow)
                  )

        ##### 복잡하게 생각할 건 없고 와이는 엑스분의케이 그래프에서 케이는 그냥 어떤 값입니다.
        ##### 그런데 아까 우리는 케이가 엑스 곱하기 와이인 걸 봤습니다.
        # 기존에 있는 함수식 있고 다시 엑스와이는 케이 방정식 등장
        # 함수식 밑에 등장
        k_var = Variable(1, MathTex("k"), var_type=Integer).next_to(xyk_fraction, R, buff=2)
        k_tracker = k_var.tracker
        k_tracker.set_value(1)

        xyk_form = MathTex('x*y=k')

        ax = Axes(x_range=[ 0, 18, 4 ],
                  y_range=[ 0, 6500, 1000 ],
                  x_length=5,
                  y_length=5,

                  tips=True,
                  axis_config={"include_numbers": False, 'color': WHITE, 'include_ticks': False, 'font_size': 20, 'tip_width': 0.1,
                               'tip_height': 0.1},
                  y_axis_config={"include_numbers": False, 'font_size': 20}
                  ).to_edge(L, buff=1.2)

        xyk_graph_btc = ax.plot(lambda x: k_tracker.get_value() / x,
                                x_range=[ 0.00001, 6000 ],
                                use_smoothing=False, color=WHITE)

        xyk_graph_btc.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: k_tracker.get_value() / x,
                    x_range=[ k_tracker.get_value() / 6000, 16 ],
                    use_smoothing=False, color=WHITE)))

        y_axis_label = ax.get_y_axis_label(MathTex('Amount of USDT in Pool', color=WHITE).rotate(PI / 2).scale(0.4), edge=LEFT,
                                           direction=LEFT, buff=0.37)
        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool', color=WHITE).scale(0.4), edge=DOWN, direction=DOWN, buff=0.5)

        axis_labels = VGroup(x_axis_label, y_axis_label)

        coor_sys = VGroup(ax, axis_labels, xyk_graph_btc)

        self.play(Create(k_var))
        self.play(Create(coor_sys))
        # self.play(Create(axis_labels))
        # self.play(Create(xyk_graph_btc))

        ##### 자 그렇다면 현재 비티씨테더 풀의 함수식은 10곱하기 3000인 30000입니다다
        # 케이값은 30000으로 변경
        self.play(k_tracker.animate.set_value(30000), run_time=4)

        ##### 아까 말한 것처럼 가격은 풀에 각 코인이 얼마나 있는지로 결정되기 때문에
        ##### 우리는 풀의 상태, 정확히 얘기하면 풀 내부의 베이스 에셋과 쿼트 에셋의 비율로 가격을 계산할 수 있습니다
        ##### 엑스와이는 케이가 풀을 나타내는 방정식이고
        ##### 풀의 상태는 아까 본 와이는 엑스분의 케이라는 함수의 그래프 위의
        ##### 한 점으로 나타낼 수 있습니다. 여기에는 가격정보도 들어있는 것입니다.
        # 그래프 스케일링 맞게 다시 생성하고 점 하나 만들기
        # 비티씨 바리어블 테더 바리어블 생성

        # 점 옆에 (엑스, 와이) 그리고 프라이스 레이블 붙이기
        btc_var = Variable(10, MathTex("BTC"), var_type=Integer)
        btc_tracker = btc_var.tracker
        usdt_var = Variable(3000, MathTex("USDT"), var_type=Integer).next_to(btc_var, DOWN, aligned_edge=LEFT)
        usdt_tracker = usdt_var.tracker

        curr_dot = Dot(radius=0.1, color=GREY).move_to(ax.c2p(btc_tracker.get_value(),
                                                              xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        curr_dot.set_z_index(2)

        curr_dot.add_updater(lambda dot: dot.move_to(ax.c2p(btc_tracker.get_value(),
                                                            xyk_graph_btc.underlying_function(btc_tracker.get_value()))))

        dot_label = MathTex(r'(x,y)\  Price', font_size=35).next_to(curr_dot, UR)

        self.play(Create(curr_dot))
        self.play(Create(dot_label))
        self.wait(2)
        dot_label.add_updater(lambda dot: dot.become(MathTex(
            rf'({btc_tracker.get_value():.0f},{usdt_tracker.get_value():.0f})\  {usdt_tracker.get_value() / btc_tracker.get_value():.0f}USDT', font_size=35).next_to(
            curr_dot, UR)))

        ##### 거래자가 풀을 대상으로 비티씨를 매수하거나 매도한다는 것은
        ##### 풀의 상태를 변화 시키는 것이기에 현재 있는 지점에서 그래프 상의 다른 지점으로 이동한다는 것이고 풀상태예 따라 가격이 변하는데
        # 그래프에서 점 움직이면 레이블도 같이 움직이고 값도 변화

        buy_btc = Tex(r'BUY','BTC').arrange(D).scale(2).shift(R*4)
        buy_btc.set_color_by_tex("BUY", GREEN)
        # buy_btc.set_color_by_tex("T", RED)
        # buy_btc.set_color_by_tex("B", BLUE)
        sell_btc = Tex(r'SELL','BTC').arrange(D).scale(2).shift(R*4)
        sell_btc.set_color_by_tex("SELL", RED)

        self.play(Create(buy_btc))
        self.play(btc_tracker.animate.set_value(7),
                  usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
                  run_time=1)
        self.play(Uncreate(buy_btc))

        self.play(Create(sell_btc))
        self.play(btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)),
                  run_time=1)
        self.play(Uncreate(sell_btc))


        ##### 유동성 제공자가 유동성을 공급하거나 제거한다는 것은 케이값을 움직이는 것입니다.

        ##### 유동성을 공급하는 것은 비티씨와 테더를 같이 넣어주는 것이고
        ##### 그건 엑스와 와이가 둘다 늘어나기 때문에 케이값이 커지는 것입니다
        ##### 유동성을 제거하면 비티씨와 테더가 같이 빠져나가는 것이고
        ##### 엑스와 와이가 둘다 줄면 당연히 케이값도 줄어듭니다
        # 케이값 움직이면서 그래프도 움직임
        add_liq = Tex(r'ADD','Liquidity').arrange(D).scale(2).shift(R*4)
        add_liq.set_color_by_tex("ADD", GREEN)

        rmv_liq = Tex(r'REMOVE','Liquidity').arrange(D).scale(2).shift(R*4)
        rmv_liq.set_color_by_tex("REMOVE", RED)

        self.play(Create(add_liq))
        self.play(k_tracker.animate.set_value(50000),
                  run_time=1)
        self.play(Uncreate(add_liq))

        self.play(Create(rmv_liq))
        self.play(k_tracker.animate.set_value(10000),
                  run_time=1)
        self.play(Uncreate(rmv_liq))


        self.play(Uncreate(VGroup(xyk_fraction, k_var,curr_dot,dot_label, coor_sys)))

        ##### ###############################################################################################################

        ##### 아까본 와이는 엑스분의 30000을 원점으로 생각하고 실제 상황에 따라 어떻게 변하는지 보겠습니다.
        ##### 먼저 유동성 공급자의 활동을 알아보겠ㅅ브니다
        ##### 유동성을 공급하는 상황입니다.
        #####
        ##### 유동성을 공급한다는 것은 무엇을 의미할까요
        ##### 엑스와 와이가 오르면서 케이의 값이 함께 오른다는 것입니다
        #####
        ##### 애니메이션
        #####
        ##### 그런데 유동성을 공급하는데는 조건이 있습니다 반드시 비티씨와 테더를 함께 같은 가치만큼 넣어야된다는 것입니다
        ##### 여기에는 이유가 있습니다. 쉽게 생각하면 유동성 공급자체는 가격을 움직일 이유가 아니기 때문입니다
        ##### 비유하자면 하우스와 도박꾼같은 것인데 하우스는 장소와 환경을 제공할 뿐이지
        ##### 카드를 조작한다든가 하는 식으로 도박이 어떻게 흘러가는지 조작하면 안 됩니다.
        ##### 덱스에서 가격은 풀 내부의 비티씨와 테더 비율에 따라 결정됩니다.1비티씨가 몇 테더예 상응하는지로 우리는 가격을 생각합니다
        ##### 만약 현재가격대로 같은 가치만큼의 비티씨와 테더를 넣지 않으면 풀 내부의 비율이 깨지게 되고
        ##### 우리는 단순히 유동성을 공급했는데 가격을 변화시켜버립니다.
        ##### 그리고 이것과 연결되어 유동성 풀의 지분을 확인할 수 없게 됩니다.
        ##### 유동성 풀의 지분은 엘피 토큰으로 증명합니다 유동성 제공자는 비티씨와 테더를 풀에 넣고 그에 상응하는 엘피 토큰을 받습니다.
        ##### 최초로 풀을 만들게 되면 엘피 토큰이 초기 발행되고 이후 유동성을 추가하면 토큰이 추가 발행되고
        ##### 유동성을 제거하면 전체 발행량분의 자신의 발행량으로 계산되는 비율대로 풀에서 비티씨와 테더를 빼가고 엘피 토큰은 없어집니다.
        ##### 풀내부의 비티씨 테더 비율을 깨면서 즉 가격을 움직이면서 유동성을 추가하거나 제거하면 미래에 가격이 변동하면서
        ##### 풀내부의 비율이 변해버릴 때 유동성 공급자의 지분을 산정할 수 없습니다
        ##### 위와 같은 이유로 유동성 풀에는 두 코인을 현재 풀에서 계산되는 가격에 맞게 같은 가치만큼만 넣게 설정되어 있습니다
        #####
        ##### 엘피 토큰에 대해 좀 더 다루자면 최초 공긊 시 즉 풀을 만들면 루트 엑스와이 만큼 엘피토크닝 발행되고
        ##### 그 이후에는 수많은 제공자들이 유동성을 공급하기 시작합니다
        ##### 이렇게 공급할 때마다 전체발행량 분에 자신의 보유량으로 지분을 증명할 수 있도록 발행되고 공급된
        ##### 비트와 테더는 풀이라는 한 곳으로 모이게 됩니다.
        ##### 그리고 유동성을 제거할 때는 엘피 토큰이 사라지고 자신의 지분만큼 풀에서 돌려받는 것입니다.
        #####
        ##### 이쯤 되면 도대체 왜 유동성 공급을 해야하는가 궁금해집니다. 이건 뭐 자선사업또 아니고 그냥 남좋은 일 하는 걸까요?
        ##### 유동성공급을 할 이유가 없다면 사람들이 안 할 것이고 그러면 덱스도 존재할 수 없게 됩니다
        ##### 그래서 유동성 공급을 하면 수수료를 벌 수있게 만들어놧습니다
        ##### 아까처럼 풀에서 코인을 사고 팔 때 수수료가 들고 그 수수료느 풀에 쌓이고 유동성 공급자들은 유동성을 제거할 때
        ##### 그동안 수수료가 쌓인 더 커진 풀에서 본인 지분을 가져오기 때문에 수익을 얻을 수 있습니다.
        #####
        ##### ###########################################
        #####
        ##### 이제는 유동성을 제거하는 상황을 보겟ㅅ븐디
        #####
        ##### 유동성을 제거한다는 것은 풀에서 자기 지분만큼 비트와 테더를 빼가는 것입니다
        ##### 케이값이 작아졌습니다

        ##### ###############################################################################################################
        #####거래자 활동에 대해 알아보겟습니다

        ##### 먼저 풀에서 비티씨를 구매하는 경우입니다.
        ##### 오더북에서와 마찬가지로 누군가 비티씨를 사면 가격이 올라갑니다
        ##### 왜냐하면 풀에서 비티씨가 빠져나가서 비티씨 테더 비율이 변동했고 이게 비티씨의 가격을 바꾸게 됩니다
        ##### 우리가 생각한대로 내려갔습니다 그리고 케이값도 변하지 않고 그대로입니다.
        ##### 그런데 구매자가 기분이 안 좋아보입니다.
        ##### 구매자는 분명히 구매할 때 1비트코인에 300달러인 걸 보고
        ##### 3개를 구매하려고 했는데 소요된 비용이 900달러가 아니라 1286달러였습니다
        ##### 어떻게 된걸까요…
        ##### 아까 말했듰이 케이값이 변하지 않기 때문이빈다.
        ##### 케이는 30000이고 엑스와이는 케이가 유지되렴녀 현재 엑스가 10에서 7로 변했기 때문에
        ##### 와이는 4286달러가 되어야하고 구매자는 4286달러에서 원래 있던 3000테더를 뺀 1286달러 밖에 받지 못 한 것입니다.
        ##### 우리는 이것을 프라이스 임팩트라고 부릅니다. 어 이거 중앙화거래소에서 봤던 슬리피지라 비슷한데라고 생각할 수도 있습니다
        ##### 덱스에서 거래를 하다보면 슬리피지라는 것과 프라이스 임팩트란 단어가 쉽게 혼용되는 것을 볼 수 있ㅅ브니다
        ##### 잠시 차이점을 알아보고 가겠습니다
        ##### 슬리피지는 미끄러진다는 slip에서 나온 말로 예측하지 못 한다는 뉘앙스를 줍니다
        ##### 슬리피지는 주문을 전송하고 내 주문이 처리되기 전에 다른 사람의 트랜잭션이 먼저 체결되는 경우나
        ##### 현재가에 유동성이 부족하여 내 예측과 달리 벌어지는 것입니다.
        ##### 프라이스 임팩트는 내가 지금 하려는 트랜잭셕 즉 비트코인 2개를 풀에서 빼는 것이 가격에 주는 영향이라고 할 수 있습니다
        ##### 프라이스 임팩트 자체는 내가 트랜잭션을 요청하는 순간 이미 예상 된 것입니다.
        ##### 300달러를 보고 비티씨를 주문하면 나는 이미 계산을 통해
        ##### 내가 시장을 얼마나 움직일 것이고 그래서 사실상 비티씨를 300달러에 못 구매하고
        ##### 300이상의 가격에 구매할 것을 알고 있습니다 .이로인한 것은 프라이스 임팩트이지
        ##### 슬리피지가 아닙니다. 슬리피지는 그렇게 내가 평균단가 468.75 달러에 구매할 것이라 예상하는데 거기서부터 갈라지는 것입니다
        ##### 프라이스 임팩트는 468.75 달러 빼기 300 즉 168.75 달러 혹은 보통은 퍼센트로 나타내기에
        ##### 468.75 빼기 300 나누기 468.75 곱하기 100 즉 36퍼센트가 됩니다
        ##### 그러나 슬리피지와 프라이스 임팩트를 엄밀하게 구분하지 않는 경우가 많기에 주의해야합니다
        #####
        ##### 어쨋거나 명심할 것은 엑스와이는 케이모델에서 프라이스 임팩트가 없을 수는 없습니다
        ##### 왜냐하면 거래라는 것이 풀의 상태를 변화시키는 것이고 그래프상에서 이동할 수밖에 없기 때문입니다
        #####
        ##### ###########################################
        #####
        ##### 이번에는 비티씨를 파는 경우입니다
        ##### 아까와 같은 원리로 비티씨를 팔면 가격이 내려가고
        ##### 여기서도 프라이스 임팩트를 막을 수는 없습니다.
        #####
        ##### 가격은 예상대로 내려가고 매도자는 여전히 기분이 좋지 않습니다
        ##### 300달러를 보고 3개를 판매했지만 900달러가 아닌 692달러 밖에 못 받았기 때문입니다.
        ##### 이 거대한 괴리는 유동성즉 풀의 크기가 작기 때문입니다.
        #####

        #####
        ###################################################################################################################
        #####
        ##### 다음으로 넘어가기 전에 수수료예 대해 알아보겠스빈다.
        #####
        ##### 수수료는 거래가 발생할 때마다 풀에 쌓이기 때문에 매번 거래가 종료되면 케이값은 증가합니다
        ##### 덱스에서 수수료는 독특한 방식으로 작동합니다.
        ##### 거래를 하기 위해 코인을 풀로 보내면 코인이 풀에 도착하기 전에 수수료를 떼고
        ##### 남은 금액만 풀에 들어가서 그거에 맞게 거래가 일어납니다. 그리고 거래가 종료되면 풀에
        ##### 그냥 수수료를 추가합니다.
        ##### 중앙화 거래소에서는 거래소가 가져가니 우리의 수수료가 가격에 영향을 줄 일은 없었습니다
        ##### 그러나 덱스에서는 수수료가 풀 내부의 비트 테더 비율을 조금씩 바꾸기 때문에 우리가 생각한 것과 미세하게 가격이 차이가 납니다
        #####
        ##### 수수료가 1퍼인 상황을 생각해 보겠ㅅ빈다
        ##### 비트 10개 3000테더가 있는 풀에 1비트를 보내면 수수료를 뗀 0.99비트가 전송됩니다
        ##### 그리고 0.99에 대한 교환이 일어나고 풀에서 3000-30000분에 10.99테더가 빠져나가고 30000나누기 10.99인 2729테더가 남습니다
        ##### 지금까지는 케이는 여전히 30000입니다
        ##### 그뒤에 풀에 빼놨던 수수료인 0.01비트를 넣습니다. 풀에는 이제 11비트와 2729테더가 남아있습니다
        ##### 케이는 30027.297로 약간 증가했습니다 현재 비트의 가격은 248.159테더입니다
        #####
        ##### 원래 1비트를 매도했다고 생각하면 가격은 30000나누기 11나누기 11인 247.933테더가 되어야합니다
        ##### 그러나 수수료가 있었다면 30000나누기 10.99 나누기 11인 248.159 테더가 됩니다.
        #####
        ##### 즉 이전 거래자의 행동에 따라서 미세하게 이익이 바뀝니다.
        #####
        ##### 비트를 매도하는 행위에서 수수료가 있던 경우가 가격이 덜 떨어졌으므로
        ##### 같은 방향 즉 이후에 매도할 사람은 원래 앞사람이 거래하고 247테더를 생각하고 있었으나
        ##### 예상보다 돈을 좀 더 건질 수 있게 됐습니다
        ##### 반대로 앞사람과 반대방향 즉 매수를 하려던 사람은 자신이 앞사람을 보고 생각하던 247달러보다
        ##### 높은 248테더에 매수를 해야해서 예상보다 지출이 늘었습니다
        #####
        #####
        ##### ###############################################################################################################
        #####
        ##### 잠시 복습해보고 좀 더 복잡한 상황을 다뤄보겠습니다
        #####
        ##### 케이가 증가하는 상황은 색을 좀 더 진하게 감소하는 상황은 연하게
        ##### 가격이 내려가는 것은 빨간샊 올라가는 것은 초록색으로 표시했습니다.
        ##### 원점은 회색입니다
        #####
        ##### 가격상승
        ##### 가격하락
        #####
        ##### 케이상승
        ##### 케이하락
        ##### 다시한번명심할 것은 유동성 공급 제거는 가격과 관계가 없습니다
        ##### 그냥 지금 가격에 맞게 풀전체 비중에서 나의 지분을 없애는 것이므로 가격을 움직이는 행위가 아닙니다.
        ##### 프라이스 임팩트와 관계가 없습니다
        #####
        ##### 케이상승 후 가격상승 및 하락
        ##### 케이가 상승했다는 것은 유동성이 풍부해졌다는 것이고 이전과 같은 양의 비티씨를 거래하더라도 프라이스 임팩트가 적어집니다
        ##### 아까 300달러에서 3개를 매도할 때는 프라이스 임팩트가 얼마 발생
        ##### 지금은 유동성으 풍부하고 3개 매도할 때 프라이스 임팩트가 얼마 발생
        ##### 같은 3비티씨지만 풀에서 차지하는 비율이 적어졌다
        ##### 아까는 10분에 3 지금은 13분에 3
        ##### 퍼센트로 따지면 33퍼와 23퍼센트
        #####
        #####
        ##### 케이하락 후 가격상승 및 하락
        ##### 케이가 하락했다는 것은 유동성이 줄었다는 것이고 이전과 같은 양의 비티씨를 거래하더라도 프라이스 임팩트가 커집니다
        ##### 아까 300달러에서 3개를 매도할 때는 프라이스 임팩트가 얼마 발생
        ##### 지금은 유동성으 풍부하고 3개 매도할 때 프라이스 임팩트가 얼마 발생
        ##### 같은 3비티씨지만 풀에서 차지하는 비율이 적어졌다
        ##### 아까는 10분에 3 지금은 7 분에 3
        ##### 퍼센트로 따지면 33퍼와 42퍼센트
        #####
        ##### 가격상승 후 케이상승 및 하락
        ##### 아까와 달리 현재 가격은 이미 움직인 상태고 이 가격에 맞게 같은 가치를 넣어줘야합니다
        ##### 아까와 같이 2비티씨만큼 유동성을 공급하려고 하면 올라버린 가격에 맞게 테더를 넣어줘야합니다
        ##### 그래서 풀에서 같은 비중을 차지하기 위해서 더 많은 자금이 필요하게 됏ㅅ브니다
        ##### 만약 아까 넣은 2비티씨를 유동성을 빼려고 하면 현재 가격대로 돌려받게 됩니다
        #####
        ##### 가격하락 후 케이상승 및 하락
        ##### 아까와 달리 현재 가격은 이미 움직인 상태고 이 가격에 맞게 같은 가치를 넣어줘야합니다
        ##### 아까와 같이 2비티씨만큼 유동성을 공급하려고 하면 떨어진 가격에 맞게 테더를 넣어줘야합니다
        ##### 그래서 풀에서 같은 비중을 차지하기 위해서 더 적은 자금이 필요하게 됏습니다
        ##### 만약 아까 넣은 2비티씨를 유동성을 빼려고 하면 현재 가격대로 돌려받게 됩니다
        #####
        ##### 각 케이스마다 눈에 잘 보이게 선으로 연결해봤습니다
        ##### 동영상을 다시 보면서 천천히 곱씹어보시면 더 이해가 잘 될겁니다

        self.wait(5)
