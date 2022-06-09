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
        dex_pros_and_cons.construct(self)
        smart_contract.construct(self)
        cons_of_smart_c.construct(self)
        amm_xyk_basics.construct(self)
        # working.construct(self)


class L_02_S_01_dex_pros_and_cons(Scene):
    def construct(self):
        # self.play(Create(NumberPlane()))

        swap_text = Tex('Swap').scale(2)
        tex_1 = Tex('Why dex?').scale(2)
        dex_text = MathTex('DEX').scale(2).shift(L * 4)
        cex_text = MathTex('CEX').scale(2).shift(R * 4)
        self.play(Create(dex_text), Create(cex_text))

        q_mark = Tex('?').scale(8)

        self.play(ReplacementTransform(VGroup(dex_text, cex_text), q_mark))

        self.play(Uncreate(q_mark))
        self.wait(q)

        #####     그렇다면 덱스가 존재하는 이유는 무엇일까요
        # 중앙화 노드 왼쪽 탈중앙화 노드 오른쪽

        center_line = Line(UP * 10, D * 10)

        centralized_net = VGroup()

        cent_server = Dot(radius=0.3)
        cent_net_nodes_dist = [ 2.59, 2.72, 2.43, 3.06, 2.16, 2.2, 3.03, 2.2, 2.77, 2.8, 2.45, 1.76, 2.73, 1.57, 3.04, 3.1, 2.93, 1.69,
                                2.63, 2.83, 3.03, 2.24, 2.59, 1.76, 1.54, 2.65, 1.98, 2.87, 1.75, 2.1 ]

        dir = 0

        for i in range(len(cent_net_nodes_dist)):
            dir += 2 * PI / len(cent_net_nodes_dist)
            dist = cent_net_nodes_dist[ i ]
            node = Dot(radius=0.1).move_to(np.array([ cos(dir) * dist, sin(dir) * dist, 0 ]))
            centralized_net.add(node)

        centralized_net.add(cent_server)

        for i in range(len(cent_net_nodes_dist)):
            node = centralized_net[ i ]
            line = Line(node.get_center(), cent_server.get_center())
            line.set_z_index(-1)
            centralized_net.add(line)

        centralized_net.shift(L * 4 + U * 0.5)
        centralized_net_text = Tex('Centralized Network').move_to(L * 4 + D * 3.5)

        self.play(Create(center_line))

        self.play(Create(centralized_net),
                  Create(centralized_net_text))

        # # ####################################################################################
        #
        decentralized_net = VGroup()
        decentralized_nets = VGroup()

        decent_net_nodes_dist_1 = [ 1.07, 1.57, 1.3, 1.4, 1.47, 1.1, 1.21, 1.28, 1.02, 1.14 ]
        decent_net_nodes_dist_2 = [ 1.57, 1.2, 1.41, 1.23, 1.46, 1.16, 1.29, 1.5, 1.29, 1.4 ]
        decent_net_nodes_dist_3 = [ 1.36, 1.4, 1.3, 1.15, 1.45, 1.11, 1.55, 1.22, 1.35, 1.37 ]
        decent_net_nodes_dist_4 = [ 1.07, 1.04, 1.18, 1.49, 1.58, 1.17, 1.18, 1.29, 1.31, 1.05 ]
        decent_net_nodes_dist_5 = [ 1.36, 1.29, 1.14, 1.56, 1.39, 1.19, 1.11, 1.07, 1.59, 1.11 ]
        decent_net_nodes_dist_list = [ decent_net_nodes_dist_1,
                                       decent_net_nodes_dist_2,
                                       decent_net_nodes_dist_3,
                                       decent_net_nodes_dist_4,
                                       decent_net_nodes_dist_5 ]

        for j in range(len(decent_net_nodes_dist_list)):
            for i in range(len(decent_net_nodes_dist_list[ j ])):
                dir += 2 * PI / len(decent_net_nodes_dist_list[ j ])
                dist = decent_net_nodes_dist_list[ j ][ i ]
                node = Dot(radius=0.1).move_to(np.array([ cos(dir) * dist, sin(dir) * dist, 0 ]))
                decentralized_net.add(node)

            decent_server = Dot(radius=0.2, color=WHITE)
            decentralized_net.add(decent_server)

            for k in range(len(decent_net_nodes_dist_list[ j ])):
                node = decentralized_net[ k ]
                line = Line(node.get_center(), decent_server.get_center())
                decentralized_net.add(line)

            decentralized_nets.add(decentralized_net.scale(0.8))
            decentralized_net = VGroup()

        decentralized_nets[ 0 ].shift(R * 2 + U * 2)
        decentralized_nets[ 1 ].shift(R * 2 + D * 2)
        decentralized_nets[ 2 ].shift(L * 2 + U * 2)
        decentralized_nets[ 3 ].shift(L * 2 + D * 2)
        decentralized_nets.shift(R * 4 + U * 0.5)

        line_btwn_servers = VGroup()

        for i in range(len(decentralized_nets) - 1):
            line = Line(decentralized_nets[ i ][ 10 ].get_center(), decentralized_nets[ 4 ][ 10 ].get_center(), stroke_width=5)
            line.set_z_index(-1)
            line_btwn_servers.add(line)

        decentralized_nets.add(line_btwn_servers)
        decentralized_net_text = Tex('Decentralized Network').move_to(R * 4 + D * 3.5)

        self.play(Create(decentralized_nets),
                  Create(decentralized_net_text))

        #####     일단 중앙화 주체 없이 운영되는 거래소이기 때문에 오는 장점이 잇습니다
        #####  덱스는 중앙화 서버가 없고 블록체인에 의존하기 때문에 서버가 죽는 위험에 노출되지 않습니다

        # 중앙화 노드로 공격 애니메이션
        # 중앙 노드가 없어지면서 라인도 네트워크 라인도 같이 제거
        # 탈중앙화는 살아있음

        arrow_scaler = 0.6
        rect = Rectangle(width=2, height=1, fill_color=RED, fill_opacity=1, color=RED)
        triangle = Triangle(fill_color=RED, fill_opacity=1, color=RED).rotate(-PI / 2).next_to(rect, RIGHT, buff=0)
        text = Tex(r'\textbf{Attack} ', color=BLACK, font_size=65).shift(R * 0.4)
        attack_arrow_UL = VGroup(rect.copy(), triangle.copy(), text.copy()).rotate(-PI / 4).scale(arrow_scaler).shift(U * 1 + L * 2)
        attack_arrow_DL = VGroup(rect.copy(), triangle.copy(), text.copy()).rotate(PI / 4).scale(arrow_scaler).shift(D * 1 + L * 2)
        rect = Rectangle(width=2, height=1, fill_color=RED, fill_opacity=1, color=RED)
        triangle = Triangle(fill_color=RED, fill_opacity=1, color=RED).rotate(PI / 2).next_to(rect, LEFT, buff=0)
        text = Tex(r'\textbf{Attack} ', color=BLACK, font_size=65).shift(L * 0.4)
        attack_arrow_UR = VGroup(rect.copy(), triangle.copy(), text.copy()).rotate(PI / 4).scale(arrow_scaler).shift(U * 1 + R * 2)
        attack_arrow_DR = VGroup(rect.copy(), triangle.copy(), text.copy()).rotate(-PI / 4).scale(arrow_scaler).shift(D * 1 + R * 2)

        cent_attack_arrows = VGroup(attack_arrow_UR, attack_arrow_DR, attack_arrow_DL, attack_arrow_UL).scale(0.8)
        cent_attack_arrows.set_z_index(1)

        cent_server_cross = Cross(stroke_width=15).scale(0.3).move_to(centralized_net[ 30 ])
        cent_server_cross.set_z_index(1)

        self.play(Create(cent_attack_arrows.move_to(centralized_net[ 30 ])))
        self.play(Create(cent_server_cross))
        self.play(Uncreate(centralized_net[ 31: ]))

        #################################################################

        decent_attack_arrows_1 = cent_attack_arrows.copy().scale(0.6).move_to(decentralized_nets[ 3 ][ 10 ])
        decent_attack_arrows_1.set_z_index(1)
        decent_attack_arrows_2 = cent_attack_arrows.copy().scale(0.6).move_to(decentralized_nets[ 0 ][ 10 ])
        decent_attack_arrows_2.set_z_index(1)

        decent_server_cross_1 = Cross(stroke_width=15).scale(0.2).move_to(decentralized_nets[ 3 ][ 10 ])
        decent_server_cross_1.set_z_index(1)
        decent_server_cross_2 = Cross(stroke_width=15).scale(0.2).move_to(decentralized_nets[ 0 ][ 10 ])
        decent_server_cross_2.set_z_index(1)

        self.play(Create(decent_attack_arrows_1))
        self.play(Create(decent_attack_arrows_2))
        self.play(Create(decent_server_cross_1),
                  (Create(decent_server_cross_2)))
        self.play(Uncreate(decentralized_nets[ 3 ][ 11: ]),
                  Uncreate(decentralized_nets[ 0 ][ 11: ]))

        self.play(Uncreate(VGroup(centralized_net,
                                  decentralized_nets,
                                  center_line,
                                  decent_server_cross_1,
                                  decent_server_cross_2,
                                  decent_attack_arrows_1,
                                  decent_attack_arrows_2,
                                  cent_attack_arrows,
                                  cent_server_cross,
                                  centralized_net_text,
                                  decentralized_net_text)))

        ##### 그러나 블록체인 네트워크도 트래픽이 많으면 느려지고 심지어 최근 솔라나나 클레이튼 대형체인도
        ##### 정지하는 일도 심심치 않게 발생합니다. 그래서 무작정 중앙서버보다 좋다고만은 할 수도 없습니다
        # 블록생성하다가 속도 존나 줄이기
        # 블록생성하다가 멈추고 뒤에 빨ㄹ간스톱사인

        chain1 = RoundedRectangle(height=0.2, width=0.4, corner_radius=0.1)
        chain2 = Line(ORIGIN, L * 0.4).move_to(chain1).shift(L * 0.2)
        chain = VGroup()
        for i in range(3):
            chain.add(chain2.copy())
            chain.add(chain1.copy())
        chain.add(chain2.copy())
        chain.arrange(R, buff=-0.12)

        blocks = VGroup(*[ Square(1.2, fill_color=BLACK, fill_opacity=1, stroke_color=WHITE) for i in range(4) ]).arrange(R,
                                                                                                                          buff=chain.width)
        scripts = VGroup(*[ Tex(f"{format(i, '04b')}", stroke_color=WHITE).move_to(blocks[ i ]).scale(0.5) for i in range(4) ])

        blockchain = VGroup()
        for i in range(len(blocks)):
            blockchain.add(blocks[ i ])
            blockchain.add(scripts[ i ])
            blockchain.add(chain.copy().next_to(blocks[ i ], R, buff=0))

        blockchain.to_edge(L)

        sign = RegularPolygon(n=6, fill_color=RED, fill_opacity=1, stroke_color=WHITE, stroke_width=10).scale(1.4)
        stop = Text('STOP', font='Unispace')
        stop_sign = VGroup(sign, stop).scale_to_fit_width(1.2).next_to(blockchain, R, buff=0)

        self.play(Create(blockchain[ 0:-4 ]), run_time=1)
        self.play(Create(blockchain[ -4: ]), run_time=5)
        self.play(Create(stop_sign))
        self.play(Uncreate(blockchain),
                  Uncreate(stop_sign))

        ##### 또 정부의 검열으로부터 자유로울 수 있고 프라이버시를 보호할 수 있습니다
        # 덱스중앙에 텍스트
        # 눈 아이콘생성
        # 방어막

        dex_text = Tex('DEX', font_size=100)

        eyelid_1 = ArcBetweenPoints(start=3 * L, end=3 * R, stroke_width=15)
        eyelid_2 = eyelid_1.copy().flip(axis=np.array([ 1, 0, 0 ])).next_to(eyelid_1, UP, buff=-0.1)
        iris = Annulus(inner_radius=0.5, outer_radius=1)
        eye = VGroup(eyelid_1, eyelid_2, iris).scale(0.7)

        eye_UL = eye.copy().to_edge(UL)
        eye_DL = eye.copy().to_edge(DL)
        eye_UR = eye.copy().to_edge(UR)
        eye_DR = eye.copy().to_edge(DR)

        eyes = VGroup(eye_UL, eye_DL, eye_UR, eye_DR)

        shield = Circle(radius=2.5, color=BLUE)

        self.play(Create(dex_text))
        self.play(Create(eyes))
        self.play(eye_UL[ 2 ].animate.shift(DR * 0.2),
                  eye_DL[ 2 ].animate.shift(UR * 0.18),
                  eye_UR[ 2 ].animate.shift(DL * 0.2),
                  eye_DR[ 2 ].animate.shift(UL * 0.18),
                  )

        self.play(Create(shield))
        self.play(Flash(shield, line_length=1, num_lines=50, color=BLUE, flash_radius=2.5 + SMALL_BUFF, time_width=0.3, run_time=2,
                        rate_func=rush_from))

        self.play(Uncreate(dex_text),
                  Uncreate(eyes),
                  Uncreate(shield)
                  )

        ##### 모든 기록이 블록체인에 남지만 그 주소가 누군지 매칭이 안 되기 때문에 익명성이 보장됩니다
        # 블록하나 왼쪽상단 옆에는 프럼 주소 아래 화살표와 내용 그리고 투 주소
        # 그리고 물음표 아이콘
        block_1_box = Square(2)
        block_1_text = Tex(f"{format(214, '08b')}", f"{format(245, '08b')}").arrange(D).scale(0.8)
        block_1 = VGroup(block_1_box, block_1_text).to_edge(L, buff=1)

        arrow = Arrow(UP, DOWN).next_to(block_1, buff=3.5)
        send_btc_text = Tex('Send 5 BTC').next_to(arrow, R, buff=1)
        from_text = Tex('From', color=RED)
        to_text = Tex('To', color=BLUE)
        addr_1 = Tex('miESMSkUgvFeJFqjzApV7c2bf3ynBobmEz', font_size=45).next_to(arrow, U, buff=1, aligned_edge=L)
        addr_2 = Tex('mnn3aq624RfThTTJaLg4XfrsxHXiNwLxrk', font_size=45).next_to(arrow, D, buff=1, aligned_edge=L)
        from_to_text = VGroup(from_text, to_text).arrange(D, buff=4, center=False, aligned_edge=L)
        addrs_text = VGroup(addr_1, addr_2).arrange(D, buff=4)
        tx_content = VGroup(VGroup(from_to_text, addrs_text).arrange(R, buff=0.5).next_to(block_1, buff=1), arrow, send_btc_text)

        mag_circle = Dot(radius=0.5, stroke_color=WHITE, stroke_width=10, fill_color=BLACK,
                                fill_opacity=1).move_to(block_1)
        mag_circle_text = Tex('01',color=WHITE).move_to(mag_circle)
        mag_rect = Rectangle(width=12, height=6).align_to(np.array([ -4.5, 3, 0 ]), UL)
        mag_line_1 = Line(mag_circle.get_top(), mag_rect.get_corner(UL))
        mag_line_2 = Line(mag_circle.get_bottom(), mag_rect.get_corner(DL))
        mag_line = VGroup(mag_line_1, mag_line_2)
        mag = VGroup(mag_circle, mag_line)

        who_text = Tex('Who?').scale(2).shift(R * 5)

        self.play(Create(block_1))
        self.play(AnimationGroup(Create(mag_circle),
                                 Create(mag_circle_text),
                                 Create(mag_line),
                                 Create(mag_rect),
                                 Create(tx_content),
                                 Create(who_text), lag_ratio=0.5), run_time=5)

        mag_circle_text.set_z_index(2)
        self.play(AnimationGroup(Uncreate(tx_content),
                                 Uncreate(who_text),
                                 Uncreate(mag_rect),
                                 Uncreate(mag_line),
                                 Uncreate(mag_circle_text),
                                 Uncreate(mag_circle),
                                 lag_ratio=0.5), run_time=5)
        self.play(Uncreate(block_1))

        ##### 그리고 거래소의 심사 없이 코인을 자유롭게 상장할 수 있ㅅ브니다
        ##### 크립토 프로젝트들은 거래소에서 심사를 거쳐 상장이 되야하는데 이 기준이 엄격하다보닏
        ##### 거래소에는 한정된 코인들만 있ㅅ브니다.
        ##### 그러나 덱스에서는 누구나 유동성 풀을 만들어 다른 사람들의 거래를 도울 수 있습니다
        # 중앙화 거래소 오른쪽에 생성 그리고 중앙에 Eval and audit 으로 필터 막대 설정
        # 잡코인들 존나 부닥치고 튕겨나감
        # 덱스똑같이 생성시키고 유동성제공자 만든 다음에 지폐 두장 보내면 덱스에서 페어 아이콘으로 형성
        # 할 때 코인 이름 구린걸로

        cex_text = Tex('CEX').scale(2).shift(R * 4 + U * 2)
        eval_audit_text = Tex(r'Evaluation \& Audit').to_edge(U)
        center_line = Line(UP * 10, D * 10, stroke_width=30).next_to(eval_audit_text, D)

        shit_coin = LabeledDot(Tex('SHIT', color=BLACK), radius=1, color=GREEN).shift(U * 2).to_edge(L)
        sulsa_coin = LabeledDot(Tex('SULSA', color=BLACK), radius=1, color=YELLOW).shift(D * 3).to_edge(L)
        btc_coin = LabeledDot(Tex('BTC', color=BLACK), radius=1, color=ORANGE).to_edge(L).shift(0.5 * D)

        limited_pairs = Tex('Limited pairs available...', 'BTC-USDT', 'ETH-BTC', r'\vdots').arrange(D).next_to(cex_text, D, buff=1)

        btc_arc = Arc(angle=PI).flip(axis=np.array([ 0, 1, 0 ])).shift(0.5 * D)

        self.play(Create(cex_text),
                  Create(eval_audit_text),
                  Create(center_line))
        self.play(Create(limited_pairs))
        self.play(Create(VGroup(shit_coin, sulsa_coin, btc_coin)))

        self.play(shit_coin.animate.align_to(center_line, R),
                  sulsa_coin.animate.align_to(center_line, R),
                  btc_coin.animate.align_to(center_line, R))

        self.play(MoveAlongPath(btc_coin, btc_arc))
        self.play(FadeOut(btc_coin, target_position=cex_text))

        self.play(FadeOut(shit_coin),
                  FadeOut(sulsa_coin))

        ##############################################################
        dex_text = Tex('DEX').scale(2).shift(R * 4 + U * 2)
        shit_coin = LabeledDot(Tex('SHIT', color=BLACK).scale(0.5), radius=0.5, color=GREEN).shift(U * 1.5).to_edge(L)
        sulsa_coin = LabeledDot(Tex('SULSA', color=BLACK).scale(0.3), radius=0.3, color=YELLOW).shift(D * 1.5).to_edge(L)

        any_pairs = Tex('Anyone can make pairs', 'SULSA-USDT', 'SHIT-BTC', 'SHIT-SULSA', r'\vdots').arrange(D).next_to(dex_text, D, buff=1)

        random_coin_1 = LabeledDot(Tex('BLAH', color=BLACK).scale(0.5), radius=0.5, color=RED).shift(U * 3).to_edge(L)
        random_coin_2 = LabeledDot(Tex('BLUH', color=BLACK).scale(0.7), radius=0.7, color=BLUE).shift(D * 3).to_edge(L)

        coins = VGroup(shit_coin, sulsa_coin, random_coin_1, random_coin_2)

        self.play(ReplacementTransform(cex_text, dex_text),
                  Uncreate(eval_audit_text),
                  Uncreate(center_line),
                  ReplacementTransform(limited_pairs, any_pairs)
                  , run_time=1)
        self.play(*[ FadeOut(coin, target_position=dex_text) for coin in coins ], run_time=3)
        self.play(Uncreate(dex_text),
                  Uncreate(any_pairs))

        self.wait(1)

class L_02_S_02_smart_contract(Scene):
    def construct(self):
        smart_c_text = Tex('Smart Contract').scale(2)

        self.play(Create(smart_c_text))
        self.play(Uncreate(smart_c_text))

        line1 = Line(LEFT * 3, RIGHT * 3, stroke_width=5)
        line2 = Line(DOWN * 3, UP * 3, stroke_width=5)
        dot = Dot(radius=0.3)
        rev_door = VGroup(dot, line1, line2).rotate(PI / 4)

        wall_line = Rectangle(height=10, width=0.7, stroke_width=25, )
        wall_sq = Square(7, fill_color=BLUE, fill_opacity=1)

        # self.play(Create(wall_sq))
        wall = Difference(wall_line, wall_sq, color=DARK_GREY, fill_color=DARK_GREY, fill_opacity=1)
        sector1 = AnnularSector(outer_radius=3.9, inner_radius=3.2, angle=PI / 2, color=DARK_GREY, fill_color=DARK_GREY,
                                fill_opacity=1).rotate_about_origin(PI / 4)
        sector2 = AnnularSector(outer_radius=3.9, inner_radius=3.2, angle=PI / 2, color=DARK_GREY, fill_color=DARK_GREY,
                                fill_opacity=1).rotate_about_origin(-PI / 4 - PI / 2)

        walls = VGroup(wall, sector1, sector2)
        self.play(GrowFromCenter(wall),
                  GrowFromCenter(sector1),
                  GrowFromCenter(sector2)
                  )
        self.play(Create(rev_door))
        self.play(Rotate(rev_door, angle=10 * PI), run_time=5, rate_func=rate_functions.exponential_decay)

        A = create_entity("A", 0.7, WHITE, "BTC", ORANGE, 0.8, 0.3).scale(1.2).to_edge(L)
        B = create_entity("B", 0.7, WHITE, "ETH", BLUE, 0.8, 0.3).scale(1.2).to_edge(R)

        A_asset = A[ 1 ]
        B_asset = B[ 1 ]
        A_asset_pos = A[ 1 ].get_center()
        B_asset_pos = B[ 1 ].get_center()

        A_asset_arc = Arc(radius=1.5, angle=-PI).flip(axis=UP)
        B_asset_arc = Arc(radius=1.5, angle=PI)

        self.play(Create(A),
                  Create(B))

        condition = Tex(r'A gives BTC to B\\B gives ETH to A').to_edge(UL)
        self.play(Create(condition))

        self.play(A_asset.animate.move_to(LEFT * 1.5),
                  B_asset.animate.move_to(RIGHT * 1.5))

        self.play(Rotate(rev_door),
                  MoveAlongPath(A_asset, A_asset_arc),
                  MoveAlongPath(B_asset, B_asset_arc))

        self.play(A_asset.animate.move_to(B_asset_pos),
                  B_asset.animate.move_to(A_asset_pos))

        self.play(Uncreate(condition))

        rev_door_text_1 = Tex(r'Company\\or Third Party Entity').scale(0.7).next_to(dot, R)
        rev_door_text_2 = Tex(r'Programming Language\\without Emotion').scale(0.7).next_to(dot, R)

        self.play(Create(rev_door_text_1))
        self.play(Uncreate(rev_door_text_1))

        self.play(Create(rev_door_text_2))
        self.play(Uncreate(rev_door_text_2))

        self.play(FadeOut(VGroup(walls, A, B, rev_door, rev_door_text_2)))
        self.wait(q)

class L_02_S_03_cons_of_smart_c(Scene):
    def construct(self):
        chain1 = RoundedRectangle(height=0.2, width=0.4, corner_radius=0.1)
        chain2 = Line(ORIGIN, L * 0.4).move_to(chain1).shift(L * 0.2)
        chain = VGroup()
        for i in range(3):
            chain.add(chain2.copy())
            chain.add(chain1.copy())
        chain.add(chain2.copy())
        chain.arrange(R, buff=-0.12).rotate(-PI / 2)

        blocks = VGroup(*[ Square(1.2, fill_color=BLACK, fill_opacity=1, stroke_color=WHITE) for i in range(2) ]).arrange(D,
                                                                                                                          buff=chain.height)
        scripts = VGroup(*[ Tex(f"{format(i, '04b')}", stroke_color=WHITE).move_to(blocks[ i ]).scale(0.5) for i in range(2) ])

        blockchain = VGroup()
        for i in range(len(blocks)):
            blockchain.add(blocks[ i ])
            blockchain.add(scripts[ i ])
            blockchain.add(chain.copy().next_to(blocks[ i ], D, buff=0))

        blockchain.to_edge(U)

        self.play(Create(blockchain), run_time=4)

        # self.play(Uncreate(blockchain))

        def create_just_order(place_or_cancel, buy_or_sell, px, qty, asset):

            order_paper = Rectangle(height=1.8, width=1.5)
            order_text_1 = Tex(f"{place_or_cancel}").scale(0.4)
            order_text_2 = Tex(rf"{buy_or_sell} ").scale(0.4)
            order_text_3 = Tex(rf"{qty} {asset}").scale(0.4)
            order_text_4 = Tex(rf"at {px}\$").scale(0.4)
            order_text = VGroup(order_text_1, order_text_2, order_text_3, order_text_4).arrange(DOWN, buff=0.1).move_to(
                order_paper)
            order_request = VGroup(order_paper, order_text).scale(0.7)
            return order_request

        # [ 585, 793, 998, 481, 902, 418, 391, 281, 377, 806, 267, 436, 286, 715, 574 ]
        # [ 958, 548, 834, 667, 96, 464, 555, 890, 740, 404, 853, 329, 415, 579, 281 ]
        place_cancel_list_1 = [ 'Cancel', 'Place', 'Cancel', 'Cancel', 'Place', 'Cancel', 'Cancel', 'Cancel', 'Place', 'Place', 'Cancel',
                                'Cancel', 'Cancel',
                                'Cancel', 'Place' ]
        place_cancel_list_2 = [ 'Cancel', 'Place', 'Place', 'Cancel', 'Cancel', 'Place', 'Cancel', 'Place', 'Cancel', 'Cancel', 'Cancel',
                                'Place', 'Place',
                                'Place', 'Place' ]
        buy_sell_list_1 = [ 'BUY', 'SELL', 'SELL', 'SELL', 'SELL', 'SELL', 'BUY', 'BUY', 'BUY', 'SELL', 'SELL', 'BUY', 'BUY', 'BUY',
                            'SELL' ]
        buy_sell_list_2 = [ 'BUY', 'SELL', 'SELL', 'BUY', 'BUY', 'SELL', 'SELL', 'BUY', 'SELL', 'BUY', 'BUY', 'SELL', 'SELL', 'SELL',
                            'SELL' ]

        # [ 5559, 489, 6391, 5846, 53, 6524, 261, 4085, 7125, 1469, 992, 6371, 3573, 3977, 2597 ]
        px_list_1 = [ 1234, 4176, 2147, 1176, 7696, 6887, 7656, 3569, 987, 4132, 2648, 8526, 9250, 6579, 9631 ]
        px_list_2 = [ 1234, 4176, 2147, 1176, 7696, 6887, 7656, 3569, 987, 4132, 2648, 8526, 9250, 6579, 9631 ]
        qty_list_1 = [ 5791, 8883, 8891, 5444, 9804, 9794, 8271, 3465, 534, 2722, 7260, 2788, 8760, 6763, 7481 ]
        qty_list_2 = [ 4246, 4949, 4666, 1270, 8461, 1531, 3198, 8123, 6257, 3186, 883, 3460, 490, 9394, 4736 ]
        asset_list_1 = [ 'SOL', 'MATIC', 'MATIC', 'MATIC', 'ADA', 'MATIC', 'UNI', 'DOT', 'XLM', 'ADA', 'BTC', 'DOT', 'MATIC', 'TRX', 'ETH' ]
        asset_list_2 = [ 'DOT', 'MATIC', 'AVAX', 'TRX', 'ADA', 'SOL', 'UNI', 'XLM', 'XLM', 'ADA', 'UNI', 'AVAX', 'XLM', 'ETH', 'DOT' ]

        orders_left = VGroup()
        orders_left_list = [ ]
        for i in range(15):
            element = create_just_order(place_cancel_list_1[ i ], buy_sell_list_1[ i ], px_list_1[ i ], qty_list_1[ i ], asset_list_1[ i ])
            orders_left.add(element)
            orders_left_list.append(element)
        orders_right = VGroup()
        orders_right_list = [ ]
        for i in range(15):
            element = create_just_order(place_cancel_list_2[ i ], buy_sell_list_2[ i ], px_list_2[ i ], qty_list_2[ i ], asset_list_2[ i ])
            orders_right.add(element)
            orders_right_list.append(element)

        orders_left.arrange_in_grid(5, 3).to_edge(L)
        orders_right.arrange_in_grid(5, 3, buff=0.4).to_edge(R)

        self.play(FadeIn(orders_right),
                  FadeIn(orders_left))

        self.play(LaggedStart(*[ FadeOut(order, target_position=blocks[ 1 ]) for order in orders_left_list + orders_right_list ]))

        # self.play(Uncreate(blockchain))

        # chain1 = RoundedRectangle(height=0.2, width=0.4, corner_radius=0.1)
        # chain2 = Line(ORIGIN, L * 0.4).move_to(chain1).shift(L * 0.2)
        # chain = VGroup()
        # for i in range(3):
        #     chain.add(chain2.copy())
        #     chain.add(chain1.copy())
        # chain.add(chain2.copy())
        # chain.arrange(R, buff=-0.12)
        #
        # blocks = VGroup(*[ Square(1.2, fill_color=BLACK, fill_opacity=1, stroke_color=WHITE) for i in range(3) ]).arrange(R,
        #                                                                                                                   buff=chain.width)
        # scripts = VGroup(*[ Tex(f"{format(i, '04b')}", stroke_color=WHITE).move_to(blocks[ i ]).scale(0.5) for i in range(3) ])
        #
        # blockchain = VGroup()
        # for i in range(len(blocks)):
        #     blockchain.add(blocks[ i ])
        #     blockchain.add(scripts[ i ])
        #     blockchain.add(chain.copy().next_to(blocks[ i ], R, buff=0))
        #
        # blockchain.to_edge(L)
        #
        # self.play(Create(blockchain), run_time=10)

        fees = Tex('Lots of Fees').shift(L * 4.5)
        fees_arrow = MathTex(r'\Uparrow').scale(2).next_to(fees, U, buff=0.5)
        speed = Tex('Slow Speed').shift(R * 4.5)
        speed_arrow = MathTex(r'\Downarrow').scale(2).next_to(speed, D, buff=0.5)

        self.play(Create(fees))

        self.play(fees.animate.scale(2),
                  Create(fees_arrow))

        self.play(Create(speed))

        self.play(speed.animate.scale(2),
                  Create(speed_arrow))

        self.play(Uncreate(blockchain),
                  Uncreate(VGroup(fees, fees_arrow, speed, speed_arrow)))

