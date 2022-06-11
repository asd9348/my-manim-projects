from manim import *
import random as rd
import numpy as np
from math import *
from colour import Color
from custom_manim_utils.custom_colors import *

config.frame_width = 16
config.frame_height = 9
# config.background_color=WHITE

q = 0.3
qq = 2 * q
qqq = 3 * q

t = 3
tt = 5
ttt = 7

L = LEFT
R = RIGHT
U = UP
D = DOWN


def there_and_back_expo(t: float) -> float:
    return -t + 1


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
        # 씬 1에써 디센트럴 네트워크 메인 선 2개 더 끊어져야됨
        # 씬1에서 이밸앤 오딧 바 짧게
        # 씬1에서 설사 코인 좀 더 크게

        # 씬3에서 체인이 생기기 전까지만 재생하고 그 다음 체인은 롯츠오브피 슬로우스피드와 같이 재생하면서 존나 느리게
        # 씬4에서 테더 자산 색 변경

        # 씬5부터 전부 해당 엑스춛 레이블 간격
        # 안 맞음
        # 씬5에서 케이값 변경에 따라서 좌표값 안 움직임
        # 씬6에서 쉐어에 178분의 87이라고 값 한 번 주기
        # 씬6에서 오리지널 그래프느 녹색으로 가자
        # 씬7에서는 이닛 제공자 없애지 말고 그냥 냅두기
        # 씬8에 색 안 맞음
        # 씬10 유저 돈트 오타

        circles = VGroup()

        for i in range(0, 360, 10):


            circle = Circle(radius=0.5,stroke_width=0, fill_color=Color(hsl=(i/360,1,0.5)),fill_opacity=1)
            text = Tex(f'{int((i+10)/10)}',color=BLACK).move_to(circle)
            circle.add(text)

            circles.add(circle)


        sat = 0
        for i in range(9):
            sat+=0.1
            circle = Circle(radius=0.5,stroke_width=0, fill_color=Color(hsl=(10/360,sat,0.5)),fill_opacity=1)
            text = Tex(f'{i+1}', color=BLACK).move_to(circle)
            circle.add(text)
            circles.add(circle)

        lum = 0
        for i in range(9):
            lum+=0.1
            circle = Circle(radius=0.5,stroke_width=0, fill_color=Color(hsl=(10/360,1,lum)),fill_opacity=1)
            text = Tex(f'{i+1}', color=BLACK).move_to(circle)
            circle.add(text)
            circles.add(circle)






        circles.arrange_in_grid(6,9).scale(1.1)

        test_circle = Circle(fill_color=cosmos_text, fill_opacity=1)

        mtex_1 = MathTex('for', 'dkjfkd').arrange(D)
        self.add(test_circle)

        # self.wait(5)


