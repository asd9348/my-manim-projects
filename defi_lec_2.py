from manim import *
import random as rd
import numpy as np
from math import *
from colour import Color
from custom_manim_utils.custom_consts import *

config.frame_width = 16
config.frame_height = 9

BTC = C_BTC
ETH = C_ETH
DOT = C_DOT
SOL2 = C_SOL2
USDT = C_USDT
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
        L_02_S_01_dex_pros_and_cons.construct(self)
        L_02_S_02_smart_contract.construct(self)
        L_02_S_03_cons_of_smart_c.construct(self)
        L_02_S_04_amm_xyk_basics.construct(self)
        L_02_S_05_amm_xyk_basics_with_math.construct(self)
        L_02_S_06_amm_xyk_adv_k_dn_1.construct(self)
        L_02_S_07_amm_xyk_adv_k_up_2.construct(self)
        L_02_S_08_amm_xyk_adv_px_up_3.construct(self)
        L_02_S_09_px_impact_and_slippage.construct(self)
        L_02_S_10_amm_xyk_adv_px_dn_4.construct(self)
        L_02_S_11_fees.construct(self)
        L_02_S_12_amm_xyk_various_cases_5.construct(self)
        L_02_S_13_why_the_word_swap.construct(self)
        L_02_S_14_arbitrage.construct(self)


class L_02_S_01_dex_pros_and_cons(Scene):
    def construct(self):
        script = speak(self, title='테스트입니다', txt=
        '그렇다면 이 덱스라는 게 도대체 중앙화 거래소와 어떤 점이 다르기에 존재하는걸까요#1'
        '덱스는 중앙화 서버가 없고 탈중앙화된 네트워크에 의존하기 때문에 전쟁과 같은 물리적인 위험에서도 중앙서버가 망가지면 네트워크가 마비되는 중앙화 거래소와 달리 훨씬 안전합니다#1'
        '그러나 블록체인 네트워크도 트래픽이 많으면 느려지고, 심지어 최근 솔라나나 클레이튼 같은 대형체인도 정지하는 일이 심심치 않게 발생합니다#1'
        '그래서 무작정 중앙서버보다 좋다고만은 할 수도 없습니다#1'
        '또 덱스는 정부의 검열으로부터 자유로울 수 있고 프라이버시를 보호할 수 있습니다#1'
        '모든 기록이 블록체인에 남지만 그 주소가 누군지 매칭이 안 되기 때문에 익명성이 보장됩니다#1'
        '그리고 거래소의 심사 없이 코인을 자유롭게 상장할 수 있습니다#1'
        '크립토 프로젝트들은 거래소에서 심사를 거쳐 상장이 되야하는데 이 기준이 엄격하다보니, 거래소에는 한정된 코인들만 있습니다.#1'
        '그러나 덱스에서는 누구나 유동성 풀을 만들어 다른 사람들의 거래를 도울 수 있습니다#1'
              ,keep_pitch=True, update=True, speed=1.4)

        # TODO 5.014 secs그렇다면 이 덱스라는 게 도대체 중앙화 거래소와 어떤 점이 다르기에 존재하는걸까요
        # TODO 1.0 secs1

        why = Tex('Why dex?').scale(2)
        self.play(Create(why))
        self.wait(0.8)
        # self.play(Uncreate(why))

        dex_text = MathTex('DEX').scale(2).shift(L * 4)
        vs_text = MathTex('VS').scale(2)
        cex_text = MathTex('CEX').scale(2).shift(R * 4)
        q_mark = Tex('?').scale(8)
        self.play(ReplacementTransform(why,VGroup(dex_text,cex_text,vs_text)))
        self.wait(0.8)


        self.play(ReplacementTransform(VGroup(dex_text, cex_text,vs_text), q_mark))
        self.wait(0.3)

        self.play(Uncreate(q_mark))

        self.wait(0.2)

        # TODO 11.102 secs덱스는 중앙화 서버가 없고 탈중앙화된 네트워크에 의존하기 때문에 전쟁과 같은 물리적인 위험에서도 중앙서버가 망가지면 네트워크가 마비되는 중앙화 거래소와 달리 훨씬 안전합니다
        # TODO 1.0 secs1

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

        self.play(Create(center_line),run_time=0.3)
        self.play(Create(centralized_net),
                  Create(centralized_net_text), run_time=2)
        self.wait(0.3)

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
                  Create(decentralized_net_text), run_time=2)
        self.wait(0.5)

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

        self.play(Create(cent_attack_arrows.move_to(centralized_net[ 30 ])),run_time=0.5)
        self.play(Create(cent_server_cross),run_time=0.5)
        self.wait(0.25)

        self.play(Uncreate(centralized_net[ 31: ]), run_time=0.5)
        self.wait(0.25)
        decent_attack_arrows_1 = cent_attack_arrows.copy().scale(0.6).move_to(decentralized_nets[ 3 ][ 10 ])
        decent_attack_arrows_1.set_z_index(1)
        decent_attack_arrows_2 = cent_attack_arrows.copy().scale(0.6).move_to(decentralized_nets[ 0 ][ 10 ])
        decent_attack_arrows_2.set_z_index(1)

        decent_server_cross_1 = Cross(stroke_width=15).scale(0.2).move_to(decentralized_nets[ 3 ][ 10 ])
        decent_server_cross_1.set_z_index(1)
        decent_server_cross_2 = Cross(stroke_width=15).scale(0.2).move_to(decentralized_nets[ 0 ][ 10 ])
        decent_server_cross_2.set_z_index(1)

        self.play(Create(decent_attack_arrows_1),
                  Create(decent_attack_arrows_2),run_time=0.5)
        self.play(Create(decent_server_cross_1),
                  (Create(decent_server_cross_2)),run_time=0.5)
        self.wait(0.25)

        self.play(Uncreate(decentralized_nets[ 3 ][ 11: ]),
                  Uncreate(decentralized_nets[ 0 ][ 11: ]), run_time=0.25)
        self.play(Uncreate(decentralized_nets[ -1 ][ 3 ]),
                  Uncreate(decentralized_nets[ -1 ][ 0 ]), run_time=0.25)
        self.wait(1)

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
                                  decentralized_net_text)), run_time=1.5)
        self.wait(0.5)

        # TODO 9.157 secs그러나 블록체인 네트워크도 트래픽이 많으면 느려지고, 심지어 최근 솔라나나 클레이튼 같은 대형체인도 정지하는 일이 심심치 않게 발생합니다
        # TODO 1.0 secs1
        # TODO 3.721 secs그래서 무작정 중앙서버보다 좋다고만은 할 수도 없습니다
        # TODO 1.0 secs1

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
        self.wait(1)
        self.play(Create(blockchain[ -4: ]), run_time=4.5)
        self.play(Create(stop_sign))

        self.wait(4)
        self.play(Uncreate(blockchain),
                  Uncreate(stop_sign),run_time=2.5)
        self.wait(0.5)


        # 4.881 secs또 덱스는 정부의 검열으로부터 자유로울 수 있고 프라이버시를 보호할 수 있습니다
        # 1.0 secs1

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

        self.play(Create(dex_text,run_time=0.5))
        self.play(Create(eyes),run_time=0.5)
        self.play(eye_UL[ 2 ].animate.shift(DR * 0.2),
                  eye_DL[ 2 ].animate.shift(UR * 0.18),
                  eye_UR[ 2 ].animate.shift(DL * 0.2),
                  eye_DR[ 2 ].animate.shift(UL * 0.18),
                  )

        self.play(Create(shield),run_time=0.5)

        self.play(Flash(shield, line_length=1, num_lines=50, color=BLUE, flash_radius=2.5 + SMALL_BUFF, time_width=0.3, run_time=1,
                        rate_func=rush_from))
        self.play(Flash(shield, line_length=1, num_lines=50, color=BLUE, flash_radius=2.5 + SMALL_BUFF, time_width=0.3, run_time=1,
                        rate_func=rush_from))
        self.wait(0.5)

        self.play(Uncreate(dex_text),
                  Uncreate(eyes),
                  Uncreate(shield)
                  )
        self.wait(0.5)

        # TODO 5.956 secs모든 기록이 블록체인에 남지만 그 주소가 누군지 매칭이 안 되기 때문에 익명성이 보장됩니다
        # TODO 1.0 secs1

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
        mag_circle_text = Tex('01', color=WHITE).move_to(mag_circle)
        mag_rect = Rectangle(width=12, height=6).align_to(np.array([ -4.5, 3, 0 ]), UL)
        mag_line_1 = Line(mag_circle.get_top(), mag_rect.get_corner(UL))
        mag_line_2 = Line(mag_circle.get_bottom(), mag_rect.get_corner(DL))
        mag_line = VGroup(mag_line_1, mag_line_2)
        mag = VGroup(mag_circle, mag_line)

        who_text = Tex('Who?').scale(2).shift(R * 5)

        self.play(Create(block_1), run_time=0.3)
        self.play(AnimationGroup(Create(mag_circle),
                                 Create(mag_circle_text),
                                 Create(mag_line),
                                 Create(mag_rect),
                                 Create(tx_content),
                                 Create(who_text), lag_ratio=0.5), run_time=2)

        self.play(Indicate(who_text),run_time=2)
        self.wait(0.5)


        mag_circle_text.set_z_index(2)
        self.play(AnimationGroup(Uncreate(tx_content),
                                 Uncreate(who_text),
                                 Uncreate(mag_rect),
                                 Uncreate(mag_line),
                                 Uncreate(mag_circle_text),
                                 Uncreate(mag_circle),
                                 lag_ratio=0.5), run_time=1)
        self.play(Uncreate(block_1), run_time=0.3)
        self.wait(0.5)

        # TODO 3.926 secs그리고 거래소의 심사 없이 코인을 자유롭게 상장할 수 있습니다
        # TODO 1.0 secs1
        # TODO 8.263 secs크립토 프로젝트들은 거래소에서 심사를 거쳐 상장이 되야하는데 이 기준이 엄격하다보니, 거래소에는 한정된 코인들만 있습니다.
        # TODO 1.0 secs1

        cex_text = Tex('CEX').scale(2).shift(R * 4 + U * 2)
        eval_audit_text = Tex(r'Evaluation \& Audit').to_edge(U)
        center_line = Line(UP * 7.5, ORIGIN, stroke_width=30).next_to(eval_audit_text, D)

        shit_coin = LabeledDot(Tex('SHIT', color=BLACK), radius=1, color=GREEN).shift(U * 2).to_edge(L)
        poop_coin = LabeledDot(Tex('POOP', color=BLACK), radius=1, color=YELLOW).shift(D * 3).to_edge(L)
        btc_coin = LabeledDot(Tex('BTC', color=BLACK), radius=1, color=C_BTC).to_edge(L).shift(0.5 * D)

        limited_pairs = Tex('Limited pairs available...', 'BTC-USDT', 'ETH-BTC', r'\vdots').arrange(D).next_to(cex_text, D, buff=1)

        btc_arc = Arc(angle=PI).flip(axis=np.array([ 0, 1, 0 ])).shift(0.5 * D)

        self.play(Create(cex_text),
                  Create(eval_audit_text),
                  Create(center_line), run_time=1)
        self.wait(1)

        self.play(Create(limited_pairs), run_time=1)
        self.wait(1)

        self.play(Create(VGroup(shit_coin, poop_coin, btc_coin)), run_time=1.5)

        self.play(shit_coin.animate.align_to(center_line, R),
                  poop_coin.animate.align_to(center_line, R),
                  btc_coin.animate.align_to(center_line, R), run_time=1)
        self.play(MoveAlongPath(btc_coin, btc_arc), run_time=1)
        self.play(FadeOut(btc_coin, target_position=cex_text), run_time=2)
        self.wait(1)

        self.play(FadeOut(shit_coin),
                  FadeOut(poop_coin), run_time=1)
        self.wait(2)


        # TODO 5.267 secs그러나 덱스에서는 누구나 유동성 풀을 만들어 다른 사람들의 거래를 도울 수 있습니다
        # TODO 1.0 secs1
        dex_text = Tex('DEX').scale(2).shift(R * 4 + U * 2)
        shit_coin = LabeledDot(Tex('SHIT', color=BLACK).scale(0.5), radius=0.5, color=GREEN).shift(U * 1).to_edge(L)
        poop_coin = LabeledDot(Tex('POOP', color=BLACK).scale(0.5), radius=0.5, color=YELLOW).shift(D * 1).to_edge(L)

        any_pairs = Tex('Anyone can make pairs', 'POOP-USDT', 'SHIT-BTC', 'SHIT-POOP', r'\vdots').arrange(D).next_to(dex_text, D, buff=1)

        random_coin_1 = LabeledDot(Tex('BLAH', color=BLACK).scale(0.5), radius=0.5, color=RED).shift(U * 3).to_edge(L)
        random_coin_2 = LabeledDot(Tex('BLUH', color=BLACK).scale(0.5), radius=0.5, color=BLUE).shift(D * 3).to_edge(L)

        coins = VGroup(shit_coin, poop_coin, random_coin_1, random_coin_2)

        self.play(ReplacementTransform(cex_text, dex_text),
                  Uncreate(eval_audit_text),
                  Uncreate(center_line),
                  ReplacementTransform(limited_pairs, any_pairs)
                  , run_time=2)
        self.wait(0.5)

        self.play(*[ Create(coin, target_position=dex_text) for coin in coins ], run_time=1.5)
        self.play(*[ FadeOut(coin, target_position=dex_text) for coin in coins ], run_time=2)
        self.wait(0.5)

        self.play(Uncreate(dex_text),
                  Uncreate(any_pairs), run_time=1.5)
        self.wait(2)



class L_02_S_02_smart_contract(Scene):
    def construct(self):
        smart_c_text = Tex('Smart Contract').scale(2)

        self.play(Create(smart_c_text))
        self.wait(t)
        self.play(Uncreate(smart_c_text))
        self.wait(t)

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
                  , run_time=tt)
        self.wait(t)

        self.play(Create(rev_door), run_time=tt)
        self.wait(t)

        self.play(Rotate(rev_door, angle=10 * PI), rate_func=rate_functions.exponential_decay, run_time=t)
        self.wait(t)

        A = create_entity("A", 0.7, WHITE, "BTC", BTC, 0.8, 0.3).scale(1.2).to_edge(L)
        B = create_entity("B", 0.7, WHITE, "ETH", ETH, 0.8, 0.3).scale(1.2).to_edge(R)

        A_asset = A[ 1 ]
        B_asset = B[ 1 ]
        A_asset_pos = A[ 1 ].get_center()
        B_asset_pos = B[ 1 ].get_center()

        A_asset_arc = Arc(radius=1.5, angle=-PI).flip(axis=UP)
        B_asset_arc = Arc(radius=1.5, angle=PI)

        self.play(Create(A),
                  Create(B), run_time=t)
        self.wait(t)

        condition = Tex(r'A gives BTC to B\\B gives ETH to A').to_edge(UL)
        self.play(Create(condition), run_time=t)
        self.wait(t)

        self.play(A_asset.animate.move_to(LEFT * 1.5),
                  B_asset.animate.move_to(RIGHT * 1.5), run_time=t)
        self.wait(t)

        self.play(Rotate(rev_door),
                  MoveAlongPath(A_asset, A_asset_arc),
                  MoveAlongPath(B_asset, B_asset_arc), run_time=t)

        self.play(A_asset.animate.move_to(B_asset_pos),
                  B_asset.animate.move_to(A_asset_pos), run_time=t)

        self.play(Uncreate(condition))
        self.wait(t)

        rev_door_text_1 = Tex(r'Company\\or Third Party Entity').scale(0.7).next_to(dot, R)
        rev_door_text_2 = Tex(r'Programming Language\\without Emotion').scale(0.7).next_to(dot, R)

        self.play(Create(rev_door_text_1), run_time=tt)
        self.wait(t)

        self.play(Uncreate(rev_door_text_1), run_time=tt)
        self.wait(t)

        self.play(Create(rev_door_text_2), run_time=tt)
        self.wait(t)
        self.play(Uncreate(rev_door_text_2), run_time=tt)
        self.wait(t)

        self.play(FadeOut(VGroup(walls, A, B, rev_door, rev_door_text_2)), run_time=tt)
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

        self.play(Create(blockchain[ :-2 ]), run_time=1)
        self.wait(t)

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
                  FadeIn(orders_left), run_time=tt)
        self.wait(t)

        self.play(LaggedStart(*[ FadeOut(order, target_position=blocks[ 1 ]) for order in orders_left_list + orders_right_list ]),
                  run_time=tt)
        self.wait(t)
        self.play(Create(blockchain[ -2: ]), run_time=tt)
        self.wait(t)

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
        self.wait(t)

        self.play(Create(speed))

        self.play(speed.animate.scale(2),
                  Create(speed_arrow))
        self.wait(t)

        self.play(Uncreate(blockchain),
                  Uncreate(VGroup(fees, fees_arrow, speed, speed_arrow)), run_time=tt)
        self.wait(t)