class L_02_S_04_amm_xyk_basics(Scene):
    def construct(self):
        # self.play(Create(NumberPlane()))
        ##### 그리하여 오늘은 에이엠엠ㅇ과 엑스와잉는 케이 공식에 대해 알아보겠습니다
        # 에이엠엠 타이틀과
        # 엑스와이는 케이 띄움
        amm_text = Tex('Automatic Market Maker').scale(2)
        xyk = MathTex('x', r'\times', 'y', '=', 'k').scale(2).next_to(amm_text, D)
        self.play(Create(amm_text))
        self.play(Create(xyk))
        self.play(Uncreate(amm_text))
        self.play(Uncreate(xyk))

        ##### 원래 덱스는 이더리움 생태계에서 나왔고 비트코인이 wbtc같이 이더리움 체인에서
        ##### 사용된 건 시간이 걸렸지만 이해를 위해 그냥 비티씨를 사용하겠스빈다

        ##### 뎩스가 탄생하고 사람들은 비트코인과 usdt의 거래쌍을 만들고 싶었습니다.
        ##### 그래서 중앙화 거래소에서 비트코인 가격이 300달러인 걸 보고
        ##### 비트코인 10개와 3000달러를 함께 유동성 풀이라는 것에 넣었습니다
        ##### 이것은 스마트 컨트랙트를 통해 자신의 자산으로 유동성으로 제공하곘다는 것입니다.
        ##### 이제 이 유동성 제공자로 인하여 거래자들은 비트코인과 테더 거래쌍을 이용할 수 있습니다
        ##### 말만 들으면 뭔지 이해가 안 될테니 이제 자세히 알아보겠습니다
        # 그냥 텍스트만
        expl_plain_text = Text(
            'DEX가 생기고 사람들은 BTC와 USDT의 거래쌍을 만들고 싶었습니다.\n그래서 중앙화 거래소에서 비트코인 가격이 300달러인 걸 보고\n비트코인 10개와 3000달러를 함께 유동성 풀이라는 것에 넣었습니다\n스마트 컨트랙트를 통해 자신의 자산을 유동성으로 제공한다는 것입니다.\n이제 거래자들은 비트코인과 테더 거래쌍을 이용할 수 있습니다',
            font='Batang', line_spacing=3, font_size=25)
        self.play(Create(expl_plain_text))
        self.play(Uncreate(expl_plain_text))

        ##### 일단 우리가 알고있는 오더북이 없이 어떻게 거래를 하는가가 궁금하실 겁니다
        ##### 오더북에서는 그저 사람들이 거래하는 것을 바탕으로 알아서 각겨이 정해집니다
        # 오더북 열고
        pair_rect = RoundedRectangle(corner_radius=0.5, height=8, width=4)
        pair_rect_text = Tex("BTCUSD").next_to(pair_rect, UP, buff=0.2).scale(0.8)
        pair = VGroup(pair_rect, pair_rect_text).move_to(ORIGIN)

        # self.play(Create(pair, run_time=q))
        self.wait(q)

        dummy = IntegerTable(
            [
                [ 1000000 ]
            ],
            row_labels=[ Tex(r"105\$") ],
            include_outer_lines=True, arrange_in_grid_config={"cell_alignment": LEFT},
            line_config={'stroke_color': GRAY, 'stroke_width': 2, 'stroke_opacity': 0.5}).scale(0.5)

        curr_px_height = dummy[ 1 ].get_y() - dummy[ 2 ].get_y()
        curr_px_width = dummy[ 4 ].get_x() - dummy[ 3 ].get_x()
        curr_px_rect = Rectangle(width=curr_px_width, height=curr_px_height, color=RED)

        curr_px_valuetracker = ValueTracker(100)
        curr_px_number_100 = Integer(100, unit=r"\$", color=RED).move_to(curr_px_rect)

        int_valuetracker = ValueTracker(100)

        self.play(Create(curr_px_rect))

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

        order_book_long_table.set_row_colors(GREEN, GREEN, GREEN, GREEN, GREEN)

        self.play(Create(order_book_long_table), Create(order_book_shrt_table))

        self.wait(1)

        ##### 덱스에서는 오더북대신 오토매틱마켓메이커를 사용하고
        # 오더북 엑스자 치고 에이엠엠 텍스트로 트랜스폼
        order_book_cross = Cross(stroke_width=25).scale(3)
        order_book_shit = VGroup(curr_px_rect, curr_px_number_100, order_book_long_table, order_book_shrt_table, order_book_cross)
        self.play(Create(order_book_cross))
        self.play(ReplacementTransform(order_book_shit, amm_text))

        amm_text = Tex('Automatic Market Maker').scale(2)
        self.play(GrowFromCenter(amm_text))

        ##### 오토매틱마켓메이커는 줄여서 amm이라고 부르고
        # 풀네임 약자로 줄이고
        amm_acronym_text = Tex('AMM').scale(2).move_to(amm_text)
        self.play(ReplacementTransform(amm_text, amm_acronym_text))

        ##### 그냥 프로그램 혹은 가격을 정하는 방식같은 추상적 개념이라고 생각하시면 됩니다
        # 에이엠엠 텍스트 밑에 프로그램 혹은 컨셉
        program_or_concept_text = Tex('Program or Concept?').next_to(amm_text, D)
        self.play(Create(program_or_concept_text))

        ##### 오토매틱마켓메이커를 돌리는데는 일반적으로 유동성 풀이 필요합니다
        # 에이엠엠이 풀박스로 트랜스폼

        pool_rect = RoundedRectangle(width=7, height=4, corner_radius=0.5)
        pool_rect_text = Tex('Pool').next_to(pool_rect, U)
        self.play(ReplacementTransform(program_or_concept_text, pool_rect_text),
                  ReplacementTransform(amm_acronym_text, pool_rect))

        ##### 이 유동성 풀은 우리가 중앙화 거래소에서 봤던 거래쌍이라고 생각하시면 됩니ㅏㄷ
        ##### 우리가 비티씨나 테더를 들고 중앙화 거래소에서 비티씨테더 거래쌍 창으로 가듯이
        ##### 덱스에서는 유동성 풀에 접근해서 거래를 하게됩니다
        ##### 그렇다면 비티씨테더 풀이라는 것은 이더리움 같은게 아니라 비티씨와 테더를 가지고 있어야할 것입니다
        # 풀위에 비티씨 테더라고 텍스트 하나 더 생기고
        # 비티씨 덩어리 테더 덩어리 풀로 풍덩

        btc_usdt_text = Tex('BTC/USDT').next_to(pool_rect_text, U)
        btc_usdt_text_final = Tex('BTC/USDT Pool').move_to(pool_rect_text)

        self.play(Create(btc_usdt_text))
        self.play(ReplacementTransform(VGroup(pool_rect_text, btc_usdt_text), btc_usdt_text_final))

        btc_lump = LabeledDot('BTC', radius=1, color=ORANGE).shift(L * 5.5)
        usdt_lump = LabeledDot('USDT', radius=1, color=GREEN_C).shift(R * 5.5)
        btc_lump.save_state()
        usdt_lump.save_state()
        btc_lump_arc = Arc(radius=2, angle=PI).flip(axis=np.array([ 0, 1, 0 ])).shift(L * 3.5)
        usdt_lump_arc = Arc(radius=2, angle=PI).shift(R * 3.5)

        self.play(Create(btc_lump),
                  Create(usdt_lump))
        self.play(MoveAlongPath(btc_lump, btc_lump_arc),
                  MoveAlongPath(usdt_lump, usdt_lump_arc))

        ##### 중앙화 거래소 비티씨테더 페어에서 사람들이 이더리움을 들고 모인게 아니라
        ##### 비티씨와 테더를 들고 모인것 처럼 말입니다
        # 옆에 이더리움 솔라나 생기고 엑스자 후 페이드 아웃

        sol_lump = LabeledDot('SOL', radius=1, color=PURPLE_E).shift(L * 5.5 + U * 1)
        eth_lump = LabeledDot('ETH', radius=1, color=DARK_BLUE).shift(R * 5.5 + U * 2)
        dot_lump = LabeledDot('DOT', radius=1, color=MAROON_C).shift(R * 5.5 + D * 3)
        sol_lump_cross = Cross(stroke_width=15).scale(1.5).move_to(sol_lump)
        eth_lump_cross = Cross(stroke_width=15).scale(1.5).move_to(eth_lump)
        dot_lump_cross = Cross(stroke_width=15).scale(1.5).move_to(dot_lump)
        other_coins = VGroup(sol_lump, eth_lump, dot_lump)
        other_coins_cross = VGroup(sol_lump_cross, eth_lump_cross, dot_lump_cross)

        self.play(Create(other_coins))
        self.play(Create(other_coins_cross))
        self.play(Uncreate(other_coins),
                  Uncreate(other_coins_cross))

        ##### 당연한 얘기지만 비티씨 테더 페어에 만약 비티씨만 존재한다면 아무것도 일어나지 않을 것입니다
        ##### 왜냐하면 비티씨 테더 페어라는 것은 두가지의 교환이 일어나는 공간이라는 것인데
        ##### 둘 중 하나만 있으면 교환이 성립하지 않으니까요
        # 먼저 테더 없애고 풀에 비티씨만 남은 거 보여주면서 정지
        # 사이클릭 리플레이스 데어 앤 백
        # 그 다음은 테더가 다시 생기고 비티씨가 없어진 상태를 보여주면 서 정지
        # 사임클릭 리플레이스 데어 앤 백

        exchange_speech_text_1 = Tex(r'I am here to\\get USDT with my BTC').shift(5.5 * R + 3 * D).scale(0.7)
        long_face_1 = Tex(':(').rotate(-PI / 2).move_to(exchange_speech_text_1).scale(3)
        btc_lump_long_face = btc_lump.copy().shift(R * 15)

        self.play(FadeOut(usdt_lump))
        self.play(Create(exchange_speech_text_1),
                  btc_lump_long_face.animate.move_to(R * 5))
        self.play(ReplacementTransform(exchange_speech_text_1, long_face_1))
        self.play(Uncreate(long_face_1),
                  Uncreate(btc_lump_long_face))
        self.play(FadeIn(usdt_lump))

        exchange_speech_text_2 = Tex(r'I am here to\\get BTC with my USDT').shift(5.5 * L + 3 * D).scale(0.7)
        long_face_2 = Tex(':(').rotate(-PI / 2).move_to(exchange_speech_text_2).scale(3)
        usdt_lump_long_face = usdt_lump.copy().shift(L * 15)

        self.play(FadeOut(btc_lump))
        self.play(Create(exchange_speech_text_2), usdt_lump_long_face.animate.move_to(L * 5))
        self.play(ReplacementTransform(exchange_speech_text_2, long_face_2))
        self.play(Uncreate(long_face_2),
                  Uncreate(usdt_lump_long_face))
        self.play(FadeIn(btc_lump))

        ##### 그래서 우리는 풀에 사람들이 거래할 수 있도록 유동성을 공급하고
        ##### 유동성을 공급한다는 것은 비티씨와 테더를 같이 넣어준다는 것입니다
        ##### 반드시 같이 넣어야하는 이유는 곧 알게됩니다
        # 왼쪽에서 비티씨하고 테더 같이 들어감
        # 오른쪽에서 비티씨하고 테더하고 같이 들어감
        btc_lump_liq_prov_1 = btc_lump.copy().move_to(np.array([ -6, 2, 0 ]))
        usdt_lump_liq_prov_1 = usdt_lump.copy().move_to(np.array([ -6, -2, 0 ]))
        btc_lump_liq_prov_2 = btc_lump.copy().move_to(np.array([ 6, 2, 0 ]))
        usdt_lump_liq_prov_2 = usdt_lump.copy().move_to(np.array([ 6, -2, 0 ]))

        self.play(Create(VGroup(btc_lump_liq_prov_1, usdt_lump_liq_prov_1, btc_lump_liq_prov_2, usdt_lump_liq_prov_2)))
        self.play(FadeOut(btc_lump_liq_prov_1, target_position=pool_rect),
                  FadeOut(usdt_lump_liq_prov_1, target_position=pool_rect),
                  btc_lump.animate.scale(1.1),
                  usdt_lump.animate.scale(1.1))
        self.play(FadeOut(btc_lump_liq_prov_2, target_position=pool_rect),
                  FadeOut(usdt_lump_liq_prov_2, target_position=pool_rect),
                  btc_lump.animate.scale(1.1),
                  usdt_lump.animate.scale(1.1))

        ##### 덱스의 있는 참여자는 크게 두 종류입니다
        ##### 유동성 제공자와 거래자입니다
        ##### 유동성 제공자는 영어로 줄여서 엘피라고도 부릅니다
        # 중앙에는 여전히 풀이 있고 그 위에 덱스 파티시 펀트라고 텍스트 생김
        # 덱스파티시펀트 트리로 갈라지고 유동성제공자
        dex_participants_text = Tex('DEX Participants').scale(1.2).to_edge(U)
        liq_prov_text = Tex('Liq Provider').shift(L * 5.5 + U * 2.5)
        trader_text = Tex('Trader').shift(R * 5.5 + U * 2.5)
        line_to_liq_prov = Line(dex_participants_text.get_corner(DL), liq_prov_text.get_top())
        line_to_trader = Line(dex_participants_text.get_corner(DR), trader_text.get_top())

        self.play(Create(dex_participants_text))
        self.play(Create(line_to_liq_prov),
                  Create(line_to_trader))
        self.play(Create(liq_prov_text),
                  Create(trader_text))

        ##### 유동성 제공자는 아까처럼 말한 것처럼 비티씨와 테더를 같이 넣어주거나 빼면서
        ##### 유동성을 조절합니다. 즉 풀 사이즈를 키우거나 줄입니다. 이것은 나중에 보겠지만
        ##### 케이값을 움직이는 것입니다. 곧 보게 될테니 걱정 안 하셔도 됩니다
        # 유동성 제공자 텍스트 밑에 엔터티 만들고 엔터티가 비티씨와 테더를 함께 풀에 넣는 모션
        # 그리고 밑에 텍스트로 체인징 케이 옆에 조그맣게 그래프 케이값 왔다 갔다
        liq_provider = create_entity(Tex(r' \emph{Init Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "BTC", ORANGE, 1.4,
                                     0.3).next_to(liq_prov_text, D)
        liq_prov_btc_asset = liq_provider[ 1 ]
        liq_prov_usdt_asset = create_entity("A", 0.5, WHITE, "USDT", BLUE, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)
        liq_provider.add(liq_prov_usdt_asset)
        self.play(Create(liq_provider))

        moving_k_text = Tex('Moving K').shift(L * 5.5 + D * 1.5)
        liq_prov_tracker = ValueTracker(5)

        coor_sys_liq_prov = Axes(x_range=[ 0, 10, 2 ], y_range=[ 0, 10, 2 ], x_length=2, y_length=2, tips=False,
                                 y_axis_config={"include_numbers": False, 'include_tip': True, 'include_ticks': False, 'tip_width': 0.1,
                                                'tip_height': 5},
                                 x_axis_config={"include_numbers": False, 'include_tip': True, 'include_ticks': False, 'tip_width': 0.1,
                                                'tip_height': 5}
                                 ).next_to(moving_k_text, D)

        liq_prov_graph = coor_sys_liq_prov.plot(lambda x: 5 / x, x_range=[ 5 / 8, 8 ], use_smoothing=False, color=WHITE)
        liq_prov_graph.add_updater(lambda graph: graph.become(
            coor_sys_liq_prov.plot(lambda x: liq_prov_tracker.get_value() / x, x_range=[ liq_prov_tracker.get_value() / 8, 8 ],
                                   use_smoothing=False, color=WHITE)))

        self.play(Create(moving_k_text))
        self.play(Create(coor_sys_liq_prov),
                  Create(liq_prov_graph))
        self.play(liq_prov_tracker.animate.set_value(9))
        self.play(liq_prov_tracker.animate.set_value(1))
        liq_prov_btc_asset.save_state()
        liq_prov_usdt_asset.save_state()
        self.play(liq_prov_tracker.animate.set_value(9),
                  FadeOut(liq_prov_btc_asset, target_position=btc_lump),
                  FadeOut(liq_prov_usdt_asset, target_position=usdt_lump),
                  btc_lump.animate.scale(1.1),
                  usdt_lump.animate.scale(1.1))
        liq_prov_btc_asset.restore()
        liq_prov_usdt_asset.restore()
        self.play(liq_prov_tracker.animate.set_value(1),
                  FadeIn(liq_prov_btc_asset, target_position=btc_lump),
                  FadeIn(liq_prov_usdt_asset, target_position=usdt_lump),
                  btc_lump.animate.scale(1/1.1),
                  usdt_lump.animate.scale(1/1.1))

        ##### 거래자들은 풀에 자신이 테더를 넣고 그에 상응하는 비트코인을 빼가든지
        ##### 가진 비트코인을 넣고 그에 상응하는 테더를 빼가든지 할 수 있습니다
        ##### 각각 비트코인 매도와 매수에 대응하는 행위입니다
        ##### 이것은 그래프위의 점을 이동시키는 행위입니다.
        ##### 이것또한 곳 보게 될테니 걱정 안 하셔도 됩니다
        ##### 유동성제공자는 케이값을 움직이고 거래자는 점을 이동시킨다라고만 기억해두십시오
        ##### 그리고 유동성 제공자는 거래자들이 내는 수수료를 받으면서 수익을 냅니다
        ##### 거래자들은 코인을 사고 팔며 가격차익을 얻습니다
        # 거래자 텍스트 밑에 엔터티 만들고 엔터티가 비티씨넣고 풀에서 테더 돌려받고
        # 테더 넣고 비티씨 돌렵받는 모션
        # 그리고 무빙 닷 텍스트 밑에ㅔ 띄우거 옆에는 작은 그래프에서 점왔다갔다
        # 트리 구조 전부 사라짐
        trader = create_entity(Tex(r' \emph{Trader}', color=BLACK).scale(0.9), 1, WHITE, "BTC", ORANGE, 1.4,
                               0.3).next_to(trader_text, D)
        trader_btc_asset = trader[ 1 ]
        trader_usdt_asset = create_entity("A", 0.5, WHITE, "USDT", BLUE, 1.4, 0.3)[ 1 ].next_to(trader, DOWN, buff=0.1)
        trader_usdt_asset_copy = create_entity("A", 0.5, WHITE, "USDT", BLUE, 1.4, 0.3)[ 1 ].move_to(trader_btc_asset)
        trader.add(trader_usdt_asset)
        self.play(Create(trader))

        moving_dot_text = Tex('Moving Dot').shift(R * 5.5 + D * 1.5)
        trader_tracker = ValueTracker(3)

        coor_sys_trader = Axes(x_range=[ 0, 10, 2 ], y_range=[ 0, 10, 2 ], x_length=2, y_length=2, tips=False,
                               y_axis_config={"include_numbers": False, 'include_tip': True, 'include_ticks': False, 'tip_width': 0.1,
                                              'tip_height': 5},
                               x_axis_config={"include_numbers": False, 'include_tip': True, 'include_ticks': False, 'tip_width': 0.1,
                                              'tip_height': 5}
                               ).next_to(moving_dot_text, D)

        trader_graph = coor_sys_trader.plot(lambda x: 5 / x, x_range=[ 5 / 8, 8 ], use_smoothing=False, color=WHITE)
        curr_dot = Dot(radius=0.1, color=RED).move_to(coor_sys_trader.c2p(trader_tracker.get_value(),
                                                                          trader_graph.underlying_function(trader_tracker.get_value())))
        curr_dot.set_z_index(2)
        curr_dot.add_updater(lambda dot: dot.move_to(coor_sys_trader.c2p(trader_tracker.get_value(),
                                                                         trader_graph.underlying_function(trader_tracker.get_value()))))

        self.play(Create(moving_dot_text))

        self.play(Create(coor_sys_trader),
                  Create(trader_graph),
                  Create(curr_dot))
        self.play(trader_tracker.animate.set_value(6))
        self.play(trader_tracker.animate.set_value(1))

        self.play(trader_tracker.animate.set_value(6),
                  FadeOut(trader_btc_asset, target_position=btc_lump),
                  FadeIn(trader_usdt_asset_copy, target_position=usdt_lump),
                  btc_lump.animate.scale(1.1),
                  usdt_lump.animate.scale(1/1.1))
        self.play(trader_tracker.animate.set_value(1),
                  FadeIn(trader_btc_asset, target_position=btc_lump),
                  FadeOut(trader_usdt_asset_copy, target_position=usdt_lump),
                  btc_lump.animate.scale(1/1.1),
                  usdt_lump.animate.scale(1.1))

        ##### 풀이 운영되는 기본 원칙은 언제나 같은 가치의 자산이 들어있게 한다는 것입니다
        ##### 그래서 이걸 기반으로 오토매틱 마켔메이커는 가격을 산정합니다
        ##### 현재 풀의 상태를 10비티씨와 3000테더라고 하겠습니다
        ##### 10비트와 3000테더가 같은 가치기 때문에
        ##### 비티씨는 1개에 300테더입니다

        # 올웨이즈 이퀄 밸류 우측 상단에 띄우면서 풀 내부에 비티씨 테더 사이에 이콜 싸인
        # 올웨이즈 이퀄 밸류 텍스트가 에이엠엠 프라이스 디터미네이션으로 트랜스폼
        equal_sign = Tex('=').scale(1.5)
        always_equal_value = Tex('Always Equal Values')
        price_determination = Tex('Price determined')
        always_equal_value_texts = VGroup(always_equal_value, price_determination).arrange(D).shift(D * 3)

        value_equal_1 = MathTex(r'Value\  of\  BTC in Pool', '=', r'Value\  of\   USDT in Pool').arrange(D).scale(0.94).shift(D * 3)
        value_equal_2 = MathTex(r'10 BTC', '=', r'3000 USDT').shift(D * 3)

        price_frac = MathTex(r'\frac{3000 USDT}{10 BTC}').shift(D * 3)

        final_price_per_btc = MathTex(r'300 USDT\  per \  BTC').shift(D * 3)

        self.play(Create(always_equal_value_texts))
        self.play(Create(equal_sign))

        self.play(ReplacementTransform(always_equal_value_texts, value_equal_1))
        self.play(ReplacementTransform(value_equal_1, value_equal_2))
        self.play(ReplacementTransform(value_equal_2, price_frac))
        self.play(ReplacementTransform(price_frac, final_price_per_btc))

        ##### 이것은 모두 미리 작성된 프로그래밍 언어의 스크립트를 실행하는 것으로 이루어집니다
        ##### 스마트 컨트랙트 덕분에 우리는 중앙화 거래서와 같은 제3자를 거치지 않을 수 있게 됐습니다
        all_thanks_to = Tex('Everything without 3rd entity', 'All thanks to Smart Contract').arrange(D).shift(D * 3)
        self.play(ReplacementTransform(final_price_per_btc, all_thanks_to))

class L_02_S_05_amm_xyk_basics_with_math(Scene):
    def construct(self):
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

class L_02_S_06_amm_xyk_adv_k_up_1(Scene):
    def construct(self):
        # self.play(Create(NumberPlane()))

        ##### ###############################################################################################################

        ##### 아까본 와이는 엑스분의 30000을 원점으로 생각하고 실제 상황에 따라 어떻게 변하는지 보겠습니다.
        ##### 먼저 유동성 공급자의 활동을 알아보겠ㅅ브니다
        ##### 유동성을 공급하는 상황입니다.최초 유동성 공급 부터 그 이후 유동성 추가하는 것을 살펴보겠ㅅ브니다
        # 기본 셋업

        # 케이 바리어블, 초기 엘피, 좌표계
        xyk_fraction = MathTex('y', '=', r'\frac{k}{x}').to_edge(UL)

        liq_pool_rect = RoundedRectangle(height=6.3, width=4, corner_radius=0.5)
        liq_pool_text = Tex('Liquidity Pool').next_to(liq_pool_rect, UP)
        liq_pool = VGroup(liq_pool_rect, liq_pool_text).to_edge(UL).shift(R*0.5)
        liq_pool.set_z_index(3)

        k_var = Variable(30000, MathTex("k"), var_type=Integer).to_edge(UR)
        k_tracker = k_var.tracker
        k_tracker.set_value(30000)

        self.play(Create(liq_pool))

        liq_provider = create_entity(Tex(r' \emph{Init Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", ORANGE, 1.4,
                                     0.3).next_to(liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", GREEN, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)
        liq_provider.add(usdt_asset)

        self.play(Create(liq_provider))

        ax = Axes(x_range=[ 0, 18, 4 ], y_range=[ 0, 6500, 1000 ], x_length=5, y_length=5, tips=True,
                  axis_config={"include_numbers": False, 'color': WHITE, 'include_ticks': False, 'font_size': 20}, ).to_edge(DR,buff = 0.8)

        ax.shift(U*(liq_pool_rect.get_bottom()[1]-ax[0].get_y()))

        y_axis_label = ax.get_y_axis_label(MathTex('Amount of USDT in Pool', color=WHITE).rotate(PI / 2).scale(0.4), edge=LEFT,
                                           direction=LEFT, buff=0.37)
        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool', color=WHITE).scale(0.4), edge=DOWN, direction=DOWN, buff=0.5)
        axis_labels = VGroup(x_axis_label, y_axis_label)

        usdt_bar = Rectangle(height=3, width=1.2, fill_color=GREEN, fill_opacity=1, color=GREEN)
        btc_bar = Rectangle(height=1, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE)
        bars = VGroup(btc_bar, usdt_bar)
        bars.arrange(RIGHT, aligned_edge=DOWN).move_to(liq_pool_rect).align_to(liq_pool_rect, DOWN)

        usdt_bar_pos = usdt_bar.get_bottom()
        btc_bar_pos = btc_bar.get_bottom()

        btc_var = Variable(10, MathTex("BTC"), var_type=Integer)
        usdt_var = Variable(3000, MathTex("USDT"), var_type=Integer).next_to(btc_var, DOWN, aligned_edge=LEFT)
        btc_tracker = btc_var.tracker
        usdt_tracker = usdt_var.tracker
        usdt_var[ 0 ][ 0 ].set_color(GREEN)
        btc_var[ 0 ][ 0 ].set_color(ORANGE)

        vars = VGroup(btc_var, usdt_var).arrange(DOWN, aligned_edge=LEFT).next_to(liq_pool_rect, DOWN, buff=0.25)

        self.play(ReplacementTransform(usdt_asset, usdt_bar),
                  ReplacementTransform(btc_asset, btc_bar))
        self.play(Write(usdt_var),
                  Write(btc_var))
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=GREEN, fill_opacity=1, color=GREEN).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        pool_price = Variable(100, 'Price', var_type=DecimalNumber, num_decimal_places=2).next_to(
            liq_pool_rect, RIGHT, buff=1.5).to_edge(UP)
        pool_price_tracker = pool_price.tracker
        pool_price.add_updater(lambda v: pool_price_tracker.set_value(usdt_tracker.get_value() / btc_tracker.get_value()))
        pool_price_unit = Tex(r'\$').next_to(pool_price, buff=0.1)
        self.play(Write(k_var[ 0 ]))
        self.play(Create(ax),
                  Create(axis_labels),
                  Create(pool_price_unit),
                  Create(pool_price),
                  TransformMatchingShapes(Group(btc_var[ 1 ].copy(), usdt_var[ 1 ].copy()), k_var[ 1 ].copy()),
                  Create(xyk_fraction.next_to(k_var, LEFT, buff=1))
                  )

        lp_amt_form_1 = MathTex(r'Init\  l =\sqrt{x \times y}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_2 = MathTex(r'Init\  l =\sqrt{10 \times 3000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_3 = MathTex(r'Init\  l =\sqrt{30000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_int = Tex(rf'{int(30000 ** (1 / 2))} LP token').move_to(lp_amt_form_1).scale(0.7)

        self.play(Create(lp_amt_form_1))
        self.play(TransformMatchingShapes(lp_amt_form_1, lp_amt_form_2))
        self.play(TransformMatchingShapes(lp_amt_form_2, lp_amt_form_3))
        self.play(TransformMatchingShapes(lp_amt_form_3, lp_amt_int))

        box = Rectangle(width=1.6, height=1, fill_color=WHITE, stroke_color=WHITE, fill_opacity=1)
        text = Tex(r"173\\BTC-USDT\\LP", color=BLACK).scale(0.5)
        lp_asset = VGroup(box, text).next_to(liq_provider[ 0 ], DOWN, buff=0.1)

        self.play(Create(lp_asset),
                  Uncreate(lp_amt_int))

        self.play(FadeOut(liq_provider),
                  FadeOut(lp_amt_int),
                  FadeOut(lp_asset))

        xyk_graph_btc = ax.plot(lambda x: k_tracker.get_value() / x,
                                x_range=[ 0.00001, 6000 ],
                                use_smoothing=False, color=WHITE)

        xyk_graph_btc.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: k_tracker.get_value() / x,
                    x_range=[ k_tracker.get_value() / 6000, 16 ],
                    use_smoothing=False, color=WHITE)))

        curr_dot = Dot(radius=0.1, color=GREY).move_to(ax.c2p(btc_tracker.get_value(),
                                                              xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        curr_dot.set_z_index(2)

        curr_dot.add_updater(lambda dot: dot.move_to(ax.c2p(btc_tracker.get_value(),
                                                            xyk_graph_btc.underlying_function(btc_tracker.get_value()))))

        vertical_line = ax.get_vertical_line(ax.c2p(btc_tracker.get_value(),
                                                    xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        horizontal_line = ax.get_horizontal_line(ax.c2p(btc_tracker.get_value(),
                                                        xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        new_horzontal_line = VGroup()
        for i in range(1, len(horizontal_line) + 1):
            new_horzontal_line.add(horizontal_line[ -i ])

        horizontal_line = new_horzontal_line
        x_marker = Triangle(color=ORANGE, fill_color=ORANGE, fill_opacity=1).scale(0.1).next_to(vertical_line, DOWN, buff=0)
        x_marker.add_updater(lambda marker: marker.next_to(vertical_line, DOWN, buff=0))
        x_marker_val = Integer(btc_tracker.get_value())
        x_marker_val.add_updater(
            lambda integer: integer.become(Integer(btc_tracker.get_value()).scale(0.4).next_to(vertical_line, DOWN, buff=0.3)))

        y_marker = Triangle(color=GREEN, fill_color=GREEN, fill_opacity=1).scale(0.1).rotate(-PI / 2).next_to(horizontal_line, LEFT, buff=0)
        y_marker.add_updater(lambda marker: marker.next_to(horizontal_line, LEFT, buff=0))
        y_marker_val = Integer(usdt_tracker.get_value())
        y_marker_val.add_updater(lambda integer: integer.become(
            Integer(usdt_tracker.get_value()).scale(0.4).rotate(PI / 2).next_to(horizontal_line, LEFT, buff=0.3)))

        lines = VGroup(vertical_line, horizontal_line)
        markers = VGroup(x_marker, x_marker_val, y_marker, y_marker_val)

        self.play(Create(xyk_graph_btc))
        self.play(Create(curr_dot))

        self.play(Create(lines), run_time=2)
        self.play(Create(markers), run_time=2)

        vertical_line.add_updater(lambda line: line.become(ax.get_vertical_line(ax.c2p(btc_tracker.get_value(),
                                                                                       xyk_graph_btc.underlying_function(
                                                                                           btc_tracker.get_value())))))
        horizontal_line.add_updater(lambda line: line.become(ax.get_horizontal_line(ax.c2p(btc_tracker.get_value(),
                                                                                           xyk_graph_btc.underlying_function(
                                                                                               btc_tracker.get_value())))))

        area = Rectangle(width=curr_dot.get_x() - ax.get_origin()[ 0 ], height=curr_dot.get_y() - ax.get_origin()[ 1 ], fill_color=BLUE,
                         fill_opacity=0.5, stroke_width=0).align_to(curr_dot.get_center(), UR)
        area.add_updater(lambda area: area.become(
            Rectangle(width=curr_dot.get_x() - ax.get_origin()[ 0 ], height=curr_dot.get_y() - ax.get_origin()[ 1 ], fill_color=BLUE,
                      fill_opacity=0.5, stroke_width=0).align_to(curr_dot.get_center(), UR)))

        area_text = MathTex(r'BTC \times  USDT').scale(0.5).arrange(DOWN, buff=0.1)
        area_text.add_updater(
            lambda text: text.become(MathTex(r'BTC \times USDT', 'in \  Pool').scale(0.4).arrange(DOWN, buff=0.1).move_to(area)))

        self.play(Create(area))
        self.play(Create(area_text))

        #####
        ##### 유동성을 공급한다는 것은 무엇을 의미할까요
        ##### 엑스와 와이가 오르면서 케이의 값이 함께 오른다는 것입니다
        #####

        btc_bar.clear_updaters()
        usdt_bar.clear_updaters()

        liq_provider = create_entity(Tex(r' \emph{New Liq\\provider}', color=BLACK).scale(0.8), 1, WHITE, "3 BTC", ORANGE, 1.4,
                                     0.3).next_to(
            liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "900 USDT", GREEN, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)

        self.play(Create(VGroup(liq_provider, usdt_asset)))

        scene3_13btc_box = Rectangle(width=btc_bar.width, height=btc_bar.height * 0.3, stroke_width=3,
                                     stroke_color=GREEN_E).next_to(btc_bar, UP, buff=0)
        scene3_3900usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.3, stroke_width=3,
                                        stroke_color=GREEN_E).next_to(usdt_bar, UP, buff=0)

        self.play(Create(VGroup(scene3_13btc_box, scene3_3900usdt_box)))

        scene3_3900usdt_fill_box = scene3_3900usdt_box.copy().set_fill(GREEN, opacity=1)
        scene3_13btc_fill_box = scene3_13btc_box.copy().set_fill(ORANGE, opacity=1)
        scene3_13btc_fill_box.set_stroke(width=0, opacity=0)
        scene3_3900usdt_fill_box.set_stroke(width=0, opacity=0)

        scene3_13btc_fill_box.set_z_index(3)
        scene3_3900usdt_fill_box.set_z_index(3)

        scene3_3900usdt_brace = BraceBetweenPoints(scene3_3900usdt_box.get_corner(UR), scene3_3900usdt_box.get_corner(DR), color=GREEN_E,
                                                   stroke_color=GREEN_E,
                                                   stroke_width=3,
                                                   ).flip(axis=np.array([ 0., 1., 0. ])).next_to(scene3_3900usdt_fill_box,
                                                                                                 RIGHT)
        scene3_13btc_brace = BraceBetweenPoints(scene3_13btc_box.get_corner(UL), scene3_13btc_box.get_corner(DL), color=GREEN_E,
                                                stroke_color=GREEN_E, stroke_width=3
                                                ).next_to(scene3_13btc_fill_box,
                                                          LEFT)

        scene3_3900usdt_brace_label = Integer(btc_tracker.get_value())
        scene3_3900usdt_brace_label.add_updater(lambda label: label.become(
            Integer(900).scale(0.4).rotate(-PI / 2).next_to(scene3_3900usdt_brace, RIGHT, buff=0.3)))
        scene3_13btc_brace_label = Integer(usdt_tracker.get_value())
        scene3_13btc_brace_label.add_updater(lambda label: label.become(
            Integer(3).scale(0.4).rotate(PI / 2).next_to(scene3_13btc_brace, LEFT, buff=0.3)))

        scene3_braces = VGroup(scene3_3900usdt_brace, scene3_13btc_brace)
        scene3_brace_labels = VGroup(scene3_3900usdt_brace_label, scene3_13btc_brace_label)

        new_liquidity_text = MathTex('3BTC', '=', '900USDT').scale(0.5).next_to(liq_provider, DOWN, buff=2)

        scene3_origin_graph = xyk_graph_btc.copy()
        scene3_origin_graph.clear_updaters()
        scene3_origin_graph.set_color(RED)
        scene3_origin_graph.set_z_index(-1)
        self.add(scene3_origin_graph)

        self.play(Create(scene3_braces),
                  Create(scene3_brace_labels))

        box = Rectangle(width=1.6, height=1, fill_color=WHITE, stroke_color=WHITE, fill_opacity=1)
        text = Tex(r"87\\BTC-USDT\\LP", color=BLACK).scale(0.5)
        new_liq_provider_lp_asset = VGroup(box, text).next_to(liq_provider[ 0 ], DOWN, buff=0.1)

        lp_add_form_1 = MathTex(r"Added\  {l}' =l\times\frac{{x}'}{x}").next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_add_form_2 = MathTex(r"Added\  {l}' =\sqrt{30000}\times\frac{3}{10}").move_to(lp_add_form_1).scale(0.7)
        lp_add_form_3 = MathTex(r"Added\  {l}' =173\times0.3").move_to(lp_add_form_1).scale(0.7)
        lp_add_int = Tex(rf"{int(30000 ** (1 / 2) *3/10)} LP token").move_to(lp_add_form_1).scale(0.7)
        total_lp_supply_1 = MathTex(r"Total\  l =l+{l}'").next_to(lp_add_form_1, UP).scale(0.7)
        total_lp_supply_2 = MathTex(r"Total\  l =173+86").move_to(lp_add_form_1).scale(0.7)
        total_lp_supply_int = Tex(rf"{int(30000 ** (1 / 2) + 30000 ** (1 / 2) *3/10)} LP token").move_to(lp_add_form_1).scale(0.7)

        self.play(Create(lp_add_form_1))
        self.play(TransformMatchingShapes(lp_add_form_1, lp_add_form_2))
        self.play(TransformMatchingShapes(lp_add_form_2, lp_add_form_3))
        self.play(TransformMatchingShapes(lp_add_form_3, lp_add_int))
        self.play(Uncreate(lp_add_int))

        self.play(Create(total_lp_supply_1))
        self.play(TransformMatchingShapes(total_lp_supply_1, total_lp_supply_2))
        self.play(TransformMatchingShapes(total_lp_supply_2, total_lp_supply_int))
        self.play(Uncreate(total_lp_supply_int))

        usdt_asset.save_state()
        btc_asset.save_state()
        self.play(k_tracker.animate.set_value(50700),
                  btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(50700 / 13),
                  ReplacementTransform(usdt_asset, scene3_3900usdt_fill_box),
                  ReplacementTransform(btc_asset, scene3_13btc_fill_box),
                  FadeIn(new_liq_provider_lp_asset, target_position=liq_pool_rect),
                  run_time=6)

        new_user_share_1 = MathTex(r"Share =\frac{UserLP}{TotSupply}").move_to(lp_add_form_1).scale(0.7)
        new_user_share_2 = MathTex(r"Share =0.23").move_to(lp_add_form_1).scale(0.7)
        new_user_share_3 = Tex(r"23\%").move_to(lp_add_form_1)

        self.play(Create(new_user_share_1))
        self.play(ReplacementTransform(new_user_share_1, new_user_share_2))
        self.play(TransformMatchingShapes(new_user_share_2, new_user_share_3))
        self.play(Uncreate(new_user_share_3))

        usdt_asset.restore()
        btc_asset.restore()

        dummydot = Dot(1, color=RED).move_to(liq_pool_rect)

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(30000 / 10),
                  Transform(scene3_3900usdt_fill_box, usdt_asset),
                  Transform(scene3_13btc_fill_box, btc_asset),
                  FadeOut(new_liq_provider_lp_asset, target_position=dummydot),
                  run_time=6)

        self.wait(4)

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

class L_02_S_07_amm_xyk_adv_k_dn_2(Scene):
    def construct(self):
        ##### ###############################################################################################################

        ##### 이제는 유동성을 제거하는 상황을 보겟ㅅ븐디
        #####
        ##### 유동성을 제거한다는 것은 풀에서 자기 지분만큼 비트와 테더를 빼가는 것입니다
        ##### 케이값이 작아졌습니다
        # 기본 셋업

        # 케이 바리어블, 초기 엘피, 좌표계
        xyk_fraction = MathTex('y', '=', r'\frac{k}{x}').to_edge(UL)

        liq_pool_rect = RoundedRectangle(height=6.3, width=4, corner_radius=0.5)
        liq_pool_text = Tex('Liquidity Pool').next_to(liq_pool_rect, UP)
        liq_pool = VGroup(liq_pool_rect, liq_pool_text).to_edge(UL).shift(R*0.5)
        liq_pool.set_z_index(3)

        k_var = Variable(30000, MathTex("k"), var_type=Integer).to_edge(UR)
        k_tracker = k_var.tracker
        k_tracker.set_value(30000)

        self.play(Create(liq_pool))

        liq_provider = create_entity(Tex(r' \emph{Init Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", ORANGE, 1.4,
                                     0.3).next_to(liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", GREEN, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)
        liq_provider.add(usdt_asset)

        self.play(Create(liq_provider))

        ax = Axes(x_range=[ 0, 18, 4 ], y_range=[ 0, 6500, 1000 ], x_length=5, y_length=5, tips=True,
                  axis_config={"include_numbers": False, 'color': WHITE, 'include_ticks': False, 'font_size': 20}, ).to_edge(DR,buff = 0.8)

        ax.shift(U*(liq_pool_rect.get_bottom()[1]-ax[0].get_y()))


        y_axis_label = ax.get_y_axis_label(MathTex('Amount of USDT in Pool', color=WHITE).rotate(PI / 2).scale(0.4), edge=LEFT,
                                           direction=LEFT, buff=0.37)
        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool', color=WHITE).scale(0.4), edge=DOWN, direction=DOWN, buff=0.5)
        axis_labels = VGroup(x_axis_label, y_axis_label)

        usdt_bar = Rectangle(height=3, width=1.2, fill_color=GREEN, fill_opacity=1, color=GREEN)
        btc_bar = Rectangle(height=1, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE)
        bars = VGroup(btc_bar, usdt_bar)
        bars.arrange(RIGHT, aligned_edge=DOWN).move_to(liq_pool_rect).align_to(liq_pool_rect, DOWN)

        usdt_bar_pos = usdt_bar.get_bottom()
        btc_bar_pos = btc_bar.get_bottom()

        btc_var = Variable(10, MathTex("BTC"), var_type=Integer)
        usdt_var = Variable(3000, MathTex("USDT"), var_type=Integer).next_to(btc_var, DOWN, aligned_edge=LEFT)
        btc_tracker = btc_var.tracker
        usdt_tracker = usdt_var.tracker
        usdt_var[ 0 ][ 0 ].set_color(GREEN)
        btc_var[ 0 ][ 0 ].set_color(ORANGE)

        vars = VGroup(btc_var, usdt_var).arrange(DOWN, aligned_edge=LEFT).next_to(liq_pool_rect, DOWN, buff=0.25)

        self.play(ReplacementTransform(usdt_asset, usdt_bar),
                  ReplacementTransform(btc_asset, btc_bar))
        self.play(Write(usdt_var),
                  Write(btc_var))
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=GREEN, fill_opacity=1, color=GREEN).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        pool_price = Variable(100, 'Price', var_type=DecimalNumber, num_decimal_places=2).next_to(
            liq_pool_rect, RIGHT, buff=1.5).to_edge(UP)
        pool_price_tracker = pool_price.tracker
        pool_price.add_updater(lambda v: pool_price_tracker.set_value(usdt_tracker.get_value() / btc_tracker.get_value()))
        pool_price_unit = Tex(r'\$').next_to(pool_price, buff=0.1)
        self.play(Write(k_var[ 0 ]))
        self.play(Create(ax),
                  Create(axis_labels),
                  Create(pool_price_unit),
                  Create(pool_price),
                  TransformMatchingShapes(Group(btc_var[ 1 ].copy(), usdt_var[ 1 ].copy()), k_var[ 1 ].copy()),
                  Create(xyk_fraction.next_to(k_var, LEFT, buff=1))
                  )

        lp_amt_form_1 = MathTex(r'Init\  l =\sqrt{x \times y}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_2 = MathTex(r'Init\  l =\sqrt{10 \times 3000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_3 = MathTex(r'Init\  l =\sqrt{30000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_int = Tex(rf'{int(30000 ** (1 / 2))} LP token').move_to(lp_amt_form_1).scale(0.7)

        self.play(Create(lp_amt_form_1))
        self.play(TransformMatchingShapes(lp_amt_form_1, lp_amt_form_2))
        self.play(TransformMatchingShapes(lp_amt_form_2, lp_amt_form_3))
        self.play(TransformMatchingShapes(lp_amt_form_3, lp_amt_int))

        box = Rectangle(width=1.6, height=1, fill_color=WHITE, stroke_color=WHITE, fill_opacity=1)
        text = Tex(r"173\\BTC-USDT\\LP", color=BLACK).scale(0.5)
        lp_asset = VGroup(box, text).next_to(liq_provider[ 0 ], DOWN, buff=0.1)

        self.play(Create(lp_asset),
                  Uncreate(lp_amt_int))

        self.play(FadeOut(liq_provider),
                  FadeOut(lp_amt_int),
                  FadeOut(lp_asset))

        xyk_graph_btc = ax.plot(lambda x: k_tracker.get_value() / x,
                                x_range=[ 0.00001, 6000 ],
                                use_smoothing=False, color=WHITE)

        xyk_graph_btc.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: k_tracker.get_value() / x,
                    x_range=[ k_tracker.get_value() / 6000, 16 ],
                    use_smoothing=False, color=WHITE)))

        curr_dot = Dot(radius=0.1, color=GREY).move_to(ax.c2p(btc_tracker.get_value(),
                                                              xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        curr_dot.set_z_index(2)

        curr_dot.add_updater(lambda dot: dot.move_to(ax.c2p(btc_tracker.get_value(),
                                                            xyk_graph_btc.underlying_function(btc_tracker.get_value()))))

        vertical_line = ax.get_vertical_line(ax.c2p(btc_tracker.get_value(),
                                                    xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        horizontal_line = ax.get_horizontal_line(ax.c2p(btc_tracker.get_value(),
                                                        xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        new_horzontal_line = VGroup()
        for i in range(1, len(horizontal_line) + 1):
            new_horzontal_line.add(horizontal_line[ -i ])

        horizontal_line = new_horzontal_line
        x_marker = Triangle(color=ORANGE, fill_color=ORANGE, fill_opacity=1).scale(0.1).next_to(vertical_line, DOWN, buff=0)
        x_marker.add_updater(lambda marker: marker.next_to(vertical_line, DOWN, buff=0))
        x_marker_val = Integer(btc_tracker.get_value())
        x_marker_val.add_updater(
            lambda integer: integer.become(Integer(btc_tracker.get_value()).scale(0.4).next_to(vertical_line, DOWN, buff=0.3)))

        y_marker = Triangle(color=GREEN, fill_color=GREEN, fill_opacity=1).scale(0.1).rotate(-PI / 2).next_to(horizontal_line, LEFT, buff=0)
        y_marker.add_updater(lambda marker: marker.next_to(horizontal_line, LEFT, buff=0))
        y_marker_val = Integer(usdt_tracker.get_value())
        y_marker_val.add_updater(lambda integer: integer.become(
            Integer(usdt_tracker.get_value()).scale(0.4).rotate(PI / 2).next_to(horizontal_line, LEFT, buff=0.3)))

        lines = VGroup(vertical_line, horizontal_line)
        markers = VGroup(x_marker, x_marker_val, y_marker, y_marker_val)

        self.play(Create(xyk_graph_btc))
        self.play(Create(curr_dot))

        self.play(Create(lines), run_time=2)
        self.play(Create(markers), run_time=2)

        vertical_line.add_updater(lambda line: line.become(ax.get_vertical_line(ax.c2p(btc_tracker.get_value(),
                                                                                       xyk_graph_btc.underlying_function(
                                                                                           btc_tracker.get_value())))))
        horizontal_line.add_updater(lambda line: line.become(ax.get_horizontal_line(ax.c2p(btc_tracker.get_value(),
                                                                                           xyk_graph_btc.underlying_function(
                                                                                               btc_tracker.get_value())))))

        area = Rectangle(width=curr_dot.get_x() - ax.get_origin()[ 0 ], height=curr_dot.get_y() - ax.get_origin()[ 1 ], fill_color=BLUE,
                         fill_opacity=0.5, stroke_width=0).align_to(curr_dot.get_center(), UR)
        area.add_updater(lambda area: area.become(
            Rectangle(width=curr_dot.get_x() - ax.get_origin()[ 0 ], height=curr_dot.get_y() - ax.get_origin()[ 1 ], fill_color=BLUE,
                      fill_opacity=0.5, stroke_width=0).align_to(curr_dot.get_center(), UR)))

        area_text = MathTex(r'BTC \times  USDT').scale(0.5).arrange(DOWN, buff=0.1)
        area_text.add_updater(
            lambda text: text.become(MathTex(r'BTC \times USDT', 'in \  Pool').scale(0.4).arrange(DOWN, buff=0.1).move_to(area)))

        self.play(Create(area))
        self.play(Create(area_text))


        ##### 이제는 유동성을 제거하는 상황을 보겟ㅅ븐디
        #####
        ##### 유동성을 제거한다는 것은 풀에서 자기 지분만큼 비트와 테더를 빼가는 것입니다
        ##### 케이값이 작아졌습니다

        #####
        # 아ㅣ거 유동성 5개 아니라 3개로 수정
        def create_lp_token(text):
            box = Rectangle(width=1.6, height=1, fill_color=WHITE, stroke_color=WHITE, fill_opacity=1)
            text = Tex(text, color=BLACK).scale(0.5)
            return VGroup(box, text)

        liq_provider = create_entity(Tex(r' \emph{Init Liq\\provider}', color=BLACK).scale(0.8), 1, WHITE, "3 BTC", ORANGE, 1.4, 0.3).next_to(
            liq_pool_rect, RIGHT, buff=1.5)

        lp_asset = create_lp_token(r"173\\BTC-USDT\\LP").next_to(liq_provider[ 0 ], DOWN, buff=0.1)
        lp_asset_121=create_lp_token(r"121\\BTC-USDT\\LP").next_to(liq_provider[ 0 ], DOWN, buff=0.1)
        lp_asset_51 = create_lp_token(r"52\\BTC-USDT\\LP").next_to(lp_asset_121, DOWN, buff=0.1)
        lp_asset_divided = VGroup(lp_asset_121,lp_asset_51)

        btc_asset = liq_provider[ 1 ].next_to(lp_asset_121, D, buff=0.1)
        usdt_asset = create_entity("A", 0.5, WHITE, "900 USDT", GREEN, 1.4, 0.3)[ 1 ].next_to(btc_asset, DOWN, buff=0.1)
        # text = Tex(r"173\\BTC-USDT\\LP", color=BLACK).scale(0.5)



        self.play(Create(liq_provider[ 0 ]),
                  Create(lp_asset))

        btc_bar.clear_updaters()
        usdt_bar.clear_updaters()

        # # scene2_btc_dashed_box = Rectangle(color=RED).align_to(btc_bar[0],UL,alignment_vect=btc_bar[0].get_edge_center(UP))
        # scene2_2308usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.2307, stroke_width=3,
        #                                 stroke_color=RED_E).align_to(usdt_bar, UL)

        scene4_5btc_box = Rectangle(width=btc_bar.width, height=btc_bar.height * 0.3, stroke_width=3,
                                    stroke_color=RED_E).align_to(btc_bar, UL)
        scene4_1500usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.3, stroke_width=3,
                                        stroke_color=RED_E).align_to(usdt_bar, UL)

        scene4_1500usdt_fill_box = scene4_1500usdt_box.copy().set_fill(GREEN, opacity=1)
        scene4_5btc_fill_box = scene4_5btc_box.copy().set_fill(ORANGE, opacity=1)

        scene4_5btc_fill_box.set_stroke(width=0, opacity=0)
        scene4_1500usdt_fill_box.set_stroke(width=0, opacity=0)
        scene4_5btc_fill_box.set_z_index(3)
        scene4_1500usdt_fill_box.set_z_index(3)

        self.play(Create(VGroup(scene4_5btc_box, scene4_1500usdt_box)))
        self.add(scene4_5btc_fill_box, scene4_1500usdt_fill_box)

        scene4_1500usdt_brace = BraceBetweenPoints(scene4_1500usdt_box.get_corner(UR), scene4_1500usdt_box.get_corner(DR), color=RED_E,
                                                   stroke_color=RED_E,
                                                   stroke_width=3,
                                                   ).flip(axis=np.array([ 0., 1., 0. ])).next_to(scene4_1500usdt_fill_box,
                                                                                                 RIGHT)
        scene4_5btc_brace = BraceBetweenPoints(scene4_5btc_box.get_corner(UL), scene4_5btc_box.get_corner(DL), color=RED_E,
                                               stroke_color=RED_E, stroke_width=3
                                               ).next_to(scene4_5btc_fill_box,
                                                         LEFT)
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=2100 / 1000, width=1.2, fill_color=GREEN, fill_opacity=1, color=GREEN).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=7 / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        scene4_1500usdt_brace_label = Integer(btc_tracker.get_value())
        scene4_1500usdt_brace_label.add_updater(lambda label: label.become(
            Integer(900).scale(0.4).rotate(-PI / 2).next_to(scene4_1500usdt_brace, RIGHT, buff=0.3)))
        scene4_5btc_brace_label = Integer(usdt_tracker.get_value())
        scene4_5btc_brace_label.add_updater(lambda label: label.become(
            Integer(3).scale(0.4).rotate(PI / 2).next_to(scene4_5btc_brace, LEFT, buff=0.3)))

        scene4_braces = VGroup(scene4_1500usdt_brace, scene4_5btc_brace)
        scene4_brace_labels = VGroup(scene4_1500usdt_brace_label, scene4_5btc_brace_label)

        new_liquidity_text = MathTex('3BTC', '=', '900USDT').scale(0.5).next_to(liq_provider, DOWN, buff=2)

        # self.play(Create(new_liquidity_text))

        scene4_origin_graph = xyk_graph_btc.copy()
        scene4_origin_graph.clear_updaters()
        scene4_origin_graph.set_color(RED)
        scene4_origin_graph.set_z_index(-1)
        self.add(scene4_origin_graph)

        self.play(Create(scene4_braces),
                  Create(scene4_brace_labels))


        dummydot = Dot(1, color=RED).move_to(liq_pool_rect)


        # self.play(Create(origin_dot))
        self.play(ReplacementTransform(lp_asset, lp_asset_divided))
        self.play(k_tracker.animate.set_value(14700),
                  btc_tracker.animate.set_value(7),
                  usdt_tracker.animate.set_value(14700 / 7),
                  Transform(scene4_1500usdt_fill_box, usdt_asset),
                  Transform(scene4_5btc_fill_box, btc_asset),
                  FadeOut(lp_asset_51, target_position=dummydot),
                  run_time=6, rate_func=rate_functions.ease_in_out_quint)

        self.wait(4)

class L_02_S_08_amm_xyk_adv_px_up_3(Scene):
    def construct(self):
        #####거래자 활동에 대해 알아보겟습니다

        ##### 먼저 풀에서 비티씨를 구매하는 경우입니다.
        ##### 오더북에서와 마찬가지로 누군가 비티씨를 사면 가격이 올라갑니다
        ##### 왜냐하면 풀에서 비티씨가 빠져나가서 비티씨 테더 비율이 변동했고 이게 비티씨의 가격을 바꾸게 됩니다
        ##### 우리가 생각한대로 내려갔습니다 그리고 케이값도 변하지 않고 그대로입니다.
        ##### 그런데 구매자가 기분이 안 좋아보입니다.
        ##### 구매자는 분명히 구매할 때 1비트코인에 300달러인 걸 보고
        ##### 3개를 구매하려고 했는데 소요된 비용이 900달러가 아니라 1286달러였습니다
        ##### 어떻게 된걸까요…

        # 기본 셋업

        # 케이 바리어블, 초기 엘피, 좌표계
        xyk_fraction = MathTex('y', '=', r'\frac{k}{x}').to_edge(UL)

        liq_pool_rect = RoundedRectangle(height=6.3, width=4, corner_radius=0.5)
        liq_pool_text = Tex('Liquidity Pool').next_to(liq_pool_rect, UP)
        liq_pool = VGroup(liq_pool_rect, liq_pool_text).to_edge(UL).shift(R * 0.5)
        liq_pool.set_z_index(3)

        k_var = Variable(30000, MathTex("k"), var_type=Integer).to_edge(UR)
        k_tracker = k_var.tracker
        k_tracker.set_value(30000)

        self.play(Create(liq_pool))

        liq_provider = create_entity(Tex(r' \emph{Init Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", ORANGE, 1.4,
                                     0.3).next_to(liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", GREEN, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)
        liq_provider.add(usdt_asset)

        self.play(Create(liq_provider))

        ax = Axes(x_range=[ 0, 18, 4 ], y_range=[ 0, 6500, 1000 ], x_length=5, y_length=5, tips=True,
                  axis_config={"include_numbers": False, 'color': WHITE, 'include_ticks': False, 'font_size': 20}, ).to_edge(DR, buff=0.8)

        ax.shift(U * (liq_pool_rect.get_bottom()[ 1 ] - ax[ 0 ].get_y()))

        # ax[0].move_to(np.array([ax[0].g() ,liq_pool_rect.get_bottom()[1],0]))
        y_axis_label = ax.get_y_axis_label(MathTex('Amount of USDT in Pool', color=WHITE).rotate(PI / 2).scale(0.4), edge=LEFT,
                                           direction=LEFT, buff=0.37)
        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool', color=WHITE).scale(0.4), edge=DOWN, direction=DOWN, buff=0.5)
        axis_labels = VGroup(x_axis_label, y_axis_label)

        usdt_bar = Rectangle(height=3, width=1.2, fill_color=GREEN, fill_opacity=1, color=GREEN)
        btc_bar = Rectangle(height=1, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE)
        bars = VGroup(btc_bar, usdt_bar)
        bars.arrange(RIGHT, aligned_edge=DOWN).move_to(liq_pool_rect).align_to(liq_pool_rect, DOWN)

        usdt_bar_pos = usdt_bar.get_bottom()
        btc_bar_pos = btc_bar.get_bottom()

        btc_var = Variable(10, MathTex("BTC"), var_type=Integer)
        usdt_var = Variable(3000, MathTex("USDT"), var_type=Integer).next_to(btc_var, DOWN, aligned_edge=LEFT)
        btc_tracker = btc_var.tracker
        usdt_tracker = usdt_var.tracker
        usdt_var[ 0 ][ 0 ].set_color(GREEN)
        btc_var[ 0 ][ 0 ].set_color(ORANGE)

        vars = VGroup(btc_var, usdt_var).arrange(DOWN, aligned_edge=LEFT).next_to(liq_pool_rect, DOWN, buff=0.25)

        self.play(ReplacementTransform(usdt_asset, usdt_bar),
                  ReplacementTransform(btc_asset, btc_bar))
        self.play(Write(usdt_var),
                  Write(btc_var))
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=GREEN, fill_opacity=1, color=GREEN).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        pool_price = Variable(100, 'Price', var_type=DecimalNumber, num_decimal_places=2).next_to(
            liq_pool_rect, RIGHT, buff=1.5).to_edge(UP)
        pool_price_tracker = pool_price.tracker
        pool_price.add_updater(lambda v: pool_price_tracker.set_value(usdt_tracker.get_value() / btc_tracker.get_value()))
        pool_price_unit = Tex(r'\$').next_to(pool_price, buff=0.1)
        self.play(Write(k_var[ 0 ]))
        self.play(Create(ax),
                  Create(axis_labels),
                  Create(pool_price_unit),
                  Create(pool_price),
                  TransformMatchingShapes(Group(btc_var[ 1 ].copy(), usdt_var[ 1 ].copy()), k_var[ 1 ].copy()),
                  Create(xyk_fraction.next_to(k_var, LEFT, buff=1))
                  )

        lp_amt_form_1 = MathTex(r'Init\  l =\sqrt{x \times y}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_2 = MathTex(r'Init\  l =\sqrt{10 \times 3000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_3 = MathTex(r'Init\  l =\sqrt{30000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_int = Tex(rf'{int(30000 ** (1 / 2))} LP token').move_to(lp_amt_form_1).scale(0.7)

        self.play(Create(lp_amt_form_1))
        self.play(TransformMatchingShapes(lp_amt_form_1, lp_amt_form_2))
        self.play(TransformMatchingShapes(lp_amt_form_2, lp_amt_form_3))
        self.play(TransformMatchingShapes(lp_amt_form_3, lp_amt_int))

        box = Rectangle(width=1.6, height=1, fill_color=WHITE, stroke_color=WHITE, fill_opacity=1)
        text = Tex(r"173\\BTC-USDT\\LP", color=BLACK).scale(0.5)
        lp_asset = VGroup(box, text).next_to(liq_provider[ 0 ], DOWN, buff=0.1)

        self.play(Create(lp_asset),
                  Uncreate(lp_amt_int))

        self.play(FadeOut(liq_provider),
                  FadeOut(lp_amt_int),
                  FadeOut(lp_asset))

        xyk_graph_btc = ax.plot(lambda x: k_tracker.get_value() / x,
                                x_range=[ 0.00001, 6000 ],
                                use_smoothing=False, color=WHITE)

        xyk_graph_btc.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: k_tracker.get_value() / x,
                    x_range=[ k_tracker.get_value() / 6000, 16 ],
                    use_smoothing=False, color=WHITE)))

        curr_dot = Dot(radius=0.1, color=GREY).move_to(ax.c2p(btc_tracker.get_value(),
                                                              xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        curr_dot.set_z_index(2)

        curr_dot.add_updater(lambda dot: dot.move_to(ax.c2p(btc_tracker.get_value(),
                                                            xyk_graph_btc.underlying_function(btc_tracker.get_value()))))

        vertical_line = ax.get_vertical_line(ax.c2p(btc_tracker.get_value(),
                                                    xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        horizontal_line = ax.get_horizontal_line(ax.c2p(btc_tracker.get_value(),
                                                        xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        new_horzontal_line = VGroup()
        for i in range(1, len(horizontal_line) + 1):
            new_horzontal_line.add(horizontal_line[ -i ])

        horizontal_line = new_horzontal_line
        x_marker = Triangle(color=ORANGE, fill_color=ORANGE, fill_opacity=1).scale(0.1).next_to(vertical_line, DOWN, buff=0)
        x_marker.add_updater(lambda marker: marker.next_to(vertical_line, DOWN, buff=0))
        x_marker_val = Integer(btc_tracker.get_value())
        x_marker_val.add_updater(
            lambda integer: integer.become(Integer(btc_tracker.get_value()).scale(0.4).next_to(vertical_line, DOWN, buff=0.3)))

        y_marker = Triangle(color=GREEN, fill_color=GREEN, fill_opacity=1).scale(0.1).rotate(-PI / 2).next_to(horizontal_line, LEFT, buff=0)
        y_marker.add_updater(lambda marker: marker.next_to(horizontal_line, LEFT, buff=0))
        y_marker_val = Integer(usdt_tracker.get_value())
        y_marker_val.add_updater(lambda integer: integer.become(
            Integer(usdt_tracker.get_value()).scale(0.4).rotate(PI / 2).next_to(horizontal_line, LEFT, buff=0.3)))

        lines = VGroup(vertical_line, horizontal_line)
        markers = VGroup(x_marker, x_marker_val, y_marker, y_marker_val)

        self.play(Create(xyk_graph_btc))
        self.play(Create(curr_dot))

        self.play(Create(lines), run_time=2)
        self.play(Create(markers), run_time=2)

        vertical_line.add_updater(lambda line: line.become(ax.get_vertical_line(ax.c2p(btc_tracker.get_value(),
                                                                                       xyk_graph_btc.underlying_function(
                                                                                           btc_tracker.get_value())))))
        horizontal_line.add_updater(lambda line: line.become(ax.get_horizontal_line(ax.c2p(btc_tracker.get_value(),
                                                                                           xyk_graph_btc.underlying_function(
                                                                                               btc_tracker.get_value())))))

        area = Rectangle(width=curr_dot.get_x() - ax.get_origin()[ 0 ], height=curr_dot.get_y() - ax.get_origin()[ 1 ], fill_color=BLUE,
                         fill_opacity=0.5, stroke_width=0).align_to(curr_dot.get_center(), UR)
        area.add_updater(lambda area: area.become(
            Rectangle(width=curr_dot.get_x() - ax.get_origin()[ 0 ], height=curr_dot.get_y() - ax.get_origin()[ 1 ], fill_color=BLUE,
                      fill_opacity=0.5, stroke_width=0).align_to(curr_dot.get_center(), UR)))

        area_text = MathTex(r'BTC \times  USDT').scale(0.5).arrange(DOWN, buff=0.1)
        area_text.add_updater(
            lambda text: text.become(MathTex(r'BTC \times USDT', 'in \  Pool').scale(0.4).arrange(DOWN, buff=0.1).move_to(area)))

        self.play(Create(area))
        self.play(Create(area_text))

        ##### DIVERGE
        #####
        user = create_entity(Tex(r' \emph{User}', color=BLACK), 1, WHITE, "1286 USDT", BLUE, 1.4, 0.3).next_to(liq_pool_rect, RIGHT,
                                                                                                               buff=1.5)
        user_asset_usdt = user[ 1 ]
        user_asset_pos = user_asset_usdt.get_center()
        user_asset_btc = create_entity("A", 0.5, WHITE, "3 BTC", ORANGE, 1.4, 0.3)[ 1 ].move_to(user_asset_pos)

        user_line = Tex(r'I want 3 BTC\\I have some USDT').scale(0.5).next_to(user, DOWN)

        self.play(Create(user))
        self.play(Create(user_line))
        self.play(Uncreate(user_line))

        # self.add(index_labels(btc_bar))###

        # scene1_btc_dashed_box = Rectangle(color=RED).align_to(btc_bar[0],UL,alignment_vect=btc_bar[0].get_edge_center(UP))
        scene1_7btc_box = Rectangle(width=btc_bar.width, height=btc_bar.height * 0.3, stroke_width=3, stroke_color=RED_E).align_to(
            btc_bar[ 0 ], UL)
        scene1_1286usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.4286, stroke_width=3,
                                     stroke_color=GREEN_E).next_to(usdt_bar, UP, buff=0)

        scene1_7btc_fill_box = scene1_7btc_box.copy().set_fill(ORANGE, opacity=1)
        scene1_1286usdt_fill_box = scene1_1286usdt_box.copy().set_fill(GREEN, opacity=1)
        scene1_7btc_fill_box.set_stroke(width=0, opacity=0)
        scene1_1286usdt_fill_box.set_stroke(width=0, opacity=0)
        scene1_7btc_fill_box.set_z_index(3)
        scene1_1286usdt_fill_box.set_z_index(3)

        self.play(Create(scene1_7btc_box))
        self.play(Create(scene1_1286usdt_box))
        scene1_7btc_brace = BraceBetweenPoints(scene1_7btc_box.get_corner(UL), scene1_7btc_box.get_corner(DL), color=RED_E,
                                               stroke_color=RED_E,
                                               stroke_width=3,
                                               ).next_to(scene1_7btc_box, LEFT)
        scene1_1286usdt_brace = BraceBetweenPoints(scene1_1286usdt_box.get_corner(UR), scene1_1286usdt_box.get_corner(DR), color=GREEN_E,
                                                stroke_color=GREEN_E, stroke_width=3
                                                ).flip(axis=np.array([ 0., 1., 0. ])).next_to(scene1_1286usdt_box,
                                                                                              RIGHT)

        scene1_7btc_brace_label = Integer(btc_tracker.get_value())
        scene1_7btc_brace_label.add_updater(lambda label: label.become(
            Integer(3).scale(0.4).rotate(PI / 2).next_to(scene1_7btc_brace, LEFT, buff=0.3)))
        scene1_1286usdt_brace_label = Integer(usdt_tracker.get_value())
        scene1_1286usdt_brace_label.add_updater(lambda label: label.become(
            Integer(1286).scale(0.4).rotate(-PI / 2).next_to(scene1_1286usdt_brace, RIGHT, buff=0.3)))

        scene1_braces = VGroup(scene1_7btc_brace, scene1_1286usdt_brace)
        scene1_brace_labels = VGroup(scene1_7btc_brace_label, scene1_1286usdt_brace_label)

        self.play(Create(scene1_braces),
                  Create(scene1_brace_labels))

        usdt_bar.clear_updaters()
        btc_bar.clear_updaters()

        self.add(scene1_7btc_fill_box)
        # usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
        #     Rectangle(height=4283 / 1000, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE).move_to(
        #         usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=7 / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        origin_dot = curr_dot.copy()
        origin_dot.clear_updaters()
        origin_dot.set_color(GREEN)
        origin_dot.set_z_index(1.5)
        self.play(Create(origin_dot))
        self.play(btc_tracker.animate.set_value(7),
                  usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
                  ReplacementTransform(scene1_7btc_fill_box, user_asset_btc),
                  ReplacementTransform(user_asset_usdt, scene1_1286usdt_fill_box))

        scene1_arrow = CurvedArrow(origin_dot.get_center(), curr_dot.get_center(), radius=-4, tip_length=0.25).shift(
            RIGHT * 0.3 + UP * 0.3)
        scene1_arrow_label = Tex('Buy BTC in exchange of USDT').scale(0.3).next_to(scene1_arrow, UR)

        self.play(Create(scene1_arrow))

        scene1_slippage_text = Tex(r'I used 1283 USDT \\to buy 3 BTC').scale(0.7).next_to(user_asset_pos, DOWN)
        scene1_slippage_form = MathTex(r'1283 \divisionsymbol 3').next_to(scene1_slippage_text, DOWN)
        scene1_slippage_result = MathTex(rf'{int((k_tracker.get_value() / btc_tracker.get_value() - 3000) / 3)}\$ \  per\ BTC ').move_to(
            scene1_slippage_form.get_center())

        self.play(Create(scene1_slippage_form),
                  Create(scene1_slippage_text))

        self.play(ReplacementTransform(scene1_slippage_form, scene1_slippage_result))

        self.wait(2)

class L_02_S_09_px_impact_and_slippage(Scene):
    def construct(self):
        dot = LabeledDot('Fuck')
        ##### 아까 말했듰이 케이값이 변하지 않기 때문이빈다.

        ##### 케이는 30000이고 엑스와이는 케이가 유지되렴녀 현재 엑스가 10에서 7로 변했기 때문에
        ##### 와이는 4286달러가 되어야하고 구매자는 4286달러에서 원래 있던 3000테더를 뺀 1286달러 밖에 받지 못 한 것입니다.
        # 중앙에 엑스와이는 케이
        # 케이는 30000ㅇ로 바꿈
        # 3개를 구매하니 비트코인은 10개에서 3개가 빠져서 엑스에는 7을 넣어줌
        # 10-3식이 7으로 트랜스폼하고 엑스트랜스폼 시킴
        # 와이는 4286으로 트랜스폼
        # 4286빼기 3000은 1286

        xyk = MathTex(r'x', '*', 'y', '=', 'k').scale(2)
        num_30000 = MathTex('30000').scale(2).to_edge(R).align_to(xyk[ 4 ], L)
        num_10_minus_3 = MathTex('(10-3)').scale(2).to_edge(L).align_to(xyk[ 0 ], R)
        num_7 = MathTex('7').scale(2).to_edge(L).align_to(xyk[ 0 ], R)
        y_is = MathTex(r'y', '=', r'\frac{30000}{7}').scale(2)
        num_4286 = MathTex(r'4286').scale(2).to_edge(R).align_to(y_is[ 2 ], L)

        self.play(Create(xyk))
        self.play(Transform(xyk[ 4 ], num_30000))
        self.play(Transform(xyk[ 0 ], num_10_minus_3))
        self.play(Transform(xyk[ 0 ], num_7))
        self.play(TransformMatchingShapes(xyk, y_is))
        self.play(Transform(y_is[ 2 ], num_4286))

        self.play(Uncreate(y_is))

        ##### 우리는 이것을 프라이스 임팩트라고 부릅니다. 어 이거 중앙화거래소에서 봤던 슬리피지라 비슷하다고 생각되어
        ##### 슬리피지라는 것과 프라이스 임팩트란 단어가 쉽게 혼용되는 것을 볼 수 있ㅅ브니다
        ##### 잠시 차이점을 알아보고 가겠습니다
        # 프라이스 임팩트 텍스트 만들고
        # 아래 슬리피지 나오면서 낫 이꼴
        # 텍스트 둘다 사라짐

        px_impact_not_equal = MathTex(r'Price\  Imapact', r'\neq', 'Slippage').scale(2).arrange(D)
        self.play(Create(px_impact_not_equal))
        self.play(Uncreate(px_impact_not_equal))

        ##### 슬리피지는 미끄러진다는 slip에서 나온 말로 예측하지 못 한다는 뉘앙스를 줍니다
        ##### 저번 동영상에서 봤듯이슬리피지는 주문을 전송하고 내 주문이 처리되기 전에 다른 사람의 트랜잭션이 먼저 체결되는 경우나
        ##### 현재가에 유동성이 부족하여 내 예측과 달리 벌어지는 것입니다.
        # 랙오브리퀴디티 텍스트
        # 테크니컬 프라블럼
        p1 = np.array([ -3, 1, 0 ])
        p1b = p1 + [ 1, 0, 0 ]
        l1 = Line(p1, p1b)
        p2 = np.array([ 3, -1, 0 ])
        p2b = p2 - [ 1, 0, 0 ]
        bezier_1 = CubicBezier(p1b, p1b + 3 * RIGHT, p2b - 3 * RIGHT, p2b)
        bezier_2 = CubicBezier(p2b, p2b - 3 * RIGHT, p1b + 3 * RIGHT, p1b).flip(axis=np.array([ 0, 1, 0 ])).shift(U * 2)
        curve_group = VGroup(l1, bezier_1, bezier_2).move_to(ORIGIN)
        slippage = MathTex('Slippage').scale(1.5).next_to(curve_group, LEFT)
        tech_problem = MathTex('Technical Problem').next_to(bezier_2, R).shift(U * 1)
        low_liq = MathTex(r'Low\  Liquidity').next_to(bezier_1, R).shift(D * 1)
        self.play(Create(slippage))
        self.play(Create(curve_group))
        self.play(Create(tech_problem),
                  Create(low_liq))
        self.play(Uncreate(slippage), Uncreate(curve_group), Uncreate(tech_problem),
                  Uncreate(low_liq))

        ##### 프라이스 임팩트는 내가 지금 하려는 트랜잭셕 즉 비트코인 3개를 풀에서 빼는 것이 가격에 주는 영향이라고 할 수 있습니다
        ##### 프라이스 임팩트 자체는 내가 트랜잭션을 요청하는 순간 이미 예상 된 것입니다.
        ##### 300달러를 보고 비티씨를 주문하면 나는 이미 계산을 통해
        ##### 내가 시장을 얼마나 움직일 것이고 그래서 사실상 비티씨를 300달러에 못 구매하고
        ##### 428에 구매할 것을 알고 있습니다 .이로인한 것은 프라이스 임팩트이지 슬리피지가 아닙니다.
        # 입력창 만들고 밑에 ㅏ
        # 에스티메이티드 프라이스
        # 입력창에 3삐티씨 입력되면 에스티메이티드 프라이스 업데이트
        # 그 밑에 스왑버튼 만들고 클릭 효과음과 이펙트
        # 밑에 with 임팩트 텍스트 동시에 띄우기

        input_box_1_rect = RoundedRectangle(width=8, height=2)
        input_box_1_split = Line(UP * 0.4, D * 0.4).shift(R * 1.5)
        input_box_1_drop = Elbow().rotate(-3 * PI / 4).shift(R * 3.5)
        input_box_1_text = Tex('USDT').next_to(input_box_1_split, R, buff=0.25)
        input_box_1_amt = Tex('1286').scale(1.2).next_to(input_box_1_rect.get_left(), buff=0.75)
        input_box_1 = VGroup(input_box_1_rect, input_box_1_split, input_box_1_drop, input_box_1_text, input_box_1_amt)
        input_box_1_without_amd = VGroup(input_box_1_rect, input_box_1_split, input_box_1_drop, input_box_1_text)

        input_box_2_rect = RoundedRectangle(width=8, height=2)
        input_box_2_split = Line(UP * 0.4, D * 0.4).shift(R * 1.5)
        input_box_2_drop = Elbow().rotate(-3 * PI / 4).shift(R * 3.5)
        input_box_2_text = Tex('BTC').next_to(input_box_2_split, R, buff=0.25)
        input_box_2_amt = Tex('3').scale(1.2).next_to(input_box_2_rect.get_left(), buff=0.75)
        input_box_2 = VGroup(input_box_2_rect, input_box_2_split, input_box_2_drop, input_box_2_text, input_box_2_amt)
        input_box_2_without_amd = VGroup(input_box_2_rect, input_box_2_split, input_box_2_drop, input_box_2_text)

        VGroup(input_box_1, input_box_2).arrange(D).shift(U * 1)

        est_px = Tex('1 BTC = 300USDT', font_size=30).next_to(input_box_2, D).align_to(input_box_2, L)
        new_est_px = Tex('1 BTC = 429USDT', font_size=30).next_to(input_box_2, D).align_to(input_box_2, L)
        fees = Tex('Est. Fee : 0.0001 ETH', font_size=30).next_to(input_box_2, D).align_to(input_box_2, R)

        swap_button_rect = RoundedRectangle(width=8, height=1.2, fill_color=MAROON_E, fill_opacity=1).next_to(input_box_2, D, buff=1)
        swap_button_text = Tex('SWAP').move_to(swap_button_rect)
        swap_button = VGroup(swap_button_rect, swap_button_text)

        dex_elements_without_amt = VGroup(input_box_1_without_amd, input_box_2_without_amd, fees, est_px, swap_button)
        dex_elements = VGroup(input_box_1, input_box_2, fees, est_px, swap_button)
        self.play(Create(dex_elements_without_amt))

        self.play(Create(input_box_1_amt))
        self.play(Create(input_box_2_amt))
        self.play(Transform(est_px, new_est_px),
                  Circumscribe(est_px))

        self.play(Indicate(swap_button_text, color=GREY))
        self.play(dex_elements.animate.to_edge(L))

        ##### 슬리피지는 그렇게 내가 평균단가 468.75 달러에 구매할 것이라 예상하는데 거기서부터 갈라지는 것입니다
        ##### 3개를 받으려고 1283을 보냈는데 2.8개를 받았을 때 우리는 0.2비티씨의 슬리피지가 생겼다고 합니다다
        # 돌려받은게 3비티씨가 아니라 2.8비티씨임
        returned_btc_2 = Tex('We just got 2.8 BTC', r'Slippage of 11\%', 'A slippage cost of 0.3 BTC').scale(0.8).arrange(D).shift(
            R * 4 + U * 2.5)
        self.play(Create(returned_btc_2))

        ##### 프라이스 임팩트는 428에 달러 빼기 300 즉 168.75 달러 혹은 보통은 퍼센트로 나타내기에
        ##### 428에 빼기 300 나누기 428에 곱하기 100 즉 36퍼센트가 됩니다
        ##### 그러나 슬리피지와 프라이스 임팩트를 엄밀하게 구분하지 않는 경우가 많기에 주의해야합니다
        # 여백에 프라이스 임팩트 이꼴 128빼기 300나누기 428 곱하기 100 적고 36퍼로 바뀜
        px_impact_text = Tex('Price Impact').shift(R * 4+U*0.5)
        px_impact_form = MathTex(r'\frac{429-300}{300}*100 = ', '0.3').shift(R * 4 + D * 0.5)
        px_impact_30perc = MathTex(r'30\%').move_to(px_impact_form[ 1 ]).to_edge(R).align_to(px_impact_form[ 1 ], L)
        self.play(Create(px_impact_text))
        self.play(Create(px_impact_form))
        self.play(Transform(px_impact_form[ 1 ], px_impact_30perc))

        ##### 어쨋거나 명심할 것은 엑스와이는 케이모델에서 프라이스 임팩트가 없을 수는 없습니다
        ##### 프라이스 임팩트가 없으려면 그래프를 벗어나야되는데 거래라는 것이 풀의 상태를 변화시키는 것이고 그래프상에서 이동할 수밖에 없기 때문입니다
        # 그래프 하나 만들고 레이트 펑셩 데어앤백이지만 고무줄 팅기는 것 마냥 레이트 펑션하나 만들기

        coor_sys = Axes(x_range=[ 0, 10, 2 ], y_range=[ 0, 10, 2 ], x_length=2, y_length=2, tips=False,
                               y_axis_config={"include_numbers": False, 'include_tip': True, 'include_ticks': False, 'tip_width': 0.1,
                                              'tip_height': 5},
                               x_axis_config={"include_numbers": False, 'include_tip': True, 'include_ticks': False, 'tip_width': 0.1,
                                              'tip_height': 5}
                               ).next_to(px_impact_form,D)

        trader_graph = coor_sys.plot(lambda x: 5 / x, x_range=[ 5 / 8, 8 ], use_smoothing=False, color=WHITE)
        curr_dot = Dot(radius=0.1, color=RED).move_to(coor_sys.c2p(2,2.5))

        self.play(Create(coor_sys),
                  Create(trader_graph),
                  Create(curr_dot))

        self.play(curr_dot.animate.shift(R*0.5+U*0.5),rate_func=there_and_back_with_pause)

        self.wait(5)

class L_02_S_10_amm_xyk_adv_px_dn_4(Scene):
    def construct(self):

        ##### ###############################################################################################################

        ##### 이번에는 비티씨를 파는 경우입니다
        ##### 아까와 같은 원리로 비티씨를 팔면 가격이 내려가고
        ##### 여기서도 프라이스 임팩트를 막을 수는 없습니다.
        #####
        ##### 가격은 예상대로 내려가고 매도자는 여전히 기분이 좋지 않습니다
        ##### 300달러를 보고 3개를 판매했지만 900달러가 아닌 692달러 밖에 못 받았기 때문입니다.
        ##### 이 거대한 괴리는 유동성즉 풀의 크기가 작기 때문입니다.
        #####

        # 케이 바리어블, 초기 엘피, 좌표계
        xyk_fraction = MathTex('y', '=', r'\frac{k}{x}').to_edge(UL)

        liq_pool_rect = RoundedRectangle(height=6.3, width=4, corner_radius=0.5)
        liq_pool_text = Tex('Liquidity Pool').next_to(liq_pool_rect, UP)
        liq_pool = VGroup(liq_pool_rect, liq_pool_text).to_edge(UL).shift(R * 0.5)
        liq_pool.set_z_index(3)

        k_var = Variable(30000, MathTex("k"), var_type=Integer).to_edge(UR)
        k_tracker = k_var.tracker
        k_tracker.set_value(30000)

        self.play(Create(liq_pool))

        liq_provider = create_entity(Tex(r' \emph{Init Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", ORANGE, 1.4,
                                     0.3).next_to(liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", GREEN, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)
        liq_provider.add(usdt_asset)

        self.play(Create(liq_provider))

        ax = Axes(x_range=[ 0, 18, 4 ], y_range=[ 0, 6500, 1000 ], x_length=5, y_length=5, tips=True,
                  axis_config={"include_numbers": False, 'color': WHITE, 'include_ticks': False, 'font_size': 20}, ).to_edge(DR, buff=0.8)

        ax.shift(U * (liq_pool_rect.get_bottom()[ 1 ] - ax[ 0 ].get_y()))

        # ax[0].move_to(np.array([ax[0].g() ,liq_pool_rect.get_bottom()[1],0]))
        y_axis_label = ax.get_y_axis_label(MathTex('Amount of USDT in Pool', color=WHITE).rotate(PI / 2).scale(0.4), edge=LEFT,
                                           direction=LEFT, buff=0.37)
        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool', color=WHITE).scale(0.4), edge=DOWN, direction=DOWN, buff=0.5)
        axis_labels = VGroup(x_axis_label, y_axis_label)

        usdt_bar = Rectangle(height=3, width=1.2, fill_color=GREEN, fill_opacity=1, color=GREEN)
        btc_bar = Rectangle(height=1, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE)
        bars = VGroup(btc_bar, usdt_bar)
        bars.arrange(RIGHT, aligned_edge=DOWN).move_to(liq_pool_rect).align_to(liq_pool_rect, DOWN)

        usdt_bar_pos = usdt_bar.get_bottom()
        btc_bar_pos = btc_bar.get_bottom()

        btc_var = Variable(10, MathTex("BTC"), var_type=Integer)
        usdt_var = Variable(3000, MathTex("USDT"), var_type=Integer).next_to(btc_var, DOWN, aligned_edge=LEFT)
        btc_tracker = btc_var.tracker
        usdt_tracker = usdt_var.tracker
        usdt_var[ 0 ][ 0 ].set_color(GREEN)
        btc_var[ 0 ][ 0 ].set_color(ORANGE)

        vars = VGroup(btc_var, usdt_var).arrange(DOWN, aligned_edge=LEFT).next_to(liq_pool_rect, DOWN, buff=0.25)

        self.play(ReplacementTransform(usdt_asset, usdt_bar),
                  ReplacementTransform(btc_asset, btc_bar))
        self.play(Write(usdt_var),
                  Write(btc_var))
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=GREEN, fill_opacity=1, color=GREEN).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        pool_price = Variable(100, 'Price', var_type=DecimalNumber, num_decimal_places=2).next_to(
            liq_pool_rect, RIGHT, buff=1.5).to_edge(UP)
        pool_price_tracker = pool_price.tracker
        pool_price.add_updater(lambda v: pool_price_tracker.set_value(usdt_tracker.get_value() / btc_tracker.get_value()))
        pool_price_unit = Tex(r'\$').next_to(pool_price, buff=0.1)
        self.play(Write(k_var[ 0 ]))
        self.play(Create(ax),
                  Create(axis_labels),
                  Create(pool_price_unit),
                  Create(pool_price),
                  TransformMatchingShapes(Group(btc_var[ 1 ].copy(), usdt_var[ 1 ].copy()), k_var[ 1 ].copy()),
                  Create(xyk_fraction.next_to(k_var, LEFT, buff=1))
                  )

        lp_amt_form_1 = MathTex(r'Init\  l =\sqrt{x \times y}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_2 = MathTex(r'Init\  l =\sqrt{10 \times 3000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_3 = MathTex(r'Init\  l =\sqrt{30000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_int = Tex(rf'{int(30000 ** (1 / 2))} LP token').move_to(lp_amt_form_1).scale(0.7)

        self.play(Create(lp_amt_form_1))
        self.play(TransformMatchingShapes(lp_amt_form_1, lp_amt_form_2))
        self.play(TransformMatchingShapes(lp_amt_form_2, lp_amt_form_3))
        self.play(TransformMatchingShapes(lp_amt_form_3, lp_amt_int))

        box = Rectangle(width=1.6, height=1, fill_color=WHITE, stroke_color=WHITE, fill_opacity=1)
        text = Tex(r"173\\BTC-USDT\\LP", color=BLACK).scale(0.5)
        lp_asset = VGroup(box, text).next_to(liq_provider[ 0 ], DOWN, buff=0.1)

        self.play(Create(lp_asset),
                  Uncreate(lp_amt_int))

        self.play(FadeOut(liq_provider),
                  FadeOut(lp_amt_int),
                  FadeOut(lp_asset))

        xyk_graph_btc = ax.plot(lambda x: k_tracker.get_value() / x,
                                x_range=[ 0.00001, 6000 ],
                                use_smoothing=False, color=WHITE)

        xyk_graph_btc.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: k_tracker.get_value() / x,
                    x_range=[ k_tracker.get_value() / 6000, 16 ],
                    use_smoothing=False, color=WHITE)))

        curr_dot = Dot(radius=0.1, color=GREY).move_to(ax.c2p(btc_tracker.get_value(),
                                                              xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        curr_dot.set_z_index(2)

        curr_dot.add_updater(lambda dot: dot.move_to(ax.c2p(btc_tracker.get_value(),
                                                            xyk_graph_btc.underlying_function(btc_tracker.get_value()))))

        vertical_line = ax.get_vertical_line(ax.c2p(btc_tracker.get_value(),
                                                    xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        horizontal_line = ax.get_horizontal_line(ax.c2p(btc_tracker.get_value(),
                                                        xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        new_horzontal_line = VGroup()
        for i in range(1, len(horizontal_line) + 1):
            new_horzontal_line.add(horizontal_line[ -i ])

        horizontal_line = new_horzontal_line
        x_marker = Triangle(color=ORANGE, fill_color=ORANGE, fill_opacity=1).scale(0.1).next_to(vertical_line, DOWN, buff=0)
        x_marker.add_updater(lambda marker: marker.next_to(vertical_line, DOWN, buff=0))
        x_marker_val = Integer(btc_tracker.get_value())
        x_marker_val.add_updater(
            lambda integer: integer.become(Integer(btc_tracker.get_value()).scale(0.4).next_to(vertical_line, DOWN, buff=0.3)))

        y_marker = Triangle(color=GREEN, fill_color=GREEN, fill_opacity=1).scale(0.1).rotate(-PI / 2).next_to(horizontal_line, LEFT, buff=0)
        y_marker.add_updater(lambda marker: marker.next_to(horizontal_line, LEFT, buff=0))
        y_marker_val = Integer(usdt_tracker.get_value())
        y_marker_val.add_updater(lambda integer: integer.become(
            Integer(usdt_tracker.get_value()).scale(0.4).rotate(PI / 2).next_to(horizontal_line, LEFT, buff=0.3)))

        lines = VGroup(vertical_line, horizontal_line)
        markers = VGroup(x_marker, x_marker_val, y_marker, y_marker_val)

        self.play(Create(xyk_graph_btc))
        self.play(Create(curr_dot))

        self.play(Create(lines), run_time=2)
        self.play(Create(markers), run_time=2)

        vertical_line.add_updater(lambda line: line.become(ax.get_vertical_line(ax.c2p(btc_tracker.get_value(),
                                                                                       xyk_graph_btc.underlying_function(
                                                                                           btc_tracker.get_value())))))
        horizontal_line.add_updater(lambda line: line.become(ax.get_horizontal_line(ax.c2p(btc_tracker.get_value(),
                                                                                           xyk_graph_btc.underlying_function(
                                                                                               btc_tracker.get_value())))))

        area = Rectangle(width=curr_dot.get_x() - ax.get_origin()[ 0 ], height=curr_dot.get_y() - ax.get_origin()[ 1 ], fill_color=BLUE,
                         fill_opacity=0.5, stroke_width=0).align_to(curr_dot.get_center(), UR)
        area.add_updater(lambda area: area.become(
            Rectangle(width=curr_dot.get_x() - ax.get_origin()[ 0 ], height=curr_dot.get_y() - ax.get_origin()[ 1 ], fill_color=BLUE,
                      fill_opacity=0.5, stroke_width=0).align_to(curr_dot.get_center(), UR)))

        area_text = MathTex(r'BTC \times  USDT').scale(0.5).arrange(DOWN, buff=0.1)
        area_text.add_updater(
            lambda text: text.become(MathTex(r'BTC \times USDT', 'in \  Pool').scale(0.4).arrange(DOWN, buff=0.1).move_to(area)))

        self.play(Create(area))
        self.play(Create(area_text))

        ##### DIVERGE
        #####
        user = create_entity(Tex(r' \emph{User}', color=BLACK), 1, WHITE, "3BTC", ORANGE, 1.4, 0.3).next_to(liq_pool_rect,
                                                                                                                         RIGHT, buff=1.5)
        user_asset_btc = user[ 1 ]
        user_asset_pos = user_asset_btc.get_center()
        user_asset_usdt = create_entity("A", 0.5, WHITE, "692USDT", GREEN, 1.4, 0.3)[ 1 ].move_to(user_asset_pos)

        user_line = Tex(r'I want to sell 3 BTC\\I dont have some USDT').scale(0.5).next_to(user, DOWN)

        self.play(Create(user))
        self.play(Create(user_line))
        self.play(Uncreate(user_line))

        # self.add(index_labels(btc_bar))###

        # scene2_btc_dashed_box = Rectangle(color=RED).align_to(btc_bar[0],UL,alignment_vect=btc_bar[0].get_edge_center(UP))
        scene2_2308usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.2307, stroke_width=3,
                                        stroke_color=RED_E).align_to(
            usdt_bar, UL)
        scene2_13btc_box = Rectangle(width=btc_bar.width, height=btc_bar.height * 0.3, stroke_width=3,
                                     stroke_color=GREEN_E).next_to(btc_bar, UP, buff=0)

        scene2_2308usdt_fill_box = scene2_2308usdt_box.copy().set_fill(GREEN, opacity=1)
        scene2_13btc_fill_box = scene2_13btc_box.copy().set_fill(ORANGE, opacity=1)

        scene2_2308usdt_fill_box.set_stroke(width=0, opacity=0)
        scene2_13btc_fill_box.set_stroke(width=0, opacity=0)

        scene2_2308usdt_fill_box.set_z_index(3)
        scene2_13btc_fill_box.set_z_index(3)

        self.play(Create(scene2_2308usdt_box))
        self.play(Create(scene2_13btc_box))
        scene2_2308usdt_brace = BraceBetweenPoints(scene2_2308usdt_box.get_corner(UR), scene2_2308usdt_box.get_corner(DR), color=RED_E,
                                                   stroke_color=RED_E,
                                                   stroke_width=3,
                                                   ).flip(axis=np.array([ 0., 1., 0. ])).next_to(scene2_2308usdt_fill_box,
                                                                                                 RIGHT)
        scene2_13btc_brace = BraceBetweenPoints(scene2_13btc_box.get_corner(UL), scene2_13btc_box.get_corner(DL), color=GREEN_E,
                                                stroke_color=GREEN_E, stroke_width=3
                                                ).next_to(scene2_13btc_fill_box,
                                                          LEFT)

        scene2_2308usdt_brace_label = Integer(btc_tracker.get_value())
        scene2_2308usdt_brace_label.add_updater(lambda label: label.become(
            Integer(692).scale(0.4).rotate(-PI / 2).next_to(scene2_2308usdt_brace, RIGHT, buff=0.3)))
        scene2_13btc_brace_label = Integer(usdt_tracker.get_value())
        scene2_13btc_brace_label.add_updater(lambda label: label.become(
            Integer(3).scale(0.4).rotate(PI / 2).next_to(scene2_13btc_brace, LEFT, buff=0.3)))

        scene2_braces = VGroup(scene2_2308usdt_brace, scene2_13btc_brace)
        scene2_brace_labels = VGroup(scene2_2308usdt_brace_label, scene2_13btc_brace_label)

        self.play(Create(scene2_braces),
                  Create(scene2_brace_labels))

        usdt_bar.clear_updaters()
        btc_bar.clear_updaters()

        self.add(scene2_2308usdt_fill_box)
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=2307 / 1000, width=1.2, fill_color=GREEN, fill_opacity=1, color=GREEN).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        # btc_bar.add_updater(lambda btc_bar: btc_bar.become(
        #     Rectangle(height=13 / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
        #         btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        origin_dot = curr_dot.copy()
        origin_dot.clear_updaters()
        origin_dot.set_color(RED)
        origin_dot.set_z_index(1.5)

        self.play(Create(origin_dot))
        self.play(btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)),
                  Transform(scene2_2308usdt_fill_box, user_asset_usdt),
                  Transform(user_asset_btc, scene2_13btc_fill_box))

        scene2_arrow = CurvedArrow(origin_dot.get_center(), curr_dot.get_center(), radius=4, tip_length=0.25).shift(
            RIGHT * 0.3 + UP * 0.3)
        scene2_arrow_label = Tex('Buy BTC in exchange of USDT').scale(0.3).next_to(scene2_arrow, UR)

        self.play(Create(scene2_arrow))


        scene2_slippage_text = Tex(r'I sold 3 BTC \\and got 692 USDT').scale(0.7).next_to(user_asset_pos, DOWN)
        scene2_slippage_form = MathTex(r'692 \divisionsymbol 3').next_to(scene2_slippage_text, DOWN)
        scene2_slippage_result = MathTex(rf'{int(-(k_tracker.get_value() / btc_tracker.get_value() - 3000) / 3)}\$ \  per\ BTC ').move_to(
            scene2_slippage_form.get_center())

        self.play(Create(scene2_slippage_form),
                  Create(scene2_slippage_text))

        self.play(ReplacementTransform(scene2_slippage_form, scene2_slippage_result))

        self.wait(2)

class L_02_S_11_fees(Scene):
    def construct(self):
        pass

class amm_xyk_px_up_1(Scene):
    def construct(self):
        amm_text = Tex('Automatic Market Maker').scale(2)

        #
        # 유동성 풀과 엑스와이는 케이 공식 텍스트로 보여주고
        xyk = MathTex('x', r'\times', 'y', '=', 'k').scale(2).next_to(amm_text, D)
        self.play(Create(amm_text))
        self.play(Write(xyk))

        #
        # 엑스는 거래쌍 중에 코인 A의 양 와이는 코인 비의 양 화살표로 보여주고 없애기
        A_coin_amt = Tex('A coin amount').shift(LEFT * 2 + DOWN * 2)
        B_coin_amt = Tex('B coin amount').shift(RIGHT * 2 + DOWN * 2)
        x_arrow = Arrow(end=A_coin_amt.get_top(), start=xyk[ 0 ].get_bottom())
        y_arrow = Arrow(end=B_coin_amt.get_top(), start=xyk[ 2 ].get_bottom())

        self.play(Create(x_arrow),
                  Create(y_arrow)
                  )

        self.play(Create(A_coin_amt),
                  Create(B_coin_amt))
        self.play(Uncreate(A_coin_amt),
                  Uncreate(B_coin_amt),
                  Uncreate(x_arrow),
                  Uncreate(y_arrow)
                  )

        #
        # 와이는 엑스부느이 케이로 변형
        xyk_fraction = MathTex('y', '=', r'\frac{k}{x}').scale(2)

        self.play(TransformMatchingShapes(xyk, xyk_fraction))
        self.play(xyk_fraction.animate.to_edge(UP).scale(0.6))

        self.wait(1)
        #

        # 풀도 만들기

        xyk_and_liq = VGroup(xyk_fraction)

        self.play(xyk_and_liq.animate.to_edge(LEFT).shift(RIGHT))
        #
        # 엑스는 와이분의 일 그래프 예시로 보여주기
        graph_range = 50

        ax = Axes(x_range=[ 0, graph_range, int(graph_range / 10) ],
                  y_range=[ 0, graph_range, int(graph_range / 10) ],
                  x_length=6,
                  y_length=6,

                  tips=True,
                  axis_config={"include_numbers": True, 'font_size': 20, 'tip_width': 0.1, 'tip_height': 0.1},
                  )

        self.play(Create(ax))

        k_var = Variable(1, MathTex("k"), var_type=Integer)
        k_tracker = k_var.tracker
        k_tracker.set_value(1)
        # var = 10.5
        self.wait()

        xyk_graph = ax.plot(lambda x: k_tracker.get_value() / x,
                            x_range=[ 0.00001, 20 ],
                            use_smoothing=False, color=BLUE)

        xyk_graph.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: k_tracker.get_value() / x,
                    x_range=[ k_tracker.get_value() / graph_range, graph_range ],
                    use_smoothing=False, color=BLUE)))

        self.play(Create(xyk_graph))
        k_var.next_to(ax, UR)
        self.play(Create(k_var))

        self.play(k_tracker.animate.set_value(300), run_time=4)

        xyk_fraction.save_state()

        self.play(Uncreate(ax),
                  Uncreate(xyk_graph),
                  Uncreate(xyk_fraction),
                  Uncreate(k_var))

        liq_pool_rect = RoundedRectangle(height=6.3, width=4, corner_radius=0.5)
        liq_pool_text = Tex('Liquidity Pool').next_to(liq_pool_rect, UP)

        liq_pool = VGroup(liq_pool_rect, liq_pool_text).to_edge(UL)

        liq_pool.set_z_index(3)

        # self.add(index_labels(liq_pool[ 0 ]))
        self.play(Create(liq_pool))

        liq_provider = create_entity(Tex(r' \emph{Liq\\provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", ORANGE, 1.4, 0.3).next_to(
            liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", BLUE, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)

        liq_provider_asset = VGroup(btc_asset, usdt_asset)

        liq_provider.add(usdt_asset)
        self.play(Create(liq_provider))

        # self.play(liq_provider_asset.animate.arrange(RIGHT,buff=0.5))

        graph_range = 50
        ax = Axes(x_range=[ 0, 18, 4 ],
                  y_range=[ 0, 6500, 1000 ],
                  x_length=5,
                  y_length=5,

                  tips=True,
                  axis_config={"include_numbers": False, 'include_ticks': False, 'font_size': 20, 'tip_width': 0.1, 'tip_height': 0.1},
                  y_axis_config={"include_numbers": False, 'font_size': 20}
                  ).to_edge(DR, buff=0.8)

        y_axis_label = ax.get_y_axis_label(MathTex('Amount of USDT in Pool').rotate(PI / 2).scale(0.4), edge=LEFT, direction=LEFT, buff=0.5)
        # self.add(y_axis_label)

        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool').scale(0.4), edge=DOWN, direction=DOWN, buff=0.5)
        # self.add(x_axis_label)

        axis_labels = VGroup(x_axis_label, y_axis_label)

        usdt_bar = Rectangle(height=3, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE)
        btc_bar = Rectangle(height=1, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE)

        bars = VGroup(btc_bar, usdt_bar)
        bars.arrange(RIGHT, aligned_edge=DOWN).move_to(liq_pool_rect).align_to(liq_pool_rect, DOWN)

        usdt_bar_pos = usdt_bar.get_bottom()
        btc_bar_pos = btc_bar.get_bottom()

        k_tracker.set_value(30000)

        btc_var = Variable(10, MathTex("BTC"), var_type=Integer)
        btc_tracker = btc_var.tracker

        usdt_var = Variable(3000, MathTex("USDT"), var_type=Integer).next_to(btc_var, DOWN, aligned_edge=LEFT)
        usdt_tracker = usdt_var.tracker

        usdt_var[ 0 ][ 0 ].set_color(BLUE)
        btc_var[ 0 ][ 0 ].set_color(ORANGE)

        # usdt_var_bar=usdt_var[ 1 ].copy()
        # btc_var_bar=usdt_var[ 1 ].copy()
        # usdt_var_bar.set_color(BLACK)
        # btc_var_bar.set_color(BLACK)

        vars = VGroup(btc_var, usdt_var).arrange(DOWN, aligned_edge=LEFT)

        vars.next_to(liq_pool_rect, DOWN, buff=0.25)

        self.play(ReplacementTransform(usdt_asset, usdt_bar),
                  ReplacementTransform(btc_asset, btc_bar))

        # self.play(Write(usdt_var_bar),
        #           Write(btc_var_bar))
        #
        self.play(Write(usdt_var),
                  Write(btc_var))

        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        # usdt_bar.add_updater(lambda usdt_bar : usdt_bar.become(Rectangle(height=usdt_tracker.get_value()/10, width=1.2, color=BLUE).align_to(usdt_bar_pos, DOWN)))

        # self.play(usdt_tracker.animate.set_value(4000))
        # self.play(btc_tracker.animate.set_value(30))

        # self.play(k_var.animate.set_value(30000))
        k_var = Variable(30000, MathTex("k"), var_type=Integer).to_edge(UR, buff=0.5)
        k_tracker = k_var.tracker

        # self.add(index_labels(btc_var))
        pool_price = Variable(100, 'Price', var_type=DecimalNumber, num_decimal_places=2).next_to(
            liq_pool_rect, RIGHT, buff=1.5).to_edge(UP)
        pool_price_tracker = pool_price.tracker
        pool_price.add_updater(lambda v: pool_price_tracker.set_value(usdt_tracker.get_value() / btc_tracker.get_value()))

        xyk_fraction.restore()
        self.play(Write(k_var[ 0 ]))
        self.play(Create(ax),
                  Create(axis_labels),
                  Create(pool_price),
                  TransformMatchingShapes(Group(btc_var[ 1 ].copy(), usdt_var[ 1 ].copy()), k_var[ 1 ].copy()),
                  Create(xyk_fraction.next_to(k_var, LEFT, buff=1))
                  )
        self.play(FadeOut(liq_provider))
        xyk_graph_btc = ax.plot(lambda x: k_tracker.get_value() / x,
                                x_range=[ 0.00001, 6000 ],
                                use_smoothing=False, color=PURPLE)

        xyk_graph_btc.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: k_tracker.get_value() / x,
                    x_range=[ k_tracker.get_value() / 6000, 20 ],
                    use_smoothing=False, color=GREY)))

        curr_dot = Dot(radius=0.1, color=GREY).move_to(ax.c2p(btc_tracker.get_value(),
                                                              xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        curr_dot.set_z_index(2)

        curr_dot.add_updater(lambda dot: dot.move_to(ax.c2p(btc_tracker.get_value(),
                                                            xyk_graph_btc.underlying_function(btc_tracker.get_value()))))

        lines_to_point = ax.get_lines_to_point(ax.c2p(1, 1), color=GREEN_B)

        vertical_line = ax.get_vertical_line(ax.c2p(btc_tracker.get_value(),
                                                    xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        horizontal_line = ax.get_horizontal_line(ax.c2p(btc_tracker.get_value(),
                                                        xyk_graph_btc.underlying_function(btc_tracker.get_value())))

        new_horzontal_line = VGroup()
        for i in range(1, len(horizontal_line) + 1):
            new_horzontal_line.add(horizontal_line[ -i ])

        horizontal_line = new_horzontal_line

        x_marker = Triangle(color=ORANGE, fill_color=ORANGE, fill_opacity=1).scale(0.1).next_to(vertical_line, DOWN, buff=0)
        x_marker.add_updater(lambda marker: marker.next_to(vertical_line, DOWN, buff=0))
        x_marker_val = Integer(btc_tracker.get_value())
        x_marker_val.add_updater(
            lambda integer: integer.become(Integer(btc_tracker.get_value()).scale(0.4).next_to(vertical_line, DOWN, buff=0.3)))

        y_marker = Triangle(color=BLUE, fill_color=BLUE, fill_opacity=1).scale(0.1).rotate(-PI / 2).next_to(horizontal_line, LEFT, buff=0)
        y_marker.add_updater(lambda marker: marker.next_to(horizontal_line, LEFT, buff=0))
        y_marker_val = Integer(usdt_tracker.get_value())
        y_marker_val.add_updater(lambda integer: integer.become(
            Integer(usdt_tracker.get_value()).scale(0.4).rotate(PI / 2).next_to(horizontal_line, LEFT, buff=0.3)))

        lines = VGroup(vertical_line, horizontal_line)
        markers = VGroup(x_marker, x_marker_val, y_marker, y_marker_val)

        # lines_to_point.add_updater(lambda lines: lines.become(ax.get_lines_to_point(
        #     ax.c2p(btc_tracker.get_value(),
        #            xyk_graph_btc.underlying_function(btc_tracker.get_value())),color=BLUE)))
        #
        self.play(Create(xyk_graph_btc))
        self.play(Create(curr_dot))

        self.play(Create(lines), run_time=2)
        self.play(Create(markers), run_time=2)

        vertical_line.add_updater(lambda line: line.become(ax.get_vertical_line(ax.c2p(btc_tracker.get_value(),
                                                                                       xyk_graph_btc.underlying_function(
                                                                                           btc_tracker.get_value())))))
        horizontal_line.add_updater(lambda line: line.become(ax.get_horizontal_line(ax.c2p(btc_tracker.get_value(),
                                                                                           xyk_graph_btc.underlying_function(
                                                                                               btc_tracker.get_value())))))

        # 사각형을 만들고 그 넓이와 길이는 점선 그리고 정렬을 원점에 nexxt to DR buff 0
        area = Rectangle(width=curr_dot.get_x() - ax.get_origin()[ 0 ], height=curr_dot.get_y() - ax.get_origin()[ 1 ], fill_color=GREEN,
                         fill_opacity=0.5, stroke_width=0).align_to(curr_dot.get_center(), UR)
        area.add_updater(lambda area: area.become(
            Rectangle(width=curr_dot.get_x() - ax.get_origin()[ 0 ], height=curr_dot.get_y() - ax.get_origin()[ 1 ], fill_color=GREEN,
                      fill_opacity=0.5, stroke_width=0).align_to(curr_dot.get_center(), UR)))

        area_text = MathTex(r'BTC \times  USDT').scale(0.5).arrange(DOWN, buff=0.1)
        area_text.add_updater(
            lambda text: text.become(MathTex(r'BTC \times USDT', 'in \  Pool').scale(0.4).arrange(DOWN, buff=0.1).move_to(area)))

        # area.add_updater(lambda)
        # print(ax.get_origin()-curr_dot.get_x())
        # print(ax.get_origin().get-curr_dot.get_y())

        self.play(Create(area))
        self.play(Create(area_text))

        # self.play(btc_tracker.animate.set_value(13),
        #           usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)))
        #
        # self.wait(1)
        #
        # self.play(btc_tracker.animate.set_value(7),
        #           usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)))
        #
        # self.play(FadeOut(liq_provider[ 0 ]))

        ####scnee 1 user will get btc from the pool in exchange of usdt

        ########################################################################################올라갔을 때
        ######################################Scen1#############################올라갔을 때
        ########################################################################################올라갔을 때

        user = create_entity(Tex(r' \emph{User}', color=BLACK).scale(0.5), 0.5, WHITE, "1286 USDT", BLUE, 1.4, 0.3).next_to(liq_pool_rect,
                                                                                                                            RIGHT,
                                                                                                                            buff=2)
        user_asset_usdt = user[ 1 ]
        user_asset_pos = user_asset_usdt.get_center()
        user_asset_btc = create_entity("A", 0.5, WHITE, "3 BTC", ORANGE, 1.4, 0.3)[ 1 ].move_to(user_asset_pos)

        user_line = Tex(r'I want 3 BTC\\I have some USDT').scale(0.5).next_to(user, DOWN)

        self.play(Create(user))
        self.play(Create(user_line))
        self.play(Uncreate(user_line))

        # self.add(index_labels(btc_bar))###

        # scene1_btc_dashed_box = Rectangle(color=RED).align_to(btc_bar[0],UL,alignment_vect=btc_bar[0].get_edge_center(UP))
        scene1_7btc_box = Rectangle(width=btc_bar.width, height=btc_bar.height * 0.3, stroke_width=3, stroke_color=RED_E).align_to(
            btc_bar[ 0 ], UL)
        scene1_13btc_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.4286, stroke_width=3,
                                     stroke_color=GREEN_E).next_to(usdt_bar, UP, buff=0)

        scene1_7btc_fill_box = scene1_7btc_box.copy().set_fill(ORANGE, opacity=1)
        scene1_13btc_fill_box = scene1_13btc_box.copy().set_fill(BLUE, opacity=1)
        scene1_7btc_fill_box.set_stroke(width=0, opacity=0)
        scene1_13btc_fill_box.set_stroke(width=0, opacity=0)
        scene1_7btc_fill_box.set_z_index(3)
        scene1_13btc_fill_box.set_z_index(3)

        self.play(Create(scene1_7btc_box))
        self.play(Create(scene1_13btc_box))
        scene1_7btc_brace = BraceBetweenPoints(scene1_7btc_box.get_corner(UL), scene1_7btc_box.get_corner(DL), color=RED_E,
                                               stroke_color=RED_E,
                                               stroke_width=3,
                                               ).next_to(scene1_7btc_box, LEFT)
        scene1_13btc_brace = BraceBetweenPoints(scene1_13btc_box.get_corner(UR), scene1_13btc_box.get_corner(DR), color=GREEN_E,
                                                stroke_color=GREEN_E, stroke_width=3
                                                ).flip(axis=np.array([ 0., 1., 0. ])).next_to(scene1_13btc_box,
                                                                                              RIGHT)

        scene1_7btc_brace_label = Integer(btc_tracker.get_value())
        scene1_7btc_brace_label.add_updater(lambda label: label.become(
            Integer(3).scale(0.4).rotate(PI / 2).next_to(scene1_7btc_brace, LEFT, buff=0.3)))
        scene1_13btc_brace_label = Integer(usdt_tracker.get_value())
        scene1_13btc_brace_label.add_updater(lambda label: label.become(
            Integer(1286).scale(0.4).rotate(-PI / 2).next_to(scene1_13btc_brace, RIGHT, buff=0.3)))

        scene1_braces = VGroup(scene1_7btc_brace, scene1_13btc_brace)
        scene1_brace_labels = VGroup(scene1_7btc_brace_label, scene1_13btc_brace_label)

        self.play(Create(scene1_braces),
                  Create(scene1_brace_labels))

        usdt_bar.clear_updaters()
        btc_bar.clear_updaters()

        self.add(scene1_7btc_fill_box)
        # usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
        #     Rectangle(height=4283 / 1000, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE).move_to(
        #         usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=7 / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        origin_dot = curr_dot.copy()
        origin_dot.clear_updaters()
        origin_dot.set_color(GREEN)
        origin_dot.set_z_index(1.5)
        self.play(Create(origin_dot))
        self.play(btc_tracker.animate.set_value(7),
                          usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
                  ReplacementTransform(scene1_7btc_fill_box, user_asset_btc),
                  ReplacementTransform(user_asset_usdt, scene1_13btc_fill_box))

        scene1_arrow = CurvedArrow(origin_dot.get_center(), curr_dot.get_center(), radius=-4, tip_length=0.25).shift(
            RIGHT * 0.3 + UP * 0.3)
        scene1_arrow_label = Tex('Buy BTC in exchange of USDT').scale(0.3).next_to(scene1_arrow, UR)

        self.play(Create(scene1_arrow))

        scene1_slippage_text = Tex(r'I just used 1283 USDT \\to buy 3 BTC').scale(0.5).next_to(user_asset_pos, DOWN)
        scene1_slippage_form = MathTex(r'1283 \divisionsymbol 3').next_to(scene1_slippage_text, DOWN)
        scene1_slippage_result = MathTex(rf'{int((k_tracker.get_value() / btc_tracker.get_value() - 3000) / 3)}\$ \  per\ BTC ').move_to(
            scene1_slippage_form.get_center())

        self.play(Create(scene1_slippage_form),
                  Create(scene1_slippage_text))

        self.play(ReplacementTransform(scene1_slippage_form, scene1_slippage_result))

        # self.play()

        # self.play(Restore(whole_mobs))


        self.play(Uncreate(scene1_7btc_box))
        self.play(Uncreate(scene1_13btc_box))
        self.play(Uncreate(scene1_braces),
                  Uncreate(scene1_brace_labels))
        self.play(Uncreate(scene1_7btc_fill_box))
        self.play(Uncreate(scene1_slippage_result),
                  Uncreate(scene1_slippage_text))
        self.play(Uncreate(user),
                  Uncreate(btc_asset))


        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))




        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=1)


        self.wait(2)


class amm_xyk_px_dn_2(Scene):
    def construct(self):
        amm_text = Tex('Automatic Market Maker').scale(2)

        #
        # 유동성 풀과 엑스와이는 케이 공식 텍스트로 보여주고
        xyk = MathTex('x', r'\times', 'y', '=', 'k').scale(2).next_to(amm_text, D)
        self.play(Create(amm_text))
        self.play(Write(xyk))

        #
        # 엑스는 거래쌍 중에 코인 A의 양 와이는 코인 비의 양 화살표로 보여주고 없애기
        A_coin_amt = Tex('A coin amount').shift(LEFT * 2 + DOWN * 2)
        B_coin_amt = Tex('B coin amount').shift(RIGHT * 2 + DOWN * 2)
        x_arrow = Arrow(end=A_coin_amt.get_top(), start=xyk[ 0 ].get_bottom())
        y_arrow = Arrow(end=B_coin_amt.get_top(), start=xyk[ 2 ].get_bottom())

        self.play(Create(x_arrow),
                  Create(y_arrow)
                  )

        self.play(Create(A_coin_amt),
                  Create(B_coin_amt))
        self.play(Uncreate(A_coin_amt),
                  Uncreate(B_coin_amt),
                  Uncreate(x_arrow),
                  Uncreate(y_arrow)
                  )

        #
        # 와이는 엑스부느이 케이로 변형
        xyk_fraction = MathTex('y', '=', r'\frac{k}{x}').scale(2)

        self.play(TransformMatchingShapes(xyk, xyk_fraction))
        self.play(xyk_fraction.animate.to_edge(UP).scale(0.6))

        self.wait(1)
        #

        # 풀도 만들기

        xyk_and_liq = VGroup(xyk_fraction)

        self.play(xyk_and_liq.animate.to_edge(LEFT).shift(RIGHT))
        #
        # 엑스는 와이분의 일 그래프 예시로 보여주기
        graph_range = 50

        ax = Axes(x_range=[ 0, graph_range, int(graph_range / 10) ],
                  y_range=[ 0, graph_range, int(graph_range / 10) ],
                  x_length=6,
                  y_length=6,

                  tips=True,
                  axis_config={"include_numbers": True, 'font_size': 20, 'tip_width': 0.1, 'tip_height': 0.1},
                  )

        self.play(Create(ax))

        k_var = Variable(1, MathTex("k"), var_type=Integer)
        k_tracker = k_var.tracker
        k_tracker.set_value(1)
        # var = 10.5
        self.wait()

        xyk_graph = ax.plot(lambda x: k_tracker.get_value() / x,
                            x_range=[ 0.00001, 20 ],
                            use_smoothing=False, color=BLUE)

        xyk_graph.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: k_tracker.get_value() / x,
                    x_range=[ k_tracker.get_value() / graph_range, graph_range ],
                    use_smoothing=False, color=BLUE)))

        self.play(Create(xyk_graph))
        k_var.next_to(ax, UR)
        self.play(Create(k_var))

        self.play(k_tracker.animate.set_value(300), run_time=4)

        xyk_fraction.save_state()

        self.play(Uncreate(ax),
                  Uncreate(xyk_graph),
                  Uncreate(xyk_fraction),
                  Uncreate(k_var))

        liq_pool_rect = RoundedRectangle(height=6.3, width=4, corner_radius=0.5)
        liq_pool_text = Tex('Liquidity Pool').next_to(liq_pool_rect, UP)

        liq_pool = VGroup(liq_pool_rect, liq_pool_text).to_edge(UL)

        liq_pool.set_z_index(3)

        # self.add(index_labels(liq_pool[ 0 ]))
        self.play(Create(liq_pool))

        liq_provider = create_entity(Tex(r' \emph{Liq\\provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", ORANGE, 1.4, 0.3).next_to(
            liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", BLUE, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)

        liq_provider_asset = VGroup(btc_asset, usdt_asset)

        liq_provider.add(usdt_asset)
        self.play(Create(liq_provider))

        # self.play(liq_provider_asset.animate.arrange(RIGHT,buff=0.5))

        graph_range = 50
        ax = Axes(x_range=[ 0, 18, 4 ],
                  y_range=[ 0, 6500, 1000 ],
                  x_length=5,
                  y_length=5,

                  tips=True,
                  axis_config={"include_numbers": False, 'include_ticks': False, 'font_size': 20, 'tip_width': 0.1, 'tip_height': 0.1},
                  y_axis_config={"include_numbers": False, 'font_size': 20}
                  ).to_edge(DR, buff=0.8)

        y_axis_label = ax.get_y_axis_label(MathTex('Amount of USDT in Pool').rotate(PI / 2).scale(0.4), edge=LEFT, direction=LEFT, buff=0.5)
        # self.add(y_axis_label)

        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool').scale(0.4), edge=DOWN, direction=DOWN, buff=0.5)
        # self.add(x_axis_label)

        axis_labels = VGroup(x_axis_label, y_axis_label)

        usdt_bar = Rectangle(height=3, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE)
        btc_bar = Rectangle(height=1, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE)

        bars = VGroup(btc_bar, usdt_bar)
        bars.arrange(RIGHT, aligned_edge=DOWN).move_to(liq_pool_rect).align_to(liq_pool_rect, DOWN)

        usdt_bar_pos = usdt_bar.get_bottom()
        btc_bar_pos = btc_bar.get_bottom()

        k_tracker.set_value(30000)

        btc_var = Variable(10, MathTex("BTC"), var_type=Integer)
        btc_tracker = btc_var.tracker

        usdt_var = Variable(3000, MathTex("USDT"), var_type=Integer).next_to(btc_var, DOWN, aligned_edge=LEFT)
        usdt_tracker = usdt_var.tracker

        usdt_var[ 0 ][ 0 ].set_color(BLUE)
        btc_var[ 0 ][ 0 ].set_color(ORANGE)

        # usdt_var_bar=usdt_var[ 1 ].copy()
        # btc_var_bar=usdt_var[ 1 ].copy()
        # usdt_var_bar.set_color(BLACK)
        # btc_var_bar.set_color(BLACK)

        vars = VGroup(btc_var, usdt_var).arrange(DOWN, aligned_edge=LEFT)

        vars.next_to(liq_pool_rect, DOWN, buff=0.25)

        self.play(ReplacementTransform(usdt_asset, usdt_bar),
                  ReplacementTransform(btc_asset, btc_bar))

        # self.play(Write(usdt_var_bar),
        #           Write(btc_var_bar))
        #
        self.play(Write(usdt_var),
                  Write(btc_var))

        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        # usdt_bar.add_updater(lambda usdt_bar : usdt_bar.become(Rectangle(height=usdt_tracker.get_value()/10, width=1.2, color=BLUE).align_to(usdt_bar_pos, DOWN)))

        # self.play(usdt_tracker.animate.set_value(4000))
        # self.play(btc_tracker.animate.set_value(30))

        # self.play(k_var.animate.set_value(30000))
        k_var = Variable(30000, MathTex("k"), var_type=Integer).to_edge(UR, buff=0.5)
        k_tracker = k_var.tracker

        # self.add(index_labels(btc_var))
        pool_price = Variable(100, 'Price', var_type=DecimalNumber, num_decimal_places=2).next_to(
            liq_pool_rect, RIGHT, buff=1.5).to_edge(UP)
        pool_price_tracker = pool_price.tracker
        pool_price.add_updater(lambda v: pool_price_tracker.set_value(usdt_tracker.get_value() / btc_tracker.get_value()))

        xyk_fraction.restore()
        self.play(Write(k_var[ 0 ]))
        self.play(Create(ax),
                  Create(axis_labels),
                  Create(pool_price),
                  TransformMatchingShapes(Group(btc_var[ 1 ].copy(), usdt_var[ 1 ].copy()), k_var[ 1 ].copy()),
                  Create(xyk_fraction.next_to(k_var, LEFT, buff=1))
                  )
        self.play(FadeOut(liq_provider))
        xyk_graph_btc = ax.plot(lambda x: k_tracker.get_value() / x,
                                x_range=[ 0.00001, 6000 ],
                                use_smoothing=False, color=PURPLE)

        xyk_graph_btc.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: k_tracker.get_value() / x,
                    x_range=[ k_tracker.get_value() / 6000, 20 ],
                    use_smoothing=False, color=GREY)))

        curr_dot = Dot(radius=0.1, color=GREY).move_to(ax.c2p(btc_tracker.get_value(),
                                                              xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        curr_dot.set_z_index(2)

        curr_dot.add_updater(lambda dot: dot.move_to(ax.c2p(btc_tracker.get_value(),
                                                            xyk_graph_btc.underlying_function(btc_tracker.get_value()))))

        lines_to_point = ax.get_lines_to_point(ax.c2p(1, 1), color=GREEN_B)

        vertical_line = ax.get_vertical_line(ax.c2p(btc_tracker.get_value(),
                                                    xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        horizontal_line = ax.get_horizontal_line(ax.c2p(btc_tracker.get_value(),
                                                        xyk_graph_btc.underlying_function(btc_tracker.get_value())))

        new_horzontal_line = VGroup()
        for i in range(1, len(horizontal_line) + 1):
            new_horzontal_line.add(horizontal_line[ -i ])

        horizontal_line = new_horzontal_line

        x_marker = Triangle(color=ORANGE, fill_color=ORANGE, fill_opacity=1).scale(0.1).next_to(vertical_line, DOWN, buff=0)
        x_marker.add_updater(lambda marker: marker.next_to(vertical_line, DOWN, buff=0))
        x_marker_val = Integer(btc_tracker.get_value())
        x_marker_val.add_updater(
            lambda integer: integer.become(Integer(btc_tracker.get_value()).scale(0.4).next_to(vertical_line, DOWN, buff=0.3)))

        y_marker = Triangle(color=BLUE, fill_color=BLUE, fill_opacity=1).scale(0.1).rotate(-PI / 2).next_to(horizontal_line, LEFT, buff=0)
        y_marker.add_updater(lambda marker: marker.next_to(horizontal_line, LEFT, buff=0))
        y_marker_val = Integer(usdt_tracker.get_value())
        y_marker_val.add_updater(lambda integer: integer.become(
            Integer(usdt_tracker.get_value()).scale(0.4).rotate(PI / 2).next_to(horizontal_line, LEFT, buff=0.3)))

        lines = VGroup(vertical_line, horizontal_line)
        markers = VGroup(x_marker, x_marker_val, y_marker, y_marker_val)

        # lines_to_point.add_updater(lambda lines: lines.become(ax.get_lines_to_point(
        #     ax.c2p(btc_tracker.get_value(),
        #            xyk_graph_btc.underlying_function(btc_tracker.get_value())),color=BLUE)))
        #
        self.play(Create(xyk_graph_btc))
        self.play(Create(curr_dot))

        self.play(Create(lines), run_time=2)
        self.play(Create(markers), run_time=2)

        vertical_line.add_updater(lambda line: line.become(ax.get_vertical_line(ax.c2p(btc_tracker.get_value(),
                                                                                       xyk_graph_btc.underlying_function(
                                                                                           btc_tracker.get_value())))))
        horizontal_line.add_updater(lambda line: line.become(ax.get_horizontal_line(ax.c2p(btc_tracker.get_value(),
                                                                                           xyk_graph_btc.underlying_function(
                                                                                               btc_tracker.get_value())))))

        # 사각형을 만들고 그 넓이와 길이는 점선 그리고 정렬을 원점에 nexxt to DR buff 0
        area = Rectangle(width=curr_dot.get_x() - ax.get_origin()[ 0 ], height=curr_dot.get_y() - ax.get_origin()[ 1 ], fill_color=GREEN,
                         fill_opacity=0.5, stroke_width=0).align_to(curr_dot.get_center(), UR)
        area.add_updater(lambda area: area.become(
            Rectangle(width=curr_dot.get_x() - ax.get_origin()[ 0 ], height=curr_dot.get_y() - ax.get_origin()[ 1 ], fill_color=GREEN,
                      fill_opacity=0.5, stroke_width=0).align_to(curr_dot.get_center(), UR)))

        area_text = MathTex(r'BTC \times  USDT').scale(0.5).arrange(DOWN, buff=0.1)
        area_text.add_updater(
            lambda text: text.become(MathTex(r'BTC \times USDT', 'in \  Pool').scale(0.4).arrange(DOWN, buff=0.1).move_to(area)))

        # area.add_updater(lambda)
        # print(ax.get_origin()-curr_dot.get_x())
        # print(ax.get_origin().get-curr_dot.get_y())

        self.play(Create(area))
        self.play(Create(area_text))

        # self.play(btc_tracker.animate.set_value(13),
        #           usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)))
        #
        # self.wait(1)
        #
        # self.play(btc_tracker.animate.set_value(7),
        #           usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)))
        #
        # self.play(FadeOut(liq_provider[ 0 ]))

        ####scnee 1 user will get btc from the pool in exchange of usdt

        #######################################################################################
        #################################scene2##############################################
        #######################################################################################

        user = create_entity(Tex(r' \emph{User}', color=BLACK).scale(0.5), 0.5, WHITE, "3BTC", ORANGE, 1.4, 0.3).next_to(liq_pool_rect,
                                                                                                                         RIGHT, buff=2)
        user_asset_btc = user[ 1 ]
        user_asset_pos = user_asset_btc.get_center()
        user_asset_usdt = create_entity("A", 0.5, WHITE, "692USDT", BLUE, 1.4, 0.3)[ 1 ].move_to(user_asset_pos)

        user_line = Tex(r'I want to sell 3 BTC\\I dont have some USDT').scale(0.5).next_to(user, DOWN)

        self.play(Create(user))
        self.play(Create(user_line))
        self.play(Uncreate(user_line))

        # self.add(index_labels(btc_bar))###

        # scene2_btc_dashed_box = Rectangle(color=RED).align_to(btc_bar[0],UL,alignment_vect=btc_bar[0].get_edge_center(UP))
        scene2_2308usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.2307, stroke_width=3,
                                        stroke_color=RED_E).align_to(
            usdt_bar, UL)
        scene2_13btc_box = Rectangle(width=btc_bar.width, height=btc_bar.height * 0.3, stroke_width=3,
                                     stroke_color=GREEN_E).next_to(btc_bar, UP, buff=0)

        scene2_2308usdt_fill_box = scene2_2308usdt_box.copy().set_fill(BLUE, opacity=1)
        scene2_13btc_fill_box = scene2_13btc_box.copy().set_fill(ORANGE, opacity=1)

        scene2_2308usdt_fill_box.set_stroke(width=0, opacity=0)
        scene2_13btc_fill_box.set_stroke(width=0, opacity=0)

        scene2_2308usdt_fill_box.set_z_index(3)
        scene2_13btc_fill_box.set_z_index(3)

        self.play(Create(scene2_2308usdt_box))
        self.play(Create(scene2_13btc_box))
        scene2_2308usdt_brace = BraceBetweenPoints(scene2_2308usdt_box.get_corner(UR), scene2_2308usdt_box.get_corner(DR), color=RED_E,
                                                   stroke_color=RED_E,
                                                   stroke_width=3,
                                                   ).flip(axis=np.array([ 0., 1., 0. ])).next_to(scene2_2308usdt_fill_box,
                                                                                                 RIGHT)
        scene2_13btc_brace = BraceBetweenPoints(scene2_13btc_box.get_corner(UL), scene2_13btc_box.get_corner(DL), color=GREEN_E,
                                                stroke_color=GREEN_E, stroke_width=3
                                                ).next_to(scene2_13btc_fill_box,
                                                          LEFT)

        scene2_2308usdt_brace_label = Integer(btc_tracker.get_value())
        scene2_2308usdt_brace_label.add_updater(lambda label: label.become(
            Integer(692).scale(0.4).rotate(-PI / 2).next_to(scene2_2308usdt_brace, RIGHT, buff=0.3)))
        scene2_13btc_brace_label = Integer(usdt_tracker.get_value())
        scene2_13btc_brace_label.add_updater(lambda label: label.become(
            Integer(3).scale(0.4).rotate(PI / 2).next_to(scene2_13btc_brace, LEFT, buff=0.3)))

        scene2_braces = VGroup(scene2_2308usdt_brace, scene2_13btc_brace)
        scene2_brace_labels = VGroup(scene2_2308usdt_brace_label, scene2_13btc_brace_label)

        self.play(Create(scene2_braces),
                  Create(scene2_brace_labels))

        usdt_bar.clear_updaters()
        btc_bar.clear_updaters()

        self.add(scene2_2308usdt_fill_box)
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=2307 / 1000, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        # btc_bar.add_updater(lambda btc_bar: btc_bar.become(
        #     Rectangle(height=13 / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
        #         btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        origin_dot = curr_dot.copy()
        origin_dot.clear_updaters()
        origin_dot.set_color(RED)
        origin_dot.set_z_index(1.5)

        self.play(Create(origin_dot))
        self.play(btc_tracker.animate.set_value(13),
                  # usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)),
                  Transform(scene2_2308usdt_fill_box, user_asset_usdt),
                  Transform(user_asset_btc, scene2_13btc_fill_box))

        scene2_arrow = CurvedArrow(origin_dot.get_center(), curr_dot.get_center(), radius=4, tip_length=0.25).shift(
            RIGHT * 0.3 + UP * 0.3)
        scene2_arrow_label = Tex('Buy BTC in exchange of USDT').scale(0.3).next_to(scene2_arrow, UR)

        # bars.clear_updaters()
        # vars.clear_updaters()
        # k_var.clear_updaters()
        # area.clear_updaters()
        # curr_dot.clear_updaters()
        # axis_labels.clear_updaters()
        # markers.clear_updaters()
        self.play(Create(scene2_arrow))

        # self.play(Restore(whole_mobs))

        scene2_slippage_text = Tex(r'I just sold 3 BTC \\and got 602 USDT').scale(0.5).next_to(user_asset_pos, DOWN)
        scene2_slippage_form = MathTex(r'692 \divisionsymbol 3').next_to(scene2_slippage_text, DOWN)
        scene2_slippage_result = MathTex(rf'{int(-(k_tracker.get_value() / btc_tracker.get_value() - 3000) / 3)}\$ \  per\ BTC ').move_to(
            scene2_slippage_form.get_center())

        self.play(Create(scene2_slippage_form),
                  Create(scene2_slippage_text))

        self.play(ReplacementTransform(scene2_slippage_form, scene2_slippage_result))

        self.wait(2)

        self.wait(2)


## Scene 3 will be used for Base structure for 1245
class amm_xyk_k_up_3(Scene):
    def construct(self):
        amm_text = Tex('Automatic Market Maker').scale(2)

        #
        # 유동성 풀과 엑스와이는 케이 공식 텍스트로 보여주고
        xyk = MathTex('x', r'\times', 'y', '=', 'k').scale(2)
        self.play(Create(amm_text))
        self.play(Uncreate(amm_text))
        self.play(Write(xyk))

        # 상단에 함수들 팝업  와이는 이엑스 와잉는 오엑스 빼기 3 와이느
        # 그리고 사라짐

        #
        # 엑스는 거래쌍 중에 코인 A의 양 와이는 코인 비의 양 화살표로 보여주고 없애기
        A_coin_amt = Tex('A coin amount').shift(LEFT * 2 + DOWN * 2)
        B_coin_amt = Tex('B coin amount').shift(RIGHT * 2 + DOWN * 2)
        x_arrow = Arrow(end=A_coin_amt.get_top(), start=xyk[ 0 ].get_bottom())
        y_arrow = Arrow(end=B_coin_amt.get_top(), start=xyk[ 2 ].get_bottom())

        self.play(Create(x_arrow),
                  Create(y_arrow)
                  )

        self.play(Create(A_coin_amt),
                  Create(B_coin_amt))
        self.play(Uncreate(A_coin_amt),
                  Uncreate(B_coin_amt),
                  Uncreate(x_arrow),
                  Uncreate(y_arrow)
                  )

        #
        # 와이는 엑스부느이 케이로 변형
        xyk_fraction = MathTex('y', '=', r'\frac{k}{x}').scale(2)

        self.play(TransformMatchingShapes(xyk, xyk_fraction))
        self.play(xyk_fraction.animate.to_edge(UP).scale(0.6))

        self.wait(1)
        #

        # 풀도 만들기

        xyk_and_liq = VGroup(xyk_fraction)

        self.play(xyk_and_liq.animate.to_edge(LEFT).shift(RIGHT))
        #
        # 엑스는 와이분의 일 그래프 예시로 보여주기
        graph_range = 50

        ax = Axes(x_range=[ 0, graph_range, int(graph_range / 10) ],
                  y_range=[ 0, graph_range, int(graph_range / 10) ],
                  x_length=6,
                  y_length=6,

                  tips=True,
                  axis_config={"include_numbers": True, 'color': WHITE, 'font_size': 20, 'tip_width': 0.1, 'tip_height': 0.1},
                  )

        self.play(Create(ax))

        k_var = Variable(1, MathTex("k"), var_type=Integer)
        k_tracker = k_var.tracker
        k_tracker.set_value(1)
        # var = 10.5
        self.wait()

        xyk_graph = ax.plot(lambda x: k_tracker.get_value() / x,
                            x_range=[ 0.00001, 20 ],
                            use_smoothing=False, color=BLUE)

        xyk_graph.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: k_tracker.get_value() / x,
                    x_range=[ k_tracker.get_value() / graph_range, graph_range ],
                    use_smoothing=False, color=BLUE)))

        self.play(Create(xyk_graph))
        k_var.next_to(ax, UR)
        self.play(Create(k_var))

        self.play(k_tracker.animate.set_value(300), run_time=4)

        xyk_fraction.save_state()

        self.play(Uncreate(ax),
                  Uncreate(xyk_graph),
                  Uncreate(xyk_fraction),
                  Uncreate(k_var))

        liq_pool_rect = RoundedRectangle(height=6.3, width=4, corner_radius=0.5)
        liq_pool_text = Tex('Liquidity Pool').next_to(liq_pool_rect, UP)

        liq_pool = VGroup(liq_pool_rect, liq_pool_text).to_edge(UL)

        liq_pool.set_z_index(3)

        # self.add(index_labels(liq_pool[ 0 ]))
        self.play(Create(liq_pool))

        liq_provider = create_entity(Tex(r' \emph{Init Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", ORANGE, 1.4,
                                     0.3).next_to(
            liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", BLUE, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)

        liq_provider_asset = VGroup(btc_asset, usdt_asset)

        liq_provider.add(usdt_asset)
        self.play(Create(liq_provider))

        # self.play(liq_provider_asset.animate.arrange(RIGHT,buff=0.5))

        graph_range = 50
        ax = Axes(x_range=[ 0, 18, 4 ],
                  y_range=[ 0, 6500, 1000 ],
                  x_length=5,
                  y_length=5,

                  tips=True,
                  axis_config={"include_numbers": False, 'color': WHITE, 'include_ticks': False, 'font_size': 20, 'tip_width': 0.1,
                               'tip_height': 0.1},
                  y_axis_config={"include_numbers": False, 'font_size': 20}
                  ).to_edge(DR, buff=0.8)

        y_axis_label = ax.get_y_axis_label(MathTex('Amount of USDT in Pool', color=WHITE).rotate(PI / 2).scale(0.4), edge=LEFT,
                                           direction=LEFT, buff=0.37)
        # self.add(y_axis_label)

        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool', color=WHITE).scale(0.4), edge=DOWN, direction=DOWN, buff=0.5)
        # self.add(x_axis_label)

        axis_labels = VGroup(x_axis_label, y_axis_label)

        usdt_bar = Rectangle(height=3, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE)
        btc_bar = Rectangle(height=1, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE)

        bars = VGroup(btc_bar, usdt_bar)
        bars.arrange(RIGHT, aligned_edge=DOWN).move_to(liq_pool_rect).align_to(liq_pool_rect, DOWN)

        usdt_bar_pos = usdt_bar.get_bottom()
        btc_bar_pos = btc_bar.get_bottom()

        k_tracker.set_value(30000)

        btc_var = Variable(10, MathTex("BTC"), var_type=Integer)
        btc_tracker = btc_var.tracker

        usdt_var = Variable(3000, MathTex("USDT"), var_type=Integer).next_to(btc_var, DOWN, aligned_edge=LEFT)
        usdt_tracker = usdt_var.tracker

        usdt_var[ 0 ][ 0 ].set_color(BLUE)
        btc_var[ 0 ][ 0 ].set_color(ORANGE)

        # usdt_var_bar=usdt_var[ 1 ].copy()
        # btc_var_bar=usdt_var[ 1 ].copy()
        # usdt_var_bar.set_color(BLACK)
        # btc_var_bar.set_color(BLACK)

        vars = VGroup(btc_var, usdt_var).arrange(DOWN, aligned_edge=LEFT)

        vars.next_to(liq_pool_rect, DOWN, buff=0.25)

        self.play(ReplacementTransform(usdt_asset, usdt_bar),
                  ReplacementTransform(btc_asset, btc_bar))

        # self.play(Create())

        # self.play(Write(usdt_var_bar),
        #           Write(btc_var_bar))
        #
        self.play(Write(usdt_var),
                  Write(btc_var))
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        # usdt_bar.add_updater(lambda usdt_bar : usdt_bar.become(Rectangle(height=usdt_tracker.get_value()/10, width=1.2, color=BLUE).align_to(usdt_bar_pos, DOWN)))

        # self.play(usdt_tracker.animate.set_value(4000))
        # self.play(btc_tracker.animate.set_value(30))

        # self.play(k_var.animate.set_value(30000))
        k_var = Variable(30000, MathTex("k"), var_type=Integer).to_edge(UR, buff=0.5)
        k_tracker = k_var.tracker

        # self.add(index_labels(btc_var))
        pool_price = Variable(100, 'Price', var_type=DecimalNumber, num_decimal_places=2).next_to(
            liq_pool_rect, RIGHT, buff=1.5).to_edge(UP)
        pool_price_tracker = pool_price.tracker
        pool_price.add_updater(lambda v: pool_price_tracker.set_value(usdt_tracker.get_value() / btc_tracker.get_value()))
        pool_price_unit = Tex(r'\$').next_to(pool_price, buff=0.1)
        xyk_fraction.restore()
        self.play(Write(k_var[ 0 ]))
        self.play(Create(ax),
                  Create(axis_labels),
                  Create(pool_price_unit),
                  Create(pool_price),
                  TransformMatchingShapes(Group(btc_var[ 1 ].copy(), usdt_var[ 1 ].copy()), k_var[ 1 ].copy()),
                  Create(xyk_fraction.next_to(k_var, LEFT, buff=1))
                  )

        lp_amt_form_1 = MathTex(r'Init\  l =\sqrt{x \times y}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_2 = MathTex(r'Init\  l =\sqrt{10 \times 3000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_3 = MathTex(r'Init\  l =\sqrt{30000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_int = Tex(rf'{int(30000 ** (1 / 2))} LP token').move_to(lp_amt_form_1).scale(0.7)

        self.play(Create(lp_amt_form_1))
        self.play(TransformMatchingShapes(lp_amt_form_1, lp_amt_form_2))
        self.play(TransformMatchingShapes(lp_amt_form_2, lp_amt_form_3))
        self.play(TransformMatchingShapes(lp_amt_form_3, lp_amt_int))

        box = Rectangle(width=1.6, height=1, fill_color=WHITE, stroke_color=WHITE, fill_opacity=1)
        text = Tex(r"173\\BTC-USDT\\LP", color=BLACK).scale(0.5)

        lp_asset = VGroup(box, text).next_to(liq_provider[ 0 ], DOWN, buff=0.1)
        self.play(Create(lp_asset),
                  Uncreate(lp_amt_int))

        self.play(FadeOut(liq_provider),
                  FadeOut(lp_amt_int),
                  FadeOut(lp_asset))

        xyk_graph_btc = ax.plot(lambda x: k_tracker.get_value() / x,
                                x_range=[ 0.00001, 6000 ],
                                use_smoothing=False, color=GREY)

        xyk_graph_btc.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: k_tracker.get_value() / x,
                    x_range=[ k_tracker.get_value() / 6000, 16 ],
                    use_smoothing=False, color=GREY)))

        curr_dot = Dot(radius=0.1, color=GREY).move_to(ax.c2p(btc_tracker.get_value(),
                                                              xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        curr_dot.set_z_index(2)

        curr_dot.add_updater(lambda dot: dot.move_to(ax.c2p(btc_tracker.get_value(),
                                                            xyk_graph_btc.underlying_function(btc_tracker.get_value()))))

        lines_to_point = ax.get_lines_to_point(ax.c2p(1, 1), color=GREEN_B)

        vertical_line = ax.get_vertical_line(ax.c2p(btc_tracker.get_value(),
                                                    xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        horizontal_line = ax.get_horizontal_line(ax.c2p(btc_tracker.get_value(),
                                                        xyk_graph_btc.underlying_function(btc_tracker.get_value())))

        new_horzontal_line = VGroup()
        for i in range(1, len(horizontal_line) + 1):
            new_horzontal_line.add(horizontal_line[ -i ])

        horizontal_line = new_horzontal_line

        x_marker = Triangle(color=ORANGE, fill_color=ORANGE, fill_opacity=1).scale(0.1).next_to(vertical_line, DOWN, buff=0)
        x_marker.add_updater(lambda marker: marker.next_to(vertical_line, DOWN, buff=0))
        x_marker_val = Integer(btc_tracker.get_value())
        x_marker_val.add_updater(
            lambda integer: integer.become(Integer(btc_tracker.get_value()).scale(0.4).next_to(vertical_line, DOWN, buff=0.3)))

        y_marker = Triangle(color=BLUE, fill_color=BLUE, fill_opacity=1).scale(0.1).rotate(-PI / 2).next_to(horizontal_line, LEFT, buff=0)
        y_marker.add_updater(lambda marker: marker.next_to(horizontal_line, LEFT, buff=0))
        y_marker_val = Integer(usdt_tracker.get_value())
        y_marker_val.add_updater(lambda integer: integer.become(
            Integer(usdt_tracker.get_value()).scale(0.4).rotate(PI / 2).next_to(horizontal_line, LEFT, buff=0.3)))

        lines = VGroup(vertical_line, horizontal_line)
        markers = VGroup(x_marker, x_marker_val, y_marker, y_marker_val)

        # lines_to_point.add_updater(lambda lines: lines.become(ax.get_lines_to_point(
        #     ax.c2p(btc_tracker.get_value(),
        #            xyk_graph_btc.underlying_function(btc_tracker.get_value())),color=BLUE)))
        #
        self.play(Create(xyk_graph_btc))
        self.play(Create(curr_dot))

        self.play(Create(lines), run_time=2)
        self.play(Create(markers), run_time=2)

        vertical_line.add_updater(lambda line: line.become(ax.get_vertical_line(ax.c2p(btc_tracker.get_value(),
                                                                                       xyk_graph_btc.underlying_function(
                                                                                           btc_tracker.get_value())))))
        horizontal_line.add_updater(lambda line: line.become(ax.get_horizontal_line(ax.c2p(btc_tracker.get_value(),
                                                                                           xyk_graph_btc.underlying_function(
                                                                                               btc_tracker.get_value())))))

        # 사각형을 만들고 그 넓이와 길이는 점선 그리고 정렬을 원점에 nexxt to DR buff 0
        area = Rectangle(width=curr_dot.get_x() - ax.get_origin()[ 0 ], height=curr_dot.get_y() - ax.get_origin()[ 1 ], fill_color=GREEN,
                         fill_opacity=0.5, stroke_width=0).align_to(curr_dot.get_center(), UR)
        area.add_updater(lambda area: area.become(
            Rectangle(width=curr_dot.get_x() - ax.get_origin()[ 0 ], height=curr_dot.get_y() - ax.get_origin()[ 1 ], fill_color=GREEN,
                      fill_opacity=0.5, stroke_width=0).align_to(curr_dot.get_center(), UR)))

        area_text = MathTex(r'BTC \times  USDT').scale(0.5).arrange(DOWN, buff=0.1)
        area_text.add_updater(
            lambda text: text.become(MathTex(r'BTC \times USDT', 'in \  Pool').scale(0.4).arrange(DOWN, buff=0.1).move_to(area)))

        # area.add_updater(lambda)
        # print(ax.get_origin()-curr_dot.get_x())
        # print(ax.get_origin().get-curr_dot.get_y())

        self.play(Create(area))
        self.play(Create(area_text))

        # self.play(btc_tracker.animate.set_value(13),
        #           usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)))
        #
        # self.wait(1)
        #
        # self.play(btc_tracker.animate.set_value(7),
        #           usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)))
        #
        # self.play(FadeOut(liq_provider[ 0 ]))

        ####scnee 1 user will get btc from the pool in exchange of usdt

        self.wait(2)
        #######################################################################################
        #################################scene3##############################################
        # 이건 k값 상승을 위한 것
        #######################################################################################
        # 아ㅣ거 유동성 5개 아니라 3개로 수정

        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        # 유저 사라짐

        # self.play(FadeOut(user),
        #           FadeOut(user_asset_btc),
        #           FadeOut(user_asset_usdt))

        # 리퀴디티 프로바이더 다시 생성
        liq_provider = create_entity(Tex(r' \emph{New Liq\\provider}', color=BLACK).scale(0.8), 1, WHITE, "5 BTC", ORANGE, 1.4,
                                     0.3).next_to(
            liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "500 USDT", BLUE, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)

        self.play(Create(VGroup(liq_provider, usdt_asset)))

        btc_bar.clear_updaters()
        usdt_bar.clear_updaters()

        scene3_15btc_box = Rectangle(width=btc_bar.width, height=btc_bar.height * 0.5, stroke_width=3,
                                     stroke_color=GREEN_E).next_to(btc_bar, UP, buff=0)
        scene3_4500usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.5, stroke_width=3,
                                        stroke_color=GREEN_E).next_to(usdt_bar, UP, buff=0)

        self.play(Create(VGroup(scene3_15btc_box, scene3_4500usdt_box)))

        scene3_4500usdt_fill_box = scene3_4500usdt_box.copy().set_fill(BLUE, opacity=1)
        scene3_15btc_fill_box = scene3_15btc_box.copy().set_fill(ORANGE, opacity=1)
        scene3_15btc_fill_box.set_stroke(width=0, opacity=0)
        scene3_4500usdt_fill_box.set_stroke(width=0, opacity=0)

        scene3_15btc_fill_box.set_z_index(3)
        scene3_4500usdt_fill_box.set_z_index(3)

        scene3_4500usdt_brace = BraceBetweenPoints(scene3_4500usdt_box.get_corner(UR), scene3_4500usdt_box.get_corner(DR), color=GREEN_E,
                                                   stroke_color=GREEN_E,
                                                   stroke_width=3,
                                                   ).flip(axis=np.array([ 0., 1., 0. ])).next_to(scene3_4500usdt_fill_box,
                                                                                                 RIGHT)
        scene3_15btc_brace = BraceBetweenPoints(scene3_15btc_box.get_corner(UL), scene3_15btc_box.get_corner(DL), color=GREEN_E,
                                                stroke_color=GREEN_E, stroke_width=3
                                                ).next_to(scene3_15btc_fill_box,
                                                          LEFT)

        scene3_4500usdt_brace_label = Integer(btc_tracker.get_value())
        scene3_4500usdt_brace_label.add_updater(lambda label: label.become(
            Integer(1500).scale(0.4).rotate(-PI / 2).next_to(scene3_4500usdt_brace, RIGHT, buff=0.3)))
        scene3_15btc_brace_label = Integer(usdt_tracker.get_value())
        scene3_15btc_brace_label.add_updater(lambda label: label.become(
            Integer(5).scale(0.4).rotate(PI / 2).next_to(scene3_15btc_brace, LEFT, buff=0.3)))

        scene3_braces = VGroup(scene3_4500usdt_brace, scene3_15btc_brace)
        scene3_brace_labels = VGroup(scene3_4500usdt_brace_label, scene3_15btc_brace_label)

        new_liquidity_text = MathTex('5BTC', '=', '1500USDT').scale(0.5).next_to(liq_provider, DOWN, buff=2)

        scene3_origin_graph = xyk_graph_btc.copy()
        scene3_origin_graph.clear_updaters()
        scene3_origin_graph.set_color(RED)
        scene3_origin_graph.set_z_index(-1)
        self.add(scene3_origin_graph)

        # xyk_graph_btc = ax.plot(lambda x: k_tracker.get_value() / x,
        #                         x_range=[ 0.00001, 6000 ],
        #                         use_smoothing=False, color=PURPLE)
        #
        # xyk_graph_btc.add_updater(lambda graph: graph.become(
        #     ax.plot(lambda x: k_tracker.get_value() / x,
        #             x_range=[ k_tracker.get_value() / 6000, 20 ],
        #             use_smoothing=False, color=PURPLE)))

        self.play(Create(scene3_braces),
                  Create(scene3_brace_labels))

        # self.play(Create(origin_dot))
        box = Rectangle(width=1.6, height=1, fill_color=WHITE, stroke_color=WHITE, fill_opacity=1)
        text = Tex(r"87\\BTC-USDT\\LP", color=BLACK).scale(0.5)
        new_liq_provider_lp_asset = VGroup(box, text).next_to(liq_provider[ 0 ], DOWN, buff=0.1)

        lp_add_form_1 = MathTex(r"Added\  {l}' =l\times\frac{{x}'}{x}").next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_add_form_2 = MathTex(r"Added\  {l}' =\sqrt{30000}\times\frac{5}{10}").move_to(lp_add_form_1).scale(0.7)
        # lp_add_form_2.set_color_by_tex("5", ORANGE)
        # lp_add_form_2.set_color_by_tex("10", ORANGE)
        lp_add_form_3 = MathTex(r"Added\  {l}' =173\times0.5").move_to(lp_add_form_1).scale(0.7)
        lp_add_int = Tex(rf"{int(30000 ** (1 / 2) / 2)} LP token").move_to(lp_add_form_1).scale(0.7)
        total_lp_supply_1 = MathTex(r"Total\  l =l+{l}'").next_to(lp_add_form_1, UP).scale(0.7)
        total_lp_supply_2 = MathTex(r"Total\  l =173+86").move_to(lp_add_form_1).scale(0.7)
        total_lp_supply_int = Tex(rf"{int(30000 ** (1 / 2) + 30000 ** (1 / 2) / 2)} LP token").move_to(lp_add_form_1).scale(0.7)

        self.play(Create(lp_add_form_1))
        self.play(TransformMatchingShapes(lp_add_form_1, lp_add_form_2))
        self.play(TransformMatchingShapes(lp_add_form_2, lp_add_form_3))
        self.play(TransformMatchingShapes(lp_add_form_3, lp_add_int))
        self.play(Uncreate(lp_add_int))

        self.play(Create(total_lp_supply_1))
        self.play(TransformMatchingShapes(total_lp_supply_1, total_lp_supply_2))
        self.play(TransformMatchingShapes(total_lp_supply_2, total_lp_supply_int))
        self.play(Uncreate(total_lp_supply_int))

        usdt_asset.save_state()
        btc_asset.save_state()
        self.play(k_tracker.animate.set_value(67500),
                  btc_tracker.animate.set_value(15),
                  usdt_tracker.animate.set_value(67500 / 15),
                  ReplacementTransform(usdt_asset, scene3_4500usdt_fill_box),
                  ReplacementTransform(btc_asset, scene3_15btc_fill_box),
                  FadeIn(new_liq_provider_lp_asset, target_position=liq_pool_rect),
                  run_time=6)

        new_user_share_1 = MathTex(r"Share =\frac{UserLP}{TotSupply}").move_to(lp_add_form_1).scale(0.7)
        new_user_share_2 = MathTex(r"Share =0.33").move_to(lp_add_form_1).scale(0.7)
        new_user_share_3 = Tex(r"33\%").move_to(lp_add_form_1)

        self.play(Create(new_user_share_1))
        self.play(ReplacementTransform(new_user_share_1, new_user_share_2))
        self.play(TransformMatchingShapes(new_user_share_2, new_user_share_3))
        self.play(Uncreate(new_user_share_3))

        usdt_asset.restore()
        btc_asset.restore()

        dummydot = Dot(1, color=RED).move_to(liq_pool_rect)
        # self.play(Create(dummydot))

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(30000 / 10),
                  Transform(scene3_4500usdt_fill_box, usdt_asset),
                  Transform(scene3_15btc_fill_box, btc_asset),
                  FadeOut(new_liq_provider_lp_asset, target_position=dummydot),
                  run_time=6)

        self.wait(4)

        self.wait(2)


class amm_xyk_k_dn_4(Scene):
    def construct(self):
        amm_text = Tex('Automatic Market Maker').scale(2)

        #
        # 유동성 풀과 엑스와이는 케이 공식 텍스트로 보여주고
        xyk = MathTex('x', r'\times', 'y', '=', 'k').scale(2).next_to(amm_text, D)
        self.play(Create(amm_text))
        self.play(Write(xyk))

        #
        # 엑스는 거래쌍 중에 코인 A의 양 와이는 코인 비의 양 화살표로 보여주고 없애기
        A_coin_amt = Tex('A coin amount').shift(LEFT * 2 + DOWN * 2)
        B_coin_amt = Tex('B coin amount').shift(RIGHT * 2 + DOWN * 2)
        x_arrow = Arrow(end=A_coin_amt.get_top(), start=xyk[ 0 ].get_bottom())
        y_arrow = Arrow(end=B_coin_amt.get_top(), start=xyk[ 2 ].get_bottom())

        self.play(Create(x_arrow),
                  Create(y_arrow)
                  )

        self.play(Create(A_coin_amt),
                  Create(B_coin_amt))
        self.play(Uncreate(A_coin_amt),
                  Uncreate(B_coin_amt),
                  Uncreate(x_arrow),
                  Uncreate(y_arrow)
                  )

        #
        # 와이는 엑스부느이 케이로 변형
        xyk_fraction = MathTex('y', '=', r'\frac{k}{x}').scale(2)

        self.play(TransformMatchingShapes(xyk, xyk_fraction))
        self.play(xyk_fraction.animate.to_edge(UP).scale(0.6))

        self.wait(1)
        #

        # 풀도 만들기

        xyk_and_liq = VGroup(xyk_fraction)

        self.play(xyk_and_liq.animate.to_edge(LEFT).shift(RIGHT))
        #
        # 엑스는 와이분의 일 그래프 예시로 보여주기
        graph_range = 50

        ax = Axes(x_range=[ 0, graph_range, int(graph_range / 10) ],
                  y_range=[ 0, graph_range, int(graph_range / 10) ],
                  x_length=6,
                  y_length=6,

                  tips=True,
                  axis_config={"include_numbers": True, 'font_size': 20, 'tip_width': 0.1, 'tip_height': 0.1},
                  )

        self.play(Create(ax))

        k_var = Variable(1, MathTex("k"), var_type=Integer)
        k_tracker = k_var.tracker
        k_tracker.set_value(1)
        # var = 10.5
        self.wait()

        xyk_graph = ax.plot(lambda x: k_tracker.get_value() / x,
                            x_range=[ 0.00001, 20 ],
                            use_smoothing=False, color=BLUE)

        xyk_graph.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: k_tracker.get_value() / x,
                    x_range=[ k_tracker.get_value() / graph_range, graph_range ],
                    use_smoothing=False, color=BLUE)))

        self.play(Create(xyk_graph))
        k_var.next_to(ax, UR)
        self.play(Create(k_var))

        self.play(k_tracker.animate.set_value(300), run_time=4)

        xyk_fraction.save_state()

        self.play(Uncreate(ax),
                  Uncreate(xyk_graph),
                  Uncreate(xyk_fraction),
                  Uncreate(k_var))

        liq_pool_rect = RoundedRectangle(height=6.3, width=4, corner_radius=0.5)
        liq_pool_text = Tex('Liquidity Pool').next_to(liq_pool_rect, UP)

        liq_pool = VGroup(liq_pool_rect, liq_pool_text).to_edge(UL)

        liq_pool.set_z_index(3)

        # self.add(index_labels(liq_pool[ 0 ]))
        self.play(Create(liq_pool))

        liq_provider = create_entity(Tex(r' \emph{Liq\\provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", ORANGE, 1.4, 0.3).next_to(
            liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", BLUE, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)

        liq_provider_asset = VGroup(btc_asset, usdt_asset)

        liq_provider.add(usdt_asset)
        self.play(Create(liq_provider))

        # self.play(liq_provider_asset.animate.arrange(RIGHT,buff=0.5))

        graph_range = 50
        ax = Axes(x_range=[ 0, 18, 4 ],
                  y_range=[ 0, 6500, 1000 ],
                  x_length=5,
                  y_length=5,

                  tips=True,
                  axis_config={"include_numbers": False, 'include_ticks': False, 'font_size': 20, 'tip_width': 0.1, 'tip_height': 0.1},
                  y_axis_config={"include_numbers": False, 'font_size': 20}
                  ).to_edge(DR, buff=0.8)

        y_axis_label = ax.get_y_axis_label(MathTex('Amount of USDT in Pool').rotate(PI / 2).scale(0.4), edge=LEFT, direction=LEFT, buff=0.5)
        # self.add(y_axis_label)

        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool').scale(0.4), edge=DOWN, direction=DOWN, buff=0.5)
        # self.add(x_axis_label)

        axis_labels = VGroup(x_axis_label, y_axis_label)

        usdt_bar = Rectangle(height=3, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE)
        btc_bar = Rectangle(height=1, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE)

        bars = VGroup(btc_bar, usdt_bar)
        bars.arrange(RIGHT, aligned_edge=DOWN).move_to(liq_pool_rect).align_to(liq_pool_rect, DOWN)

        usdt_bar_pos = usdt_bar.get_bottom()
        btc_bar_pos = btc_bar.get_bottom()

        k_tracker.set_value(30000)

        btc_var = Variable(10, MathTex("BTC"), var_type=Integer)
        btc_tracker = btc_var.tracker

        usdt_var = Variable(3000, MathTex("USDT"), var_type=Integer).next_to(btc_var, DOWN, aligned_edge=LEFT)
        usdt_tracker = usdt_var.tracker

        usdt_var[ 0 ][ 0 ].set_color(BLUE)
        btc_var[ 0 ][ 0 ].set_color(ORANGE)

        # usdt_var_bar=usdt_var[ 1 ].copy()
        # btc_var_bar=usdt_var[ 1 ].copy()
        # usdt_var_bar.set_color(BLACK)
        # btc_var_bar.set_color(BLACK)

        vars = VGroup(btc_var, usdt_var).arrange(DOWN, aligned_edge=LEFT)

        vars.next_to(liq_pool_rect, DOWN, buff=0.25)

        self.play(ReplacementTransform(usdt_asset, usdt_bar),
                  ReplacementTransform(btc_asset, btc_bar))

        # self.play(Write(usdt_var_bar),
        #           Write(btc_var_bar))
        #
        self.play(Write(usdt_var),
                  Write(btc_var))

        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        # usdt_bar.add_updater(lambda usdt_bar : usdt_bar.become(Rectangle(height=usdt_tracker.get_value()/10, width=1.2, color=BLUE).align_to(usdt_bar_pos, DOWN)))

        # self.play(usdt_tracker.animate.set_value(4000))
        # self.play(btc_tracker.animate.set_value(30))

        # self.play(k_var.animate.set_value(30000))
        k_var = Variable(30000, MathTex("k"), var_type=Integer).to_edge(UR, buff=0.5)
        k_tracker = k_var.tracker

        # self.add(index_labels(btc_var))
        pool_price = Variable(100, 'Price', var_type=DecimalNumber, num_decimal_places=2).next_to(
            liq_pool_rect, RIGHT, buff=1.5).to_edge(UP)
        pool_price_tracker = pool_price.tracker
        pool_price.add_updater(lambda v: pool_price_tracker.set_value(usdt_tracker.get_value() / btc_tracker.get_value()))

        xyk_fraction.restore()
        self.play(Write(k_var[ 0 ]))
        self.play(Create(ax),
                  Create(axis_labels),
                  Create(pool_price),
                  TransformMatchingShapes(Group(btc_var[ 1 ].copy(), usdt_var[ 1 ].copy()), k_var[ 1 ].copy()),
                  Create(xyk_fraction.next_to(k_var, LEFT, buff=1))
                  )
        self.play(FadeOut(liq_provider))
        xyk_graph_btc = ax.plot(lambda x: k_tracker.get_value() / x,
                                x_range=[ 0.00001, 6000 ],
                                use_smoothing=False, color=PURPLE)

        xyk_graph_btc.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: k_tracker.get_value() / x,
                    x_range=[ k_tracker.get_value() / 6000, 20 ],
                    use_smoothing=False, color=GREY)))

        curr_dot = Dot(radius=0.1, color=GREY).move_to(ax.c2p(btc_tracker.get_value(),
                                                              xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        curr_dot.set_z_index(2)

        curr_dot.add_updater(lambda dot: dot.move_to(ax.c2p(btc_tracker.get_value(),
                                                            xyk_graph_btc.underlying_function(btc_tracker.get_value()))))

        lines_to_point = ax.get_lines_to_point(ax.c2p(1, 1), color=GREEN_B)

        vertical_line = ax.get_vertical_line(ax.c2p(btc_tracker.get_value(),
                                                    xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        horizontal_line = ax.get_horizontal_line(ax.c2p(btc_tracker.get_value(),
                                                        xyk_graph_btc.underlying_function(btc_tracker.get_value())))

        new_horzontal_line = VGroup()
        for i in range(1, len(horizontal_line) + 1):
            new_horzontal_line.add(horizontal_line[ -i ])

        horizontal_line = new_horzontal_line

        x_marker = Triangle(color=ORANGE, fill_color=ORANGE, fill_opacity=1).scale(0.1).next_to(vertical_line, DOWN, buff=0)
        x_marker.add_updater(lambda marker: marker.next_to(vertical_line, DOWN, buff=0))
        x_marker_val = Integer(btc_tracker.get_value())
        x_marker_val.add_updater(
            lambda integer: integer.become(Integer(btc_tracker.get_value()).scale(0.4).next_to(vertical_line, DOWN, buff=0.3)))

        y_marker = Triangle(color=BLUE, fill_color=BLUE, fill_opacity=1).scale(0.1).rotate(-PI / 2).next_to(horizontal_line, LEFT, buff=0)
        y_marker.add_updater(lambda marker: marker.next_to(horizontal_line, LEFT, buff=0))
        y_marker_val = Integer(usdt_tracker.get_value())
        y_marker_val.add_updater(lambda integer: integer.become(
            Integer(usdt_tracker.get_value()).scale(0.4).rotate(PI / 2).next_to(horizontal_line, LEFT, buff=0.3)))

        lines = VGroup(vertical_line, horizontal_line)
        markers = VGroup(x_marker, x_marker_val, y_marker, y_marker_val)

        # lines_to_point.add_updater(lambda lines: lines.become(ax.get_lines_to_point(
        #     ax.c2p(btc_tracker.get_value(),
        #            xyk_graph_btc.underlying_function(btc_tracker.get_value())),color=BLUE)))
        #
        self.play(Create(xyk_graph_btc))
        self.play(Create(curr_dot))

        self.play(Create(lines), run_time=2)
        self.play(Create(markers), run_time=2)

        vertical_line.add_updater(lambda line: line.become(ax.get_vertical_line(ax.c2p(btc_tracker.get_value(),
                                                                                       xyk_graph_btc.underlying_function(
                                                                                           btc_tracker.get_value())))))
        horizontal_line.add_updater(lambda line: line.become(ax.get_horizontal_line(ax.c2p(btc_tracker.get_value(),
                                                                                           xyk_graph_btc.underlying_function(
                                                                                               btc_tracker.get_value())))))

        # 사각형을 만들고 그 넓이와 길이는 점선 그리고 정렬을 원점에 nexxt to DR buff 0
        area = Rectangle(width=curr_dot.get_x() - ax.get_origin()[ 0 ], height=curr_dot.get_y() - ax.get_origin()[ 1 ], fill_color=GREEN,
                         fill_opacity=0.5, stroke_width=0).align_to(curr_dot.get_center(), UR)
        area.add_updater(lambda area: area.become(
            Rectangle(width=curr_dot.get_x() - ax.get_origin()[ 0 ], height=curr_dot.get_y() - ax.get_origin()[ 1 ], fill_color=GREEN,
                      fill_opacity=0.5, stroke_width=0).align_to(curr_dot.get_center(), UR)))

        area_text = MathTex(r'BTC \times  USDT').scale(0.5).arrange(DOWN, buff=0.1)
        area_text.add_updater(
            lambda text: text.become(MathTex(r'BTC \times USDT', 'in \  Pool').scale(0.4).arrange(DOWN, buff=0.1).move_to(area)))

        # area.add_updater(lambda)
        # print(ax.get_origin()-curr_dot.get_x())
        # print(ax.get_origin().get-curr_dot.get_y())

        self.play(Create(area))
        self.play(Create(area_text))

        # self.play(btc_tracker.animate.set_value(13),
        #           usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)))
        #
        # self.wait(1)
        #
        # self.play(btc_tracker.animate.set_value(7),
        #           usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)))
        #
        # self.play(FadeOut(liq_provider[ 0 ]))

        ####scnee 1 user will get btc from the pool in exchange of usdt

        self.wait(2)

        #######################################################################################
        #################################scene4##############################################
        #######################################################################################
        # 아ㅣ거 유동성 5개 아니라 3개로 수정

        liq_provider = create_entity(Tex(r' \emph{Liq\\provider}', color=BLACK).scale(0.8), 1, WHITE, "5 BTC", ORANGE, 1.4, 0.3).next_to(
            liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "1500 USDT", BLUE, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)

        self.play(Create(liq_provider[ 0 ]))

        btc_bar.clear_updaters()
        usdt_bar.clear_updaters()

        # # scene2_btc_dashed_box = Rectangle(color=RED).align_to(btc_bar[0],UL,alignment_vect=btc_bar[0].get_edge_center(UP))
        # scene2_2308usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.2307, stroke_width=3,
        #                                 stroke_color=RED_E).align_to(usdt_bar, UL)

        scene4_5btc_box = Rectangle(width=btc_bar.width, height=btc_bar.height * 0.5, stroke_width=3,
                                    stroke_color=RED_E).align_to(btc_bar, UL)
        scene4_1500usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.5, stroke_width=3,
                                        stroke_color=RED_E).align_to(usdt_bar, UL)

        scene4_1500usdt_fill_box = scene4_1500usdt_box.copy().set_fill(BLUE, opacity=1)
        scene4_5btc_fill_box = scene4_5btc_box.copy().set_fill(ORANGE, opacity=1)

        scene4_5btc_fill_box.set_stroke(width=0, opacity=0)
        scene4_1500usdt_fill_box.set_stroke(width=0, opacity=0)
        scene4_5btc_fill_box.set_z_index(3)
        scene4_1500usdt_fill_box.set_z_index(3)

        self.play(Create(VGroup(scene4_5btc_box, scene4_1500usdt_box)))
        self.add(scene4_5btc_fill_box, scene4_1500usdt_fill_box)

        scene4_1500usdt_brace = BraceBetweenPoints(scene4_1500usdt_box.get_corner(UR), scene4_1500usdt_box.get_corner(DR), color=RED_E,
                                                   stroke_color=RED_E,
                                                   stroke_width=3,
                                                   ).flip(axis=np.array([ 0., 1., 0. ])).next_to(scene4_1500usdt_fill_box,
                                                                                                 RIGHT)
        scene4_5btc_brace = BraceBetweenPoints(scene4_5btc_box.get_corner(UL), scene4_5btc_box.get_corner(DL), color=RED_E,
                                               stroke_color=RED_E, stroke_width=3
                                               ).next_to(scene4_5btc_fill_box,
                                                         LEFT)
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=1500 / 1000, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=5 / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        scene4_1500usdt_brace_label = Integer(btc_tracker.get_value())
        scene4_1500usdt_brace_label.add_updater(lambda label: label.become(
            Integer(1500).scale(0.4).rotate(-PI / 2).next_to(scene4_1500usdt_brace, RIGHT, buff=0.3)))
        scene4_5btc_brace_label = Integer(usdt_tracker.get_value())
        scene4_5btc_brace_label.add_updater(lambda label: label.become(
            Integer(5).scale(0.4).rotate(PI / 2).next_to(scene4_5btc_brace, LEFT, buff=0.3)))

        scene4_braces = VGroup(scene4_1500usdt_brace, scene4_5btc_brace)
        scene4_brace_labels = VGroup(scene4_1500usdt_brace_label, scene4_5btc_brace_label)

        new_liquidity_text = MathTex('5BTC', '=', '1500USDT').scale(0.5).next_to(liq_provider, DOWN, buff=2)

        self.play(Create(new_liquidity_text))

        scene4_origin_graph = xyk_graph_btc.copy()
        scene4_origin_graph.clear_updaters()
        scene4_origin_graph.set_color(RED)
        scene4_origin_graph.set_z_index(-1)
        self.add(scene4_origin_graph)

        self.play(Create(scene4_braces),
                  Create(scene4_brace_labels))

        # self.play(Create(origin_dot))
        self.play(k_tracker.animate.set_value(7500),
                  btc_tracker.animate.set_value(5),
                  usdt_tracker.animate.set_value(7500 / 5),
                  Transform(scene4_1500usdt_fill_box, usdt_asset),
                  Transform(scene4_5btc_fill_box, btc_asset),
                  run_time=6, rate_func=rate_functions.ease_in_out_quint)

        self.wait(4)


class amm_xyk_various_case_5(Scene):
    def construct(self):
        amm_text = Tex('Automatic Market Maker').scale(2)

        #
        # 유동성 풀과 엑스와이는 케이 공식 텍스트로 보여주고
        xyk = MathTex('x', r'\times', 'y', '=', 'k').scale(2)
        self.play(Create(amm_text))
        self.play(Uncreate(amm_text))
        self.play(Write(xyk))

        #
        # 엑스는 거래쌍 중에 코인 A의 양 와이는 코인 비의 양 화살표로 보여주고 없애기
        A_coin_amt = Tex('A coin amount').shift(LEFT * 2 + DOWN * 2)
        B_coin_amt = Tex('B coin amount').shift(RIGHT * 2 + DOWN * 2)
        x_arrow = Arrow(end=A_coin_amt.get_top(), start=xyk[ 0 ].get_bottom())
        y_arrow = Arrow(end=B_coin_amt.get_top(), start=xyk[ 2 ].get_bottom())

        self.play(Create(x_arrow),
                  Create(y_arrow)
                  )

        self.play(Create(A_coin_amt),
                  Create(B_coin_amt))
        self.play(Uncreate(A_coin_amt),
                  Uncreate(B_coin_amt),
                  Uncreate(x_arrow),
                  Uncreate(y_arrow)
                  )

        #
        # 와이는 엑스부느이 케이로 변형
        xyk_fraction = MathTex('y', '=', r'\frac{k}{x}').scale(2)

        self.play(TransformMatchingShapes(xyk, xyk_fraction))
        self.play(xyk_fraction.animate.to_edge(UP).scale(0.6))

        self.wait(1)
        #

        # 풀도 만들기

        xyk_and_liq = VGroup(xyk_fraction)

        self.play(xyk_and_liq.animate.to_edge(LEFT).shift(RIGHT))
        #
        # 엑스는 와이분의 일 그래프 예시로 보여주기
        graph_range = 50

        ax = Axes(x_range=[ 0, graph_range, int(graph_range / 10) ],
                  y_range=[ 0, graph_range, int(graph_range / 10) ],
                  x_length=6,
                  y_length=6,

                  tips=True,
                  axis_config={"include_numbers": True, 'color': GREY, 'font_size': 20, 'tip_width': 0.1, 'tip_height': 0.1},
                  )

        self.play(Create(ax))

        k_var = Variable(1, MathTex("k"), var_type=Integer)
        k_tracker = k_var.tracker
        k_tracker.set_value(1)
        # var = 10.5
        self.wait()

        xyk_graph = ax.plot(lambda x: k_tracker.get_value() / x,
                            x_range=[ 0.00001, 20 ],
                            use_smoothing=False, color=BLUE)

        xyk_graph.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: k_tracker.get_value() / x,
                    x_range=[ k_tracker.get_value() / graph_range, graph_range ],
                    use_smoothing=False, color=BLUE)))

        self.play(Create(xyk_graph))
        k_var.next_to(ax, UR)
        self.play(Create(k_var))

        self.play(k_tracker.animate.set_value(300), run_time=4)

        xyk_fraction.save_state()

        self.play(Uncreate(ax),
                  Uncreate(xyk_graph),
                  Uncreate(xyk_fraction),
                  Uncreate(k_var))

        liq_pool_rect = RoundedRectangle(height=6.3, width=4, corner_radius=0.5)
        liq_pool_text = Tex('Liquidity Pool').next_to(liq_pool_rect, UP)

        liq_pool = VGroup(liq_pool_rect, liq_pool_text).to_edge(UL)

        liq_pool.set_z_index(3)

        # self.add(index_labels(liq_pool[ 0 ]))
        self.play(Create(liq_pool))

        liq_provider = create_entity(Tex(r' \emph{Init Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", ORANGE, 1.4,
                                     0.3).next_to(
            liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", BLUE, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)

        liq_provider_asset = VGroup(btc_asset, usdt_asset)

        liq_provider.add(usdt_asset)
        self.play(Create(liq_provider))

        # self.play(liq_provider_asset.animate.arrange(RIGHT,buff=0.5))

        graph_range = 50
        ax = Axes(x_range=[ 0, 18, 4 ],
                  y_range=[ 0, 6500, 1000 ],
                  x_length=5,
                  y_length=5,

                  tips=True,
                  axis_config={"include_numbers": False, 'color': GREY, 'include_ticks': False, 'font_size': 20, 'tip_width': 0.1,
                               'tip_height': 0.1},
                  y_axis_config={"include_numbers": False, 'font_size': 20}
                  ).to_edge(DR, buff=0.8)

        y_axis_label = ax.get_y_axis_label(MathTex('Amount of USDT in Pool').rotate(PI / 2).scale(0.4), edge=LEFT, direction=LEFT, buff=0.5)
        # self.add(y_axis_label)

        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool').scale(0.4), edge=DOWN, direction=DOWN, buff=0.5)
        # self.add(x_axis_label)

        axis_labels = VGroup(x_axis_label, y_axis_label)

        usdt_bar = Rectangle(height=3, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE)
        btc_bar = Rectangle(height=1, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE)

        bars = VGroup(btc_bar, usdt_bar)
        bars.arrange(RIGHT, aligned_edge=DOWN).move_to(liq_pool_rect).align_to(liq_pool_rect, DOWN)

        usdt_bar_pos = usdt_bar.get_bottom()
        btc_bar_pos = btc_bar.get_bottom()

        k_tracker.set_value(30000)

        btc_var = Variable(10, MathTex("BTC"), var_type=Integer)
        btc_tracker = btc_var.tracker

        usdt_var = Variable(3000, MathTex("USDT"), var_type=Integer).next_to(btc_var, DOWN, aligned_edge=LEFT)
        usdt_tracker = usdt_var.tracker

        usdt_var[ 0 ][ 0 ].set_color(BLUE)
        btc_var[ 0 ][ 0 ].set_color(ORANGE)

        # usdt_var_bar=usdt_var[ 1 ].copy()
        # btc_var_bar=usdt_var[ 1 ].copy()
        # usdt_var_bar.set_color(BLACK)
        # btc_var_bar.set_color(BLACK)

        vars = VGroup(btc_var, usdt_var).arrange(DOWN, aligned_edge=LEFT)

        vars.next_to(liq_pool_rect, DOWN, buff=0.25)

        self.play(ReplacementTransform(usdt_asset, usdt_bar),
                  ReplacementTransform(btc_asset, btc_bar))

        # self.play(Create())

        # self.play(Write(usdt_var_bar),
        #           Write(btc_var_bar))
        #
        self.play(Write(usdt_var),
                  Write(btc_var))
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        # usdt_bar.add_updater(lambda usdt_bar : usdt_bar.become(Rectangle(height=usdt_tracker.get_value()/10, width=1.2, color=BLUE).align_to(usdt_bar_pos, DOWN)))

        # self.play(usdt_tracker.animate.set_value(4000))
        # self.play(btc_tracker.animate.set_value(30))

        # self.play(k_var.animate.set_value(30000))
        k_var = Variable(30000, MathTex("k"), var_type=Integer).to_edge(UR, buff=0.5)
        k_tracker = k_var.tracker

        # self.add(index_labels(btc_var))
        pool_price = Variable(100, 'Price', var_type=DecimalNumber, num_decimal_places=2).next_to(
            liq_pool_rect, RIGHT, buff=1.5).to_edge(UP)
        pool_price_tracker = pool_price.tracker
        pool_price.add_updater(lambda v: pool_price_tracker.set_value(usdt_tracker.get_value() / btc_tracker.get_value()))
        pool_price_unit = Tex(r'\$').next_to(pool_price, RIGHT, buff=0.1)
        xyk_fraction.restore()
        self.play(Write(k_var[ 0 ]))
        self.play(Create(ax),
                  Create(axis_labels),
                  Create(pool_price),
                  Create(pool_price_unit),
                  TransformMatchingShapes(Group(btc_var[ 1 ].copy(), usdt_var[ 1 ].copy()), k_var[ 1 ].copy()),
                  Create(xyk_fraction.next_to(k_var, LEFT, buff=1))
                  )

        lp_amt_form_1 = MathTex(r'Init\  l =\sqrt{x \times y}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_2 = MathTex(r'Init\  l =\sqrt{10 \times 3000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_3 = MathTex(r'Init\  l =\sqrt{30000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_int = Integer(int(30000 ** (1 / 2))).move_to(lp_amt_form_1).scale(0.7)

        self.play(Create(lp_amt_form_1))
        self.play(TransformMatchingShapes(lp_amt_form_1, lp_amt_form_2))
        self.play(TransformMatchingShapes(lp_amt_form_2, lp_amt_form_3))
        self.play(TransformMatchingShapes(lp_amt_form_3, lp_amt_int))

        box = Rectangle(width=1.6, height=1, fill_color=BLUE, stroke_color=BLUE, fill_opacity=1)
        text = Tex(r"173\\BTC-USDT\\LP", color=BLACK).scale(0.5)

        lp_asset = VGroup(box, text).next_to(liq_provider[ 0 ], DOWN, buff=0.1)
        self.play(Create(lp_asset))

        self.play(FadeOut(liq_provider),
                  FadeOut(lp_amt_int),
                  FadeOut(lp_asset))

        xyk_graph_btc = ax.plot(lambda x: k_tracker.get_value() / x,
                                x_range=[ 0.00001, 6000 ],
                                use_smoothing=False, color=GREY)

        xyk_graph_btc.add_updater(lambda graph: graph.become(
            ax.plot(lambda x: k_tracker.get_value() / x,
                    x_range=[ k_tracker.get_value() / 6000, 16 ],
                    use_smoothing=False, color=GREY)))

        curr_dot = Dot(radius=0.1, color=GREY).move_to(ax.c2p(btc_tracker.get_value(),
                                                              xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        curr_dot.set_z_index(2)

        curr_dot.add_updater(lambda dot: dot.move_to(ax.c2p(btc_tracker.get_value(),
                                                            xyk_graph_btc.underlying_function(btc_tracker.get_value()))))

        lines_to_point = ax.get_lines_to_point(ax.c2p(1, 1), color=GREEN_B)

        vertical_line = ax.get_vertical_line(ax.c2p(btc_tracker.get_value(),
                                                    xyk_graph_btc.underlying_function(btc_tracker.get_value())))
        horizontal_line = ax.get_horizontal_line(ax.c2p(btc_tracker.get_value(),
                                                        xyk_graph_btc.underlying_function(btc_tracker.get_value())))

        new_horzontal_line = VGroup()
        for i in range(1, len(horizontal_line) + 1):
            new_horzontal_line.add(horizontal_line[ -i ])

        horizontal_line = new_horzontal_line

        x_marker = Triangle(color=ORANGE, fill_color=ORANGE, fill_opacity=1).scale(0.1).next_to(vertical_line, DOWN, buff=0)
        x_marker.add_updater(lambda marker: marker.next_to(vertical_line, DOWN, buff=0))
        x_marker_val = Integer(btc_tracker.get_value())
        x_marker_val.add_updater(
            lambda integer: integer.become(Integer(btc_tracker.get_value()).scale(0.4).next_to(vertical_line, DOWN, buff=0.3)))

        y_marker = Triangle(color=BLUE, fill_color=BLUE, fill_opacity=1).scale(0.1).rotate(-PI / 2).next_to(horizontal_line, LEFT, buff=0)
        y_marker.add_updater(lambda marker: marker.next_to(horizontal_line, LEFT, buff=0))
        y_marker_val = Integer(usdt_tracker.get_value())
        y_marker_val.add_updater(lambda integer: integer.become(
            Integer(usdt_tracker.get_value()).scale(0.4).rotate(PI / 2).next_to(horizontal_line, LEFT, buff=0.3)))

        lines = VGroup(vertical_line, horizontal_line)
        markers = VGroup(x_marker, x_marker_val, y_marker, y_marker_val)

        # lines_to_point.add_updater(lambda lines: lines.become(ax.get_lines_to_point(
        #     ax.c2p(btc_tracker.get_value(),
        #            xyk_graph_btc.underlying_function(btc_tracker.get_value())),color=BLUE)))
        #
        self.play(Create(xyk_graph_btc))
        self.play(Create(curr_dot))

        self.play(Create(lines), run_time=2)
        self.play(Create(markers), run_time=2)

        vertical_line.add_updater(lambda line: line.become(ax.get_vertical_line(ax.c2p(btc_tracker.get_value(),
                                                                                       xyk_graph_btc.underlying_function(
                                                                                           btc_tracker.get_value())))))
        horizontal_line.add_updater(lambda line: line.become(ax.get_horizontal_line(ax.c2p(btc_tracker.get_value(),
                                                                                           xyk_graph_btc.underlying_function(
                                                                                               btc_tracker.get_value())))))

        # 사각형을 만들고 그 넓이와 길이는 점선 그리고 정렬을 원점에 nexxt to DR buff 0
        area = Rectangle(width=curr_dot.get_x() - ax.get_origin()[ 0 ], height=curr_dot.get_y() - ax.get_origin()[ 1 ], fill_color=GREEN,
                         fill_opacity=0.5, stroke_width=0).align_to(curr_dot.get_center(), UR)
        area.add_updater(lambda area: area.become(
            Rectangle(width=curr_dot.get_x() - ax.get_origin()[ 0 ], height=curr_dot.get_y() - ax.get_origin()[ 1 ], fill_color=GREEN,
                      fill_opacity=0.5, stroke_width=0).align_to(curr_dot.get_center(), UR)))

        area_text = MathTex(r'BTC \times  USDT').scale(0.5).arrange(DOWN, buff=0.1)
        area_text.add_updater(
            lambda text: text.become(MathTex(r'BTC \times USDT', 'in \  Pool').scale(0.4).arrange(DOWN, buff=0.1).move_to(area)))

        # area.add_updater(lambda)
        # print(ax.get_origin()-curr_dot.get_x())
        # print(ax.get_origin().get-curr_dot.get_y())

        self.play(Create(area))
        self.play(Create(area_text))

        # self.play(btc_tracker.animate.set_value(13),
        #           usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)))
        #
        # self.wait(1)
        #
        # self.play(btc_tracker.animate.set_value(7),
        #           usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)))
        #
        # self.play(FadeOut(liq_provider[ 0 ]))

        ####scnee 1 user will get btc from the pool in exchange of usdt

        self.wait(2)

        ########################################################################################올라갔을 때
        ######################################Scen1#############################올라갔을 때
        ########################################################################################올라갔을 때

        # user = create_entity(Tex(r' \emph{User}', color=BLACK).scale(0.5), 0.5, WHITE, "1286 USDT", BLUE,1.4, 0.3).next_to(liq_pool_rect, RIGHT,
        #                                                                                                                buff=2)
        # user_asset_usdt = user[ 1 ]
        # user_asset_pos = user_asset_usdt.get_center()
        # user_asset_btc = create_entity("A", 0.5, WHITE, "3 BTC", ORANGE, 1.4, 0.3)[ 1 ].move_to(user_asset_pos)
        #
        # user_line = Tex(r'I want 3 BTC\\I have some USDT').scale(0.5).next_to(user, DOWN)
        #
        # self.play(Create(user))
        # self.play(Create(user_line))
        # self.play(Uncreate(user_line))
        #
        # # self.add(index_labels(btc_bar))###
        #
        # # scene1_btc_dashed_box = Rectangle(color=RED).align_to(btc_bar[0],UL,alignment_vect=btc_bar[0].get_edge_center(UP))
        # scene1_7btc_box = Rectangle(width=btc_bar.width, height=btc_bar.height * 0.3, stroke_width=3, stroke_color=RED_E).align_to(
        #     btc_bar[ 0 ], UL)
        # scene1_13btc_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.4286, stroke_width=3,
        #                              stroke_color=GREEN_E).next_to(usdt_bar, UP, buff=0)
        #
        # scene1_7btc_fill_box = scene1_7btc_box.copy().set_fill(ORANGE, opacity=1)
        # scene1_13btc_fill_box = scene1_13btc_box.copy().set_fill(BLUE, opacity=1)
        # scene1_7btc_fill_box.set_stroke(width=0, opacity=0)
        # scene1_13btc_fill_box.set_stroke(width=0, opacity=0)
        # scene1_7btc_fill_box.set_z_index(3)
        # scene1_13btc_fill_box.set_z_index(3)

        # self.play(Create(scene1_7btc_box))
        # self.play(Create(scene1_13btc_box))
        # scene1_7btc_brace = BraceBetweenPoints(scene1_7btc_box.get_corner(UL), scene1_7btc_box.get_corner(DL), color=RED_E,
        #                                        stroke_color=RED_E,
        #                                        stroke_width=3,
        #                                        ).next_to(scene1_7btc_box, LEFT)
        # scene1_13btc_brace = BraceBetweenPoints(scene1_13btc_box.get_corner(UR), scene1_13btc_box.get_corner(DR), color=GREEN_E,
        #                                         stroke_color=GREEN_E, stroke_width=3
        #                                         ).flip(axis=np.array([ 0., 1., 0. ])).next_to(scene1_13btc_box,
        #                                                                                       RIGHT)
        #
        # scene1_7btc_brace_label = Integer(btc_tracker.get_value())
        # scene1_7btc_brace_label.add_updater(lambda label: label.become(
        #     Integer(3).scale(0.4).rotate(PI / 2).next_to(scene1_7btc_brace, LEFT, buff=0.3)))
        # scene1_13btc_brace_label = Integer(usdt_tracker.get_value())
        # scene1_13btc_brace_label.add_updater(lambda label: label.become(
        #     Integer(1286).scale(0.4).rotate(-PI / 2).next_to(scene1_13btc_brace, RIGHT, buff=0.3)))
        #
        # scene1_braces = VGroup(scene1_7btc_brace, scene1_13btc_brace)
        # scene1_brace_labels = VGroup(scene1_7btc_brace_label, scene1_13btc_brace_label)
        #
        # self.play(Create(scene1_braces),
        #           Create(scene1_brace_labels))
        #
        # usdt_bar.clear_updaters()
        # btc_bar.clear_updaters()
        #
        # self.add(scene1_7btc_fill_box)
        # # usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
        # #     Rectangle(height=4283 / 1000, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE).move_to(
        # #         usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        # btc_bar.add_updater(lambda btc_bar: btc_bar.become(
        #     Rectangle(height=7 / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
        #         btc_bar_pos).align_to(liq_pool_rect, DOWN)))
        #
        # origin_dot = curr_dot.copy()
        # origin_dot.clear_updaters()
        # origin_dot.set_color(GREEN)
        # origin_dot.set_z_index(1.5)
        # self.play(Create(origin_dot))
        # self.play(btc_tracker.animate.set_value(7),
        # #         usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
        #           Transform(scene1_7btc_fill_box, user_asset_btc),
        #           Transform(user_asset_usdt, scene1_13btc_fill_box))
        #
        # scene1_arrow = CurvedArrow(origin_dot.get_center(), curr_dot.get_center(), radius=-4, tip_length=0.25).shift(
        #     RIGHT * 0.3 + UP * 0.3)
        # scene1_arrow_label = Tex('Buy BTC in exchange of USDT').scale(0.3).next_to(scene1_arrow, UR)
        #
        # self.play(Create(scene1_arrow))
        #
        # scene1_slippage_text = Tex(r'I just used 1283 USDT \\to buy 3 BTC').scale(0.5).next_to(user_asset_pos, DOWN)
        # scene1_slippage_form = MathTex(r'1283 \divisionsymbol 3').next_to(scene1_slippage_text, DOWN)
        # scene1_slippage_result = MathTex(rf'{int((k_tracker.get_value() / btc_tracker.get_value()-3000)/3)}\$ \  per\ BTC ').move_to(scene1_slippage_form.get_center())
        #
        # self.play(Create(scene1_slippage_form),
        #           Create(scene1_slippage_text))
        #
        # self.play(ReplacementTransform(scene1_slippage_form,scene1_slippage_result))
        #
        # # self.play()
        #
        #
        #
        # # self.play(Restore(whole_mobs))
        #
        # self.wait(2)

        #######################################################################################
        #################################scene2##############################################
        #######################################################################################

        #
        # user = create_entity(Tex(r' \emph{User}', color=BLACK).scale(0.5), 0.5, WHITE, "3BTC", ORANGE, 1.4, 0.3).next_to(liq_pool_rect,
        #                                                                                                                 RIGHT, buff=2)
        # user_asset_btc = user[ 1 ]
        # user_asset_pos = user_asset_btc.get_center()
        # user_asset_usdt = create_entity("A", 0.5, WHITE, "692USDT", BLUE, 1.4, 0.3)[ 1 ].move_to(user_asset_pos)
        #
        # user_line = Tex(r'I want to sell 3 BTC\\I dont have some USDT').scale(0.5).next_to(user, DOWN)
        #
        # self.play(Create(user))
        # self.play(Create(user_line))
        # self.play(Uncreate(user_line))
        #
        # # self.add(index_labels(btc_bar))###
        #
        # # scene2_btc_dashed_box = Rectangle(color=RED).align_to(btc_bar[0],UL,alignment_vect=btc_bar[0].get_edge_center(UP))
        # scene2_2308usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.2307, stroke_width=3,
        #                                 stroke_color=RED_E).align_to(
        #     usdt_bar, UL)
        # scene2_13btc_box = Rectangle(width=btc_bar.width, height=btc_bar.height * 0.3, stroke_width=3,
        #                              stroke_color=GREEN_E).next_to(btc_bar, UP, buff=0)
        #
        # scene2_2308usdt_fill_box = scene2_2308usdt_box.copy().set_fill(BLUE, opacity=1)
        # scene2_13btc_fill_box = scene2_13btc_box.copy().set_fill(ORANGE, opacity=1)
        #
        # scene2_2308usdt_fill_box.set_stroke(width=0, opacity=0)
        # scene2_13btc_fill_box.set_stroke(width=0, opacity=0)

        # scene2_2308usdt_fill_box.set_z_index(3)
        # scene2_13btc_fill_box.set_z_index(3)

        # self.play(Create(scene2_2308usdt_box))
        # self.play(Create(scene2_13btc_box))
        # scene2_2308usdt_brace = BraceBetweenPoints(scene2_2308usdt_box.get_corner(UR), scene2_2308usdt_box.get_corner(DR), color=RED_E,
        #                                            stroke_color=RED_E,
        #                                            stroke_width=3,
        #                                            ).flip(axis=np.array([ 0., 1., 0. ])).next_to(scene2_2308usdt_fill_box,
        #                                                                                          RIGHT)
        # scene2_13btc_brace = BraceBetweenPoints(scene2_13btc_box.get_corner(UL), scene2_13btc_box.get_corner(DL), color=GREEN_E,
        #                                         stroke_color=GREEN_E, stroke_width=3
        #                                         ).next_to(scene2_13btc_fill_box,
        #                                                   LEFT)
        #
        # scene2_2308usdt_brace_label = Integer(btc_tracker.get_value())
        # scene2_2308usdt_brace_label.add_updater(lambda label: label.become(
        #     Integer(692).scale(0.4).rotate(-PI / 2).next_to(scene2_2308usdt_brace, RIGHT, buff=0.3)))
        # scene2_13btc_brace_label = Integer(usdt_tracker.get_value())
        # scene2_13btc_brace_label.add_updater(lambda label: label.become(
        #     Integer(3).scale(0.4).rotate(PI / 2).next_to(scene2_13btc_brace, LEFT, buff=0.3)))
        #
        # scene2_braces = VGroup(scene2_2308usdt_brace, scene2_13btc_brace)
        # scene2_brace_labels = VGroup(scene2_2308usdt_brace_label, scene2_13btc_brace_label)
        #
        # self.play(Create(scene2_braces),
        #           Create(scene2_brace_labels))
        #
        # usdt_bar.clear_updaters()
        # btc_bar.clear_updaters()
        #
        # self.add(scene2_2308usdt_fill_box)
        # usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
        #     Rectangle(height= 2307/ 1000, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE).move_to(
        #         usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        # # btc_bar.add_updater(lambda btc_bar: btc_bar.become(
        # #     Rectangle(height=13 / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
        # #         btc_bar_pos).align_to(liq_pool_rect, DOWN)))
        #
        # origin_dot = curr_dot.copy()
        # origin_dot.clear_updaters()
        # origin_dot.set_color(RED)
        # origin_dot.set_z_index(1.5)
        #
        # self.play(Create(origin_dot))
        # self.play(btc_tracker.animate.set_value(13),
        #           # usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)),
        #           Transform(scene2_2308usdt_fill_box, user_asset_usdt),
        #           Transform(user_asset_btc, scene2_13btc_fill_box))
        #
        # scene2_arrow = CurvedArrow(origin_dot.get_center(), curr_dot.get_center(), radius=4, tip_length=0.25).shift(
        #     RIGHT * 0.3 + UP * 0.3)
        # scene2_arrow_label = Tex('Buy BTC in exchange of USDT').scale(0.3).next_to(scene2_arrow, UR)
        #
        # # bars.clear_updaters()
        # # vars.clear_updaters()
        # # k_var.clear_updaters()
        # # area.clear_updaters()
        # # curr_dot.clear_updaters()
        # # axis_labels.clear_updaters()
        # # markers.clear_updaters()
        # self.play(Create(scene2_arrow))
        #
        # # self.play(Restore(whole_mobs))
        #
        # scene2_slippage_text = Tex(r'I just sold 3 BTC \\and got 602 USDT').scale(0.5).next_to(user_asset_pos, DOWN)
        # scene2_slippage_form = MathTex(r'692 \divisionsymbol 3').next_to(scene2_slippage_text, DOWN)
        # scene2_slippage_result = MathTex(rf'{int(-(k_tracker.get_value() / btc_tracker.get_value()-3000)/3)}\$ \  per\ BTC ').move_to(scene2_slippage_form.get_center())
        #
        # self.play(Create(scene2_slippage_form),
        #           Create(scene2_slippage_text))
        #
        # self.play(ReplacementTransform(scene2_slippage_form,scene2_slippage_result))
        #
        #
        # self.wait(2)
        #
        # self.wait(2)
        #######################################################################################
        #################################scene3##############################################
        # 이건 k값 상승을 위한 것
        #######################################################################################
        # 아ㅣ거 유동성 5개 아니라 3개로 수정

        # usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
        #     Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE).move_to(
        #         usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        # btc_bar.add_updater(lambda btc_bar: btc_bar.become(
        #     Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
        #         btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        # 유저 사라짐

        # self.play(FadeOut(user),
        #           FadeOut(user_asset_btc),
        #           FadeOut(user_asset_usdt))
        #
        # 리퀴디티 프로바이더 다시 생성
        # liq_provider = create_entity(Tex(r' \emph{Liq\\provider}', color=BLACK).scale(0.8), 1, WHITE, "5 BTC", ORANGE, 1.4, 0.3).next_to(
        #     liq_pool_rect, RIGHT, buff=1.5)
        # btc_asset = liq_provider[ 1 ]
        # usdt_asset = create_entity("A", 0.5, WHITE, "500 USDT", BLUE, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)
        #
        # self.play(Create(VGroup(liq_provider, usdt_asset)))
        #
        # btc_bar.clear_updaters()
        # usdt_bar.clear_updaters()
        #
        # scene3_15btc_box = Rectangle(width=btc_bar.width, height=btc_bar.height * 0.5, stroke_width=3,
        #                              stroke_color=GREEN_E).next_to(btc_bar, UP, buff=0)
        # scene3_4500usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.5, stroke_width=3,
        #                                 stroke_color=GREEN_E).next_to(usdt_bar, UP, buff=0)
        #
        # self.play(Create(VGroup(scene3_15btc_box, scene3_4500usdt_box)))
        #
        # scene3_4500usdt_fill_box = scene3_4500usdt_box.copy().set_fill(BLUE, opacity=1)
        # scene3_15btc_fill_box = scene3_15btc_box.copy().set_fill(ORANGE, opacity=1)
        # scene3_15btc_fill_box.set_stroke(width=0, opacity=0)
        # scene3_4500usdt_fill_box.set_stroke(width=0, opacity=0)
        #
        # scene3_15btc_fill_box.set_z_index(3)
        # scene3_4500usdt_fill_box.set_z_index(3)
        #
        #
        # scene3_4500usdt_brace = BraceBetweenPoints(scene3_4500usdt_box.get_corner(UR), scene3_4500usdt_box.get_corner(DR), color=GREEN_E,
        #                                            stroke_color=GREEN_E,
        #                                            stroke_width=3,
        #                                            ).flip(axis=np.array([ 0., 1., 0. ])).next_to(scene3_4500usdt_fill_box,
        #                                                                                          RIGHT)
        # scene3_15btc_brace = BraceBetweenPoints(scene3_15btc_box.get_corner(UL), scene3_15btc_box.get_corner(DL), color=GREEN_E,
        #                                         stroke_color=GREEN_E, stroke_width=3
        #                                         ).next_to(scene3_15btc_fill_box,
        #                                                   LEFT)
        #
        # scene3_4500usdt_brace_label = Integer(btc_tracker.get_value())
        # scene3_4500usdt_brace_label.add_updater(lambda label: label.become(
        #     Integer(1500).scale(0.4).rotate(-PI / 2).next_to(scene3_4500usdt_brace, RIGHT, buff=0.3)))
        # scene3_15btc_brace_label = Integer(usdt_tracker.get_value())
        # scene3_15btc_brace_label.add_updater(lambda label: label.become(
        #     Integer(5).scale(0.4).rotate(PI / 2).next_to(scene3_15btc_brace, LEFT, buff=0.3)))
        #
        # scene3_braces = VGroup(scene3_4500usdt_brace, scene3_15btc_brace)
        # scene3_brace_labels = VGroup(scene3_4500usdt_brace_label, scene3_15btc_brace_label)
        #
        # new_liquidity_text = MathTex('5BTC', '=', '1500USDT').scale(0.5).next_to(liq_provider, DOWN, buff=2)
        #
        # scene3_origin_graph = xyk_graph_btc.copy()
        # scene3_origin_graph.clear_updaters()
        # scene3_origin_graph.set_color(RED)
        # scene3_origin_graph.set_z_index(-1)
        # self.add(scene3_origin_graph)
        #
        # # xyk_graph_btc = ax.plot(lambda x: k_tracker.get_value() / x,
        # #                         x_range=[ 0.00001, 6000 ],
        # #                         use_smoothing=False, color=PURPLE)
        # #
        # # xyk_graph_btc.add_updater(lambda graph: graph.become(
        # #     ax.plot(lambda x: k_tracker.get_value() / x,
        # #             x_range=[ k_tracker.get_value() / 6000, 20 ],
        # #             use_smoothing=False, color=PURPLE)))
        #
        # self.play(Create(scene3_braces),
        #           Create(scene3_brace_labels))
        #
        # # self.play(Create(origin_dot))
        # self.play(k_tracker.animate.set_value(67500),
        #           btc_tracker.animate.set_value(15),
        #           usdt_tracker.animate.set_value(67500/15),
        #           Transform(usdt_asset, scene3_4500usdt_fill_box),
        #           Transform(btc_asset, scene3_15btc_fill_box),
        #           run_time=6)
        #
        # self.wait(4)

        #######################################################################################
        #################################scene4##############################################
        #######################################################################################
        # 아ㅣ거 유동성 5개 아니라 3개로 수정

        # liq_provider = create_entity(Tex(r' \emph{Liq\\provider}', color=BLACK).scale(0.8), 1, WHITE, "5 BTC", ORANGE, 1.4, 0.3).next_to(
        #     liq_pool_rect, RIGHT, buff=1.5)
        # btc_asset = liq_provider[ 1 ]
        # usdt_asset = create_entity("A", 0.5, WHITE, "1500 USDT", BLUE, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)
        #
        # self.play(Create(liq_provider[ 0 ]))
        #
        # btc_bar.clear_updaters()
        # usdt_bar.clear_updaters()
        #
        # # # scene2_btc_dashed_box = Rectangle(color=RED).align_to(btc_bar[0],UL,alignment_vect=btc_bar[0].get_edge_center(UP))
        # # scene2_2308usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.2307, stroke_width=3,
        # #                                 stroke_color=RED_E).align_to(usdt_bar, UL)
        #
        # scene4_5btc_box = Rectangle(width=btc_bar.width, height=btc_bar.height * 0.5, stroke_width=3,
        #                             stroke_color=RED_E).align_to(btc_bar, UL)
        # scene4_1500usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.5, stroke_width=3,
        #                                 stroke_color=RED_E).align_to(usdt_bar, UL)
        #
        # scene4_1500usdt_fill_box = scene4_1500usdt_box.copy().set_fill(BLUE, opacity=1)
        # scene4_5btc_fill_box = scene4_5btc_box.copy().set_fill(ORANGE, opacity=1)
        #
        # scene4_5btc_fill_box.set_stroke(width=0, opacity=0)
        # scene4_1500usdt_fill_box.set_stroke(width=0, opacity=0)
        # scene4_5btc_fill_box.set_z_index(3)
        # scene4_1500usdt_fill_box.set_z_index(3)
        #
        # self.play(Create(VGroup(scene4_5btc_box, scene4_1500usdt_box)))
        # self.add(scene4_5btc_fill_box,scene4_1500usdt_fill_box)
        #
        # scene4_1500usdt_brace = BraceBetweenPoints(scene4_1500usdt_box.get_corner(UR), scene4_1500usdt_box.get_corner(DR), color=RED_E,
        #                                            stroke_color=RED_E,
        #                                            stroke_width=3,
        #                                            ).flip(axis=np.array([ 0., 1., 0. ])).next_to(scene4_1500usdt_fill_box,
        #                                                                                          RIGHT)
        # scene4_5btc_brace = BraceBetweenPoints(scene4_5btc_box.get_corner(UL), scene4_5btc_box.get_corner(DL), color=RED_E,
        #                                        stroke_color=RED_E, stroke_width=3
        #                                        ).next_to(scene4_5btc_fill_box,
        #                                                  LEFT)
        # usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
        #     Rectangle(height=1500 / 1000, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE).move_to(
        #         usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        # btc_bar.add_updater(lambda btc_bar: btc_bar.become(
        #     Rectangle(height=5 / 10, width=1.2, fill_color=ORANGE, fill_opacity=1, color=ORANGE).move_to(
        #         btc_bar_pos).align_to(liq_pool_rect, DOWN)))
        #
        # scene4_1500usdt_brace_label = Integer(btc_tracker.get_value())
        # scene4_1500usdt_brace_label.add_updater(lambda label: label.become(
        #     Integer(1500).scale(0.4).rotate(-PI / 2).next_to(scene4_1500usdt_brace, RIGHT, buff=0.3)))
        # scene4_5btc_brace_label = Integer(usdt_tracker.get_value())
        # scene4_5btc_brace_label.add_updater(lambda label: label.become(
        #     Integer(5).scale(0.4).rotate(PI / 2).next_to(scene4_5btc_brace, LEFT, buff=0.3)))
        #
        # scene4_braces = VGroup(scene4_1500usdt_brace, scene4_5btc_brace)
        # scene4_brace_labels = VGroup(scene4_1500usdt_brace_label, scene4_5btc_brace_label)
        #
        # new_liquidity_text = MathTex('5BTC', '=', '1500USDT').scale(0.5).next_to(liq_provider, DOWN, buff=2)
        #
        # self.play(Create(new_liquidity_text))
        #
        # scene4_origin_graph = xyk_graph_btc.copy()
        # scene4_origin_graph.clear_updaters()
        # scene4_origin_graph.set_color(RED)
        # scene4_origin_graph.set_z_index(-1)
        # self.add(scene4_origin_graph)
        #
        # self.play(Create(scene4_braces),
        #           Create(scene4_brace_labels))
        #
        # # self.play(Create(origin_dot))
        # self.play(k_tracker.animate.set_value(7500),
        #           btc_tracker.animate.set_value(5),
        #           usdt_tracker.animate.set_value(7500 / 5),
        #           Transform(scene4_1500usdt_fill_box, usdt_asset),
        #           Transform(scene4_5btc_fill_box, btc_asset),
        #           run_time=6,rate_func=rate_functions.ease_in_out_quint)
        #
        # self.wait(4)

        #######################################################################################
        #################################scene5##############################################
        #######################################################################################
        k_org_px_org_dot = curr_dot.copy().clear_updaters().set_color(GREY).set_z_index(1.5).scale(1.2)
        self.play(Create(k_org_px_org_dot))

        # 가격 상승#####################################################################################

        self.play(
            btc_tracker.animate.set_value(7),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
            run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # px_up = Tex('Price goes up')
        # self.play(Write(px_up))
        # self.play(Unwrite(px_up))

        # 가격이 올라간다는 건 btc가 usdt보다 상대적으로 인기가 많아진다는 것입니다.

        self.wait(2)

        k_org_px_up_dot = curr_dot.copy().clear_updaters().set_color(GREEN_C).set_z_index(1.5)
        self.add(k_org_px_up_dot)

        # 가격 하락#####################################################################################

        self.play(
            btc_tracker.animate.set_value(13),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)),
            run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # px_dn = Tex('Price goes Down')
        # self.play(Write(px_dn))
        # self.play(Unwrite(px_dn))

        # 가격이 내려간다는 건 btc가 usdt보다 상대적으로 인기가 없어진다는 것

        self.wait(2)

        k_org_px_dn_dot = curr_dot.copy().clear_updaters().set_color(RED_C).set_z_index(1.5)
        self.add(k_org_px_dn_dot)

        # 가격 원점#####################################################################################
        self.play(
            btc_tracker.animate.set_value(7),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
            run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # px_origin = Tex('Price origin').scale(0.7).next_to()
        # self.play(Write(px_origin))
        # self.play(Unwrite(px_origin))

        self.wait(2)

        # K 하락#####################################################################################
        self.play(k_tracker.animate.set_value(14700),
                  btc_tracker.animate.set_value(7),
                  usdt_tracker.animate.set_value(14700 / 7),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # k_dn = Tex('K goes down')
        # self.play(Write(k_dn))
        # self.play(Unwrite(k_dn))
        # 케이가 하락한다는 건 풀에서 누군가 유동성을 빼간 것입니다.
        # 명심할 것은 케이의 변동은 가격과 관계가 없음
        # 내가 유동성 풀에 제거하고 싶으면
        # 그냥 지금 가격에 맞게 빼가면 됨
        # 스왑처럼 내가 가격을 움직이며 하는 행위가 아님
        # 왜냐하면 가격이란 풀 내부의 비율인데
        # 지금 비율(1개에 300달러) 그대로 빼기 때문에
        # 가격은 움직이지 않고 그로인해 슬리피지등이 발생하지 않는다
        # 착각 금지

        self.wait(2)

        k_dn_px_org_dot = curr_dot.copy().clear_updaters().set_color(WHITE).set_z_index(1.5)
        self.add(k_dn_px_org_dot)

        # K 상승#####################################################################################
        self.play(k_tracker.animate.set_value(50700),
                  btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(50700 / 13),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # k_up = Tex('K goes up')
        # self.play(Write(k_up))
        # self.play(Unwrite(k_up))
        # 케이가 상승한다는 건 풀에 누군가 추가 유동성을 공급하는 것입니다.
        # 마찬가지로 가격은 전혀 움직이지 않음
        # 현재 가격에 맞게 비티씨와 유에스디티를 그대로 추가함
        # 풀사이즈는 커짐

        self.wait(2)

        k_up_px_org_dot = curr_dot.copy().clear_updaters().set_color(DARK_GREY).set_z_index(1.5)
        self.add(k_up_px_org_dot)

        # K 원점#####################################################################################
        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # k_origin = Tex('K origin')
        # self.play(Write(k_origin))
        # self.play(Unwrite(k_origin))

        self.wait(2)

        # K 상승#####################################################################################
        self.play(k_tracker.animate.set_value(50700),
                  btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(50700 / 13),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        k_up = Tex('K goes up')
        self.play(Write(k_up))
        self.play(Unwrite(k_up))

        self.wait(2)

        # K 상승 가격 하락#####################################################################################
        self.play(
            btc_tracker.animate.set_value(16),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(16)),
            run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # k_up_px_dn = Tex('K up, Price goes down')
        # self.play(Write(k_up_px_dn))
        # self.play(Unwrite(k_up_px_dn))

        # 케이가 상승한 상황에서 가격이 하락
        # 가격이 하락한다는 건 누군가 풀에서 비티씨를 넣고 테더를 빼가는 것
        # 즉 풀에다 비티씨를 매도하는 것
        # 여기서 명심할 건
        # 케이가 상승했다는 건 풀 사이즈가 커진거곡
        # 그만큼 리퀴디티가 충분하다는 것입니다
        # 그러니까 같은 금액의 비티씨를 매도하더라도
        # 이전보다 더 슬리피지가 적습니다
        # 아까 봤을 때 300달러에서 3개 매도할 때는 슬리피지가 얼마 발생
        # 근데 지금은 유동성이 더 충분한 상태고 300달러에서 3개 매도했는데
        # 슬리피지 얼마 발생
        # 유동성이 크면 좋은 것이다
        # 같은 개수를 메도해도 내가 넣는 비티씨의 양이 풀내부에 차지하는 비율이
        # 더 적어졌기 때문입니다
        # 아까는 10개에서 3개 매도
        # 지금은 15개에서 3개 매도
        # 비율로 따지면 30퍼와 20퍼기 땨문에 풀에주는 영향력이 크다

        self.wait(2)

        k_up_px_dn_dot = curr_dot.copy().clear_updaters().set_color(RED_E).set_z_index(1.5)
        self.add(k_up_px_dn_dot)

        # K 상승 가격 상승#####################################################################################
        self.play(
            btc_tracker.animate.set_value(10),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(10)),
            run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # k_up_px_up = Tex('K up, Price goes up')
        # self.play(Write(k_up_px_up))
        # self.play(Unwrite(k_up_px_up))

        # 케이가 상승한 상황에서 가격이 올라가는 경우도 마찬가지
        # 가격이 오른다는 건 누군가 풀에서 비티씨를 빼고 테더를 넣는 것
        # 즉 풀에서 비티씨를 매수하는 것
        # 명심할 건
        # 케이가 상승한 건 풀사이즈가 커졌고
        # 마찬가지로 아까 비티씨를 살 때 슬리피지를 겪었던 것보다
        # 슬리피지를 적게 겪음
        # 아까 300달러에서 3개매수는 슬리피지 얼마
        # 근데 지금은 얼마
        # 같은 개수를 매수해도 내가 빼는 비티씨의 양이 풀내부에 차지하는 비율이
        # 더 적어졌기 때문입니다
        # 아까는 10개에서 3개 매수
        # 지금은 15개에서 3개 매ㅑ수
        # 비율로 따지면 30퍼와 20퍼기 땨문에 풀에주는 영향력이 크다

        self.wait(2)

        k_up_px_up_dot = curr_dot.copy().clear_updaters().set_color(GREEN_E).set_z_index(1.5)
        self.add(k_up_px_up_dot)

        # K 원점#####################################################################################
        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # k_origin_px_origin = Tex('K origin, px origin')
        # self.play(Write(k_origin_px_origin))
        # self.play(Unwrite(k_origin_px_origin))

        self.wait(2)

        # K 하락#####################################################################################
        self.play(k_tracker.animate.set_value(14700),
                  btc_tracker.animate.set_value(7),
                  usdt_tracker.animate.set_value(14700 / 7),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # k_dn = Tex('K goes down')
        # self.play(Write(k_dn))
        # self.play(Unwrite(k_dn))

        # 역으로 케이가 하락했는데
        # 그말은 유동성이 줄었다는 거하고
        # 아까 유동성이 늘었서 슬리피지가 덜 발행하던 것과 달리
        # 지금부터는 슬리피지가 더 발생합니다
        #

        self.wait(2)

        # K 하락 가격 하락#####################################################################################
        self.play(
            btc_tracker.animate.set_value(10),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(10)),
            run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # k_dn_px_dn = Tex('K down, Price goes dn')
        # self.play(Write(k_dn_px_dn))
        # self.play(Unwrite(k_dn_px_dn))

        # 케이가 하락한 상태에서 누군가 풀에다 비티씨를 매도해서
        # 가격도 하락합니다
        # 비티씨를 매도하는데 아까와 같이 300달러에서 매도하지만
        # 아까는 슬리피지 얼마
        # 지금은 얼마입니다
        # 당연히 아까는 10개에서 3개를 넣는 거였고
        # 지금은 5개에서 3개를 넣는거니까
        # 비율은 30퍼와 60퍼로
        # 완전 차이나게 된다

        k_dn_px_dn_dot = curr_dot.copy().clear_updaters().set_color(RED_A).set_z_index(1.5)
        self.add(k_dn_px_dn_dot)

        self.wait(2)

        # K 하락 가격 상승#####################################################################################
        self.play(
            btc_tracker.animate.set_value(4),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(4)),
            # area_text.animate.rotate(PI / 2),
            run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # k_dn_px_dn = Tex('K down, Price goes up')
        # self.play(Write(k_dn_px_dn))
        # self.play(Unwrite(k_dn_px_dn))

        # 케이가 하락한 상태에서 누군가 풀에서 비티씨를 빼가면서 즉 매수하면서
        # 가격도 상승합니다
        # 비티씨를 매수하는데 아까와 같이 300달러ㅓ에서 매수하지만
        # 아까는 슬리피지 얼마
        # 지금은 얼마
        # 당연히 아까는 10개에서 3개를 빼는 거였고
        # 지금은 5개에서 3개를 빼는 것
        # 비율은 30퍼와 60퍼로 상당히 차이난다

        self.wait(2)

        k_dn_px_up_dot = curr_dot.copy().clear_updaters().set_color(GREEN_A).set_z_index(1.5)
        self.add(k_dn_px_up_dot)

        # 원점#####################################################################################
        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # k_origin_px_origin = Tex('K origin, px origin')
        # self.play(Write(k_origin_px_origin))
        # self.play(Unwrite(k_origin_px_origin))

        self.wait(2)

        # 가격 상승#####################################################################################
        self.play(
            btc_tracker.animate.set_value(7),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
            run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # px_up = Tex('Price goes up')
        # self.play(Write(px_up))
        # self.play(Unwrite(px_up))

        # 이제는 가격이 상승한 상태에서 k를 움직여보겟습니다

        # 가격 상승에서 K상승#####################################################################################
        self.play(k_tracker.animate.set_value(3000000 / 49),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000000 / 49 / 10),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        px_up_k_up = Tex('Price goes up, K up')
        self.play(Write(px_up_k_up))
        self.play(Unwrite(px_up_k_up))

        # 아까와는 상황이 다릅니다
        # 현재 가격은 이미 움직여버렸습니다
        # 현재가격은 이미 300에서 올라왔고 여기서
        # 유동성을 넣기 때문에
        # 같은 2비티씨를 유동성을 추가한다고 하면
        # 1비티씨마다 상응하는 올라간 가격의 테더를 같이 넣어줘야합니다
        #

        self.wait(2)

        px_up_k_up_dot = curr_dot.copy().clear_updaters().set_color(TEAL_E).set_z_index(1.5)
        self.add(px_up_k_up_dot)

        # 가격 상승에서 K하락#####################################################################################
        self.play(k_tracker.animate.set_value(480000 / 49),
                  btc_tracker.animate.set_value(4),
                  usdt_tracker.animate.set_value(480000 / 49 / 4),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # px_up_k_dn = Tex('Price goes up, K dn')
        # self.play(Write(px_up_k_dn))
        # self.play(Unwrite(px_up_k_dn))

        # 가격이 올랐을 때 케이가 떨어진다는 건
        # 즉 유동성을 공급했던 사람이 유동성을 회수한다는 것은
        # 풀 사이즈가 작아진다는 것입니다
        # 그 말은 공급자가 1비티씨를 뺄 때 오른 가격만큼의 테더를 회수한다는 애기입니다
        # 2비티씨를 빼면 얼마가 빠집니다

        self.wait(2)

        px_up_k_dn_dot = curr_dot.copy().clear_updaters().set_color(TEAL_A).set_z_index(1.5)
        self.add(px_up_k_dn_dot)

        # 원점점#####################################################################################
        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # k_origin_px_origin = Tex('K origin, px origin')
        # self.play(Write(k_origin_px_origin))
        # self.play(Unwrite(k_origin_px_origin))

        # 가격 하락#####################################################################################
        self.play(
            btc_tracker.animate.set_value(13),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)),
            run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # px_dn = Tex('Price goes down')
        # self.play(Write(px_dn))
        # self.play(Unwrite(px_dn))

        # 가격이 하락한 상태에서 케이를 움직여보겟습니다

        self.wait(2)

        # 가격 하락에서 K상승#####################################################################################
        self.play(k_tracker.animate.set_value(7680000 / 169),
                  btc_tracker.animate.set_value(16),
                  usdt_tracker.animate.set_value(7680000 / 169 / 16),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # px_dn_k_up = Tex('Price goes down, K up')
        # self.play(Write(px_dn_k_up))
        # self.play(Unwrite(px_dn_k_up))

        # 가격이 하락한 상태에서 케이를 넣으렴녀 원래보다 돈이 적게 듭니다
        # 왜냐하면 비티씨 1개를 넣을 때 하락한 각겨만큼의 테더를 넣으면 됩니다

        self.wait(2)

        px_dn_k_up_dot = curr_dot.copy().clear_updaters().set_color(MAROON_E).set_z_index(1.5)
        self.add(px_dn_k_up_dot)

        # 가격 하락에서 K하락#####################################################################################
        self.play(k_tracker.animate.set_value(3000000 / 169),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000000 / 169 / 11),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # px_dn_k_dn = Tex('Price goes down, K dn')
        # self.play(Write(px_dn_k_dn))
        # self.play(Unwrite(px_dn_k_dn))

        # 마찬가지로 하락한 상태에서 유동성을 제거하면
        # 비티씨 한 개를 뺄 때 떨어진 가격만큼의 테더만 되찾을 수 있습니다

        px_dn_k_dn_dot = curr_dot.copy().clear_updaters().set_color(MAROON_A).set_z_index(1.5)
        self.add(px_dn_k_dn_dot)

        self.wait(2)

        # 가격 원점#####################################################################################
        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # px_origin = Tex('Price origin')
        # self.play(Write(px_origin))
        # self.play(Unwrite(px_origin))

        self.wait(2)

        # 라인 생성#####################################################################################

        def making_a_line_3points(p1, p2, p3, color):
            l1 = Line(p1.get_center(), p2.get_center(), color=color)
            l2 = Line(p2.get_center(), p3.get_center(), color=color)
            l1.set_z_index(-2)
            l2.set_z_index(-2)
            line = VGroup(l1, l2)

            return line

        self.play(FadeOut(area),
                  FadeOut(area_text))
        k_px_org_line = making_a_line_3points(k_dn_px_org_dot, k_org_px_org_dot, k_up_px_org_dot, DARK_GREY)
        self.play(Create(k_px_org_line))
        k_px_up_line = making_a_line_3points(k_dn_px_up_dot, k_org_px_up_dot, k_up_px_up_dot, GREEN_E)
        self.play(Create(k_px_up_line))
        k_px_dn_line = making_a_line_3points(k_dn_px_dn_dot, k_org_px_dn_dot, k_up_px_dn_dot, RED_E)
        self.play(Create(k_px_dn_line))
        px_up_k_line = making_a_line_3points(px_up_k_dn_dot, k_org_px_up_dot, px_up_k_up_dot, TEAL_E)
        self.play(Create(px_up_k_line))
        px_dn_k_line = making_a_line_3points(px_dn_k_dn_dot, k_org_px_dn_dot, px_dn_k_up_dot, MAROON_E)
        self.play(Create(px_dn_k_line))

        self.wait(2)