class working1(Scene):
    def construct(self):
        mtex_1 = MathTex('for', 'dkjfkd').arrange(D)
        ##### 그리고 한 가지 더 주목할 점은 우리는 덱스에서 오더라는 단어를 사용하지 않고 스왑이라는 단어르 ㄹ사용합니다
        ##### 덱스에서 하는 거래는 기본적으로 지정가가 아니라 그 자리에서 스마트 컨트랙트를 실행시켜서
        ##### 코인 바꾸는 것입니다
        ##### 오더라는 단어는 오더를 실행시키는 다른주체를 암시하거나 혹은 지정가주문처럼 실행이 될지 안 될지 모르는
        ##### 뉘앙스를 주기에 그자리에스 바로 교환하고 거럐가 끝나는 덱스의 특성에 어울리는 스왑이라는 단어를 사용합니다
        ##### ###############################################################################################################
        ##### ###############################################################################################################
        ##### 그리고 수익이라는 것은 기본적으로 시장의 비효율성이나 에러를 잡아내 이용하는 것입니다
        ##### 그리고 시장이 많으면 많을수록 그런 기회가 많아지기에 덱스를 마다할 이유는 없습니다
        # 인이피션시 화살표 수익
        inefficiency_profit = MathTex(r'Inefficiency \  \Rightarrow\  Profit')

        ##### 아비트라지를 설명하고 마치겠습니다
        # 아비트라지 제목
        arb = Tex('Arbitrage').scale(2)
        self.play(Create(arb))
        self.play(Uncreate(arb))

        ##### 아비트라지란 한국어로 재정거래라고 불리고 두 개의 시장 사이이서 가격차가 발쌩하면
        ##### 그 차익을 노리고 거래하는 것입닏
        # 양쪽 끝에 마켓 박스 두개 만들고 비티씨 가격이 두개가 다른 걸 보여줌
        # 그리고 가운데 보따리 엔터티 만들기
        # 불릿으로 아래 목록들 전부 나열하면서
        dex_1_rect = RoundedRectangle(height=5, width=3, corner_radius=0.5)
        dex_1_text = Tex('DEX A').next_to(dex_1_rect, UP)
        dex_1 = VGroup(dex_1_rect, dex_1_text).to_edge(L)

        dex_2_rect = RoundedRectangle(height=5, width=3, corner_radius=0.5)
        dex_2_text = Tex('DEX B').next_to(dex_2_rect, UP)
        dex_2 = VGroup(dex_2_rect, dex_2_text).to_edge(R)

        dex_1_px = Variable(500, 'BTC', var_type=Integer)
        dex_1_px_tracker = dex_1_px.tracker
        dex_1_px_unit = Tex(r'\$').next_to(dex_1_px, R)
        dex_1_px.add(dex_1_px_unit).scale(0.8).move_to(dex_1_rect)

        dex_2_px = Variable(470, 'BTC', var_type=Integer)
        dex_2_px_tracker = dex_2_px.tracker
        dex_2_px_unit = Tex(r'\$').next_to(dex_2_px, R)
        dex_2_px.add(dex_2_px_unit).scale(0.8).move_to(dex_2_rect)

        self.play(Create(dex_1),
                  Create(dex_2), run_time=t)
        self.wait(1)
        self.play(Create(dex_1_px),
                  Create(dex_2_px), run_time=t)
        self.wait(1)

        blist = BulletedList("Exposure to BTC fluctuation",
                             "Fees, time from DEX B",
                             r"In case of CEX, time, \\trade fees and high tx fees",
                             r"In case of DEX, time, \\high trade fees, tx fees",
                             r"In case of another blockchain,\\time and bridging fees",
                             "Slippage risk from every trade", height=7, width=7)

        self.play(Create(blist[ 0 ]), run_time=t)
        self.wait(1)
        self.play(Create(blist[ 1 ]), run_time=t)
        self.wait(1)
        self.play(Create(blist[ 2 ]), run_time=t)
        self.wait(1)
        self.play(Create(blist[ 3 ]), run_time=t)
        self.wait(1)
        self.play(Create(blist[ 4 ]), run_time=t)
        self.wait(1)
        self.play(Create(blist[ 5 ]), run_time=t)
        self.wait(1)

        ##### 지금 덱스 에이에서 비트코인이 500달러 덱스 비에서 470달러면
        ##### 덱스 비에서 비트코인을 구매하고 비트코인 가격변동에 대한 노출
        ##### 덱스 비에서 구매하는 거래수수료
        ##### 혹시나 다른 중앙화 거래소로 옮긴다면 전송수수료도 들고 시간 소요
        ##### 다른 블록체인으로 브릿지를 해도 브릿지 비용이 들것이고 시간 소요
        ##### 거래소 에이에서 비로 도착해서 다시 팔때도 거래 수수료가 발생합니다
        ##### 각거래마다 슬리피지
        ##### 그리고 성공할지 안 할지 보장도 없구요
        ##### 그런데도 가격이 매력적이라면 아비트라지를 하는 것입니다
        # 다 지우고
        # 스틸 낫 슈어 텍스트 좀 더 크게 제일 밑에

        still_not_sure = Tex('Still not sure...').scale(1.5)

        self.play(ReplacementTransform(blist, still_not_sure), run_time=t)
        self.wait(t)

        self.play(Uncreate(still_not_sure), run_time=t)
        self.wait(t)

        ##### 싼데서 사서 비싼데 팔기에 보따리장사라고도 부릅니다.
        ##### 얼핏보면 하는 거 없이 돈 버는 것 같지만
        ##### 보통은 미세한 차이를 보고 하기 때문에 규모가 커야지 수익이 좀 남는 편이고
        ##### 생각보다 리스크가 있고 인간의 손으로 하기에는 24시간 못 하고 너무 느려서
        ##### 보통 컴퓨터로 봇을 만ㄷ르어 돌리게 됩니다.
        # 불릿 더 라저 더 베터
        # 왓치 24 앤 패스트 핸드
        # 보통 컴퓨터 프로그램 오토메이티드
        blist_2 = BulletedList("The Larger, The Better",
                               "Watch 24/7, Act Fast",
                               r"Normally automated\\with programming", height=7, width=7)

        self.play(Create(blist_2[ 0 ]), run_time=t)
        self.wait(1)
        self.play(Create(blist_2[ 1 ]), run_time=t)
        self.wait(1)
        self.play(Create(blist_2[ 2 ]), run_time=t)
        self.wait(1)

        ##### 그리고 결정적으로 아비트라지는 가격 안정에 매우 중요한 역할을 합니다
        ##### 여러분이 사용하는 거래소의 가격이 싸면 좋겠지만 만약 이상하게 비싼 상태로 유지되고 있다면
        ##### 당연히 코인을 사는데 불리한 상황이겠지만 곧 아비트라저들의 와서 모든 시장의 가격의 평형을 이루게 합니다
        # 가격 전부 다르게 해놓고 똑같이 맞춰짐
        # 3번정도 반복

        dex_3_rect = RoundedRectangle(height=5, width=3, corner_radius=0.5)
        dex_3_text = Tex('DEX C').next_to(dex_3_rect, UP)
        dex_3 = VGroup(dex_3_rect, dex_3_text)

        dex_3_px = Variable(500, 'BTC', var_type=Integer)
        dex_3_px_tracker = dex_3_px.tracker
        dex_3_px_unit = Tex(r'\$').next_to(dex_3_px, R)
        dex_3_px.add(dex_3_px_unit).scale(0.8).move_to(dex_3_rect)

        self.play(ReplacementTransform(blist_2, dex_3),
                  Create(dex_3_px), run_time=t)
        self.wait(t)

        ##### 수많은 거래소 사이에서 이 아비트라지 봇들이 코인을 사고 팔며 가격을 전부 똑같이 맞춰주고
        ##### 그래서 우리는 어느 거래소든 다 비슷한 가격을 보게 됩니다.
        self.play(dex_1_px_tracker.animate.set_value(510),
                  dex_2_px_tracker.animate.set_value(550),
                  dex_3_px_tracker.animate.set_value(540), run_time=t)
        self.wait(t)
        self.play(dex_1_px_tracker.animate.set_value(530),
                  dex_2_px_tracker.animate.set_value(530),
                  dex_3_px_tracker.animate.set_value(530), run_time=t)
        self.wait(t)

        self.play(dex_1_px_tracker.animate.set_value(420),
                  dex_2_px_tracker.animate.set_value(480),
                  dex_3_px_tracker.animate.set_value(450), run_time=t)
        self.wait(t)

        self.play(dex_1_px_tracker.animate.set_value(455),
                  dex_2_px_tracker.animate.set_value(455),
                  dex_3_px_tracker.animate.set_value(455), run_time=t)
        self.wait(t)

        self.play(dex_1_px_tracker.animate.set_value(755),
                  dex_2_px_tracker.animate.set_value(741),
                  dex_3_px_tracker.animate.set_value(787), run_time=t)
        self.wait(t)

        self.play(dex_1_px_tracker.animate.set_value(751),
                  dex_2_px_tracker.animate.set_value(751),
                  dex_3_px_tracker.animate.set_value(751), run_time=t)
        self.wait(t)

        ##### 마찬가지로 덱스에서 내가 최초로 풀을 만들 때 말도안 되는 가격으로 공급해도
        ##### 곧 아비트라저들이 와서 시장가격으로 맞춰줍니다.
        # 다 없애고 덱스에 최초로 코인 상장해서 비트를 올릴 때 올라가는데 내가 뉴코인 10개와 5000달러를 넣어 개당 500달러로 만들어놓으면
        # 전부 없어짐 아비트라지로 민주화 당함

        self.play(Uncreate(VGroup(dex_1, dex_1_px, dex_2, dex_2_px, dex_3, dex_3_px)))
        self.wait(t)

        pool_rect = RoundedRectangle(width=7, height=4, corner_radius=0.5)
        pool_rect_text = Tex('BTC/USDT Pool').next_to(pool_rect, U)
        pool_btc_px = Variable(500, 'BTC', var_type=Integer)
        px_unit = Tex(r'\$').next_to(pool_btc_px, R)
        pool_btc_px.add(px_unit).scale(0.8).next_to(pool_rect, D)

        self.play(Create(pool_rect_text),
                  Create(pool_rect), run_time=t)
        self.wait(t)

        btc_lump = LabeledDot(Tex(r'10\\BTC', color=BLACK), radius=1, color=ORANGE).shift(L * 1.5)
        usdt_lump = LabeledDot(Tex(r'5000\\USDT', color=BLACK), radius=1, color=GREEN_C).shift(R * 1.5)
        usdt_lump_tracker = ValueTracker(5000)
        btc_lump_tracker = ValueTracker(10)

        liq_provider = create_entity(Tex(r' \emph{Init Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", ORANGE, 1.4,
                                     0.3).shift(R * 5)
        btc_asset_liq_prov = liq_provider[ 1 ]
        usdt_asset_liq_prov = create_entity("A", 0.5, WHITE, "3000 USDT", GREEN, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)
        liq_provider.add(usdt_asset_liq_prov)
        arbitrager = create_entity(Tex(r' \emph{Arbitrager}', color=BLACK).scale(0.7), 1, WHITE, "2.9 BTC", ORANGE, 1.4,
                                   0.3).shift(L * 5)
        btc_asset_arbitrager = arbitrager[ 1 ]
        usdt_asset_arbitrager = create_entity("A", 0.5, WHITE, "1127 USDT", GREEN, 1.4, 0.3)[ 1 ].move_to(btc_asset_arbitrager)

        self.play(FadeIn(liq_provider, target_position=R * 10), run_time=t)
        self.wait(t)

        self.play(ReplacementTransform(liq_provider[ 1 ], btc_lump),
                  ReplacementTransform(liq_provider[ 2 ], usdt_lump), run_time=t)
        self.wait(t)

        self.play(Create(pool_btc_px), run_time=t)
        self.wait(t)

        self.play(FadeIn(arbitrager, target_position=L * 10), run_time=t)
        self.wait(t)

        btc_lump.add_updater(lambda x: x.become(
            LabeledDot(Tex(rf'{round(btc_lump_tracker.get_value(), 1)}\\BTC', color=BLACK), radius=1, color=ORANGE).shift(L * 1.5)))
        usdt_lump.add_updater(lambda x: x.become(
            LabeledDot(Tex(rf'{int(round(usdt_lump_tracker.get_value(), 0))}\\USDT', color=BLACK), radius=1, color=GREEN_C).shift(R * 1.5)))
        self.play(pool_btc_px.tracker.animate.set_value(300),
                  usdt_lump_tracker.animate.set_value(3873),
                  btc_lump_tracker.animate.set_value(12.9),
                  FadeOut(btc_asset_arbitrager, target_position=btc_lump),
                  FadeIn(usdt_asset_arbitrager, target_position=usdt_lump), run_time=ttt)
        self.wait(t)

        btc_lump.clear_updaters()
        usdt_lump.clear_updaters()
        self.play(FadeOut(VGroup(
            pool_btc_px,pool_rect,pool_rect_text,btc_lump,usdt_lump, arbitrager,usdt_asset_arbitrager,liq_provider[0])),run_time=5)

        ##### 덱스도 중앙화거래소에 영향을 주고 중앙화 거래소도 덱스에 영향을 줍니다
        ##### 모든 거래소가 아비트라지 봇으로 묶여있어 서로가 서로에게 영향을 줍니다.
        # 덱스하고 섹스 상호 화살표
        # 덱스 중앙화 거래소 네트워크
        arbigrager_circle = LabeledDot(Tex(rf'Arbitrager', color=BLACK,font_size=30), radius=1, color=ORANGE).set_z_index(1)

        dex_1 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=RED).set_z_index(1)
        dex_2 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=GREEN).set_z_index(0.5)
        dex_3 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=BLUE).set_z_index(1)
        dex_4 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=TEAL).set_z_index(1)
        dex_5 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=YELLOW).set_z_index(1)
        dex_6 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=MAROON).set_z_index(1)
        dex_7 = LabeledDot(Tex('DEX', font_size=20, color=BLACK), radius=0.5, color=PURPLE).set_z_index(1)
        cex_1 = LabeledDot(Tex('CEX', font_size=20, color=BLACK), radius=0.5, color=RED).set_z_index(1)
        cex_2 = LabeledDot(Tex('CEX', font_size=20, color=BLACK), radius=0.5, color=GREEN).set_z_index(1)
        cex_3 = LabeledDot(Tex('CEX', font_size=20, color=BLACK), radius=0.5, color=BLUE).set_z_index(1)
        cex_4 = LabeledDot(Tex('CEX', font_size=20, color=BLACK), radius=0.5, color=TEAL).set_z_index(1)
        cex_5 = LabeledDot(Tex('CEX', font_size=20, color=BLACK), radius=0.5, color=YELLOW).set_z_index(1)
        cex_6 = LabeledDot(Tex('CEX', font_size=20, color=BLACK), radius=0.5, color=MAROON).set_z_index(1)
        cex_7 = LabeledDot(Tex('CEX', font_size=20, color=BLACK), radius=0.5, color=PURPLE).set_z_index(1)

        dex_line_1 = Line(dex_1.get_center(), arbigrager_circle.get_center(), color=WHITE)
        dex_line_2 = Line(dex_2.get_center(), arbigrager_circle.get_center(), color=WHITE)
        dex_line_3 = Line(dex_3.get_center(), arbigrager_circle.get_center(), color=WHITE)
        dex_line_4 = Line(dex_4.get_center(), arbigrager_circle.get_center(), color=WHITE)
        dex_line_5 = Line(dex_5.get_center(), arbigrager_circle.get_center(), color=WHITE)
        dex_line_6 = Line(dex_6.get_center(), arbigrager_circle.get_center(), color=WHITE)
        dex_line_7 = Line(dex_7.get_center(), arbigrager_circle.get_center(), color=WHITE)
        cex_line_1 = Line(cex_1.get_center(), arbigrager_circle.get_center(), color=WHITE)
        cex_line_2 = Line(cex_2.get_center(), arbigrager_circle.get_center(), color=WHITE)
        cex_line_3 = Line(cex_3.get_center(), arbigrager_circle.get_center(), color=WHITE)
        cex_line_4 = Line(cex_4.get_center(), arbigrager_circle.get_center(), color=WHITE)
        cex_line_5 = Line(cex_5.get_center(), arbigrager_circle.get_center(), color=WHITE)
        cex_line_6 = Line(cex_6.get_center(), arbigrager_circle.get_center(), color=WHITE)
        cex_line_7 = Line(cex_7.get_center(), arbigrager_circle.get_center(), color=WHITE)

        ex_group = VGroup(dex_1, dex_2, dex_3, dex_4, dex_5, dex_6, dex_7, cex_1, cex_2, cex_3, cex_4, cex_5, cex_6, cex_7)
        line_group = VGroup(dex_line_1, dex_line_2, dex_line_3, dex_line_4, dex_line_5, dex_line_6, dex_line_7, cex_line_1, cex_line_2, cex_line_3, cex_line_4, cex_line_5, cex_line_6, cex_line_7)
        ex_list = [ dex_1, dex_2, dex_3, dex_4, dex_5, dex_6, dex_7, cex_1, cex_2, cex_3, cex_4, cex_5, cex_6, cex_7 ]



        rotation_val_tracker = ValueTracker(1)

        dist_dict = {0: 3.66, 1: 3.2, 2: 3.21, 3: 3.12, 4: 3.42, 5: 3.37, 6: 3.34, 7: 3.04, 8: 3.24, 9: 3.43, 10: 3.4, 11: 3.26, 12: 3.1,
                     13: 3.24}
        dist_dict ={0: 3.76, 1: 2.6, 2: 3.24, 3: 3.29, 4: 3.46, 5: 2.83, 6: 2.74, 7: 2.82, 8: 2.63, 9: 2.85, 10: 2.85, 11: 3.47, 12: 3.38, 13: 3.07}
        dist_dict ={0: 2.8, 1: 3.6, 2: 2.99, 3: 3.71, 4: 2.83, 5: 3.89, 6: 2.82, 7: 3.82, 8: 2.8, 9: 3.8, 10:2.8, 11: 3.6, 12: 3.54, 13: 3.7}

        # dist_dict = {0: 3, 1: 3, 2: 3, 3: 3, 4: 3, 5: 3, 6: 3, 7: 3, 8: 3, 9: 3, 10: 3, 11: 3, 12: 3,
        #              13: 3}
        dir_dict = {0: 0.4488, 1: 0.8976, 2: 1.3464, 3: 1.7952, 4: 2.24399, 5: 2.69279, 6: 3.14159, 7: 3.59039, 8: 4.03919, 9: 4.48799, 10: 4.93679, 11: 5.38559, 12: 5.83439, 13: 6.28319}



        ex_group[ 0 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 0 ]  + rotation_val_tracker.get_value()) * dist_dict[ 0 ],
              sin(dir_dict[ 0 ]  + rotation_val_tracker.get_value()) * dist_dict[ 0 ], 0 ])))
        ex_group[ 1 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 1 ]  + rotation_val_tracker.get_value()) * dist_dict[ 1 ],
              sin(dir_dict[ 1 ]  + rotation_val_tracker.get_value()) * dist_dict[ 1 ], 0 ])))
        ex_group[ 2 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 2 ]  + rotation_val_tracker.get_value()) * dist_dict[ 2 ],
              sin(dir_dict[ 2 ]  + rotation_val_tracker.get_value()) * dist_dict[ 2 ], 0 ])))
        ex_group[ 3 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 3 ]  + rotation_val_tracker.get_value()) * dist_dict[ 3 ],
              sin(dir_dict[ 3 ]  + rotation_val_tracker.get_value()) * dist_dict[ 3 ], 0 ])))
        ex_group[ 4 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 4 ]  + rotation_val_tracker.get_value()) * dist_dict[ 4 ],
              sin(dir_dict[ 4 ]  + rotation_val_tracker.get_value()) * dist_dict[ 4 ], 0 ])))
        ex_group[ 5 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 5 ]  + rotation_val_tracker.get_value()) * dist_dict[ 5 ],
              sin(dir_dict[ 5 ]  + rotation_val_tracker.get_value()) * dist_dict[ 5 ], 0 ])))
        ex_group[ 6 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 6 ]  + rotation_val_tracker.get_value()) * dist_dict[ 6 ],
              sin(dir_dict[ 6 ]  + rotation_val_tracker.get_value()) * dist_dict[ 6 ], 0 ])))
        ex_group[ 7 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 7 ]  + rotation_val_tracker.get_value()) * dist_dict[ 7 ],
              sin(dir_dict[ 7 ]  + rotation_val_tracker.get_value()) * dist_dict[ 7 ], 0 ])))
        ex_group[ 8 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 8 ]  + rotation_val_tracker.get_value()) * dist_dict[ 8 ],
              sin(dir_dict[ 8 ]  + rotation_val_tracker.get_value()) * dist_dict[ 8 ], 0 ])))
        ex_group[ 9 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 9 ]  + rotation_val_tracker.get_value()) * dist_dict[ 9 ],
              sin(dir_dict[ 9 ]  + rotation_val_tracker.get_value()) * dist_dict[ 9 ], 0 ])))
        ex_group[ 10 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 10 ]  + rotation_val_tracker.get_value()) * dist_dict[ 10 ],
              sin(dir_dict[ 10 ]  + rotation_val_tracker.get_value()) * dist_dict[ 10 ], 0 ])))
        ex_group[ 11 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 11 ]  + rotation_val_tracker.get_value()) * dist_dict[ 11 ],
              sin(dir_dict[ 11 ]  + rotation_val_tracker.get_value()) * dist_dict[ 11 ], 0 ])))
        ex_group[ 12 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 12 ]  + rotation_val_tracker.get_value()) * dist_dict[ 12 ],
              sin(dir_dict[ 12 ]  + rotation_val_tracker.get_value()) * dist_dict[ 12 ], 0 ])))
        ex_group[ 13 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 13 ]  + rotation_val_tracker.get_value()) * dist_dict[ 13 ],
              sin(dir_dict[ 13 ]  + rotation_val_tracker.get_value()) * dist_dict[ 13 ], 0 ])))

        dex_line_1.add_updater(lambda x: x.become(Line(dex_1.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        dex_line_2.add_updater(lambda x: x.become(Line(dex_2.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        dex_line_3.add_updater(lambda x: x.become(Line(dex_3.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        dex_line_4.add_updater(lambda x: x.become(Line(dex_4.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        dex_line_5.add_updater(lambda x: x.become(Line(dex_5.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        dex_line_6.add_updater(lambda x: x.become(Line(dex_6.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        dex_line_7.add_updater(lambda x: x.become(Line(dex_7.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        cex_line_1.add_updater(lambda x: x.become(Line(cex_1.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        cex_line_2.add_updater(lambda x: x.become(Line(cex_2.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        cex_line_3.add_updater(lambda x: x.become(Line(cex_3.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        cex_line_4.add_updater(lambda x: x.become(Line(cex_4.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        cex_line_5.add_updater(lambda x: x.become(Line(cex_5.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        cex_line_6.add_updater(lambda x: x.become(Line(cex_6.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))
        cex_line_7.add_updater(lambda x: x.become(Line(cex_7.get_center(), arbigrager_circle.get_center(), color=WHITE).set_z_index(0)))

        
        
        self.play(Create(ex_group), run_time=t)
        self.wait(t)

        self.play(Create(arbigrager_circle), run_time=t)
        self.wait(t)

        self.play(Create(line_group), run_time=t)
        self.wait(t)

        self.play(rotation_val_tracker.animate.set_value(6), run_time=tt,rate_functions=exponential_decay)
        self.wait(t)

        cex_line_5.set_color(RED_E)
        self.wait(q)
        cex_line_2.set_color(RED_E)
        self.wait(q)
        cex_line_5.set_color(WHITE)
        cex_line_2.set_color(WHITE)
        self.wait(q)

        dex_line_5.set_color(RED_E)
        self.wait(q)
        cex_line_3.set_color(RED_E)
        self.wait(q)
        dex_line_5.set_color(WHITE)
        cex_line_3.set_color(WHITE)
        self.wait(q)

        dex_line_1.set_color(RED_E)
        self.wait(q)
        cex_line_1.set_color(RED_E)
        self.wait(q)
        dex_line_1.set_color(WHITE)
        cex_line_1.set_color(WHITE)
        self.wait(q)

        dex_line_2.set_color(RED_E)
        self.wait(q)
        cex_line_7.set_color(RED_E)
        self.wait(q)
        dex_line_2.set_color(WHITE)
        cex_line_7.set_color(WHITE)
        self.wait(q)

        dex_line_3.set_color(RED_E)
        self.wait(q)
        dex_line_4.set_color(RED_E)
        self.wait(q)
        dex_line_3.set_color(WHITE)
        dex_line_4.set_color(WHITE)
        self.wait(q)