class L_02_S_04_amm_xyk_basics(Scene):
    def construct(self):
        # self.play(Create(NumberPlane()))
        ##### 그리하여 오늘은 에이엠엠ㅇ과 엑스와잉는 케이 공식에 대해 알아보겠습니다
        # 에이엠엠 타이틀과
        # 엑스와이는 케이 띄움
        amm_text = Tex('Automatic Market Maker').scale(2)
        xyk = MathTex('x', r'\times', 'y', '=', 'k').scale(2).next_to(amm_text, D)
        self.play(Create(amm_text), run_time=t)
        self.wait(t)
        self.play(Create(xyk), run_time=tt)
        self.wait(t)

        self.play(Uncreate(amm_text), run_time=t)
        self.wait(t)

        self.play(Uncreate(xyk), run_time=t)
        self.wait(t)

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
            'DEX가 생기고 사람들은 BTC와 USDT의 거래쌍을 만들고 싶었습니다.\n그래서 중앙화 거래소에서 BTC 가격이 300 USDT인 걸 보고\n10 BTC와 3000USDT를 함께 유동성 풀이라는 것에 넣었습니다\n스마트 컨트랙트를 통해 자신의 자산을 유동성으로 제공한다는 것입니다.\n이제 거래자들은 비트코인과 테더 거래쌍을 이용할 수 있습니다.',
            font='Batang', line_spacing=3, font_size=25)
        self.play(Create(expl_plain_text), run_time=ttt)
        self.wait(t)

        self.play(Uncreate(expl_plain_text), run_time=t)
        self.wait(t)

        ##### 일단 우리가 알고있는 오더북이 없이 어떻게 거래를 하는가가 궁금하실 겁니다
        ##### 오더북에서는 그저 사람들이 거래하는 것을 바탕으로 알아서 각겨이 정해집니다
        # 오더북 열고
        pair_rect = RoundedRectangle(corner_radius=0.5, height=8, width=4)
        pair_rect_text = Tex("BTCUSD").next_to(pair_rect, UP, buff=0.2).scale(0.8)

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

        curr_px_number_100 = Integer(100, unit=r"\$", color=RED).move_to(curr_px_rect)

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
        order_book_stuff = VGroup(curr_px_rect, curr_px_number_100, order_book_long_table, order_book_shrt_table, order_book_cross)
        self.play(Create(order_book_cross), run_time=t)
        self.wait(t)

        self.play(ReplacementTransform(order_book_stuff, amm_text), run_time=t)
        self.wait(t)

        amm_text = Tex('Automatic Market Maker').scale(2)
        self.play(GrowFromCenter(amm_text), run_time=t)
        self.wait(t)

        ##### 오토매틱마켓메이커는 줄여서 amm이라고 부르고
        # 풀네임 약자로 줄이고
        amm_acronym_text = Tex('AMM').scale(2).move_to(amm_text)
        self.play(ReplacementTransform(amm_text, amm_acronym_text), run_time=t)
        self.wait(t)

        ##### 그냥 프로그램 혹은 가격을 정하는 방식같은 추상적 개념이라고 생각하시면 됩니다
        # 에이엠엠 텍스트 밑에 프로그램 혹은 컨셉
        program_or_concept_text = Tex('Program or Concept?').next_to(amm_text, D)
        self.play(Create(program_or_concept_text), run_time=t)
        self.wait(t)

        ##### 오토매틱마켓메이커를 돌리는데는 일반적으로 유동성 풀이 필요합니다
        # 에이엠엠이 풀박스로 트랜스폼

        pool_rect = RoundedRectangle(width=7, height=4, corner_radius=0.5)
        pool_rect_text = Tex('Pool').next_to(pool_rect, U)
        self.play(ReplacementTransform(program_or_concept_text, pool_rect_text),
                  ReplacementTransform(amm_acronym_text, pool_rect), run_time=t)
        self.wait(t)

        ##### 이 유동성 풀은 우리가 중앙화 거래소에서 봤던 거래쌍이라고 생각하시면 됩니ㅏㄷ
        ##### 우리가 비티씨나 테더를 들고 중앙화 거래소에서 비티씨테더 거래쌍 창으로 가듯이
        ##### 덱스에서는 유동성 풀에 접근해서 거래를 하게됩니다
        ##### 그렇다면 비티씨테더 풀이라는 것은 이더리움 같은게 아니라 비티씨와 테더를 가지고 있어야할 것입니다
        # 풀위에 비티씨 테더라고 텍스트 하나 더 생기고
        # 비티씨 덩어리 테더 덩어리 풀로 풍덩

        btc_usdt_text = Tex('BTC/USDT').next_to(pool_rect_text, U)
        btc_usdt_text_final = Tex('BTC/USDT Pool').move_to(pool_rect_text)

        self.play(Create(btc_usdt_text), run_time=t)
        self.play(ReplacementTransform(VGroup(pool_rect_text, btc_usdt_text), btc_usdt_text_final), run_time=t)
        self.wait(t)

        btc_lump = LabeledDot('BTC', radius=1, color=BTC).shift(L * 5.5)
        usdt_lump = LabeledDot('USDT', radius=1, color=USDT).shift(R * 5.5)
        btc_lump.save_state()
        usdt_lump.save_state()
        btc_lump_arc = Arc(radius=2, angle=PI).flip(axis=np.array([ 0, 1, 0 ])).shift(L * 3.5)
        usdt_lump_arc = Arc(radius=2, angle=PI).shift(R * 3.5)

        self.play(Create(btc_lump),
                  Create(usdt_lump), run_time=t)
        self.wait(t)

        self.play(MoveAlongPath(btc_lump, btc_lump_arc),
                  MoveAlongPath(usdt_lump, usdt_lump_arc), run_time=t)
        self.wait(t)

        ##### 중앙화 거래소 비티씨테더 페어에서 사람들이 이더리움을 들고 모인게 아니라
        ##### 비티씨와 테더를 들고 모인것 처럼 말입니다
        # 옆에 이더리움 솔라나 생기고 엑스자 후 페이드 아웃

        sol_lump = LabeledDot('SOL', radius=1, color=SOL2).shift(L * 5.5 + U * 1)
        eth_lump = LabeledDot('ETH', radius=1, color=ETH).shift(R * 5.5 + U * 2)
        dot_lump = LabeledDot('DOT', radius=1, color=DOT).shift(R * 5.5 + D * 3)
        sol_lump_cross = Cross(stroke_width=15).scale(1.5).move_to(sol_lump)
        eth_lump_cross = Cross(stroke_width=15).scale(1.5).move_to(eth_lump)
        dot_lump_cross = Cross(stroke_width=15).scale(1.5).move_to(dot_lump)
        other_coins = VGroup(sol_lump, eth_lump, dot_lump)
        other_coins_cross = VGroup(sol_lump_cross, eth_lump_cross, dot_lump_cross)

        self.play(Create(other_coins), run_time=t)
        self.wait(t)

        self.play(Create(other_coins_cross), run_time=t)
        self.wait(t)

        self.play(Uncreate(other_coins),
                  Uncreate(other_coins_cross), run_time=t)
        self.wait(t)

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

        self.play(FadeOut(usdt_lump), run_time=t)
        self.wait(t)

        self.play(Create(exchange_speech_text_1),
                  btc_lump_long_face.animate.move_to(R * 5), run_time=t)
        self.wait(t)

        self.play(ReplacementTransform(exchange_speech_text_1, long_face_1), run_time=t)
        self.wait(t)

        self.play(Uncreate(long_face_1),
                  Uncreate(btc_lump_long_face), run_time=t)
        self.wait(t)

        self.play(FadeIn(usdt_lump), run_time=t)
        self.wait(t)

        exchange_speech_text_2 = Tex(r'I am here to\\get BTC with my USDT').shift(5.5 * L + 3 * D).scale(0.7)
        long_face_2 = Tex(':(').rotate(-PI / 2).move_to(exchange_speech_text_2).scale(3)
        usdt_lump_long_face = usdt_lump.copy().shift(L * 15)

        self.play(FadeOut(btc_lump), run_time=t)
        self.wait(t)

        self.play(Create(exchange_speech_text_2), usdt_lump_long_face.animate.move_to(L * 5), run_time=t)
        self.wait(t)

        self.play(ReplacementTransform(exchange_speech_text_2, long_face_2), run_time=t)
        self.wait(t)

        self.play(Uncreate(long_face_2),
                  Uncreate(usdt_lump_long_face), run_time=t)
        self.wait(t)

        self.play(FadeIn(btc_lump), run_time=t)
        self.wait(t)

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
        self.wait(t)

        self.play(FadeOut(btc_lump_liq_prov_1, target_position=pool_rect),
                  FadeOut(usdt_lump_liq_prov_1, target_position=pool_rect),
                  btc_lump.animate.scale(1.1),
                  usdt_lump.animate.scale(1.1), run_time=tt)
        self.wait(t)

        self.play(FadeOut(btc_lump_liq_prov_2, target_position=pool_rect),
                  FadeOut(usdt_lump_liq_prov_2, target_position=pool_rect),
                  btc_lump.animate.scale(1.1),
                  usdt_lump.animate.scale(1.1), run_time=tt)
        self.wait(t)

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

        self.play(Create(dex_participants_text), run_time=t)
        self.play(Create(line_to_liq_prov),
                  Create(line_to_trader), run_time=t)
        self.wait(t)

        self.play(Create(liq_prov_text),
                  Create(trader_text), run_time=t)
        self.wait(t)

        ##### 유동성 제공자는 아까처럼 말한 것처럼 비티씨와 테더를 같이 넣어주거나 빼면서
        ##### 유동성을 조절합니다. 즉 풀 사이즈를 키우거나 줄입니다. 이것은 나중에 보겠지만
        ##### 케이값을 움직이는 것입니다. 곧 보게 될테니 걱정 안 하셔도 됩니다
        # 유동성 제공자 텍스트 밑에 엔터티 만들고 엔터티가 비티씨와 테더를 함께 풀에 넣는 모션
        # 그리고 밑에 텍스트로 체인징 케이 옆에 조그맣게 그래프 케이값 왔다 갔다
        liq_provider = create_entity(Tex(r' \emph{Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "BTC", BTC, 1.4,
                                     0.3).next_to(liq_prov_text, D)
        liq_prov_btc_asset = liq_provider[ 1 ]
        liq_prov_usdt_asset = create_entity("A", 0.5, WHITE, "USDT", USDT, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)
        liq_provider.add(liq_prov_usdt_asset)
        self.play(Create(liq_provider), run_time=tt)
        self.wait(t)

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

        self.play(Create(moving_k_text), run_time=t)
        self.wait(t)

        self.play(Create(coor_sys_liq_prov),
                  Create(liq_prov_graph), run_time=tt)
        self.wait(t)

        self.play(liq_prov_tracker.animate.set_value(9))
        self.wait(t)

        self.play(liq_prov_tracker.animate.set_value(1))
        self.wait(t)
        liq_prov_btc_asset.save_state()
        liq_prov_usdt_asset.save_state()
        self.play(liq_prov_tracker.animate.set_value(9),
                  FadeOut(liq_prov_btc_asset, target_position=btc_lump),
                  FadeOut(liq_prov_usdt_asset, target_position=usdt_lump),
                  btc_lump.animate.scale(1.1),
                  usdt_lump.animate.scale(1.1), run_time=tt)
        self.wait(t)
        liq_prov_btc_asset.restore()
        liq_prov_usdt_asset.restore()
        self.play(liq_prov_tracker.animate.set_value(1),
                  FadeIn(liq_prov_btc_asset, target_position=btc_lump),
                  FadeIn(liq_prov_usdt_asset, target_position=usdt_lump),
                  btc_lump.animate.scale(1 / 1.1),
                  usdt_lump.animate.scale(1 / 1.1), run_time=tt)
        self.wait(t)

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
        trader = create_entity(Tex(r' \emph{Trader}', color=BLACK).scale(0.9), 1, WHITE, "BTC", BTC, 1.4,
                               0.3).next_to(trader_text, D)
        trader_btc_asset = trader[ 1 ]
        trader_usdt_asset = create_entity("A", 0.5, WHITE, "USDT", USDT, 1.4, 0.3)[ 1 ].next_to(trader, DOWN, buff=0.1)
        trader_usdt_asset_copy = create_entity("A", 0.5, WHITE, "USDT", USDT, 1.4, 0.3)[ 1 ].move_to(trader_btc_asset)
        trader.add(trader_usdt_asset)
        self.play(Create(trader), run_time=tt)
        self.wait(t)

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

        self.play(Create(moving_dot_text), run_time=t)
        self.wait(t)
        self.play(Create(coor_sys_trader),
                  Create(trader_graph),
                  Create(curr_dot), run_time=t)
        self.wait(t)
        self.play(trader_tracker.animate.set_value(6), run_time=tt)
        self.wait(t)
        self.play(trader_tracker.animate.set_value(1), run_time=t)
        self.wait(t)

        self.play(trader_tracker.animate.set_value(6),
                  FadeOut(trader_btc_asset, target_position=btc_lump),
                  FadeIn(trader_usdt_asset_copy, target_position=usdt_lump),
                  btc_lump.animate.scale(1.1),
                  usdt_lump.animate.scale(1 / 1.1), run_time=tt)
        self.wait(t)

        self.play(trader_tracker.animate.set_value(1),
                  FadeIn(trader_btc_asset, target_position=btc_lump),
                  FadeOut(trader_usdt_asset_copy, target_position=usdt_lump),
                  btc_lump.animate.scale(1 / 1.1),
                  usdt_lump.animate.scale(1.1), run_time=tt)
        self.wait(t)

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
        self.wait(t)
        self.play(Create(equal_sign))
        self.wait(t)

        self.play(ReplacementTransform(always_equal_value_texts, value_equal_1), run_time=tt)
        self.wait(t)
        self.play(ReplacementTransform(value_equal_1, value_equal_2), run_time=t)
        self.wait(t)
        self.play(ReplacementTransform(value_equal_2, price_frac), run_time=t)
        self.wait(t)
        self.play(ReplacementTransform(price_frac, final_price_per_btc), run_time=t)
        self.wait(t)

        ##### 이것은 모두 미리 작성된 프로그래밍 언어의 스크립트를 실행하는 것으로 이루어집니다
        ##### 스마트 컨트랙트 덕분에 우리는 중앙화 거래서와 같은 제3자를 거치지 않을 수 있게 됐습니다
        all_thanks_to = Tex('Everything without 3rd entity', 'All thanks to Smart Contract').arrange(D).shift(D * 3)
        self.play(ReplacementTransform(final_price_per_btc, all_thanks_to))
        self.wait(t)


class L_02_S_05_amm_xyk_basics_with_math(Scene):
    def construct(self):
        ##### 간단하게 오토매틱 마켓 메이커를 통해 덱스가 돌아가는 원리를 배웟는데
        ##### 이젠 약간의 수학과 함께 더욱 자세히 알아보겠습니다
        amm_text = Tex('AMM').scale(2)
        with_math_text = Tex('with Math').next_to(amm_text, D)

        self.play(Create(amm_text), run_time=t)
        self.wait(t)
        self.play(Create(with_math_text), run_time=t)
        self.wait(t)

        self.play(Uncreate(VGroup(amm_text, with_math_text)), run_time=t)
        self.wait(t)

        #####
        ##### 엑스와이는 케이에서 엑스를 이항시키면
        ##### 와이는 엑스부느이 케이 형태입니다
        # 좌측 상단
        xyk = MathTex('x', r'\times', 'y', '=', 'k').scale(2)
        self.play(Write(xyk), run_time=t)
        self.wait(t)

        xyk_fraction = MathTex('y', '=', r'\frac{k}{x}').scale(2)
        self.play(TransformMatchingShapes(xyk, xyk_fraction), run_time=t)
        self.wait(t)

        self.play(xyk_fraction.animate.scale(0.5).to_edge(U).shift(L * 6), run_time=t)
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
                                 lag_ratio=0.5), run_time=t)
        self.wait(t)

        self.play(Circumscribe(func_3), run_time=t)
        self.wait(t)

        self.play(AnimationGroup(Uncreate(func_1),
                                 Uncreate(func_2),
                                 Uncreate(func_3),
                                 Uncreate(func_4),
                                 Uncreate(func_5),
                                 lag_ratio=0.5), run_time=t)
        self.wait(t)

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
        self.wait(t)

        self.play(k_tracker.animate.set_value(300), run_time=5)
        self.wait(t)

        self.play(Uncreate(k_var))
        self.play(Uncreate(ax))
        self.play(Uncreate(xyk_graph))
        self.wait(t)

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
                  , run_time=t)
        self.wait(t)

        self.play(Create(A_coin_texts),
                  Create(B_coin_texts), run_time=tt)
        self.wait(t)

        self.play(Uncreate(A_coin_texts),
                  Uncreate(B_coin_texts),
                  Uncreate(x_arrow),
                  Uncreate(y_arrow)
                  , run_time=t)
        self.wait(t)

        ##### 복잡하게 생각할 건 없고 와이는 엑스분의케이 그래프에서 케이는 그냥 어떤 값입니다.
        ##### 그런데 아까 우리는 케이가 엑스 곱하기 와이인 걸 봤습니다.
        # 기존에 있는 함수식 있고 다시 엑스와이는 케이 방정식 등장
        # 함수식 밑에 등장
        k_var = Variable(1, MathTex("k"), var_type=Integer).next_to(xyk_fraction, R, buff=2)
        k_tracker = k_var.tracker
        k_tracker.set_value(1)

        xyk_form = MathTex(r'x\times y=k')

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
        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool', color=WHITE).scale(0.4), edge=DOWN, direction=DOWN, buff=0.37)

        axis_labels = VGroup(x_axis_label, y_axis_label)

        coor_sys = VGroup(ax, axis_labels, xyk_graph_btc)

        self.play(Create(k_var), run_time=t)
        self.play(Create(coor_sys), run_time=t)
        self.wait(t)

        # self.play(Create(axis_labels))
        # self.play(Create(xyk_graph_btc))

        ##### 자 그렇다면 현재 비티씨테더 풀의 함수식은 10곱하기 3000인 30000입니다다
        # 케이값은 30000으로 변경
        self.play(k_tracker.animate.set_value(30000), run_time=tt)
        self.wait(t)

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

        self.play(Create(curr_dot), run_time=t)
        self.play(Create(dot_label), run_time=t)

        self.wait(t)

        dot_label_2 = MathTex(
            rf'({btc_tracker.get_value():.0f},{usdt_tracker.get_value():.0f})\  {usdt_tracker.get_value() / btc_tracker.get_value():.0f}USDT',
            font_size=35).next_to(curr_dot, UR)

        self.play(ReplacementTransform(dot_label,dot_label_2),run_time=3)
        self.wait(t)

        dot_label_2.add_updater(lambda dot: dot.become(MathTex(
            rf'({btc_tracker.get_value():.0f},{usdt_tracker.get_value():.0f})\  {usdt_tracker.get_value() / btc_tracker.get_value():.0f}USDT',
            font_size=35).next_to(
            curr_dot, UR)))

        ##### 거래자가 풀을 대상으로 비티씨를 매수하거나 매도한다는 것은
        ##### 풀의 상태를 변화 시키는 것이기에 현재 있는 지점에서 그래프 상의 다른 지점으로 이동한다는 것이고 풀상태예 따라 가격이 변하는데
        # 그래프에서 점 움직이면 레이블도 같이 움직이고 값도 변화

        buy_btc = Tex(r'BUY', 'BTC').arrange(D).scale(2).shift(R * 4)
        buy_btc.set_color_by_tex("BUY", GREEN)
        # buy_btc.set_color_by_tex("T", RED)
        # buy_btc.set_color_by_tex("B", BLUE)
        sell_btc = Tex(r'SELL', 'BTC').arrange(D).scale(2).shift(R * 4)
        sell_btc.set_color_by_tex("SELL", RED)

        self.play(Create(buy_btc), run_time=t)
        self.wait(t)
        self.play(btc_tracker.animate.set_value(7),
                  usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
                  run_time=tt)
        self.wait(t)

        self.play(Uncreate(buy_btc), run_time=t)
        self.wait(t)

        self.play(Create(sell_btc), run_time=t)
        self.wait(t)
        self.play(btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)),
                  run_time=tt)
        self.wait(t)

        self.play(Uncreate(sell_btc), run_time=t)
        self.wait(t)

        ##### 유동성 제공자가 유동성을 공급하거나 제거한다는 것은 케이값을 움직이는 것입니다.

        ##### 유동성을 공급하는 것은 비티씨와 테더를 같이 넣어주는 것이고
        ##### 그건 엑스와 와이가 둘다 늘어나기 때문에 케이값이 커지는 것입니다
        ##### 유동성을 제거하면 비티씨와 테더가 같이 빠져나가는 것이고
        ##### 엑스와 와이가 둘다 줄면 당연히 케이값도 줄어듭니다
        # 케이값 움직이면서 그래프도 움직임
        add_liq = Tex(r'ADD', 'Liquidity').arrange(D).scale(2).shift(R * 4)
        add_liq.set_color_by_tex("ADD", GREEN)

        rmv_liq = Tex(r'REMOVE', 'Liquidity').arrange(D).scale(2).shift(R * 4)
        rmv_liq.set_color_by_tex("REMOVE", RED)

        self.play(Create(add_liq), run_time=t)
        self.wait(t)

        self.play(k_tracker.animate.set_value(35000),
                  btc_tracker.animate.set_value(sqrt(35000*13**2/30000)),
                  usdt_tracker.animate.set_value(35000/sqrt(35000*13**2/30000)),
                  run_time=tt)
        self.wait(t)

        self.play(Uncreate(add_liq), run_time=t)
        self.wait(t)

        self.play(Create(rmv_liq), run_time=t)
        self.wait(t)

        self.play(k_tracker.animate.set_value(25000),
                  btc_tracker.animate.set_value(sqrt(25000*13**2/30000)),
                  usdt_tracker.animate.set_value(25000/sqrt(25000*13**2/30000) ), run_time=tt)
        self.wait(t)
        self.play(Uncreate(rmv_liq), run_time=t)
        self.wait(t)

        self.play(Uncreate(VGroup(xyk_fraction, k_var, curr_dot, dot_label_2, coor_sys)), run_time=tt)
        self.wait(t)


class L_02_S_06_amm_xyk_adv_k_dn_1(Scene):
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
        liq_pool = VGroup(liq_pool_rect, liq_pool_text).to_edge(UL).shift(R * 0.5)
        liq_pool.set_z_index(3)

        k_var = Variable(30000, MathTex("k"), var_type=Integer).to_edge(UR)
        k_tracker = k_var.tracker
        k_tracker.set_value(30000)

        self.play(Create(liq_pool), run_time=t)
        self.wait(t)

        liq_provider = create_entity(Tex(r' \emph{Init Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", BTC, 1.4,
                                     0.3).next_to(liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", USDT, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)
        liq_provider.add(usdt_asset)

        self.play(Create(liq_provider), run_time=t)
        self.wait(t)

        ax = Axes(x_range=[ 0, 18, 4 ], y_range=[ 0, 6500, 1000 ], x_length=5, y_length=5, tips=True,
                  axis_config={"include_numbers": False, 'color': WHITE, 'include_ticks': False, 'font_size': 20}, ).to_edge(DR, buff=0.8)

        ax.shift(U * (liq_pool_rect.get_bottom()[ 1 ] - ax[ 0 ].get_y()))

        y_axis_label = ax.get_y_axis_label(MathTex('Amount of USDT in Pool', color=WHITE).rotate(PI / 2).scale(0.4), edge=LEFT,
                                           direction=LEFT, buff=0.37)
        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool', color=WHITE).scale(0.4), edge=DOWN, direction=DOWN, buff=0.37)
        axis_labels = VGroup(x_axis_label, y_axis_label)

        usdt_bar = Rectangle(height=3, width=1.2, fill_color=USDT, fill_opacity=1, color=USDT)
        btc_bar = Rectangle(height=1, width=1.2, fill_color=BTC, fill_opacity=1, color=BTC)
        bars = VGroup(btc_bar, usdt_bar)
        bars.arrange(RIGHT, aligned_edge=DOWN).move_to(liq_pool_rect).align_to(liq_pool_rect, DOWN)

        usdt_bar_pos = usdt_bar.get_bottom()
        btc_bar_pos = btc_bar.get_bottom()

        btc_var = Variable(10, MathTex("BTC"), var_type=Integer)
        usdt_var = Variable(3000, MathTex("USDT"), var_type=Integer).next_to(btc_var, DOWN, aligned_edge=LEFT)
        btc_tracker = btc_var.tracker
        usdt_tracker = usdt_var.tracker
        usdt_var[ 0 ][ 0 ].set_color(USDT)
        btc_var[ 0 ][ 0 ].set_color(BTC)

        vars = VGroup(btc_var, usdt_var).arrange(DOWN, aligned_edge=LEFT).next_to(liq_pool_rect, DOWN, buff=0.25)

        self.play(ReplacementTransform(usdt_asset, usdt_bar),
                  ReplacementTransform(btc_asset, btc_bar), run_time=t)
        self.wait(t)
        self.play(Write(usdt_var),
                  Write(btc_var), run_time=t)
        self.wait(t)
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=USDT, fill_opacity=1, color=USDT).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=BTC, fill_opacity=1, color=BTC).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        pool_price = Variable(100, 'Price', var_type=DecimalNumber, num_decimal_places=2).next_to(
            liq_pool_rect, RIGHT, buff=0.5).scale(0.8).to_edge(UP)
        pool_price_tracker = pool_price.tracker
        pool_price.add_updater(lambda v: pool_price_tracker.set_value(usdt_tracker.get_value() / btc_tracker.get_value()))
        pool_price_unit = Tex(r'USDT').scale(0.75).next_to(pool_price, buff=0.1)
        self.play(Write(k_var[ 0 ]))
        self.wait(t)
        self.play(Create(ax),
                  Create(axis_labels),
                  Create(pool_price_unit),
                  Create(pool_price),
                  TransformMatchingShapes(Group(btc_var[ 1 ].copy(), usdt_var[ 1 ].copy()), k_var[ 1 ].copy()),
                  Create(xyk_fraction.next_to(k_var, LEFT, buff=1)), run_time=tt
                  )
        self.wait(t)

        lp_amt_form_1 = MathTex(r'Init\  l =\sqrt{x \times y}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_2 = MathTex(r'Init\  l =\sqrt{10 \times 3000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_3 = MathTex(r'Init\  l =\sqrt{30000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_int = Tex(rf'{int(30000 ** (1 / 2))} LP token').move_to(lp_amt_form_1).scale(0.7)

        self.play(Create(lp_amt_form_1), run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(lp_amt_form_1, lp_amt_form_2), run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(lp_amt_form_2, lp_amt_form_3), run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(lp_amt_form_3, lp_amt_int), run_time=t)
        self.wait(t)

        box = Rectangle(width=1.6, height=1, fill_color=WHITE, stroke_color=WHITE, fill_opacity=1)
        text = Tex(r"173\\BTC-USDT\\LP", color=BLACK).scale(0.5)
        lp_asset = VGroup(box, text).next_to(liq_provider[ 0 ], DOWN, buff=0.1)

        self.play(Create(lp_asset),
                  Uncreate(lp_amt_int), run_time=t)
        self.wait(t)

        # self.play(
        #     FadeOut(lp_amt_int),
        #     run_time=t)
        # self.wait(t)

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
        x_marker = Triangle(color=BTC, fill_color=BTC, fill_opacity=1).scale(0.1).next_to(vertical_line, DOWN, buff=0)
        x_marker.add_updater(lambda marker: marker.next_to(vertical_line, DOWN, buff=0))
        x_marker_val = Integer(btc_tracker.get_value())
        x_marker_val.add_updater(
            lambda integer: integer.become(Integer(btc_tracker.get_value()).scale(0.4).next_to(vertical_line, DOWN, buff=0.3)))

        y_marker = Triangle(color=USDT, fill_color=USDT, fill_opacity=1).scale(0.1).rotate(-PI / 2).next_to(horizontal_line, LEFT, buff=0)
        y_marker.add_updater(lambda marker: marker.next_to(horizontal_line, LEFT, buff=0))
        y_marker_val = Integer(usdt_tracker.get_value())
        y_marker_val.add_updater(lambda integer: integer.become(
            Integer(usdt_tracker.get_value()).scale(0.4).rotate(PI / 2).next_to(horizontal_line, LEFT, buff=0.3)))

        lines = VGroup(vertical_line, horizontal_line)
        markers = VGroup(x_marker, x_marker_val, y_marker, y_marker_val)

        self.play(Create(xyk_graph_btc), run_time=t)
        self.wait(t)

        self.play(Create(curr_dot), run_time=t)
        self.wait(t)

        self.play(Create(lines), run_time=t)
        self.play(Create(markers), run_time=t)
        self.wait(t)

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

        self.play(Create(area), run_time=t)
        self.play(Create(area_text), run_time=t)
        self.wait(t)

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

        self.play(FadeOut(liq_provider[ 0 ]),
                  FadeOut(lp_asset), run_time=t)

        self.wait(t)
        self.play(Create(liq_provider[ 0 ]),
                  Create(lp_asset), run_time=t)
        self.wait(t)
        lp_asset_121 = create_lp_token(r"121\\BTC-USDT\\LP").next_to(liq_provider[ 0 ], DOWN, buff=0.1)
        lp_asset_51 = create_lp_token(r"52\\BTC-USDT\\LP").next_to(lp_asset_121, DOWN, buff=0.1)
        lp_asset_divided = VGroup(lp_asset_121, lp_asset_51)

        btc_asset = create_entity("A", 0.5, WHITE, "3 BTC", BTC, 1.4, 0.3)[ 1 ].next_to(lp_asset_121, D, buff=0.1)
        usdt_asset = create_entity("A", 0.5, WHITE, "900 USDT", USDT, 1.4, 0.3)[ 1 ].next_to(btc_asset, DOWN, buff=0.1)
        # text = Tex(r"173\\BTC-USDT\\LP", color=BLACK).scale(0.5)
        #
        # self.play(Create(liq_provider[ 0 ]),
        #           Create(lp_asset), run_time=t)
        # self.wait(t)

        btc_bar.clear_updaters()
        usdt_bar.clear_updaters()

        # # scene2_btc_dashed_box = Rectangle(color=RED).align_to(btc_bar[0],UL,alignment_vect=btc_bar[0].get_edge_center(UP))
        # scene2_2308usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.2307, stroke_width=3,
        #                                 stroke_color=RED_E).align_to(usdt_bar, UL)

        scene4_5btc_box = Rectangle(width=btc_bar.width, height=btc_bar.height * 0.3, stroke_width=3,
                                    stroke_color=RED_E).align_to(btc_bar, UL)
        scene4_1500usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.3, stroke_width=3,
                                        stroke_color=RED_E).align_to(usdt_bar, UL)

        scene4_1500usdt_fill_box = scene4_1500usdt_box.copy().set_fill(USDT, opacity=1)
        scene4_5btc_fill_box = scene4_5btc_box.copy().set_fill(BTC, opacity=1)

        scene4_5btc_fill_box.set_stroke(width=0, opacity=0)
        scene4_1500usdt_fill_box.set_stroke(width=0, opacity=0)
        scene4_5btc_fill_box.set_z_index(3)
        scene4_1500usdt_fill_box.set_z_index(3)

        self.play(Create(VGroup(scene4_5btc_box, scene4_1500usdt_box)), run_time=t)
        self.wait(t)

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
            Rectangle(height=2100 / 1000, width=1.2, fill_color=USDT, fill_opacity=1, color=USDT).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=7 / 10, width=1.2, fill_color=BTC, fill_opacity=1, color=BTC).move_to(
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
                  Create(scene4_brace_labels), run_time=t)
        self.wait(t)

        dummydot = Dot(1, color=RED).move_to(liq_pool_rect)

        # self.play(Create(origin_dot))
        self.play(ReplacementTransform(lp_asset, lp_asset_divided), run_time=t)
        self.wait(t)

        self.play(k_tracker.animate.set_value(14700),
                  btc_tracker.animate.set_value(7),
                  usdt_tracker.animate.set_value(14700 / 7),
                  Transform(scene4_1500usdt_fill_box, usdt_asset),
                  Transform(scene4_5btc_fill_box, btc_asset),
                  FadeOut(lp_asset_51, target_position=dummydot),
                  run_time=ttt, rate_func=rate_functions.ease_in_out_quint)

        self.wait(4)


class L_02_S_07_amm_xyk_adv_k_up_2(Scene):
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
        liq_pool = VGroup(liq_pool_rect, liq_pool_text).to_edge(UL).shift(R * 0.5)
        liq_pool.set_z_index(3)

        k_var = Variable(30000, MathTex("k"), var_type=Integer).to_edge(UR)
        k_tracker = k_var.tracker
        k_tracker.set_value(30000)

        self.play(Create(liq_pool), run_time=t)
        self.wait(t)

        liq_provider = create_entity(Tex(r' \emph{Init Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", BTC, 1.4,
                                     0.3).next_to(liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", USDT, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)
        liq_provider.add(usdt_asset)

        self.play(Create(liq_provider), run_time=t)
        self.wait(t)

        ax = Axes(x_range=[ 0, 18, 4 ], y_range=[ 0, 6500, 1000 ], x_length=5, y_length=5, tips=True,
                  axis_config={"include_numbers": False, 'color': WHITE, 'include_ticks': False, 'font_size': 20}, ).to_edge(DR, buff=0.8)

        ax.shift(U * (liq_pool_rect.get_bottom()[ 1 ] - ax[ 0 ].get_y()))

        y_axis_label = ax.get_y_axis_label(MathTex('Amount of USDT in Pool', color=WHITE).rotate(PI / 2).scale(0.4), edge=LEFT,
                                           direction=LEFT, buff=0.37)
        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool', color=WHITE).scale(0.4), edge=DOWN, direction=DOWN, buff=0.37)
        axis_labels = VGroup(x_axis_label, y_axis_label)

        usdt_bar = Rectangle(height=3, width=1.2, fill_color=USDT, fill_opacity=1, color=USDT)
        btc_bar = Rectangle(height=1, width=1.2, fill_color=BTC, fill_opacity=1, color=BTC)
        bars = VGroup(btc_bar, usdt_bar)
        bars.arrange(RIGHT, aligned_edge=DOWN).move_to(liq_pool_rect).align_to(liq_pool_rect, DOWN)

        usdt_bar_pos = usdt_bar.get_bottom()
        btc_bar_pos = btc_bar.get_bottom()

        btc_var = Variable(10, MathTex("BTC"), var_type=Integer)
        usdt_var = Variable(3000, MathTex("USDT"), var_type=Integer).next_to(btc_var, DOWN, aligned_edge=LEFT)
        btc_tracker = btc_var.tracker
        usdt_tracker = usdt_var.tracker
        usdt_var[ 0 ][ 0 ].set_color(USDT)
        btc_var[ 0 ][ 0 ].set_color(BTC)

        vars = VGroup(btc_var, usdt_var).arrange(DOWN, aligned_edge=LEFT).next_to(liq_pool_rect, DOWN, buff=0.25)

        self.play(ReplacementTransform(usdt_asset, usdt_bar),
                  ReplacementTransform(btc_asset, btc_bar), run_time=t)
        self.wait(t)
        self.play(Write(usdt_var),
                  Write(btc_var), run_time=t)
        self.wait(t)
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=USDT, fill_opacity=1, color=USDT).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=BTC, fill_opacity=1, color=BTC).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        pool_price = Variable(100, 'Price', var_type=DecimalNumber, num_decimal_places=2).next_to(
            liq_pool_rect, RIGHT, buff=0.5).scale(0.8).to_edge(UP)
        pool_price_tracker = pool_price.tracker
        pool_price.add_updater(lambda v: pool_price_tracker.set_value(usdt_tracker.get_value() / btc_tracker.get_value()))
        pool_price_unit = Tex(r'USDT').scale(0.75).next_to(pool_price, buff=0.1)
        self.play(Write(k_var[ 0 ]))
        self.wait(t)
        self.play(Create(ax),
                  Create(axis_labels),
                  Create(pool_price_unit),
                  Create(pool_price),
                  TransformMatchingShapes(Group(btc_var[ 1 ].copy(), usdt_var[ 1 ].copy()), k_var[ 1 ].copy()),
                  Create(xyk_fraction.next_to(k_var, LEFT, buff=1)), run_time=tt
                  )
        self.wait(t)

        lp_amt_form_1 = MathTex(r'Init\  l =\sqrt{x \times y}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_2 = MathTex(r'Init\  l =\sqrt{10 \times 3000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_3 = MathTex(r'Init\  l =\sqrt{30000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_int = Tex(rf'{int(30000 ** (1 / 2))} LP token').move_to(lp_amt_form_1).scale(0.7)

        self.play(Create(lp_amt_form_1), run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(lp_amt_form_1, lp_amt_form_2), run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(lp_amt_form_2, lp_amt_form_3), run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(lp_amt_form_3, lp_amt_int), run_time=t)
        self.wait(t)

        box = Rectangle(width=1.6, height=1, fill_color=WHITE, stroke_color=WHITE, fill_opacity=1)
        text = Tex(r"173\\BTC-USDT\\LP", color=BLACK).scale(0.5)
        lp_asset = VGroup(box, text).next_to(liq_provider[ 0 ], DOWN, buff=0.1)

        self.play(Create(lp_asset),
                  Uncreate(lp_amt_int), run_time=t)
        self.wait(t)

        self.play(FadeOut(liq_provider),
                  FadeOut(lp_amt_int),
                  FadeOut(lp_asset), run_time=t)
        self.wait(t)

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
        x_marker = Triangle(color=BTC, fill_color=BTC, fill_opacity=1).scale(0.1).next_to(vertical_line, DOWN, buff=0)
        x_marker.add_updater(lambda marker: marker.next_to(vertical_line, DOWN, buff=0))
        x_marker_val = Integer(btc_tracker.get_value())
        x_marker_val.add_updater(
            lambda integer: integer.become(Integer(btc_tracker.get_value()).scale(0.4).next_to(vertical_line, DOWN, buff=0.3)))

        y_marker = Triangle(color=USDT, fill_color=USDT, fill_opacity=1).scale(0.1).rotate(-PI / 2).next_to(horizontal_line, LEFT, buff=0)
        y_marker.add_updater(lambda marker: marker.next_to(horizontal_line, LEFT, buff=0))
        y_marker_val = Integer(usdt_tracker.get_value())
        y_marker_val.add_updater(lambda integer: integer.become(
            Integer(usdt_tracker.get_value()).scale(0.4).rotate(PI / 2).next_to(horizontal_line, LEFT, buff=0.3)))

        lines = VGroup(vertical_line, horizontal_line)
        markers = VGroup(x_marker, x_marker_val, y_marker, y_marker_val)

        self.play(Create(xyk_graph_btc), run_time=t)
        self.wait(t)

        self.play(Create(curr_dot), run_time=t)
        self.wait(t)

        self.play(Create(lines), run_time=t)
        self.play(Create(markers), run_time=t)
        self.wait(t)

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

        self.play(Create(area), run_time=t)
        self.play(Create(area_text), run_time=t)
        self.wait(t)

        #####
        ##### 유동성을 공급한다는 것은 무엇을 의미할까요
        ##### 엑스와 와이가 오르면서 케이의 값이 함께 오른다는 것입니다
        #####

        btc_bar.clear_updaters()
        usdt_bar.clear_updaters()

        liq_provider = create_entity(Tex(r' \emph{New Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "3 BTC", BTC, 1.4,
                                     0.3).next_to(
            liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "900 USDT", USDT, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)

        self.play(Create(VGroup(liq_provider, usdt_asset)), run_time=t)
        self.wait(t)

        scene3_13btc_box = Rectangle(width=btc_bar.width, height=btc_bar.height * 0.3, stroke_width=3,
                                     stroke_color=GREEN_E).next_to(btc_bar, UP, buff=0)
        scene3_3900usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.3, stroke_width=3,
                                        stroke_color=GREEN_E).next_to(usdt_bar, UP, buff=0)

        self.play(Create(VGroup(scene3_13btc_box, scene3_3900usdt_box)), run_time=t)
        self.wait(t)

        scene3_3900usdt_fill_box = scene3_3900usdt_box.copy().set_fill(USDT, opacity=1)
        scene3_13btc_fill_box = scene3_13btc_box.copy().set_fill(BTC, opacity=1)
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
        scene3_origin_graph.set_color(GREEN)
        scene3_origin_graph.set_z_index(-1)
        self.add(scene3_origin_graph)

        self.play(Create(scene3_braces),
                  Create(scene3_brace_labels), run_time=t)
        self.wait(t)

        box = Rectangle(width=1.6, height=1, fill_color=WHITE, stroke_color=WHITE, fill_opacity=1)
        text = Tex(r"87\\BTC-USDT\\LP", color=BLACK).scale(0.5)
        new_liq_provider_lp_asset = VGroup(box, text).next_to(liq_provider[ 0 ], DOWN, buff=0.1)

        lp_add_form_1 = MathTex(r"Added\  {l}' =l\times\frac{{x}'}{x}").next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_add_form_2 = MathTex(r"Added\  {l}' =\sqrt{30000}\times\frac{3}{10}").move_to(lp_add_form_1).scale(0.7)
        lp_add_form_3 = MathTex(r"Added\  {l}' =173\times0.3").move_to(lp_add_form_1).scale(0.7)
        lp_add_int = Tex(rf"{int(30000 ** (1 / 2) * 3 / 10)} LP token").move_to(lp_add_form_1).scale(0.7)
        total_lp_supply_1 = MathTex(r"Total\  l =l+{l}'").next_to(lp_add_form_1, UP).scale(0.7)
        total_lp_supply_2 = MathTex(r"Total\  l =173+51").move_to(lp_add_form_1).scale(0.7)
        total_lp_supply_int = Tex(rf"{int(30000 ** (1 / 2) + 30000 ** (1 / 2) * 3 / 10)} LP token").move_to(lp_add_form_1).scale(0.7)

        self.play(Create(lp_add_form_1), run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(lp_add_form_1, lp_add_form_2), run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(lp_add_form_2, lp_add_form_3), run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(lp_add_form_3, lp_add_int), run_time=t)
        self.wait(t)
        self.play(Uncreate(lp_add_int), run_time=t)
        self.wait(t)

        self.play(Create(total_lp_supply_1), run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(total_lp_supply_1, total_lp_supply_2), run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(total_lp_supply_2, total_lp_supply_int), run_time=t)
        self.wait(t)
        self.play(Uncreate(total_lp_supply_int), run_time=t)
        self.wait(t)

        usdt_asset.save_state()
        btc_asset.save_state()
        self.play(k_tracker.animate.set_value(50700),
                  btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(50700 / 13),
                  ReplacementTransform(usdt_asset, scene3_3900usdt_fill_box),
                  ReplacementTransform(btc_asset, scene3_13btc_fill_box),
                  FadeIn(new_liq_provider_lp_asset, target_position=liq_pool_rect),
                  run_time=ttt)
        self.wait(t)

        new_user_share_1 = MathTex(r"Share =\frac{UserLP}{TotSupply}").move_to(lp_add_form_1).scale(0.7)
        new_user_share_2 = MathTex(r"Share =\frac{51}{173+51}").move_to(lp_add_form_1).scale(0.7)
        new_user_share_3 = MathTex(r"Share =0.23").move_to(lp_add_form_1).scale(0.7)
        new_user_share_4 = Tex(r"23\%").move_to(lp_add_form_1)

        self.play(Create(new_user_share_1), run_time=t)
        self.wait(t)

        self.play(ReplacementTransform(new_user_share_1, new_user_share_2), run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(new_user_share_2, new_user_share_3), run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(new_user_share_3, new_user_share_4), run_time=t)
        self.wait(t)
        self.play(Uncreate(new_user_share_4), run_time=t)
        self.wait(t)

        usdt_asset.restore()
        btc_asset.restore()

        dummydot = Dot(1, color=RED).move_to(liq_pool_rect)

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(30000 / 10),
                  Transform(scene3_3900usdt_fill_box, usdt_asset),
                  Transform(scene3_13btc_fill_box, btc_asset),
                  FadeOut(new_liq_provider_lp_asset, target_position=dummydot),
                  run_time=ttt)
        self.wait(t)

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

        self.play(Create(liq_pool), run_time=t)
        self.wait(t)

        liq_provider = create_entity(Tex(r' \emph{Init Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", BTC, 1.4,
                                     0.3).next_to(liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", USDT, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)
        liq_provider.add(usdt_asset)

        self.play(Create(liq_provider), run_time=t)
        self.wait(t)

        ax = Axes(x_range=[ 0, 18, 4 ], y_range=[ 0, 6500, 1000 ], x_length=5, y_length=5, tips=True,
                  axis_config={"include_numbers": False, 'color': WHITE, 'include_ticks': False, 'font_size': 20}, ).to_edge(DR, buff=0.8)

        ax.shift(U * (liq_pool_rect.get_bottom()[ 1 ] - ax[ 0 ].get_y()))

        y_axis_label = ax.get_y_axis_label(MathTex('Amount of USDT in Pool', color=WHITE).rotate(PI / 2).scale(0.4), edge=LEFT,
                                           direction=LEFT, buff=0.37)
        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool', color=WHITE).scale(0.4), edge=DOWN, direction=DOWN, buff=0.37)
        axis_labels = VGroup(x_axis_label, y_axis_label)

        usdt_bar = Rectangle(height=3, width=1.2, fill_color=USDT, fill_opacity=1, color=USDT)
        btc_bar = Rectangle(height=1, width=1.2, fill_color=BTC, fill_opacity=1, color=BTC)
        bars = VGroup(btc_bar, usdt_bar)
        bars.arrange(RIGHT, aligned_edge=DOWN).move_to(liq_pool_rect).align_to(liq_pool_rect, DOWN)

        usdt_bar_pos = usdt_bar.get_bottom()
        btc_bar_pos = btc_bar.get_bottom()

        btc_var = Variable(10, MathTex("BTC"), var_type=Integer)
        usdt_var = Variable(3000, MathTex("USDT"), var_type=Integer).next_to(btc_var, DOWN, aligned_edge=LEFT)
        btc_tracker = btc_var.tracker
        usdt_tracker = usdt_var.tracker
        usdt_var[ 0 ][ 0 ].set_color(USDT)
        btc_var[ 0 ][ 0 ].set_color(BTC)

        vars = VGroup(btc_var, usdt_var).arrange(DOWN, aligned_edge=LEFT).next_to(liq_pool_rect, DOWN, buff=0.25)

        self.play(ReplacementTransform(usdt_asset, usdt_bar),
                  ReplacementTransform(btc_asset, btc_bar), run_time=t)
        self.wait(t)
        self.play(Write(usdt_var),
                  Write(btc_var), run_time=t)
        self.wait(t)
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=USDT, fill_opacity=1, color=USDT).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=BTC, fill_opacity=1, color=BTC).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        pool_price = Variable(100, 'Price', var_type=DecimalNumber, num_decimal_places=2).next_to(
            liq_pool_rect, RIGHT, buff=0.5).scale(0.8).to_edge(UP)
        pool_price_tracker = pool_price.tracker
        pool_price.add_updater(lambda v: pool_price_tracker.set_value(usdt_tracker.get_value() / btc_tracker.get_value()))
        pool_price_unit = Tex(r'USDT').scale(0.75).next_to(pool_price, buff=0.1)
        self.play(Write(k_var[ 0 ]))
        self.wait(t)
        self.play(Create(ax),
                  Create(axis_labels),
                  Create(pool_price_unit),
                  Create(pool_price),
                  TransformMatchingShapes(Group(btc_var[ 1 ].copy(), usdt_var[ 1 ].copy()), k_var[ 1 ].copy()),
                  Create(xyk_fraction.next_to(k_var, LEFT, buff=1)), run_time=tt
                  )
        self.wait(t)

        lp_amt_form_1 = MathTex(r'Init\  l =\sqrt{x \times y}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_2 = MathTex(r'Init\  l =\sqrt{10 \times 3000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_3 = MathTex(r'Init\  l =\sqrt{30000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_int = Tex(rf'{int(30000 ** (1 / 2))} LP token').move_to(lp_amt_form_1).scale(0.7)

        self.play(Create(lp_amt_form_1), run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(lp_amt_form_1, lp_amt_form_2), run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(lp_amt_form_2, lp_amt_form_3), run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(lp_amt_form_3, lp_amt_int), run_time=t)
        self.wait(t)

        box = Rectangle(width=1.6, height=1, fill_color=WHITE, stroke_color=WHITE, fill_opacity=1)
        text = Tex(r"173\\BTC-USDT\\LP", color=BLACK).scale(0.5)
        lp_asset = VGroup(box, text).next_to(liq_provider[ 0 ], DOWN, buff=0.1)

        self.play(Create(lp_asset),
                  Uncreate(lp_amt_int), run_time=t)
        self.wait(t)

        self.play(FadeOut(liq_provider),
                  FadeOut(lp_amt_int),
                  FadeOut(lp_asset), run_time=t)
        self.wait(t)

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
        x_marker = Triangle(color=BTC, fill_color=BTC, fill_opacity=1).scale(0.1).next_to(vertical_line, DOWN, buff=0)
        x_marker.add_updater(lambda marker: marker.next_to(vertical_line, DOWN, buff=0))
        x_marker_val = Integer(btc_tracker.get_value())
        x_marker_val.add_updater(
            lambda integer: integer.become(Integer(btc_tracker.get_value()).scale(0.4).next_to(vertical_line, DOWN, buff=0.3)))

        y_marker = Triangle(color=USDT, fill_color=USDT, fill_opacity=1).scale(0.1).rotate(-PI / 2).next_to(horizontal_line, LEFT, buff=0)
        y_marker.add_updater(lambda marker: marker.next_to(horizontal_line, LEFT, buff=0))
        y_marker_val = Integer(usdt_tracker.get_value())
        y_marker_val.add_updater(lambda integer: integer.become(
            Integer(usdt_tracker.get_value()).scale(0.4).rotate(PI / 2).next_to(horizontal_line, LEFT, buff=0.3)))

        lines = VGroup(vertical_line, horizontal_line)
        markers = VGroup(x_marker, x_marker_val, y_marker, y_marker_val)

        self.play(Create(xyk_graph_btc), run_time=t)
        self.wait(t)

        self.play(Create(curr_dot), run_time=t)
        self.wait(t)

        self.play(Create(lines), run_time=t)
        self.play(Create(markers), run_time=t)
        self.wait(t)

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

        self.play(Create(area), run_time=t)
        self.play(Create(area_text), run_time=t)
        self.wait(t)

        ##### DIVERGE
        #####
        user = create_entity(Tex(r' \emph{Trader}', color=BLACK), 1, WHITE, "1286 USDT", USDT, 1.4, 0.3).next_to(liq_pool_rect, RIGHT,
                                                                                                                  buff=1.5)
        user_asset_usdt = user[ 1 ]
        user_asset_pos = user_asset_usdt.get_center()
        user_asset_btc = create_entity("A", 0.5, WHITE, "3 BTC", BTC, 1.4, 0.3)[ 1 ].move_to(user_asset_pos)

        user_line = Tex(r'I want 3 BTC\\I have some USDT').scale(0.5).next_to(user, DOWN)

        self.play(Create(user), run_time=t)
        self.wait(t)
        self.play(Create(user_line), run_time=t)
        self.wait(t)
        self.play(Uncreate(user_line), run_time=t)
        self.wait(t)

        # self.add(index_labels(btc_bar))###

        # scene1_btc_dashed_box = Rectangle(color=RED).align_to(btc_bar[0],UL,alignment_vect=btc_bar[0].get_edge_center(UP))
        scene1_7btc_box = Rectangle(width=btc_bar.width, height=btc_bar.height * 0.3, stroke_width=3, stroke_color=RED_E).align_to(
            btc_bar[ 0 ], UL)
        scene1_1286usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.4286, stroke_width=3,
                                        stroke_color=GREEN_E).next_to(usdt_bar, UP, buff=0)

        scene1_7btc_fill_box = scene1_7btc_box.copy().set_fill(BTC, opacity=1)
        scene1_1286usdt_fill_box = scene1_1286usdt_box.copy().set_fill(USDT, opacity=1)
        scene1_7btc_fill_box.set_stroke(width=0, opacity=0)
        scene1_1286usdt_fill_box.set_stroke(width=0, opacity=0)
        scene1_7btc_fill_box.set_z_index(3)
        scene1_1286usdt_fill_box.set_z_index(3)

        self.play(Create(scene1_7btc_box), run_time=t)
        self.play(Create(scene1_1286usdt_box), run_time=t)
        self.wait(t)

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

        self.play(Create(scene1_braces, run_time=t),
                  Create(scene1_brace_labels), run_time=t)
        self.wait(t)

        usdt_bar.clear_updaters()
        btc_bar.clear_updaters()

        self.add(scene1_7btc_fill_box)
        # usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
        #     Rectangle(height=4283 / 1000, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE).move_to(
        #         usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=7 / 10, width=1.2, fill_color=BTC, fill_opacity=1, color=BTC).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        origin_dot = curr_dot.copy()
        origin_dot.clear_updaters()
        origin_dot.set_color(GREEN)
        origin_dot.set_z_index(1.5)
        self.play(Create(origin_dot))
        self.wait(t)
        self.play(btc_tracker.animate.set_value(7),
                  usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
                  ReplacementTransform(scene1_7btc_fill_box, user_asset_btc),
                  ReplacementTransform(user_asset_usdt, scene1_1286usdt_fill_box), run_time=ttt)
        self.wait(t)

        scene1_arrow = CurvedArrow(origin_dot.get_center(), curr_dot.get_center(), radius=-4, tip_length=0.25).shift(
            RIGHT * 0.3 + UP * 0.3)
        scene1_arrow_label = Tex('Buy BTC in exchange of USDT').scale(0.3).next_to(scene1_arrow, UR)

        self.play(Create(scene1_arrow), run_time=t)
        self.wait(t)

        scene1_slippage_text = Tex(r'I used 1286 USDT \\to buy 3 BTC').scale(0.7).next_to(user_asset_pos, DOWN)
        scene1_slippage_form = MathTex(r'1286 \divisionsymbol 3').next_to(scene1_slippage_text, DOWN)
        scene1_slippage_result = MathTex(rf'{429}USDT \  per\ BTC ').scale(0.85).move_to(
            scene1_slippage_form.get_center())

        self.play(Create(scene1_slippage_form),
                  Create(scene1_slippage_text), run_time=t)
        self.wait(t)

        self.play(ReplacementTransform(scene1_slippage_form, scene1_slippage_result), run_time=t)

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

        self.play(Create(xyk), run_time=t)
        self.wait(t)
        self.play(Transform(xyk[ 4 ], num_30000), run_time=t)
        self.wait(t)

        self.play(Transform(xyk[ 0 ], num_10_minus_3), run_time=t)
        self.wait(t)
        self.play(Transform(xyk[ 0 ], num_7), run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(xyk, y_is), run_time=t)
        self.wait(t)
        self.play(Transform(y_is[ 2 ], num_4286), run_time=t)

        self.wait(t)
        self.play(Uncreate(y_is))

        ##### 우리는 이것을 프라이스 임팩트라고 부릅니다. 어 이거 중앙화거래소에서 봤던 슬리피지라 비슷하다고 생각되어
        ##### 슬리피지라는 것과 프라이스 임팩트란 단어가 쉽게 혼용되는 것을 볼 수 있ㅅ브니다
        ##### 잠시 차이점을 알아보고 가겠습니다
        # 프라이스 임팩트 텍스트 만들고
        # 아래 슬리피지 나오면서 낫 이꼴
        # 텍스트 둘다 사라짐

        px_impact_not_equal = MathTex(r'Price\  Imapact', r'\neq', 'Slippage').scale(2).arrange(D)
        self.play(Create(px_impact_not_equal), run_time=t)
        self.wait(t)
        self.play(Uncreate(px_impact_not_equal), run_time=t)
        self.wait(t)

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
        self.play(Create(slippage), run_time=t)
        self.wait(t)
        self.play(Create(curve_group), run_time=t)
        self.wait(t)
        self.play(Create(tech_problem),
                  Create(low_liq), run_time=t)
        self.wait(t)
        self.play(Uncreate(slippage), Uncreate(curve_group), Uncreate(tech_problem),
                  Uncreate(low_liq), run_time=t)
        self.wait(t)

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
        input_box_1_text = Tex('USDT').next_to(input_box_1_split, R, buff=0.25).move_to(
            np.array([input_box_1_drop.get_left()[0]-(input_box_1_drop.get_left()[0]-input_box_1_split.get_x())/2,input_box_1_split.get_y(),0]))
        input_box_1_amt = Tex('1286').scale(1.2).next_to(input_box_1_rect.get_left(), buff=0.75)
        input_box_1 = VGroup(input_box_1_rect, input_box_1_split, input_box_1_drop, input_box_1_text, input_box_1_amt)
        input_box_1_without_amd = VGroup(input_box_1_rect, input_box_1_split, input_box_1_drop, input_box_1_text)

        input_box_2_rect = RoundedRectangle(width=8, height=2)
        input_box_2_split = Line(UP * 0.4, D * 0.4).shift(R * 1.5)
        input_box_2_drop = Elbow().rotate(-3 * PI / 4).shift(R * 3.5)
        input_box_2_text = Tex('BTC').next_to(input_box_2_split, R, buff=0.25).move_to(
            np.array([input_box_2_drop.get_left()[0]-(input_box_2_drop.get_left()[0]-input_box_2_split.get_x())/2,input_box_2_split.get_y(),0]))
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
        self.wait(t)
        self.play(Create(input_box_1_amt), run_time=t)
        self.wait(t)
        self.play(Create(input_box_2_amt), run_time=t)
        self.wait(t)
        self.play(Transform(est_px, new_est_px),
                  Circumscribe(est_px), run_time=t)

        self.wait(t)
        self.play(Indicate(swap_button_text, color=GREY), run_time=t)
        self.wait(t)
        self.play(dex_elements.animate.to_edge(L), run_time=t)
        self.wait(t)

        ##### 슬리피지는 그렇게 내가 평균단가 468.75 달러에 구매할 것이라 예상하는데 거기서부터 갈라지는 것입니다
        ##### 3개를 받으려고 1283을 보냈는데 2.8개를 받았을 때 우리는 0.2비티씨의 슬리피지가 생겼다고 합니다다
        # 돌려받은게 3비티씨가 아니라 2.8비티씨임
        returned_btc_2 = Tex('We just got 2.7 BTC', r'Slippage of 11\%', 'A slippage cost of 0.3 BTC').scale(0.8).arrange(D).shift(
            R * 4 + U * 2.5)
        self.play(Create(returned_btc_2), run_time=t)
        self.wait(t)

        ##### 프라이스 임팩트는 428에 달러 빼기 300 즉 129 달러 혹은 보통은 퍼센트로 나타내기에
        ##### 428에 빼기 300 나누기 428에 곱하기 100 즉 36퍼센트가 됩니다
        ##### 그러나 슬리피지와 프라이스 임팩트를 엄밀하게 구분하지 않는 경우가 많기에 주의해야합니다
        # 여백에 프라이스 임팩트 이꼴 128빼기 300나누기 428 곱하기 100 적고 36퍼로 바뀜
        px_impact_text = Tex('Price Impact').shift(R * 4 + U * 0.5)
        px_impact_form = MathTex(r'\frac{429-300}{300}*100 = ', '0.43').shift(R * 4 + D * 0.5)
        px_impact_30perc = MathTex(r'43\%').move_to(px_impact_form[ 1 ]).to_edge(R).align_to(px_impact_form[ 1 ], L)
        self.play(Create(px_impact_text), run_time=t)
        self.wait(t)
        self.play(Create(px_impact_form), run_time=t)
        self.wait(t)
        self.play(Transform(px_impact_form[ 1 ], px_impact_30perc), run_time=t)
        self.wait(t)

        ##### 어쨋거나 명심할 것은 엑스와이는 케이모델에서 프라이스 임팩트가 없을 수는 없습니다
        ##### 프라이스 임팩트가 없으려면 그래프를 벗어나야되는데 거래라는 것이 풀의 상태를 변화시키는 것이고 그래프상에서 이동할 수밖에 없기 때문입니다
        # 그래프 하나 만들고 레이트 펑셩 데어앤백이지만 고무줄 팅기는 것 마냥 레이트 펑션하나 만들기

        coor_sys = Axes(x_range=[ 0, 10, 2 ], y_range=[ 0, 10, 2 ], x_length=2, y_length=2, tips=False,
                        y_axis_config={"include_numbers": False, 'include_tip': True, 'include_ticks': False, 'tip_width': 0.1,
                                       'tip_height': 5},
                        x_axis_config={"include_numbers": False, 'include_tip': True, 'include_ticks': False, 'tip_width': 0.1,
                                       'tip_height': 5}
                        ).next_to(px_impact_form, D)

        trader_graph = coor_sys.plot(lambda x: 5 / x, x_range=[ 5 / 8, 8 ], use_smoothing=False, color=WHITE)
        curr_dot = Dot(radius=0.1, color=RED).move_to(coor_sys.c2p(2, 2.5))

        self.play(Create(coor_sys),
                  Create(trader_graph),
                  Create(curr_dot), run_time=tt)
        self.wait(t)

        self.play(curr_dot.animate.shift(R * 0.5 + U * 0.5), rate_func=there_and_back_with_pause, run_time=t)
        self.wait(t)


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

        self.play(Create(liq_pool), run_time=t)
        self.wait(t)

        liq_provider = create_entity(Tex(r' \emph{Init Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", BTC, 1.4,
                                     0.3).next_to(liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", USDT, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)
        liq_provider.add(usdt_asset)

        self.play(Create(liq_provider), run_time=t)
        self.wait(t)

        ax = Axes(x_range=[ 0, 18, 4 ], y_range=[ 0, 6500, 1000 ], x_length=5, y_length=5, tips=True,
                  axis_config={"include_numbers": False, 'color': WHITE, 'include_ticks': False, 'font_size': 20}, ).to_edge(DR, buff=0.8)

        ax.shift(U * (liq_pool_rect.get_bottom()[ 1 ] - ax[ 0 ].get_y()))

        y_axis_label = ax.get_y_axis_label(MathTex('Amount of USDT in Pool', color=WHITE).rotate(PI / 2).scale(0.4), edge=LEFT,
                                           direction=LEFT, buff=0.37)
        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool', color=WHITE).scale(0.4), edge=DOWN, direction=DOWN, buff=0.37)
        axis_labels = VGroup(x_axis_label, y_axis_label)

        usdt_bar = Rectangle(height=3, width=1.2, fill_color=USDT, fill_opacity=1, color=USDT)
        btc_bar = Rectangle(height=1, width=1.2, fill_color=BTC, fill_opacity=1, color=BTC)
        bars = VGroup(btc_bar, usdt_bar)
        bars.arrange(RIGHT, aligned_edge=DOWN).move_to(liq_pool_rect).align_to(liq_pool_rect, DOWN)

        usdt_bar_pos = usdt_bar.get_bottom()
        btc_bar_pos = btc_bar.get_bottom()

        btc_var = Variable(10, MathTex("BTC"), var_type=Integer)
        usdt_var = Variable(3000, MathTex("USDT"), var_type=Integer).next_to(btc_var, DOWN, aligned_edge=LEFT)
        btc_tracker = btc_var.tracker
        usdt_tracker = usdt_var.tracker
        usdt_var[ 0 ][ 0 ].set_color(USDT)
        btc_var[ 0 ][ 0 ].set_color(BTC)

        vars = VGroup(btc_var, usdt_var).arrange(DOWN, aligned_edge=LEFT).next_to(liq_pool_rect, DOWN, buff=0.25)

        self.play(ReplacementTransform(usdt_asset, usdt_bar),
                  ReplacementTransform(btc_asset, btc_bar), run_time=t)
        self.wait(t)
        self.play(Write(usdt_var),
                  Write(btc_var), run_time=t)
        self.wait(t)
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=USDT, fill_opacity=1, color=USDT).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=BTC, fill_opacity=1, color=BTC).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        pool_price = Variable(100, 'Price', var_type=DecimalNumber, num_decimal_places=2).next_to(
            liq_pool_rect, RIGHT, buff=0.5).scale(0.8).to_edge(UP)
        pool_price_tracker = pool_price.tracker
        pool_price.add_updater(lambda v: pool_price_tracker.set_value(usdt_tracker.get_value() / btc_tracker.get_value()))
        pool_price_unit = Tex(r'USDT').scale(0.75).next_to(pool_price, buff=0.1)
        self.play(Write(k_var[ 0 ]))
        self.wait(t)
        self.play(Create(ax),
                  Create(axis_labels),
                  Create(pool_price_unit),
                  Create(pool_price),
                  TransformMatchingShapes(Group(btc_var[ 1 ].copy(), usdt_var[ 1 ].copy()), k_var[ 1 ].copy()),
                  Create(xyk_fraction.next_to(k_var, LEFT, buff=1)), run_time=tt
                  )
        self.wait(t)

        lp_amt_form_1 = MathTex(r'Init\  l =\sqrt{x \times y}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_2 = MathTex(r'Init\  l =\sqrt{10 \times 3000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_3 = MathTex(r'Init\  l =\sqrt{30000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_int = Tex(rf'{int(30000 ** (1 / 2))} LP token').move_to(lp_amt_form_1).scale(0.7)

        self.play(Create(lp_amt_form_1), run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(lp_amt_form_1, lp_amt_form_2), run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(lp_amt_form_2, lp_amt_form_3), run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(lp_amt_form_3, lp_amt_int), run_time=t)
        self.wait(t)

        box = Rectangle(width=1.6, height=1, fill_color=WHITE, stroke_color=WHITE, fill_opacity=1)
        text = Tex(r"173\\BTC-USDT\\LP", color=BLACK).scale(0.5)
        lp_asset = VGroup(box, text).next_to(liq_provider[ 0 ], DOWN, buff=0.1)

        self.play(Create(lp_asset),
                  Uncreate(lp_amt_int), run_time=t)
        self.wait(t)

        self.play(FadeOut(liq_provider),
                  FadeOut(lp_amt_int),
                  FadeOut(lp_asset), run_time=t)
        self.wait(t)

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
        x_marker = Triangle(color=BTC, fill_color=BTC, fill_opacity=1).scale(0.1).next_to(vertical_line, DOWN, buff=0)
        x_marker.add_updater(lambda marker: marker.next_to(vertical_line, DOWN, buff=0))
        x_marker_val = Integer(btc_tracker.get_value())
        x_marker_val.add_updater(
            lambda integer: integer.become(Integer(btc_tracker.get_value()).scale(0.4).next_to(vertical_line, DOWN, buff=0.3)))

        y_marker = Triangle(color=USDT, fill_color=USDT, fill_opacity=1).scale(0.1).rotate(-PI / 2).next_to(horizontal_line, LEFT, buff=0)
        y_marker.add_updater(lambda marker: marker.next_to(horizontal_line, LEFT, buff=0))
        y_marker_val = Integer(usdt_tracker.get_value())
        y_marker_val.add_updater(lambda integer: integer.become(
            Integer(usdt_tracker.get_value()).scale(0.4).rotate(PI / 2).next_to(horizontal_line, LEFT, buff=0.3)))

        lines = VGroup(vertical_line, horizontal_line)
        markers = VGroup(x_marker, x_marker_val, y_marker, y_marker_val)

        self.play(Create(xyk_graph_btc), run_time=t)
        self.wait(t)

        self.play(Create(curr_dot), run_time=t)
        self.wait(t)

        self.play(Create(lines), run_time=t)
        self.play(Create(markers), run_time=t)
        self.wait(t)

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

        self.play(Create(area), run_time=t)
        self.play(Create(area_text), run_time=t)
        self.wait(t)

        ##### DIVERGE
        #####
        user = create_entity(Tex(r' \emph{Trader}', color=BLACK), 1, WHITE, "3BTC", BTC, 1.4, 0.3).next_to(liq_pool_rect,
                                                                                                              RIGHT, buff=1.5)
        user_asset_btc = user[ 1 ]
        user_asset_pos = user_asset_btc.get_center()
        user_asset_usdt = create_entity("A", 0.5, WHITE, "692USDT", USDT, 1.4, 0.3)[ 1 ].move_to(user_asset_pos)

        user_line = Tex(r"I want to sell 3 BTC\\I don't have some USDT").scale(0.5).next_to(user, DOWN)

        self.play(Create(user), run_time=t)
        self.wait(t)
        self.play(Create(user_line), run_time=t)
        self.wait(t)
        self.play(Uncreate(user_line), run_time=t)
        self.wait(t)

        # self.add(index_labels(btc_bar))###

        # scene2_btc_dashed_box = Rectangle(color=RED).align_to(btc_bar[0],UL,alignment_vect=btc_bar[0].get_edge_center(UP))
        scene2_2308usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.2307, stroke_width=3,
                                        stroke_color=RED_E).align_to(
            usdt_bar, UL)
        scene2_13btc_box = Rectangle(width=btc_bar.width, height=btc_bar.height * 0.3, stroke_width=3,
                                     stroke_color=GREEN_E).next_to(btc_bar, UP, buff=0)

        scene2_2308usdt_fill_box = scene2_2308usdt_box.copy().set_fill(USDT, opacity=1)
        scene2_13btc_fill_box = scene2_13btc_box.copy().set_fill(BTC, opacity=1)

        scene2_2308usdt_fill_box.set_stroke(width=0, opacity=0)
        scene2_13btc_fill_box.set_stroke(width=0, opacity=0)

        scene2_2308usdt_fill_box.set_z_index(3)
        scene2_13btc_fill_box.set_z_index(3)

        self.play(Create(scene2_2308usdt_box), run_time=t)
        self.wait(t)

        self.play(Create(scene2_13btc_box), run_time=t)
        self.wait(t)

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
                  Create(scene2_brace_labels), run_time=t)
        self.wait(t)

        usdt_bar.clear_updaters()
        btc_bar.clear_updaters()

        self.add(scene2_2308usdt_fill_box)
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=2307 / 1000, width=1.2, fill_color=USDT, fill_opacity=1, color=USDT).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        # btc_bar.add_updater(lambda btc_bar: btc_bar.become(
        #     Rectangle(height=13 / 10, width=1.2, fill_color=BTC, fill_opacity=1, color=BTC).move_to(
        #         btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        origin_dot = curr_dot.copy()
        origin_dot.clear_updaters()
        origin_dot.set_color(RED)
        origin_dot.set_z_index(1.5)

        self.play(Create(origin_dot))
        self.wait(t)
        self.play(btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)),
                  Transform(scene2_2308usdt_fill_box, user_asset_usdt),
                  Transform(user_asset_btc, scene2_13btc_fill_box), run_time=ttt)
        self.wait(t)

        scene2_arrow = CurvedArrow(origin_dot.get_center(), curr_dot.get_center(), radius=4, tip_length=0.25).shift(
            RIGHT * 0.3 + UP * 0.3)
        scene2_arrow_label = Tex('Buy BTC in exchange of USDT').scale(0.3).next_to(scene2_arrow, UR)

        self.play(Create(scene2_arrow))
        self.wait(t)

        scene2_slippage_text = Tex(r'I sold 3 BTC \\and got 692 USDT').scale(0.7).next_to(user_asset_pos, DOWN)
        scene2_slippage_form = MathTex(r'692 \divisionsymbol 3').next_to(scene2_slippage_text, DOWN)
        scene2_slippage_result = MathTex(
            rf'{int(-(k_tracker.get_value() / btc_tracker.get_value() - 3000) / 3)}USDT \  per\ BTC ').scale(0.85).move_to(
            scene2_slippage_form.get_center())

        self.play(Create(scene2_slippage_form),
                  Create(scene2_slippage_text), run_time=t)
        self.wait(t)

        self.play(ReplacementTransform(scene2_slippage_form, scene2_slippage_result), run_time=t)

        self.wait(2)


class L_02_S_11_fees(Scene):
    def construct(self):
        dot = LabeledDot('Fuck')
        ##### 다음으로 넘어가기 전에 수수료예 대해 알아보겠스빈다.
        # fee 제목 만들기
        fees = Tex('Fees').scale(2)

        self.play(Create(fees))
        self.wait(t)
        self.play(Uncreate(fees))
        self.wait(t)

        ##### 덱스에서 수수료는 독특한 방식으로 작동합니다.
        ##### 거래를 하기 위해 코인을 풀로 보내면 코인이 풀에 도착하기 전에 수수료를 떼고
        ##### 남은 금액만 풀에 들어가서 그거에 맞게 거래가 일어납니다. 그리고 거래가 종료되면 풀에 그냥 수수료를 추가합니다.
        ##### 수수료는 거래가 발생할 때마다 풀에 쌓이기 때문에 매번 거래가 종료되면 케이값은 증가합니다
        # 풀박스 만들고 코인덩어리까지 세팅 이전 거 활용
        # 코인이들어가다 멈추고 분리됨
        # 수수료는 따로 빠져서 가만히 있고 거래완료 그리고 풀로 수수료가 들어감

        pool_rect = RoundedRectangle(width=7, height=4, corner_radius=0.5)
        pool_rect_text = Tex('BTC/USDT Pool').next_to(pool_rect, U)
        self.play(Create(pool_rect_text),
                  Create(pool_rect), run_time=t)
        self.wait(t)

        btc_lump = LabeledDot('BTC', radius=1, color=BTC).shift(L * 1.5)
        usdt_lump = LabeledDot('USDT', radius=1, color=USDT).shift(R * 1.5)
        # btc_lump.save_state()
        # usdt_lump.save_state()
        # btc_lump_arc = Arc(radius=2, angle=PI).flip(axis=np.array([ 0, 1, 0 ])).shift(L * 3.5)
        # usdt_lump_arc = Arc(radius=2, angle=PI).shift(R * 3.5)

        self.play(Create(btc_lump),
                  Create(usdt_lump), run_time=t)
        self.wait(t)

        btc_lump_inflow = LabeledDot('BTC', radius=1, color=BTC).shift(R * 5.5)

        self.play(Create(btc_lump_inflow), run_time=t)
        self.wait(t)
        self.play(btc_lump_inflow.animate.next_to(pool_rect, buff=1), run_time=t)
        self.wait(t)

        btc_lump_fee = LabeledDot(MathTex('Fee', font_size=20, color=BLACK), radius=0.3, color=BTC).move_to(btc_lump_inflow)
        btc_lump_fee.set_z_index(-1)

        self.play(btc_lump_inflow.animate.scale(0.8),
                  btc_lump_fee.animate.shift(D * 2), run_time=t)
        self.wait(t)

        self.play(FadeOut(btc_lump_inflow, target_position=btc_lump),
                  btc_lump.animate.scale(1.1), run_time=t)
        self.wait(t)
        # self.play(btc_lump.animate.scale(1.1))

        usdt_lump_outflow = LabeledDot('USDT', radius=1, color=USDT).shift(R * 5.5)
        self.play(FadeIn(usdt_lump_outflow, target_position=usdt_lump),
                  usdt_lump.animate.scale(1 / 1.1), run_time=t)
        self.wait(t)

        self.play(FadeOut(btc_lump_fee, target_position=btc_lump),
                  btc_lump.animate.scale(1.05), run_time=t)
        self.wait(t)
        self.play(FadeOut(usdt_lump_outflow, shift=R), run_time=t)
        self.wait(t)

        k_increase = Tex('K increased a bit', 'after every trade').arrange(D).next_to(pool_rect, D)

        self.play(Create(k_increase), run_time=t)
        self.wait(t)
        self.play(VGroup(pool_rect, pool_rect_text, btc_lump, usdt_lump, k_increase).animate.to_edge(L), run_time=t)
        self.wait(t)

        ##### 중앙화 거래소에서는 거래소가 가져가니 우리의 수수료가 가격에 영향을 줄 일은 없었습니다
        ##### 그러나 덱스에서는 수수료가 풀 내부의 비트 테더 비율을 조금씩 바꾸기 때문에 우리가 생각한 것과 미세하게 가격이 차이가 납니다
        ##### 수수료가 1퍼인 상황을 생각해 보겠ㅅ빈다
        ##### 비트 10개 3000테더가 있는 풀에 1비트를 보내면 수수료를 뗀 0.99비트가 전송됩니다
        ##### 그리고 0.99에 대한 교환이 일어나고 풀에서 3000-30000분에 10.99테더가 빠져나가고 30000나누기 10.99인 2729테더가 남습니다
        ##### 지금까지는 케이는 여전히 30000입니다
        ##### 그뒤에 풀에 빼놨던 수수료인 0.01비트를 넣습니다. 풀에는 이제 11비트와 2729테더가 남아있습니다
        ##### 케이는 30027.297로 약간 증가했습니다 현재 비트의 가격은 248.159테더입니다
        # 오른쪽은 수수료 있는 경우 위에 타이틀 달아주고
        # 케이 바리어블 비티씨바리어블 테더 바리어블 가격 바리어블 다 만들어줌
        fee_situation = Tex(r'1\% Fee').shift(R * 4 + U * 3)

        k_var_fee = Variable(30000, 'k', var_type=Integer)
        btc_var_fee = Variable(10.00, 'BTC')
        usdt_var_fee = Variable(3000.00, 'USDT')
        price_var_fee = Variable(300.00, 'Price')

        k_tracker_fee = k_var_fee.tracker
        btc_tracker_fee = btc_var_fee.tracker
        usdt_tracker_fee = usdt_var_fee.tracker
        price_tracker_fee = price_var_fee.tracker
        price_unit = Tex(r'USDT', color=WHITE).next_to(price_var_fee, buff=0.1)
        price_unit.add_updater(lambda unit: unit.next_to(price_var_fee, R, buff=0.1))
        # price_var_fee.add(price_unit)
        price_var_fee.add_updater(lambda v: price_tracker_fee.set_value(usdt_tracker_fee.get_value() / btc_tracker_fee.get_value()))

        VGroup(k_var_fee, btc_var_fee, usdt_var_fee, price_var_fee).arrange(D, aligned_edge=L).shift(R * 3.5, U * 1)

        self.play(Create(fee_situation))
        self.wait(t)
        self.play(Create(VGroup(k_var_fee, btc_var_fee, usdt_var_fee, price_var_fee, price_unit)))
        self.wait(2)

        self.play(btc_tracker_fee.animate.set_value(10.99),
                  usdt_tracker_fee.animate.set_value(30000 / 10.99), run_time=5)
        self.wait(2)

        self.play(btc_tracker_fee.animate.set_value(11))
        self.wait(2)

        self.play(k_tracker_fee.animate.set_value(11 * (30000 / 10.99)), run_time=5)
        self.wait(2)

        # self.play(btc_tracker_fee.animate.set_value(10.99))

        ##### 원래 1비트를 매도했다고 생각하면 가격은 30000나누기 11나누기 11인 247.933테더가 되어야합니다
        ##### 그러나 수수료가 있었다면 30000나누기 10.99 나누기 11인 248.159 테더가 됩니다.
        ##### 즉 이전 거래자의 행동에 따라서 미세하게 이익이 바뀝니다.
        # 윈쪽에 수수료가 없는 겨웅 타이틀 달고
        # 케이 바리어블 비티씨바리어블 테더 바리어블 가격 바리어블 다 만들어줌
        if_fee = Tex(r'If it were 11 BTC,', 'it would be 247.93 USDT').arrange(D).next_to(price_var_fee, D, buff=1).align_to(price_var_fee,
                                                                                                                            L)
        self.play(Create(if_fee))
        self.wait(t)

        ##### 비트를 매도하는 행위에서 수수료가 있던 경우가 가격이 덜 떨어졌으므로
        ##### 같은 방향 즉 이후에 매도할 사람은 원래 앞사람이 거래하고 247테더를 생각하고 있었으나
        ##### 예상보다 돈을 좀 더 건질 수 있게 됐습니다
        ##### 반대로 앞사람과 반대방향 즉 매수를 하려던 사람은 자신이 앞사람을 보고 생각하던 247달러보다
        ##### 높은 248테더에 매수를 해야해서 예상보다 지출이 늘었습니다
        #


class L_02_S_12_amm_xyk_various_cases_5(Scene):
    def construct(self):
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

        # 케이 바리어블, 초기 엘피, 좌표계
        xyk_fraction = MathTex('y', '=', r'\frac{k}{x}').to_edge(UL)

        liq_pool_rect = RoundedRectangle(height=6.3, width=4, corner_radius=0.5)
        liq_pool_text = Tex('Liquidity Pool').next_to(liq_pool_rect, UP)
        liq_pool = VGroup(liq_pool_rect, liq_pool_text).to_edge(UL).shift(R * 0.5)
        liq_pool.set_z_index(3)

        k_var = Variable(30000, MathTex("k"), var_type=Integer).to_edge(UR)
        k_tracker = k_var.tracker
        k_tracker.set_value(30000)

        self.play(Create(liq_pool), run_time=t)
        self.wait(t)

        liq_provider = create_entity(Tex(r' \emph{Init Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", BTC, 1.4,
                                     0.3).next_to(liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", USDT, 1.4, 0.3)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)
        liq_provider.add(usdt_asset)

        self.play(Create(liq_provider), run_time=t)
        self.wait(t)

        ax = Axes(x_range=[ 0, 18, 4 ], y_range=[ 0, 6500, 1000 ], x_length=5, y_length=5, tips=True,
                  axis_config={"include_numbers": False, 'color': WHITE, 'include_ticks': False, 'font_size': 20}, ).to_edge(DR, buff=0.8)

        ax.shift(U * (liq_pool_rect.get_bottom()[ 1 ] - ax[ 0 ].get_y()))

        y_axis_label = ax.get_y_axis_label(MathTex('Amount of USDT in Pool', color=WHITE).rotate(PI / 2).scale(0.4), edge=LEFT,
                                           direction=LEFT, buff=0.37)
        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool', color=WHITE).scale(0.4), edge=DOWN, direction=DOWN, buff=0.37)
        axis_labels = VGroup(x_axis_label, y_axis_label)

        usdt_bar = Rectangle(height=3, width=1.2, fill_color=USDT, fill_opacity=1, color=USDT)
        btc_bar = Rectangle(height=1, width=1.2, fill_color=BTC, fill_opacity=1, color=BTC)
        bars = VGroup(btc_bar, usdt_bar)
        bars.arrange(RIGHT, aligned_edge=DOWN).move_to(liq_pool_rect).align_to(liq_pool_rect, DOWN)

        usdt_bar_pos = usdt_bar.get_bottom()
        btc_bar_pos = btc_bar.get_bottom()

        btc_var = Variable(10, MathTex("BTC"), var_type=Integer)
        usdt_var = Variable(3000, MathTex("USDT"), var_type=Integer).next_to(btc_var, DOWN, aligned_edge=LEFT)
        btc_tracker = btc_var.tracker
        usdt_tracker = usdt_var.tracker
        usdt_var[ 0 ][ 0 ].set_color(USDT)
        btc_var[ 0 ][ 0 ].set_color(BTC)

        vars = VGroup(btc_var, usdt_var).arrange(DOWN, aligned_edge=LEFT).next_to(liq_pool_rect, DOWN, buff=0.25)

        self.play(ReplacementTransform(usdt_asset, usdt_bar),
                  ReplacementTransform(btc_asset, btc_bar), run_time=t)
        self.wait(t)
        self.play(Write(usdt_var),
                  Write(btc_var), run_time=t)
        self.wait(t)
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=USDT, fill_opacity=1, color=USDT).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=BTC, fill_opacity=1, color=BTC).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        pool_price = Variable(100, 'Price', var_type=DecimalNumber, num_decimal_places=2).next_to(
            liq_pool_rect, RIGHT, buff=0.5).scale(0.8).to_edge(UP)
        pool_price_tracker = pool_price.tracker
        pool_price.add_updater(lambda v: pool_price_tracker.set_value(usdt_tracker.get_value() / btc_tracker.get_value()))
        pool_price_unit = Tex(r'USDT').scale(0.75).next_to(pool_price, buff=0.1)
        self.play(Write(k_var[ 0 ]))
        self.wait(t)
        self.play(Create(ax),
                  Create(axis_labels),
                  Create(pool_price_unit),
                  Create(pool_price),
                  TransformMatchingShapes(Group(btc_var[ 1 ].copy(), usdt_var[ 1 ].copy()), k_var[ 1 ].copy()),
                  Create(xyk_fraction.next_to(k_var, LEFT, buff=1)), run_time=tt
                  )
        self.wait(t)

        lp_amt_form_1 = MathTex(r'Init\  l =\sqrt{x \times y}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_2 = MathTex(r'Init\  l =\sqrt{10 \times 3000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_3 = MathTex(r'Init\  l =\sqrt{30000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_int = Tex(rf'{int(30000 ** (1 / 2))} LP token').move_to(lp_amt_form_1).scale(0.7)

        self.play(Create(lp_amt_form_1), run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(lp_amt_form_1, lp_amt_form_2), run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(lp_amt_form_2, lp_amt_form_3), run_time=t)
        self.wait(t)
        self.play(TransformMatchingShapes(lp_amt_form_3, lp_amt_int), run_time=t)
        self.wait(t)

        box = Rectangle(width=1.6, height=1, fill_color=WHITE, stroke_color=WHITE, fill_opacity=1)
        text = Tex(r"173\\BTC-USDT\\LP", color=BLACK).scale(0.5)
        lp_asset = VGroup(box, text).next_to(liq_provider[ 0 ], DOWN, buff=0.1)

        self.play(Create(lp_asset),
                  Uncreate(lp_amt_int), run_time=t)
        self.wait(t)

        self.play(FadeOut(liq_provider),
                  FadeOut(lp_amt_int),
                  FadeOut(lp_asset), run_time=t)
        self.wait(t)

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
        x_marker = Triangle(color=BTC, fill_color=BTC, fill_opacity=1).scale(0.1).next_to(vertical_line, DOWN, buff=0)
        x_marker.add_updater(lambda marker: marker.next_to(vertical_line, DOWN, buff=0))
        x_marker_val = Integer(btc_tracker.get_value())
        x_marker_val.add_updater(
            lambda integer: integer.become(Integer(btc_tracker.get_value()).scale(0.4).next_to(vertical_line, DOWN, buff=0.3)))

        y_marker = Triangle(color=USDT, fill_color=USDT, fill_opacity=1).scale(0.1).rotate(-PI / 2).next_to(horizontal_line, LEFT, buff=0)
        y_marker.add_updater(lambda marker: marker.next_to(horizontal_line, LEFT, buff=0))
        y_marker_val = Integer(usdt_tracker.get_value())
        y_marker_val.add_updater(lambda integer: integer.become(
            Integer(usdt_tracker.get_value()).scale(0.4).rotate(PI / 2).next_to(horizontal_line, LEFT, buff=0.3)))

        lines = VGroup(vertical_line, horizontal_line)
        markers = VGroup(x_marker, x_marker_val, y_marker, y_marker_val)

        self.play(Create(xyk_graph_btc), run_time=t)
        self.wait(t)

        self.play(Create(curr_dot), run_time=t)
        self.wait(t)

        self.play(Create(lines), run_time=t)
        self.play(Create(markers), run_time=t)
        self.wait(t)

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

        self.play(Create(area), run_time=t)
        self.play(Create(area_text), run_time=t)
        self.wait(t)

        ##### DIVERGE############################################################################################################

        k_org_px_org_dot = curr_dot.copy().clear_updaters().set_color(GREY).set_z_index(1.5).scale(1.2)
        self.play(Create(k_org_px_org_dot))

        # 가격 상승#####################################################################################
        px_up = MathTex(r'Price \  \Uparrow').move_to(liq_provider[ 0 ])
        self.play(Write(px_up))

        self.play(
            btc_tracker.animate.set_value(7),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
            run_time=5, rate_func=rate_functions.ease_in_out_quint)

        # 가격이 올라간다는 건 btc가 usdt보다 상대적으로 인기가 많아진다는 것입니다.

        self.wait(2)
        self.play(Unwrite(px_up))
        self.wait(2)

        k_org_px_up_dot = curr_dot.copy().clear_updaters().set_color(GREEN_C).set_z_index(1.5)
        self.add(k_org_px_up_dot)

        # 가격 하락#####################################################################################
        px_dn = MathTex(r'Price \  \Downarrow').move_to(liq_provider[ 0 ])
        self.play(Write(px_dn))

        self.play(
            btc_tracker.animate.set_value(13),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)),
            run_time=5, rate_func=rate_functions.ease_in_out_quint)

        # 가격이 내려간다는 건 btc가 usdt보다 상대적으로 인기가 없어진다는 것

        self.wait(2)
        self.play(Unwrite(px_dn))
        self.wait(2)

        k_org_px_dn_dot = curr_dot.copy().clear_updaters().set_color(RED_C).set_z_index(1.5)
        self.add(k_org_px_dn_dot)

        # 원점#####################################################################################
        k_origin_px_origin = MathTex(r'ORIGIN').move_to(liq_provider[ 0 ])
        self.play(Write(k_origin_px_origin))

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=2, rate_func=rate_functions.ease_in_out_quint)

        self.wait(2)
        self.play(Unwrite(k_origin_px_origin))
        self.wait(2)

        # K 하락#####################################################################################
        k_dn = MathTex(r'K \  \Downarrow').move_to(liq_provider[ 0 ])
        self.play(Write(k_dn))

        self.play(k_tracker.animate.set_value(14700),
                  btc_tracker.animate.set_value(7),
                  usdt_tracker.animate.set_value(14700 / 7),
                  run_time=5, rate_func=rate_functions.ease_in_out_quint)

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
        self.play(Unwrite(k_dn))
        self.wait(2)

        k_dn_px_org_dot = curr_dot.copy().clear_updaters().set_color(WHITE).set_z_index(1.5)
        self.add(k_dn_px_org_dot)

        # K 상승#####################################################################################
        k_up = MathTex(r'K \  \Uparrow').move_to(liq_provider[ 0 ])
        self.play(Write(k_up))

        self.play(k_tracker.animate.set_value(50700),
                  btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(50700 / 13),
                  run_time=5, rate_func=rate_functions.ease_in_out_quint)

        # 케이가 상승한다는 건 풀에 누군가 추가 유동성을 공급하는 것입니다.
        # 마찬가지로 가격은 전혀 움직이지 않음
        # 현재 가격에 맞게 비티씨와 유에스디티를 그대로 추가함
        # 풀사이즈는 커짐

        self.wait(2)
        self.play(Unwrite(k_up))
        self.wait(2)

        k_up_px_org_dot = curr_dot.copy().clear_updaters().set_color(DARK_GREY).set_z_index(1.5)
        self.add(k_up_px_org_dot)

        # K 원점#####################################################################################
        k_origin = MathTex(r'ORIGIN').move_to(liq_provider[ 0 ])
        self.play(Write(k_origin))

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=2, rate_func=rate_functions.ease_in_out_quint)

        self.wait(2)
        self.play(Unwrite(k_origin))
        self.wait(2)

        # K 상승#####################################################################################
        ##### 케이상승 후 가격상승 및 하락
        ##### 케이가 상승했다는 것은 유동성이 풍부해졌다는 것이고 이전과 같은 양의 비티씨를 거래하더라도 프라이스 임팩트가 적어집니다
        ##### 아까 300달러에서 3개를 매도할 때는 프라이스 임팩트가 얼마 발생
        ##### 지금은 유동성으 풍부하고 3개 매도할 때 프라이스 임팩트가 얼마 발생
        ##### 같은 3비티씨지만 풀에서 차지하는 비율이 적어졌다
        ##### 아까는 10분에 3 지금은 13분에 3
        ##### 퍼센트로 따지면 33퍼와 23퍼센트
        k_up_px_dn = MathTex(r'K \  \Uparrow', r'Price\  \Downarrow').arrange(D).move_to(liq_provider[ 0 ])
        k_up_px_up = MathTex(r'K \  \Uparrow', r'Price\  \Uparrow').arrange(D).move_to(liq_provider[ 0 ])
        self.play(Write(k_up_px_dn[ 0 ]))

        self.play(k_tracker.animate.set_value(50700),
                  btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(50700 / 13),
                  run_time=2, rate_func=rate_functions.ease_in_out_quint)

        self.wait(2)

        # K 상승 가격 하락#####################################################################################
        ##### 케이상승 후 가격상승 및 하락
        ##### 케이가 상승했다는 것은 유동성이 풍부해졌다는 것이고 이전과 같은 양의 비티씨를 거래하더라도 프라이스 임팩트가 적어집니다
        ##### 아까 300달러에서 3개를 매도할 때는 프라이스 임팩트가 얼마 발생
        ##### 지금은 유동성으 풍부하고 3개 매도할 때 프라이스 임팩트가 얼마 발생
        ##### 같은 3비티씨지만 풀에서 차지하는 비율이 적어졌다
        ##### 아까는 10분에 3 지금은 13분에 3
        ##### 퍼센트로 따지면 33퍼와 23퍼센트
        #####
        self.play(Write(k_up_px_dn[ 1 ]))

        self.play(
            btc_tracker.animate.set_value(16),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(16)),
            run_time=5, rate_func=rate_functions.ease_in_out_quint)

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
        self.play(Unwrite(k_up_px_dn[ 1 ]))
        self.wait(2)

        k_up_px_dn_dot = curr_dot.copy().clear_updaters().set_color(C0193).set_z_index(1.5)
        self.add(k_up_px_dn_dot)

        # K 상승 가격 상승#####################################################################################
        self.play(Write(k_up_px_up[ 1 ]))

        self.play(
            btc_tracker.animate.set_value(10),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(10)),
            run_time=5, rate_func=rate_functions.ease_in_out_quint)

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
        self.play(Unwrite(k_up_px_up[ 1 ]), Unwrite(k_up_px_dn[ 0 ]))
        self.wait(2)

        k_up_px_up_dot = curr_dot.copy().clear_updaters().set_color(C1193).set_z_index(1.5)
        self.add(k_up_px_up_dot)

        # K 원점#####################################################################################
        k_origin_px_origin = MathTex(r'ORIGIN').move_to(liq_provider[ 0 ])
        self.play(Write(k_origin_px_origin))

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=2, rate_func=rate_functions.ease_in_out_quint)

        self.wait(2)
        self.play(Unwrite(k_origin_px_origin))
        self.wait(2)

        # K 하락#####################################################################################
        k_dn_px_dn = MathTex(r'K\  \Downarrow', r'Price \  \Downarrow').arrange(D).move_to(liq_provider[ 0 ])
        k_dn_px_up = MathTex(r'K\  \Downarrow', r'Price \  \Uparrow').arrange(D).move_to(liq_provider[ 0 ])
        self.play(Write(k_dn_px_dn[ 0 ]))

        self.play(k_tracker.animate.set_value(14700),
                  btc_tracker.animate.set_value(7),
                  usdt_tracker.animate.set_value(14700 / 7),
                  run_time=2, rate_func=rate_functions.ease_in_out_quint)

        # 그말은 유동성이 줄었다는 거하고
        # 아까 유동성이 늘었서 슬리피지가 덜 발행하던 것과 달리
        # 지금부터는 슬리피지가 더 발생합니다
        #

        self.wait(2)
        # 역으로 케이가 하락했는데

        # K 하락 가격 하락#####################################################################################
        #####
        ##### 케이하락 후 가격상승 및 하락
        ##### 케이가 하락했다는 것은 유동성이 줄었다는 것이고 이전과 같은 양의 비티씨를 거래하더라도 프라이스 임팩트가 커집니다
        ##### 아까 300달러에서 3개를 매도할 때는 프라이스 임팩트가 얼마 발생
        ##### 지금은 유동성으 풍부하고 3개 매도할 때 프라이스 임팩트가 얼마 발생
        ##### 같은 3비티씨지만 풀에서 차지하는 비율이 적어졌다
        ##### 아까는 10분에 3 지금은 7 분에 3
        ##### 퍼센트로 따지면 33퍼와 42퍼센트
        #####
        self.play(Write(k_dn_px_dn[ 1 ]))

        self.play(
            btc_tracker.animate.set_value(10),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(10)),
            run_time=5, rate_func=rate_functions.ease_in_out_quint)

        # 케이가 하락한 상태에서 누군가 풀에다 비티씨를 매도해서
        # 가격도 하락합니다
        # 비티씨를 매도하는데 아까와 같이 300달러에서 매도하지만
        # 아까는 슬리피지 얼마
        # 지금은 얼마입니다
        # 당연히 아까는 10개에서 3개를 넣는 거였고
        # 지금은 5개에서 3개를 넣는거니까
        # 비율은 30퍼와 60퍼로
        # 완전 차이나게 된다

        self.wait(2)
        self.play(Unwrite(k_dn_px_dn[ 1 ]))
        self.wait(2)

        k_dn_px_dn_dot = curr_dot.copy().clear_updaters().set_color(RED_A).set_z_index(1.5)
        self.add(k_dn_px_dn_dot)

        # K 하락 가격 상승#####################################################################################
        self.play(Write(k_dn_px_up[ 1 ]))

        self.play(
            btc_tracker.animate.set_value(4),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(4)),
            # area_text.animate.rotate(PI / 2),
            run_time=5, rate_func=rate_functions.ease_in_out_quint)

        # 케이가 하락한 상태에서 누군가 풀에서 비티씨를 빼가면서 즉 매수하면서
        # 가격도 상승합니다
        # 비티씨를 매수하는데 아까와 같이 300달러ㅓ에서 매수하지만
        # 아까는 슬리피지 얼마
        # 지금은 얼마
        # 당연히 아까는 10개에서 3개를 빼는 거였고
        # 지금은 5개에서 3개를 빼는 것
        # 비율은 30퍼와 60퍼로 상당히 차이난다

        self.wait(2)
        self.play(Unwrite(k_dn_px_up[ 1 ]),
                  Unwrite(k_dn_px_dn[ 0 ]))
        self.wait(2)

        k_dn_px_up_dot = curr_dot.copy().clear_updaters().set_color(GREEN_A).set_z_index(1.5)
        self.add(k_dn_px_up_dot)

        # 원점#####################################################################################
        k_origin_px_origin = MathTex(r'ORIGIN').move_to(liq_provider[ 0 ])
        self.play(Write(k_origin_px_origin))

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=2, rate_func=rate_functions.ease_in_out_quint)

        self.wait(2)
        self.play(Unwrite(k_origin_px_origin))
        self.wait(2)

        # 가격 상승#####################################################################################
        px_up_k_up = MathTex(r'Price \  \Uparrow', r'K\  \Uparrow').arrange(D).move_to(liq_provider[ 0 ])
        px_up_k_dn = MathTex(r'Price \  \Uparrow', r'K\  \Downarrow').arrange(D).move_to(liq_provider[ 0 ])
        self.play(Write(px_up_k_up[ 0 ]))

        self.play(
            btc_tracker.animate.set_value(7),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
            run_time=2, rate_func=rate_functions.ease_in_out_quint)

        self.wait(2)
        # 이제는 가격이 상승한 상태에서 k를 움직여보겟습니다

        # 가격 상승에서 K상승#####################################################################################
        ##### 가격상승 후 케이상승 및 하락
        ##### 아까와 달리 현재 가격은 이미 움직인 상태고 이 가격에 맞게 같은 가치를 넣어줘야합니다
        ##### 아까와 같이 2비티씨만큼 유동성을 공급하려고 하면 올라버린 가격에 맞게 테더를 넣어줘야합니다
        ##### 그래서 풀에서 같은 비중을 차지하기 위해서 더 많은 자금이 필요하게 됏ㅅ브니다
        ##### 만약 아까 넣은 2비티씨를 유동성을 빼려고 하면 현재 가격대로 돌려받게 됩니다
        self.play(Write(px_up_k_up[ 1 ]))

        self.play(k_tracker.animate.set_value(3000000 / 49),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000000 / 49 / 10),
                  run_time=5, rate_func=rate_functions.ease_in_out_quint)

        # 아까와는 상황이 다릅니다
        # 현재 가격은 이미 움직여버렸습니다
        # 현재가격은 이미 300에서 올라왔고 여기서
        # 유동성을 넣기 때문에
        # 같은 2비티씨를 유동성을 추가한다고 하면
        # 1비티씨마다 상응하는 올라간 가격의 테더를 같이 넣어줘야합니다
        #

        self.wait(2)
        self.play(Unwrite(px_up_k_up[ 1 ]))
        self.wait(2)

        px_up_k_up_dot = curr_dot.copy().clear_updaters().set_color(TEAL_E).set_z_index(1.5)
        self.add(px_up_k_up_dot)

        # 가격 상승에서 K하락#####################################################################################
        self.play(Write(px_up_k_dn[ 1 ]))

        self.play(k_tracker.animate.set_value(480000 / 49),
                  btc_tracker.animate.set_value(4),
                  usdt_tracker.animate.set_value(480000 / 49 / 4),
                  run_time=5, rate_func=rate_functions.ease_in_out_quint)

        # 가격이 올랐을 때 케이가 떨어진다는 건
        # 즉 유동성을 공급했던 사람이 유동성을 회수한다는 것은
        # 풀 사이즈가 작아진다는 것입니다
        # 그 말은 공급자가 1비티씨를 뺄 때 오른 가격만큼의 테더를 회수한다는 애기입니다
        # 2비티씨를 빼면 얼마가 빠집니다

        self.wait(2)
        self.play(Unwrite(px_up_k_dn[ 1 ]),
                  Uncreate(px_up_k_up[ 0 ]))
        self.wait(2)

        px_up_k_dn_dot = curr_dot.copy().clear_updaters().set_color(TEAL_A).set_z_index(1.5)
        self.add(px_up_k_dn_dot)

        # 원점점#####################################################################################

        k_origin_px_origin = MathTex(r'ORIGIN').move_to(liq_provider[ 0 ])
        self.play(Write(k_origin_px_origin))

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=2, rate_func=rate_functions.ease_in_out_quint)

        self.wait(2)
        self.play(Unwrite(k_origin_px_origin))
        self.wait(2)

        # 가격 하락#####################################################################################
        px_dn_k_up = MathTex(r'Price \  \Downarrow', r'K\  \Uparrow').arrange(D).move_to(liq_provider[ 0 ])
        px_dn_k_dn = MathTex(r'Price \  \Downarrow', r'K\  \Downarrow').arrange(D).move_to(liq_provider[ 0 ])

        # 가격이 하락한 상태에서 케이를 움직여보겟습니다
        self.play(Write(px_dn_k_up[ 0 ]))

        self.play(
            btc_tracker.animate.set_value(13),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)),
            run_time=2, rate_func=rate_functions.ease_in_out_quint)

        self.wait(2)
        self.play(Unwrite(px_dn))
        self.wait(2)

        # 가격 하락에서 K상승#####################################################################################

        #####
        ##### 가격하락 후 케이상승 및 하락
        ##### 아까와 달리 현재 가격은 이미 움직인 상태고 이 가격에 맞게 같은 가치를 넣어줘야합니다
        ##### 아까와 같이 2비티씨만큼 유동성을 공급하려고 하면 떨어진 가격에 맞게 테더를 넣어줘야합니다
        ##### 그래서 풀에서 같은 비중을 차지하기 위해서 더 적은 자금이 필요하게 됏습니다
        ##### 만약 아까 넣은 2비티씨를 유동성을 빼려고 하면 현재 가격대로 돌려받게 됩니다
        self.play(Write(px_dn_k_up[ 1 ]))

        self.play(k_tracker.animate.set_value(7680000 / 169),
                  btc_tracker.animate.set_value(16),
                  usdt_tracker.animate.set_value(7680000 / 169 / 16),
                  run_time=5, rate_func=rate_functions.ease_in_out_quint)

        # 가격이 하락한 상태에서 케이를 넣으렴녀 원래보다 돈이 적게 듭니다
        # 왜냐하면 비티씨 1개를 넣을 때 하락한 각겨만큼의 테더를 넣으면 됩니다

        self.wait(2)
        self.play(Unwrite(px_dn_k_up[ 1 ]))
        self.wait(2)

        px_dn_k_up_dot = curr_dot.copy().clear_updaters().set_color(MAROON_E).set_z_index(1.5)
        self.add(px_dn_k_up_dot)

        # 가격 하락에서 K하락#####################################################################################
        # px_dn_k_dn = MathTex(r'Price \  \Downarrow', r'K\  \Downarrow').arrange(D).move_to(liq_provider[ 0 ])
        self.play(Write(px_dn_k_dn[ 1 ]))

        self.play(k_tracker.animate.set_value(3000000 / 169),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000000 / 169 / 11),
                  run_time=5, rate_func=rate_functions.ease_in_out_quint)

        # 마찬가지로 하락한 상태에서 유동성을 제거하면
        # 비티씨 한 개를 뺄 때 떨어진 가격만큼의 테더만 되찾을 수 있습니다

        self.wait(2)
        self.play(Unwrite(px_dn_k_dn[ 1 ]),
                  Unwrite(px_dn_k_up[ 0 ]))
        self.wait(2)

        px_dn_k_dn_dot = curr_dot.copy().clear_updaters().set_color(MAROON_A).set_z_index(1.5)
        self.add(px_dn_k_dn_dot)

        # 가격 원점#####################################################################################
        px_origin = MathTex(r'ORIGIN').move_to(liq_provider[ 0 ])
        self.play(Write(px_origin))

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=2, rate_func=rate_functions.ease_in_out_quint)

        self.wait(2)
        self.play(Unwrite(px_origin))
        self.wait(2)

        # 라인 생성#####################################################################################

        ##### 각 케이스마다 눈에 잘 보이게 선으로 연결해봤습니다
        ##### 동영상을 다시 보면서 천천히 곱씹어보시면 더 이해가 잘 될겁니다

        def making_a_line_3points(p1, p2, p3, color):
            l1 = Line(p1.get_center(), p2.get_center(), color=color)
            l2 = Line(p2.get_center(), p3.get_center(), color=color)
            l1.set_z_index(-2)
            l2.set_z_index(-2)
            line = VGroup(l1, l2)

            return line

        self.play(Uncreate(area),
                  Uncreate(area_text))
        k_px_org_line = making_a_line_3points(k_dn_px_org_dot, k_org_px_org_dot, k_up_px_org_dot, DARK_GREY)
        self.wait(2)

        self.play(Create(k_px_org_line))
        k_px_up_line = making_a_line_3points(k_dn_px_up_dot, k_org_px_up_dot, k_up_px_up_dot, GREEN_E)
        self.wait(2)
        self.play(Create(k_px_up_line))
        k_px_dn_line = making_a_line_3points(k_dn_px_dn_dot, k_org_px_dn_dot, k_up_px_dn_dot, RED_E)
        self.wait(2)
        self.play(Create(k_px_dn_line))
        px_up_k_line = making_a_line_3points(px_up_k_dn_dot, k_org_px_up_dot, px_up_k_up_dot, TEAL_E)
        self.wait(2)
        self.play(Create(px_up_k_line))
        px_dn_k_line = making_a_line_3points(px_dn_k_dn_dot, k_org_px_dn_dot, px_dn_k_up_dot, MAROON_E)
        self.wait(2)
        self.play(Create(px_dn_k_line))

        self.wait(2)


class L_02_S_13_why_the_word_swap(Scene):
    def construct(self):
        pass


class L_02_S_14_arbitrage(Scene):
    def construct(self):
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
        self.wait(t)

        self.play(Uncreate(arb))
        self.wait(t)

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
        dex_1_px_unit = Tex(r'USDT').next_to(dex_1_px, R)
        dex_1_px.add(dex_1_px_unit).scale(0.65).move_to(dex_1_rect)

        dex_2_px = Variable(470, 'BTC', var_type=Integer)
        dex_2_px_tracker = dex_2_px.tracker
        dex_2_px_unit = Tex(r'USDT').next_to(dex_2_px, R,buff=0.1)
        dex_2_px.add(dex_2_px_unit).scale(0.65).move_to(dex_2_rect)

        self.play(Create(dex_1),
                  Create(dex_2), run_time=t)
        self.wait(1)
        self.play(Create(dex_1_px),
                  Create(dex_2_px), run_time=t)
        self.wait(1)

        blist = BulletedList("Exposure to BTC fluctuation",
                             "Fees, time from DEX B",
                             r"In case of CEX, time, \\trade fees and high tx fees",
                             r"In case of DEX, time, \\high trade fees and tx fees",
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
        dex_3_px_unit = Tex(r'USDT').next_to(dex_3_px, R)
        dex_3_px.add(dex_3_px_unit).scale(0.65).move_to(dex_3_rect)

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
        px_unit = Tex(r'USDT').next_to(pool_btc_px, R)
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
            pool_btc_px, pool_rect, pool_rect_text, btc_lump, usdt_lump, arbitrager, usdt_asset_arbitrager, liq_provider[ 0 ])), run_time=5)

        ##### 덱스도 중앙화거래소에 영향을 주고 중앙화 거래소도 덱스에 영향을 줍니다
        ##### 모든 거래소가 아비트라지 봇으로 묶여있어 서로가 서로에게 영향을 줍니다.
        # 덱스하고 섹스 상호 화살표
        # 덱스 중앙화 거래소 네트워크
        arbigrager_circle = LabeledDot(Tex(rf'Arbitrager', color=BLACK, font_size=30), radius=1, color=ORANGE).set_z_index(1)

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
        line_group = VGroup(dex_line_1, dex_line_2, dex_line_3, dex_line_4, dex_line_5, dex_line_6, dex_line_7, cex_line_1, cex_line_2,
                            cex_line_3, cex_line_4, cex_line_5, cex_line_6, cex_line_7)
        ex_list = [ dex_1, dex_2, dex_3, dex_4, dex_5, dex_6, dex_7, cex_1, cex_2, cex_3, cex_4, cex_5, cex_6, cex_7 ]

        rotation_val_tracker = ValueTracker(1)

        dist_dict = {0: 3.66, 1: 3.2, 2: 3.21, 3: 3.12, 4: 3.42, 5: 3.37, 6: 3.34, 7: 3.04, 8: 3.24, 9: 3.43, 10: 3.4, 11: 3.26, 12: 3.1,
                     13: 3.24}
        dist_dict = {0: 3.76, 1: 2.6, 2: 3.24, 3: 3.29, 4: 3.46, 5: 2.83, 6: 2.74, 7: 2.82, 8: 2.63, 9: 2.85, 10: 2.85, 11: 3.47, 12: 3.38,
                     13: 3.07}
        dist_dict = {0: 2.8, 1: 3.6, 2: 2.99, 3: 3.71, 4: 2.83, 5: 3.89, 6: 2.82, 7: 3.82, 8: 2.8, 9: 3.8, 10: 2.8, 11: 3.6, 12: 3.54,
                     13: 3.7}

        # dist_dict = {0: 3, 1: 3, 2: 3, 3: 3, 4: 3, 5: 3, 6: 3, 7: 3, 8: 3, 9: 3, 10: 3, 11: 3, 12: 3,
        #              13: 3}
        dir_dict = {0: 0.4488, 1: 0.8976, 2: 1.3464, 3: 1.7952, 4: 2.24399, 5: 2.69279, 6: 3.14159, 7: 3.59039, 8: 4.03919, 9: 4.48799,
                    10: 4.93679, 11: 5.38559, 12: 5.83439, 13: 6.28319}

        ex_group[ 0 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 0 ] + rotation_val_tracker.get_value()) * dist_dict[ 0 ],
              sin(dir_dict[ 0 ] + rotation_val_tracker.get_value()) * dist_dict[ 0 ], 0 ])))
        ex_group[ 1 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 1 ] + rotation_val_tracker.get_value()) * dist_dict[ 1 ],
              sin(dir_dict[ 1 ] + rotation_val_tracker.get_value()) * dist_dict[ 1 ], 0 ])))
        ex_group[ 2 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 2 ] + rotation_val_tracker.get_value()) * dist_dict[ 2 ],
              sin(dir_dict[ 2 ] + rotation_val_tracker.get_value()) * dist_dict[ 2 ], 0 ])))
        ex_group[ 3 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 3 ] + rotation_val_tracker.get_value()) * dist_dict[ 3 ],
              sin(dir_dict[ 3 ] + rotation_val_tracker.get_value()) * dist_dict[ 3 ], 0 ])))
        ex_group[ 4 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 4 ] + rotation_val_tracker.get_value()) * dist_dict[ 4 ],
              sin(dir_dict[ 4 ] + rotation_val_tracker.get_value()) * dist_dict[ 4 ], 0 ])))
        ex_group[ 5 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 5 ] + rotation_val_tracker.get_value()) * dist_dict[ 5 ],
              sin(dir_dict[ 5 ] + rotation_val_tracker.get_value()) * dist_dict[ 5 ], 0 ])))
        ex_group[ 6 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 6 ] + rotation_val_tracker.get_value()) * dist_dict[ 6 ],
              sin(dir_dict[ 6 ] + rotation_val_tracker.get_value()) * dist_dict[ 6 ], 0 ])))
        ex_group[ 7 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 7 ] + rotation_val_tracker.get_value()) * dist_dict[ 7 ],
              sin(dir_dict[ 7 ] + rotation_val_tracker.get_value()) * dist_dict[ 7 ], 0 ])))
        ex_group[ 8 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 8 ] + rotation_val_tracker.get_value()) * dist_dict[ 8 ],
              sin(dir_dict[ 8 ] + rotation_val_tracker.get_value()) * dist_dict[ 8 ], 0 ])))
        ex_group[ 9 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 9 ] + rotation_val_tracker.get_value()) * dist_dict[ 9 ],
              sin(dir_dict[ 9 ] + rotation_val_tracker.get_value()) * dist_dict[ 9 ], 0 ])))
        ex_group[ 10 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 10 ] + rotation_val_tracker.get_value()) * dist_dict[ 10 ],
              sin(dir_dict[ 10 ] + rotation_val_tracker.get_value()) * dist_dict[ 10 ], 0 ])))
        ex_group[ 11 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 11 ] + rotation_val_tracker.get_value()) * dist_dict[ 11 ],
              sin(dir_dict[ 11 ] + rotation_val_tracker.get_value()) * dist_dict[ 11 ], 0 ])))
        ex_group[ 12 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 12 ] + rotation_val_tracker.get_value()) * dist_dict[ 12 ],
              sin(dir_dict[ 12 ] + rotation_val_tracker.get_value()) * dist_dict[ 12 ], 0 ])))
        ex_group[ 13 ].add_updater(lambda x: x.move_to(np.array(
            [ cos(dir_dict[ 13 ] + rotation_val_tracker.get_value()) * dist_dict[ 13 ],
              sin(dir_dict[ 13 ] + rotation_val_tracker.get_value()) * dist_dict[ 13 ], 0 ])))

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

        self.play(rotation_val_tracker.animate.set_value(6), run_time=tt, rate_functions=exponential_decay)
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

