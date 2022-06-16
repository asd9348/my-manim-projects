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

class final(Scene):
    def construct(self):
        L_02_S_01_dex_pros_and_cons.construct(self)
        L_02_S_02_smart_contract.construct(self)


class L02S01(Scene):
    def construct(self):
        script = speak(self, title='L02S01', txt=
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



class L02S02(Scene):
    def construct(self):
        script = speak(self, title='L02S02', txt=
        '그런데 어떻게 얼굴도 본적도 없고 어디 사는지도 모르는 사람과 코인을 주고받을 수 있는 것일까요.#1'
        '이와 같은 일을 가능하게  해주는 것이 스마트 컨트랙트입니다#1'
        '스마트 컨트랙트란 컴퓨터 언어로 거래를 적어놓은 것입니다#1'
        '스마트 컨트랙트는 회전문과 비슷합니다. 예를 들어 한 사람이 회전문에 1비트코인을 넣고 한 사람은 10이더리움을 넣으면 회전문이 돌아가 둘 다 원하는 것을 얻게 됩니다 #1'
        '그러나 양쪽 중 한 사람이라도 사전에 프로그래밍된 것을 넣지 않으면 회전문은 돌아가지 않습니다#1'
        '중앙화 거래소에서는 회전문을 돌리는 주체가 거래소였지만 덱스에서는 컴퓨터 언어인 것입니다#1'
        '스마트 컨트랙트는 나중에 따로 다뤄보겠습니다#1'
        '그런데 거래소를 보면 알겠지만 엄청나게 많은 거래가 일어납니다#1'
        '누군가는 주문을 넣었다 수정하거나 취소하기도 하고, 누군가는 100비트코인을 1비트코인씩 쪼개서 주문을 넣기도 합니다#1'
        '이렇게 많은 트래픽이 발생하면 대부분의 블록체인상에서 감당할 수 없고, 주문을 넣고 한참 뒤에 반영되거나 수수료 폭탄을 맞게 됩니다.#1'
                       , keep_pitch=True, update=True, speed=1.4)

        # TODO 6.185 secs그런데 어떻게 얼굴도 본적도 없고 어디 사는지도 모르는 사람과 코인을 주고받을 수 있는 것일까요.
        # TODO 1.0 secs pause

        how_can_text = Tex(r"How can we exchange \\with people we've never met?")
        self.play(Create(how_can_text), run_time=1.5)
        self.wait(0.685)

        eth_coin = create_circle_asset('ETH', 25, WHITE, fill_color=C_ETH, stroke_color=GREEN, stroke_width=0)
        btc_coin = create_circle_asset('BTC', 25, WHITE, fill_color=C_BTC, stroke_color=GREEN, stroke_width=0)
        atom_coin = create_circle_asset('ATOM', 25, C_ATOM2, fill_color=C_ATOM1, stroke_color=GREEN, stroke_width=0)
        dot_coin = create_circle_asset('DOT', 25, WHITE, fill_color=C_DOT, stroke_color=GREEN, stroke_width=0)
        sol_text = Tex('SOL', substrings_to_isolate=[ 'S', 'O', 'L' ])
        sol_text.set_color_by_tex('S', color=C_SOL3)
        sol_text.set_color_by_tex('O', color=C_SOL2)
        sol_text.set_color_by_tex('L', color=C_SOL1)
        sol_coin = create_circle_asset(sol_text, fill_color=C_SOL0, stroke_color=GREEN, stroke_width=0)
        xrp_coin = create_circle_asset('XRP', 25, WHITE, fill_color=C_XRP, stroke_color=GREEN, stroke_width=0)

        COINS.arrange_in_grid(4, 4).scale(1.5)
        COINS_BACKUP

        A_COINS = VGroup()
        A_COINS.add(COINS[ 0 ])
        A_COINS.add(COINS[ 1 ])
        A_COINS.add(COINS[ 2 ])
        A_COINS.add(COINS[ 3 ])
        A_COINS.add(COINS[ 4 ])
        A_COINS.add(COINS[ 6 ])
        A_COINS.add(COINS[ 10 ])
        A_COINS.add(COINS[ 11 ])
        A_COINS.arrange_in_grid(4, 2)

        B_COINS = VGroup()
        B_COINS.add(COINS[ 5 ])
        B_COINS.add(COINS[ 7 ])
        B_COINS.add(COINS[ 8 ])
        B_COINS.add(COINS[ 9 ])
        B_COINS.add(COINS[ 12 ])
        B_COINS.add(COINS[ 13 ])
        B_COINS.add(COINS[ 14 ])
        B_COINS.add(COINS[ 15 ])
        B_COINS.arrange_in_grid(4, 2)

        A_text = Tex('A')
        B_text = Tex('B')
        A_rect = Rectangle(width=A_COINS.width + 0.5, height=A_COINS.height + 0.5).next_to(A_text, D)
        B_rect = Rectangle(width=B_COINS.width + 0.5, height=B_COINS.height + 0.5).next_to(B_text, D)

        A_COINS.move_to(A_rect)
        B_COINS.move_to(B_rect)

        A_group = VGroup(A_text, A_rect, A_COINS).move_to(O).to_edge(L)

        B_group = VGroup(B_text, B_rect, B_COINS).move_to(O).to_edge(R)

        self.play(Create(A_group),
                  Create(B_group))
        self.wait(0.5)
        self.play(Swap(COINS[ 0 ], COINS[ 15 ]),
                  Swap(COINS[ 1 ], COINS[ 13 ]),
                  Swap(COINS[ 6 ], COINS[ 9 ]))
        self.play(Swap(COINS[ 4 ], COINS[ 14 ]),
                  Swap(COINS[ 3 ], COINS[ 7 ]),
                  Swap(COINS[ 11 ], COINS[ 5 ]),
                  Uncreate(how_can_text), run_time=1.5)

        self.play(Swap(COINS[ 2 ], COINS[ 12 ]),
                  Swap(COINS[ 10 ], COINS[ 8 ]))
        # coins = VGroup(eth_coin,btc_coin,atom_coin,dot_coin,sol_coin,xrp_coin).arrange(D)
        # self.play(Create(coins))

        # TODO 3.588 secs이와 같은 일을 가능하게  해주는 것이 스마트 컨트랙트입니다
        # TODO 1.0 secs pause
        # TODO 3.684 secs스마트 컨트랙트란 컴퓨터 언어로 거래를 적어놓은 것입니다
        # TODO 1.0 secs pause

        smart_c_text = Tex('Smart Contract').scale(2)

        contract_terms_rect = Rectangle(width=4, height=6)
        contract_terms_text_1 = Tex(r'A gives BTC to B\\B gives ETH to A').move_to(contract_terms_rect)
        # A = create_entity("A", 0.7, WHITE, "BTC", BTC, 0.8, 0.3).scale(1.2).to_edge(L)
        # B = create_entity("B", 0.7, WHITE, "ETH", ETH, 0.8, 0.3).scale(1.2).to_edge(R)

        A = Tex('A').scale(3)
        arrows = MathTex(r'\leftrightharpoons').scale(3.5).rotate(-PI / 2).next_to(A, D, buff=0.5)
        B = Tex('B').scale(3).next_to(arrows, D, buff=0.5)
        # btc_asset_contract = create_entity("A", 0.7, WHITE, "BTC", C_BTC, 0.8, 0.3)[ 1 ].scale(2).rotate(PI / 2).next_to(A, L)
        # eth_asset_contract = create_entity("A", 0.7, WHITE, "ETH", C_ETH, 0.8, 0.3)[ 1 ].scale(2).rotate(-PI / 2).next_to(B, R)
        btc_asset_contract = BTC_COIN.copy().scale(0.7).next_to(A, L)
        eth_asset_contract = ETH_COIN.copy().scale(0.7).next_to(B, R)

        contract_terms_text_1 = VGroup(A, B, arrows, btc_asset_contract, eth_asset_contract).move_to(ORIGIN)
        contract_terms_text_2 = Tex(r'01010100', '11011010', '10001001', '01010010', '11001101', '11100110', '01110001', '01100110').scale(
            1.25).arrange(D).move_to(contract_terms_rect)

        self.play(Create(smart_c_text), run_time=1.2)
        self.play(ApplyWave(smart_c_text))
        self.play(Uncreate(A_group, remover=False),
                  Uncreate(B_group, remover=False), run_time=1.8)
        self.play(ReplacementTransform(smart_c_text, contract_terms_rect), run_time=0.588)
        self.play(Create(contract_terms_text_1), run_time=0.5)
        self.play(btc_asset_contract.animate.next_to(B, L),
                  eth_asset_contract.animate.next_to(A, R))
        self.wait(0.25)
        self.play(ReplacementTransform(contract_terms_text_1, contract_terms_text_2), run_time=1)
        self.wait(0.5)
        self.play(Uncreate(VGroup(contract_terms_text_2, contract_terms_rect)), run_time=0.5)
        # TODO 0.5 secs 앞에서 0.5초 더 받아옴
        # TODO 10.389 secs스마트 컨트랙트는 회전문과 비슷합니다. 예를 들어 한 사람이 회전문에 1비트코인을 넣고 한 사람은 10이더리움을 넣으면 회전문이 돌아가 둘 다 원하는 것을 얻게 됩니다
        # TODO 1.0 secs pause
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
        A = create_entity("A", 0.7, WHITE, "BTC", BTC, 0.8, 0.3)[ 0 ].scale(1.2).to_edge(L)
        B = create_entity("B", 0.7, WHITE, "ETH", ETH, 0.8, 0.3)[ 0 ].scale(1.2).to_edge(R)

        # COINS.restore()
        anotehr_btc = create_circle_asset(Tex(r'\textbf{BTC}', color=WHITE, font_size=30), fill_color=C_BTC)
        A_asset = create_circle_asset(Tex(r'\textbf{BTC}', color=WHITE, font_size=30), fill_color=C_BTC).scale(0.7).next_to(A, D)
        B_asset = create_circle_asset(Tex(r'\textbf{ETH}', color=WHITE, font_size=30), fill_color=C_ETH).scale(0.7).next_to(B, D)
        A_asset_pos = A_asset.get_center()
        B_asset_pos = B_asset.get_center()

        A_asset_arc = Arc(radius=1.5, angle=-PI).flip(axis=UP)
        B_asset_arc = Arc(radius=1.5, angle=PI)

        condition = Tex(r'A gives BTC to B\\B gives ETH to A').to_edge(UL)

        self.play(GrowFromCenter(wall),
                  GrowFromCenter(sector1),
                  GrowFromCenter(sector2),
                  Create(rev_door),
                  run_time=1)
        self.wait(0.5)
        self.play(Rotate(rev_door, angle=2 * PI), rate_func=rate_functions.exponential_decay,
                  run_time=1)
        self.wait(0.5)

        self.play(Create(A),
                  Create(B),
                  Create(A_asset),
                  Create(B_asset),
                  Create(condition),
                  run_time=1.5)
        self.wait(0.5)
        # whole_scene =Group(self.mobject)
        # whole_scene.save_state()
        self.play(A_asset.animate.move_to(LEFT * 1.5),
                  run_time=0.5)
        self.wait(0.5)

        self.play(B_asset.animate.move_to(RIGHT * 1.5),
                  run_time=0.5)

        self.wait(1)
        self.play(Rotate(rev_door),
                  MoveAlongPath(A_asset, A_asset_arc),
                  MoveAlongPath(B_asset, B_asset_arc),
                  run_time=1.5)

        self.play(A_asset.animate.move_to(B_asset_pos),
                  B_asset.animate.move_to(A_asset_pos),
                  run_time=2)

        # self.play(Uncreate(condition),
        #           run_time=1.5)
        self.wait(0.889)

        # TODO 6.052 secs그러나 양쪽 중 한 사람이라도 사전에 프로그래밍된 것을 넣지 않으면 회전문은 돌아가지 않습니다
        # TODO 최초 2초 웨잇은 역재생 하는 거 (그냥 다빈치로 해결
        # TODO 1.0 secs pause
        # A_asset.restore()
        # B_asset.restore()
        # whole_scene.restore()

        A_asset.next_to(A, D)
        B_asset.next_to(B, D)
        slater = Tex(r'WORK on \\DAVINCI').scale(4)

        self.add(slater)
        self.wait(2)
        self.remove(slater)
        self.play(A_asset.animate.move_to(LEFT * 1.5),
                  run_time=1)

        A_asset_arc_45 = Arc(radius=1.5, angle=-PI / 2).flip(axis=UP).shift(1.5 * L)

        self.play(Rotate(rev_door, angle=PI / 2),
                  MoveAlongPath(A_asset, A_asset_arc_45),
                  run_time=1.5, rate_func=there_and_back_with_pause)

        self.wait(1)

        # TODO 5.871 secs중앙화 거래소에서는 회전문을 돌리는 주체가 거래소였지만 덱스에서는 컴퓨터 언어인 것입니다
        # TODO 1.0 secs pause
        # TODO 3.335 secs스마트 컨트랙트는 나중에 시간이 따로 다뤄보겠습니다
        # TODO 1.0 secs pause

        rev_door_text_1 = Tex(r'Company\\or Third Party Entity').scale(0.7).next_to(dot, R)
        rev_door_text_2 = Tex(r'Programming Language\\without Emotion').scale(0.7).next_to(dot, R)
        walls = VGroup(wall, sector1, sector2)

        self.play(Create(rev_door_text_1),
                  run_time=1)
        self.wait(2)
        self.play(Uncreate(rev_door_text_1),
                  run_time=0.5)
        self.wait(0.5)
        self.play(Create(rev_door_text_2),
                  run_time=1)
        self.wait(2)
        self.play(Uncreate(rev_door_text_2),
                  run_time=0.5)
        self.play(Uncreate(walls),
                  Uncreate(condition),
                  Uncreate(rev_door),
                  Uncreate(rev_door_text_2),
                  Uncreate(A_asset),
                  Uncreate(B_asset),
                  Uncreate(A),
                  Uncreate(B),
                  run_time=3)
        self.wait(0.706)

        # TODO 3.963 secs그런데 거래소를 보면 알겠지만 엄청나게 많은 거래가 일어납니다
        # TODO 1.0 secs pause
        # TODO 7.792 secs누군가는 주문을 넣었다 수정하거나 취소하기도 하고, 누군가는 100비트코인을 1비트코인씩 쪼개서 주문을 넣기도 합니다
        # TODO 1.0 secs pause
        # TODO 8.819 secs이렇게 많은 트래픽이 발생하면 대부분의 블록체인상에서 감당할 수 없고, 주문을 넣고 한참 뒤에 반영되거나 수수료 폭탄을 맞게 됩니다.
        # TODO 1.0 secs pause

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
        place_cancel_list_1 = [ 'Place', 'Place', 'Place', 'Place', 'Place', 'Place', 'Place', 'Place', 'Place', 'Place', 'Place',
                                'Place', 'Place',
                                'Place', 'Place' ]
        place_cancel_list_2 = [ 'Cancel', 'Place', 'Place', 'Cancel', 'Cancel', 'Place', 'Cancel', 'Place', 'Cancel', 'Cancel', 'Cancel',
                                'Place', 'Place',
                                'Place', 'Place' ]
        place_cancel_list_2 = [ 'Place', 'Place', 'Place', 'Place', 'Place', 'Place', 'Place', 'Place', 'Place', 'Place', 'Place',
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

        orders_left.arrange_in_grid(5, 3)
        orders_right.arrange_in_grid(5, 3)

        entire_orders = VGroup(orders_left, orders_right).arrange(R)
        entire_orders = VGroup()
        entire_orders.add(orders_left[ 0:3 ])
        entire_orders.add(orders_right[ 0:3 ])
        entire_orders.add(orders_left[ 3:6 ])
        entire_orders.add(orders_right[ 3:6 ])
        entire_orders.add(orders_left[ 6:9 ])
        entire_orders.add(orders_right[ 6:9 ])
        entire_orders.add(orders_left[ 9:12 ])
        entire_orders.add(orders_right[ 9:12 ])
        entire_orders.add(orders_left[ 12:15 ])
        entire_orders.add(orders_right[ 12:15 ])

        create_just_order(place_cancel_list_1[ i ], buy_sell_list_1[ i ], px_list_1[ i ], qty_list_1[ i ], asset_list_1[ i ])

        changed_order_1 = create_just_order('Place', 'BUY', 257, 724, 'MATIC').move_to(orders_left[ 3 ])
        changed_order_5 = create_just_order('Place', 'BUY', 243, 38, 'TRX').move_to(orders_left[ 4 ])
        changed_order_4 = create_just_order('Place', 'BUY', 6852, 87, 'DOT').move_to(orders_left[ 11 ])
        changed_order_7 = create_just_order('Place', 'BUY', 5656, 3482, 'MATIC').move_to(orders_left[ 12 ])
        changed_order_3 = create_just_order('Place', 'BUY', 2357, 4178, 'MATIC').move_to(orders_right[ 1 ])
        changed_order_8 = create_just_order('Place', 'BUY', 1267, 6453, 'XLM').move_to(orders_right[ 8 ])
        changed_order_2 = create_just_order('Place', 'BUY', 7892, 8799, 'XLM').move_to(orders_right[ 9 ])
        changed_order_6 = create_just_order('Place', 'BUY', 756, 467, 'DOT').move_to(orders_right[ 14 ])

        lots_of_btc_order = create_just_order('Place', 'BUY', 300, 100, 'BTC').scale(2.3).align_to(orders_left, D)

        mini_orders = VGroup(*[ Rectangle(height=1.8, width=1.5, stroke_width=2) for i in range(100) ]).arrange_in_grid(5, 20).scale(
            0.2).align_to(orders_left, D)

        fees = Tex('Lots of Fees').shift(L * 4.5)
        fees_arrow = MathTex(r'\Uparrow').scale(2).next_to(fees, U, buff=0.5)
        speed = Tex('Slow Speed').shift(R * 4.5)
        speed_arrow = MathTex(r'\Downarrow').scale(2).next_to(speed, D, buff=0.5)

        self.play(Create(entire_orders),
                  run_time=2)

        # self.play(AnimationGroup(AnimationGroup(Wiggle(orders_left[ 3 ]),
        #                                         Wiggle(orders_right[ 9 ]),
        #                                         Wiggle(orders_right[ 8 ])),
        #                          AnimationGroup(Transform(orders_left[ 3 ], changed_order_1),
        #                                         Transform(orders_right[ 9 ], changed_order_2),
        #                                         Transform(orders_right[ 8 ], changed_order_8)),
        #                          AnimationGroup(Wiggle(orders_left[ 1 ]),
        #                                         Wiggle(orders_right[ 11 ]),
        #                                         Wiggle(orders_right[ 4 ])),
        #                          AnimationGroup(Transform(orders_left[ 1 ], changed_order_3),
        #                                         Transform(orders_right[ 11 ], changed_order_4),
        #                                         Transform(orders_right[ 4 ], changed_order_5)),
        #                          AnimationGroup(Wiggle(orders_right[ 14 ]),
        #                                         Wiggle(orders_left[ 12 ])),
        #                          AnimationGroup(Transform(orders_right[ 14 ], changed_order_6),
        #                                         Transform(orders_left[ 12 ], changed_order_7))
        #                          ), lag_ratio=0.3, run_time=5)
        self.play(AnimationGroup(Wiggle(orders_left[ 3 ]),
                                 Wiggle(orders_right[ 9 ]),
                                 Wiggle(orders_right[ 8 ])),
                  run_time=1.5)
        self.play(AnimationGroup(Transform(orders_left[ 3 ], changed_order_1),
                                 Transform(orders_right[ 9 ], changed_order_2),
                                 Transform(orders_right[ 8 ], changed_order_8)),
                  run_time=0.5)
        self.play(AnimationGroup(Wiggle(orders_right[ 1 ]),
                                 Wiggle(orders_left[ 11 ]),
                                 Wiggle(orders_left[ 4 ])),
                  run_time=1)
        self.play(AnimationGroup(Transform(orders_right[ 1 ], changed_order_3),
                                 Transform(orders_left[ 11 ], changed_order_4),
                                 Transform(orders_left[ 4 ], changed_order_5)),
                  run_time=0.5)
        self.play(AnimationGroup(Wiggle(orders_right[ 14 ]),
                                 Wiggle(orders_left[ 12 ])),
                  run_time=1)
        self.play(AnimationGroup(Transform(orders_right[ 14 ], changed_order_6),
                                 Transform(orders_left[ 12 ], changed_order_7)),
                  run_time=0.5)


        self.play(Uncreate(orders_left[ 5 ]), run_time=0.25)
        self.play(Uncreate(orders_right[ 11 ]), run_time=0.25)
        self.play(Uncreate(orders_left[ 10 ]), run_time=0.25)
        self.play(Uncreate(orders_right[ 1 ]), run_time=0.25)
        self.play(Uncreate(orders_right[ 12 ]), run_time=0.25)

        self.wait(1)

        self.play(AnimationGroup(AnimationGroup(orders_left.animate.to_edge(L),
                                                orders_right.animate.to_edge(R), lag_ratio=0),
                                 Create(blockchain[ :-2 ]), lag_ratio=0.5))
        self.wait(0.25)

        self.play(Create(lots_of_btc_order))
        self.wait(0.25)

        self.play(ReplacementTransform(lots_of_btc_order, mini_orders))

        self.wait(0.25)

        self.play(LaggedStart(*[ FadeOut(order, target_position=blocks[ 1 ]) for order in orders_left_list + orders_right_list ]),
                  LaggedStart(*[ FadeOut(order, target_position=blocks[ 1 ]) for order in mini_orders ]),
                  run_time=3.5)
        self.play(AnimationGroup(Create(blockchain[ -2: ], run_tiem=8),
                                 AnimationGroup(Create(speed, run_time=1), speed.animate.scale(2), GrowFromEdge(speed_arrow, edge=U),
                                                lag_ratio=0.7, run_time=2),
                                 AnimationGroup(Create(fees, run_time=1), fees.animate.scale(2), GrowFromEdge(fees_arrow, edge=D),
                                                lag_ratio=0.7, run_time=2)
                                 , lag_ratio=0.5, run_time=5), run_time=5)

        self.wait(0.5)
        self.play(Uncreate(blockchain),
                  Uncreate(VGroup(fees, fees_arrow, speed, speed_arrow)), run_time=1.5)
        self.wait(0.324)

        self.wait(5)


class L02S03(Scene):
    def construct(self):
        speak(self, title='L02S03', txt=
        '그래서 덱스는 일반 거래소처럼 오더북을 사용하지 않습니다#1'
        '대신 오토매틱 마켓 메이커라는 것을 사용합니다#1'
        '에이엠엠은 오토매틱 마켓 메이커의 약자로 오더북없이 가격을 결정하는 방식 혹은 알고리즘이라고 생각하면 됩니다#1'
        '일반적으로 엑스 와이는 케이라는 식을 사용하여 가격을 결정합니다. 이 에이엠엠과 엑스 와이는 케이 공식에 대해 알아보겠습니다#1'
        '원래 덱스는 이더리움 생태계에서 나왔고 비트코인이 랩드 비트코인같이 이더리움 체인에서 사용된 건 시간이 걸렸지만 이해를 위해 그냥 비티씨를 사용하겠습니다#1'
        '최초의 뎩스가 탄생하고 사람들은 비트코인과 테더의 거래쌍을 만들고 싶었습니다.#1'
        '그래서 중앙화 거래소에서 비트코인 가격이 300테더인 걸 보고, 비트코인 10개와 3000테더를 함께 유동성 풀이라는 것에 넣었습니다#1'
        '이것은 일종의 스마트 컨트랙트로 자신의 자산으로 유동성을 제공하곘다는 것입니다.#1'
        '이제 이 유동성 제공자로 인하여 거래자들은 비트코인과 테더 거래쌍을 이용할 수 있습니다#1'
        '말만 들으면 뭔지 이해가 안 될테니 이제 자세히 알아보겠습니다#1'
              , keep_pitch=True, update=True, speed=1.4)

        dummy_for_order_book = Tex('djfk', color=WHITE).scale(4)
        # self.play(Create())
        self.play(Uncreate(dummy_for_order_book), run_time=0.001)


        # TODO 3.697 secs그래서 덱스는 일반 거래소처럼 오더북을 사용하지 않습니다
        # TODO 1.0 secs pause
        # TODO 3.141 secs대신 오토매틱 마켓 메이커라는 것을 사용합니다
        # TODO 1.0 secs pause

        amm_text = Tex('{{A}}utomatic {{M}}arket {{M}}aker').scale(2)
        xyk = MathTex('x', r'\times', 'y', '=', 'k').scale(2)

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

        self.play(Create(curr_px_rect), run_time=0.25)

        self.play(FadeIn(curr_px_number_100), run_time=0.25)

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

        self.play(Create(order_book_long_table), Create(order_book_shrt_table), run_time=0.5)

        self.wait(1)

        order_book_cross = Cross(stroke_width=25).scale(3)
        order_book_stuff = VGroup(curr_px_rect, curr_px_number_100, order_book_long_table, order_book_shrt_table, order_book_cross)
        self.play(Create(order_book_cross), run_time=1)
        self.wait(0.5)

        self.play(AnimationGroup(ReplacementTransform(order_book_stuff, dummy_for_order_book),
                                 GrowFromCenter(amm_text), lag_ratio=0.2), run_time=2.5)
        self.wait(0.5)

        # TODO 7.007 secs에이엠엠은 오토매틱 마켓 메이커의 약자로 오더북없이 가격을 결정하는 방식 혹은 알고리즘이라고 생각하면 됩니다
        # TODO 1.0 secs pause

        amm_acronym_text = Tex('{{A}}{{M}}{{M}}').scale(2).move_to(amm_text)
        self.play(TransformMatchingTex(amm_text, amm_acronym_text), run_time=t)
        self.wait(t)

        ##### 그냥 프로그램 혹은 가격을 정하는 방식같은 추상적 개념이라고 생각하시면 됩니다
        # 에이엠엠 텍스트 밑에 프로그램 혹은 컨셉
        program_or_concept_text = Tex('Program or Concept?').next_to(amm_text, D)
        self.play(Create(program_or_concept_text), run_time=2.5)
        self.wait(1)

        # TODO 7.84 secs일반적으로 엑스 와이는 케이라는 식을 사용하여 가격을 결정합니다. 이 에이엠엠과 엑스 와이는 케이 공식에 대해 알아보겠습니다

        # TODO 1.0 secs pause
        self.play(ReplacementTransform(VGroup(amm_acronym_text, program_or_concept_text), xyk), run_time=2)
        self.play(Uncreate(xyk), run_time=2)

        self.wait(6)

        # TODO 9.894 secs원래 덱스는 이더리움 생태계에서 나왔고 비트코인이 랩드 비트코인같이 이더리움 체인에서 사용된 건 시간이 걸렸지만 이해를 위해 그냥 비티씨를 사용하겠습니다
        # TODO 1.0 secs pause

        self.wait(11)

        # TODO 5.134 secs최초의 뎩스가 탄생하고 사람들은 비트코인과 테더의 거래쌍을 만들고 싶었습니다.
        # TODO 1.0 secs pause
        # TODO 8.553 secs그래서 중앙화 거래소에서 비트코인 가격이 300테더인 걸 보고, 비트코인 10개와 3000테더를 함께 유동성 풀이라는 것에 넣었습니다
        # TODO 1.0 secs pause
        # TODO 5.182 secs이것은 일종의 스마트 컨트랙트로 자신의 자산으로 유동성을 제공하곘다는 것입니다.
        # TODO 1.0 secs pause
        # TODO 5.69 secs이제 이 유동성 제공자로 인하여 거래자들은 비트코인과 테더 거래쌍을 이용할 수 있습니다
        # TODO 1.0 secs pause
        # TODO 3.95 secs말만 들으면 뭔지 이해가 안 될테니 이제 자세히 알아보겠습니다
        # TODO 1.0 secs pause

        expl_plain_text = Text(
            '최초의 DEX가 생기고 사람들은 BTC와 USDT의 거래쌍을 만들고 싶었습니다.\n'
            '그래서 중앙화 거래소에서 BTC 가격이 300 USDT인 걸 보고,\n'
            '10 BTC와 3000USDT를 함께 유동성 풀이라는 것에 넣었습니다.\n'
            '이것은 일종의 스마트 컨트랙트로 자신의 자산으로 유동성을 제공하곘다는 것입니다.\n'
            '이제 이 유동성 제공자로 인하여 거래자들은 비트코인과 테더 거래쌍을 이용할 수 있습니다.',
            font='Batang', line_spacing=3, font_size=22)

        self.play(Create(expl_plain_text), run_time=22)
        self.wait(7)

        self.play(Uncreate(expl_plain_text), run_time=3)
        self.wait(t)

class L02S04(Scene):
    def construct(self):
        speak(self, title='L02S04', txt=
        '그래서 덱스는 일반 거래소처럼 오더북을 사용하지 않습니다#1'
        '대신 오토매틱 마켓 메이커라는 것을 사용합니다#1'
        '에이엠엠은 오토매틱 마켓 메이커의 약자로 오더북없이 가격을 결정하는 방식 혹은 알고리즘이라고 생각하면 됩니다#1'
        '일반적으로 엑스 와이는 케이라는 식을 사용하여 가격을 결정합니다. 이 에이엠엠과 엑스 와이는 케이 공식에 대해 알아보겠습니다#1'
        '원래 덱스는 이더리움 생태계에서 나왔고 비트코인이 랩드 비트코인같이 이더리움 체인에서 사용된 건 시간이 걸렸지만 이해를 위해 그냥 비티씨를 사용하겠습니다#1'
        '최초의 뎩스가 탄생하고 사람들은 비트코인과 테더의 거래쌍을 만들고 싶었습니다.#1'
        '그래서 중앙화 거래소에서 비트코인 가격이 300테더인 걸 보고, 비트코인 10개와 3000테더를 함께 유동성 풀이라는 것에 넣었습니다#1'
        '이것은 일종의 스마트 컨트랙트로 자신의 자산으로 유동성을 제공하곘다는 것입니다.#1'
        '이제 이 유동성 제공자로 인하여 거래자들은 비트코인과 테더 거래쌍을 이용할 수 있습니다#1'
        '말만 들으면 뭔지 이해가 안 될테니 이제 자세히 알아보겠습니다#1'
              , keep_pitch=True, update=True, speed=1.4)

        dummy_for_order_book = Tex('djfk', color=WHITE).scale(4)
        # self.play(Create())
        self.play(Uncreate(dummy_for_order_book), run_time=0.001)


        # TODO 3.697 secs그래서 덱스는 일반 거래소처럼 오더북을 사용하지 않습니다
        # TODO 1.0 secs pause
        # TODO 3.141 secs대신 오토매틱 마켓 메이커라는 것을 사용합니다
        # TODO 1.0 secs pause

        amm_text = Tex('{{A}}utomatic {{M}}arket {{M}}aker').scale(2)
        xyk = MathTex('x', r'\times', 'y', '=', 'k').scale(2)

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

        self.play(Create(curr_px_rect), run_time=0.25)

        self.play(FadeIn(curr_px_number_100), run_time=0.25)

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

        self.play(Create(order_book_long_table), Create(order_book_shrt_table), run_time=0.5)

        self.wait(1)

        order_book_cross = Cross(stroke_width=25).scale(3)
        order_book_stuff = VGroup(curr_px_rect, curr_px_number_100, order_book_long_table, order_book_shrt_table, order_book_cross)
        self.play(Create(order_book_cross), run_time=1)
        self.wait(0.5)

        self.play(AnimationGroup(ReplacementTransform(order_book_stuff, dummy_for_order_book),
                                 GrowFromCenter(amm_text), lag_ratio=0.2), run_time=2.5)
        self.wait(0.5)

        # TODO 7.007 secs에이엠엠은 오토매틱 마켓 메이커의 약자로 오더북없이 가격을 결정하는 방식 혹은 알고리즘이라고 생각하면 됩니다
        # TODO 1.0 secs pause

        amm_acronym_text = Tex('{{A}}{{M}}{{M}}').scale(2).move_to(amm_text)
        self.play(TransformMatchingTex(amm_text, amm_acronym_text), run_time=t)
        self.wait(t)

        ##### 그냥 프로그램 혹은 가격을 정하는 방식같은 추상적 개념이라고 생각하시면 됩니다
        # 에이엠엠 텍스트 밑에 프로그램 혹은 컨셉
        program_or_concept_text = Tex('Program or Concept?').next_to(amm_text, D)
        self.play(Create(program_or_concept_text), run_time=2.5)
        self.wait(1)

        # TODO 7.84 secs일반적으로 엑스 와이는 케이라는 식을 사용하여 가격을 결정합니다. 이 에이엠엠과 엑스 와이는 케이 공식에 대해 알아보겠습니다

        # TODO 1.0 secs pause
        self.play(ReplacementTransform(VGroup(amm_acronym_text, program_or_concept_text), xyk), run_time=2)
        self.wait(5.5)
        self.play(Uncreate(xyk), run_time=2)

        self.wait(0.5)

        # TODO 9.894 secs원래 덱스는 이더리움 생태계에서 나왔고 비트코인이 랩드 비트코인같이 이더리움 체인에서 사용된 건 시간이 걸렸지만 이해를 위해 그냥 비티씨를 사용하겠습니다
        # TODO 1.0 secs pause

        my_svg = SVGMobject('ethereum-eth-logo.svg').set_z_index(4).shift(U * 2)
        my_svg[ 1 ].set_color('#F2F2F2')
        my_svg[ 3 ].set_color('#F2F2F2')
        my_svg[ 0 ].set_color('#B7C2E9')
        my_svg[ 2 ].set_color('#B7C2E9')
        my_svg[ 5 ].set_color('#B7C2E9')
        my_svg[ 4 ].set_color('#7A90E2')

        eth_circle = Circle(color='#5D78DE', fill_color='#5D78DE', fill_opacity=1, radius=1.5).set_z_index(3).shift(U * 2)
        dex = LabeledDot('DEX', color=WHITE, radius=1).set_z_index(0.5).move_to(eth_circle)

        self.play(AnimationGroup(DrawBorderThenFill(my_svg), DrawBorderThenFill(eth_circle), run_time=1.5))
        self.play(dex.animate.move_to(D * 1),run_time=1)

        clock_min_angle = ValueTracker(PI / 2)
        clock_hour_angle = ValueTracker(PI / 2)
        clock_circle = Circle(color=WHITE)
        clock_center_dot = Dot(color=WHITE)
        clock_min_handle = Arrow(start=clock_circle.get_center(), end=clock_circle.get_center() + np.array(
            [ cos(clock_min_angle.get_value()) * 0.8, sin(clock_min_angle.get_value()) * 0.9, 0 ]), stroke_width=3, buff=0,
                                 max_stroke_width_to_length_ratio=100)
        clock_hour_handle = Arrow(start=clock_circle.get_center(), end=clock_circle.get_center() + np.array(
            [ cos(clock_hour_angle.get_value()) * 0.5, sin(clock_hour_angle.get_value()) * 0.5, 0 ]), stroke_width=5, buff=0,
                                  max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=0.4)
        clock_min_handle.add_updater(lambda x: x.become(Arrow(start=clock_circle.get_center(), end=clock_circle.get_center() + np.array(
            [ cos(clock_min_angle.get_value()) * 0.8, sin(clock_min_angle.get_value()) * 0.9, 0 ]), stroke_width=5, buff=0,
                                                              max_stroke_width_to_length_ratio=100)))
        clock_hour_handle.add_updater(lambda x: x.become(Arrow(start=clock_circle.get_center(), end=clock_circle.get_center() + np.array(
            [ cos(clock_hour_angle.get_value()) * 0.5, sin(clock_hour_angle.get_value()) * 0.5, 0 ]), stroke_width=5, buff=0,
                                                               max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=0.4)))
        clock = VGroup(clock_circle, clock_center_dot, clock_min_handle, clock_hour_handle)

        wbtc_coin = create_circle_asset(Tex(r'\textbf{WBTC}', color=WHITE, font_size=40), radius=0.97, stroke_width=20,
                                        stroke_opacity=1,
                                        stroke_color=C_ETH, fill_color=C_BTC).shift(D * 1 + R * 3)

        self.wait(0.5)
        self.play(dex.animate.shift(L * 3),
                  Create(clock.shift(D * 1)))

        self.play(AnimationGroup(AnimationGroup(clock_min_angle.animate.set_value(PI / 2 - 4 * 2 * PI),
                                                clock_hour_angle.animate.set_value(PI / 2 - 4 * 2 * PI / 12)),
                                 FadeIn(wbtc_coin,target_position=clock),lag_ratio= 0.7, run_time=3.5))

        self.wait(1)

        clock_hour_handle.clear_updaters()
        clock_min_handle.clear_updaters()

        self.play(FadeOut(VGroup(my_svg,eth_circle)),
                  FadeOut(dex),
                  FadeOut(clock),
                  FadeOut(wbtc_coin),run_time=1)



        self.wait(0.484)

        # TODO 5.134 secs최초의 뎩스가 탄생하고 사람들은 비트코인과 테더의 거래쌍을 만들고 싶었습니다.
        # TODO 1.0 secs pause
        # TODO 8.553 secs그래서 중앙화 거래소에서 비트코인 가격이 300테더인 걸 보고, 비트코인 10개와 3000테더를 함께 유동성 풀이라는 것에 넣었습니다
        # TODO 1.0 secs pause
        # TODO 5.182 secs이것은 일종의 스마트 컨트랙트로 자신의 자산으로 유동성을 제공하곘다는 것입니다.
        # TODO 1.0 secs pause
        # TODO 5.69 secs이제 이 유동성 제공자로 인하여 거래자들은 비트코인과 테더 거래쌍을 이용할 수 있습니다
        # TODO 1.0 secs pause
        # TODO 3.95 secs말만 들으면 뭔지 이해가 안 될테니 이제 자세히 알아보겠습니다
        # TODO 1.0 secs pause

        expl_plain_text = Text(
            '최초의 DEX가 생기고 사람들은 BTC와 USDT의 거래쌍을 만들고 싶었습니다.\n'
            '그래서 중앙화 거래소에서 BTC 가격이 300 USDT인 걸 보고,\n'
            '10 BTC와 3000USDT를 함께 유동성 풀이라는 것에 넣었습니다.\n'
            '이것은 일종의 스마트 컨트랙트로 자신의 자산으로 유동성을 제공하곘다는 것입니다.\n'
            '이제 이 유동성 제공자로 인하여 거래자들은 비트코인과 테더 거래쌍을 이용할 수 있습니다.',
            font='Batang', line_spacing=3, font_size=22)

        self.play(Create(expl_plain_text), run_time=22)
        self.wait(7)

        self.play(Uncreate(expl_plain_text), run_time=3)
        self.wait(t)


class L02S05(Scene):
    def construct(self):
        speak(self, title='L02S05', txt=
        '오더북에서는 그저 사람들이 거래하는 것을 바탕으로 알아서 가격이 정해집니다#1'
        '우리가 중앙화 거래소에서 봤던 거래쌍이 덱스에서는 유동성 풀이고 에이엠엠은 이 유동성 풀로 가격을 계산합니다#1'
        '당연한 얘기지만 비티씨 테더 페어에 만약 비티씨만 존재한다면 아무것도 일어나지 않을 것입니다#1'
        '왜냐하면 비티씨 테더 페어라는 것은 두가지의 교환이 일어나는 공간이라는 것인데 둘 중 하나만 있으면 교환이 성립하지 않기 때문입니다#1'
        '그래서 우리는 풀에 사람들이 거래할 수 있도록 유동성을 공급하고, 유동성을 공급한다는 것은 비티씨와 테더를 같이 넣어준다는 것입니다#1'
        '반드시 같이 넣어야하는 이유는 곧 알게됩니다#1'
        '덱스의 있는 참여자는 크게 두 종류입니다. 유동성 제공자와 거래자입니다#1'
        '유동성 제공자는 영어로 줄여서 엘피라고도 부릅니다. 유동성 제공자는 아까 말한 것처럼 비티씨와 테더를 같이 넣어주거나 빼면서 유동성을 조절합니다#1'
        '즉 풀 사이즈를 키우거나 줄입니다. 이것은 나중에 보겠지만 케이값을 움직이는 것입니다. 곧 보게 될테니 걱정 안 하셔도 됩니다#1'
        '거래자들은 풀에 자신이 테더를 넣고 그에 상응하는 비트코인을 빼가든지, 가진 비트코인을 넣고 그에 상응하는 테더를 빼가든지 할 수 있습니다#1'
        '각각 비트코인 매도와 매수에 대응하는 행위이고, 동시에 그래프위의 점을 이동시키는 행위입니다#1'
        '이것또한 곳 보게 될테니 걱정 안 하셔도 됩니다#1'
        '유동성제공자는 케이값을 움직이고 거래자는 점을 이동시킨다라고만 기억해두십시오#1'
        '유동성 제공자는 거래자들이 내는 수수료를 받으면서 수익을 냅니다. 거래자들은 코인을 사고 팔며 가격차익을 얻습니다#1'
        '풀이 운영되는 기본 원칙은 언제나 같은 가치의 자산이 들어있게 한다는 것입니다. 그래서 이걸 기반으로 오토매틱 마켓 메이커는 가격을 산정합니다#1'
        '현재 초기 공급자만 비티씨와 테더를 넣었고 10비티씨와 3000테더라고 하겠습니다#1'
        '10비트와 3000테더가 같은 가치기 때문에 비티씨는 1개에 300테더입니다#1'
        '이것은 모두 미리 작성된 프로그래밍 언어의 스크립트를 실행하는 것으로 이루어집니다#1'
        '스마트 컨트랙트 덕분에 우리는 중앙화 거래서와 같은 제3자를 거치지 않을 수 있게 됐습니다#1'

              , keep_pitch=True, update=True, speed=1.4)

        # TODO 4.663 secs오더북에서는 그저 사람들이 거래하는 것을 바탕으로 알아서 가격이 정해집니다

        # TODO 1.0 secs pause
        arrow_1 = CurvedArrow(2 * L, 2 * R, radius=-5).shift(U * 1)
        arrow_2 = CurvedArrow(2 * R, 2 * L, radius=-5).shift(D * 1)
        btc = BTC_COIN.copy().scale(1.5).shift(L * 3)
        usdt = USDT_COIN.copy().scale(1.5).shift(R * 3)

        trade_main = VGroup(btc, usdt, arrow_1, arrow_2)

        trade_1 = trade_main.copy().scale(0.6).to_edge(UR)
        trade_2 = trade_main.copy().scale(0.5).to_edge(DL)
        trade_3 = trade_main.copy().scale(0.4).to_edge(UL)
        trade_4 = trade_main.copy().scale(0.3).to_edge(DR)
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
                                 Swap(trade_2[ 1 ], trade_2[ 0 ]), lag_ratio=0.5, run_time=2)
                  )
        price = Tex('Price').scale(2)
        self.play(ReplacementTransform(VGroup(trade_main, trade_1, trade_2, trade_3, trade_4), price))
        self.wait(0.5)
        self.play(Uncreate(price), run_time=1.163)
        # self.wait(0.663)

        # TODO 8.01 secs우리가 중앙화 거래소에서 봤던 거래쌍이 덱스에서는 유동성 풀이고 에이엠엠은 이 유동성 풀로 가격을 계산합니다

        # TODO 1.0 secs pause

        liq_pool_text = Tex('{{BTC/USDT}} Liquidity Pool').scale(2)

        pair_text = Tex('{{BTC/USDT}} Pair').scale(2)
        price = Tex('Price').scale(2).shift(D * 2.5)
        arrow = MathTex(r'\Downarrow').scale(4)

        self.play(Create(pair_text))
        self.wait(2)
        self.play(TransformMatchingTex(pair_text, liq_pool_text))

        self.play(AnimationGroup(liq_pool_text.animate.shift(U * 2.5),
                                 GrowFromEdge(arrow, U),
                                 Create(price), lag_ratio=0.5, run_time=1.5))
        self.wait(0.5)
        self.play(Uncreate(VGroup(liq_pool_text, arrow, price)))

        self.wait(0.51)

        # TODO 6.089 secs당연한 얘기지만 비티씨 테더 페어에 만약 비티씨만 존재한다면 아무것도 일어나지 않을 것입니다

        # TODO 1.0 secs pause

        # TODO 8.082 secs왜냐하면 비티씨 테더 페어라는 것은 두가지의 교환이 일어나는 공간이라는 것인데 둘 중 하나만 있으면 교환이 성립하지 않기 때문입니다
        # TODO 1.0 secs pause

        pool_rect = RoundedRectangle(width=7, height=4, corner_radius=0.5)
        pool_rect_text = Tex('BTC/USDT Pool').next_to(pool_rect, U)
        pool = VGroup(pool_rect, pool_rect_text)

        self.play(Create(pool), run_time=1)

        btc_lump = create_circle_asset(Tex(r'\textbf{BTC}', color=WHITE, font_size=30), fill_color=C_BTC).scale_to_fit_height(
            height=2).shift(L * 5.5)
        usdt_lump = create_circle_asset(Tex(r'\textbf{USDT}', color=WHITE, font_size=25), fill_color=C_USDT).scale_to_fit_height(
            height=2).shift(R * 5.5)
        btc_lump.save_state()
        usdt_lump.save_state()
        btc_lump_arc = Arc(radius=2, angle=PI).flip(axis=np.array([ 0, 1, 0 ])).shift(L * 3.5)
        usdt_lump_arc = Arc(radius=2, angle=PI).shift(R * 3.5)

        self.play(Create(btc_lump),
                  Create(usdt_lump), run_time=0.5)

        self.play(MoveAlongPath(btc_lump, btc_lump_arc),
                  MoveAlongPath(usdt_lump, usdt_lump_arc), run_time=0.5)
        exchange_speech_text_1 = Tex(r'I am here to\\get USDT with my BTC').shift(5.5 * R + 3 * D).scale(0.7)
        long_face_1 = Tex(':(').rotate(-PI / 2).move_to(exchange_speech_text_1).scale(3)
        btc_lump_long_face = btc_lump.copy().shift(R * 15)

        self.play(FadeOut(usdt_lump), run_time=1)

        self.play(Create(exchange_speech_text_1),
                  btc_lump_long_face.animate.move_to(R * 5), run_time=1.5)
        self.play(Swap(btc_lump_long_face, btc_lump), rate_func=there_and_back)
        self.play(ReplacementTransform(exchange_speech_text_1, long_face_1), run_time=1)
        self.wait(0.5)

        self.play(Uncreate(long_face_1),
                  Uncreate(btc_lump_long_face), run_time=0.5)
        self.play(FadeIn(usdt_lump), run_time=0.5)
        self.wait(0.5)

        exchange_speech_text_2 = Tex(r'I am here to\\get BTC with my USDT').shift(5.5 * L + 3 * D).scale(0.7)
        long_face_2 = Tex(':(').rotate(-PI / 2).move_to(exchange_speech_text_2).scale(3)
        usdt_lump_long_face = usdt_lump.copy().shift(L * 15)

        self.play(FadeOut(btc_lump), run_time=0.5)

        self.play(Create(exchange_speech_text_2), usdt_lump_long_face.animate.move_to(L * 5), run_time=1.5)

        self.play(Swap(usdt_lump_long_face, usdt_lump), rate_func=there_and_back)
        self.play(ReplacementTransform(exchange_speech_text_2, long_face_2), run_time=1)

        self.wait(0.5)

        self.play(Uncreate(long_face_2),
                  Uncreate(usdt_lump_long_face), run_time=0.5)
        self.play(FadeIn(btc_lump), run_time=0.5)
        self.wait(1.338)
        self.play(
            Uncreate(long_face_1),
            Uncreate(long_face_2),
            run_time=1)
        self.wait(0.833)
        # TODO 8.481 secs그래서 우리는 풀에 사람들이 거래할 수 있도록 유동성을 공급하고, 유동성을 공급한다는 것은 비티씨와 테더를 같이 넣어준다는 것입니다
        # TODO 1.0 secs pause
        # TODO 3.008 secs반드시 같이 넣어야하는 이유는 곧 알게됩니다
        # TODO 1.0 secs pause

        btc_lump_liq_prov_1 = btc_lump.copy().move_to(np.array([ -6, 2, 0 ]))
        usdt_lump_liq_prov_1 = usdt_lump.copy().move_to(np.array([ -6, -2, 0 ]))
        btc_lump_liq_prov_2 = btc_lump.copy().move_to(np.array([ 6, 2, 0 ]))
        usdt_lump_liq_prov_2 = usdt_lump.copy().move_to(np.array([ 6, -2, 0 ]))

        self.play(Create(VGroup(btc_lump_liq_prov_1, usdt_lump_liq_prov_1, btc_lump_liq_prov_2, usdt_lump_liq_prov_2)), run_time=1.5)
        self.wait(1.5)

        self.play(FadeOut(btc_lump_liq_prov_1, target_position=pool_rect),
                  FadeOut(usdt_lump_liq_prov_1, target_position=pool_rect),
                  btc_lump.animate.scale(1.1),
                  usdt_lump.animate.scale(1.1), run_time=1)
        self.wait(1)

        self.play(FadeOut(btc_lump_liq_prov_2, target_position=pool_rect),
                  FadeOut(usdt_lump_liq_prov_2, target_position=pool_rect),
                  btc_lump.animate.scale(1.1),
                  usdt_lump.animate.scale(1.1), run_time=1)
        self.wait(6.489)

        # TODO 4.833 secs덱스의 있는 참여자는 크게 두 종류입니다. 유동성 제공자와 거래자입니다
        # TODO 1.0 secs pause
        dex_participants_text = Tex('DEX Participants').scale(1.2).to_edge(U)
        liq_prov_text = Tex('Liq Provider').shift(L * 5.5 + U * 2.5)
        trader_text = Tex('Trader').shift(R * 5.5 + U * 2.5)
        line_to_liq_prov = Line(dex_participants_text.get_corner(DL), liq_prov_text.get_top())
        line_to_trader = Line(dex_participants_text.get_corner(DR), trader_text.get_top())


        self.play(Create(dex_participants_text), run_time=1)
        self.play(Create(line_to_liq_prov),
                  Create(line_to_trader), run_time=1)
        self.wait(1)

        self.play(Create(liq_prov_text),
                  Create(trader_text), run_time=1.833)
        self.wait(1)

        # TODO 9.628 secs유동성 제공자는 영어로 줄여서 엘피라고도 부릅니다. 유동성 제공자는 아까 말한 것처럼 비티씨와 테더를 같이 넣어주거나 빼면서 유동성을 조절합니다
        # TODO 1.0 secs pause
        # TODO 8.191 secs즉 풀 사이즈를 키우거나 줄입니다. 이것은 나중에 보겠지만 케이값을 움직이는 것입니다. 곧 보게 될테니 걱정 안 하셔도 됩니다
        # TODO 1.0 secs pause

        liq_provider = create_entity(Tex(r' \emph{Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "BTC", C_BTC, 1.4, 0.3,
                                     asset_text_color=WHITE).next_to(liq_prov_text, D)
        liq_prov_btc_asset = liq_provider[ 1 ]
        liq_prov_usdt_asset = create_entity("A", 0.5, WHITE, "USDT", C_USDT, 1.4, 0.3, asset_text_color=WHITE)[ 1 ].next_to(liq_provider,
                                                                                                                            DOWN, buff=0.1)
        liq_provider.add(liq_prov_usdt_asset)
        self.play(Create(liq_provider), run_time=1)
        self.wait(0.5)

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

        self.play(Create(moving_k_text), run_time=1)
        self.wait(0.5)

        self.play(Create(coor_sys_liq_prov),
                  Create(liq_prov_graph), run_time=1)
        self.wait(0.5)

        self.play(liq_prov_tracker.animate.set_value(9))
        self.wait(0.5)

        self.play(liq_prov_tracker.animate.set_value(1))
        self.wait(0.5)
        liq_prov_btc_asset.save_state()
        liq_prov_usdt_asset.save_state()
        self.play(liq_prov_tracker.animate.set_value(9),
                  FadeOut(liq_prov_btc_asset, target_position=btc_lump),
                  FadeOut(liq_prov_usdt_asset, target_position=usdt_lump),
                  btc_lump.animate.scale(1.1),
                  usdt_lump.animate.scale(1.1), run_time=4)
        self.wait(1)
        liq_prov_btc_asset.restore()
        liq_prov_usdt_asset.restore()
        self.play(liq_prov_tracker.animate.set_value(1),
                  FadeIn(liq_prov_btc_asset, target_position=btc_lump),
                  FadeIn(liq_prov_usdt_asset, target_position=usdt_lump),
                  btc_lump.animate.scale(1 / 1.1),
                  usdt_lump.animate.scale(1 / 1.1), run_time=4)
        self.wait(4)

        trader = create_entity(Tex(r' \emph{Trader}', color=BLACK).scale(0.9), 1, WHITE, "BTC", C_BTC, 1.4,
                               0.3, asset_text_color=WHITE).next_to(trader_text, D)
        trader_btc_asset = trader[ 1 ]
        trader_usdt_asset = create_entity("A", 0.5, WHITE, "USDT", C_USDT, 1.4, 0.3, asset_text_color=WHITE)[ 1 ].next_to(trader, DOWN,
                                                                                                                          buff=0.1)
        trader_usdt_asset_copy = create_entity("A", 0.5, WHITE, "USDT", C_USDT, 1.4, 0.3, asset_text_color=WHITE)[ 1 ].move_to(
            trader_btc_asset)
        trader.add(trader_usdt_asset)
        self.play(Create(trader), run_time=tt)
        self.wait(0.5)

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

        self.play(Create(moving_dot_text), run_time=1)
        self.wait(0.5)
        self.play(Create(coor_sys_trader),
                  Create(trader_graph),
                  Create(curr_dot), run_time=1)
        self.wait(0.5)
        self.play(trader_tracker.animate.set_value(6), run_time=1)
        self.wait(0.5)
        self.play(trader_tracker.animate.set_value(1), run_time=1)
        self.wait(0.5)

        self.play(trader_tracker.animate.set_value(6),
                  FadeOut(trader_btc_asset, target_position=btc_lump),
                  FadeIn(trader_usdt_asset_copy, target_position=usdt_lump),
                  btc_lump.animate.scale(1.1),
                  usdt_lump.animate.scale(1 / 1.1), run_time=4)
        self.wait(0.5)

        self.play(trader_tracker.animate.set_value(1),
                  FadeIn(trader_btc_asset, target_position=btc_lump),
                  FadeOut(trader_usdt_asset_copy, target_position=usdt_lump),
                  btc_lump.animate.scale(1 / 1.1),
                  usdt_lump.animate.scale(1.1), run_time=4)
        self.wait(7)

        from_fees_text = Tex(r'From\\fees').move_to(np.array([ -2, -3, 0 ]))
        from_trades_text = Tex(r'From\\trades').move_to(np.array([ 2, -3, 0 ]))

        self.play(Create(from_fees_text), run_time=3)
        self.wait(1)
        self.play(Create(from_trades_text), run_time=3)
        self.wait(1)
        self.play(Uncreate(VGroup(from_trades_text, from_fees_text)))

        # TODO 8.662 secs풀이 운영되는 기본 원칙은 언제나 같은 가치의 자산이 들어있게 한다는 것입니다. 그래서 이걸 기반으로 오토매틱 마켓 메이커는 가격을 산정합니다
        # TODO 1.0 secs pause
        # TODO 5.485 secs현재 초기 공급자만 비티씨와 테더를 넣었고 10비티씨와 3000테더라고 하겠습니다
        # TODO 1.0 secs pause
        # TODO 5.062 secs10비트와 3000테더가 같은 가치기 때문에 비티씨는 1개에 300테더입니다
        # TODO 1.0 secs pause
        # TODO 5.014 secs이것은 모두 미리 작성된 프로그래밍 언어의 스크립트를 실행하는 것으로 이루어집니다
        # TODO 1.0 secs pause
        # TODO 5.762 secs스마트 컨트랙트 덕분에 우리는 중앙화 거래서와 같은 제3자를 거치지 않을 수 있게 됐습니다
        # TODO 1.0 secs pause

        equal_sign = Tex('=').scale(1.5)
        always_equal_value = Tex('Always Equal Values')
        price_determination = Tex('Price determined')
        always_equal_value_texts = VGroup(always_equal_value, price_determination).arrange(D).shift(D * 3)

        value_equal_1 = MathTex(r'Value\  of\  BTC in Pool', '=', r'Value\  of\   USDT in Pool').arrange(D).scale(0.94).shift(D * 3)
        value_equal_2 = MathTex(r'10 BTC', '=', r'3000 USDT').shift(D * 3)

        price_frac = MathTex(r'\frac{3000 USDT}{10 BTC}').shift(D * 3)

        final_price_per_btc = MathTex(r'300 USDT\  per \  BTC').shift(D * 3)

        self.play(Create(always_equal_value_texts))
        self.wait(3.5)
        self.play(Create(equal_sign))
        self.wait(3.5)

        self.play(ReplacementTransform(always_equal_value_texts, value_equal_1), run_time=1)
        self.wait(3)
        self.play(ReplacementTransform(value_equal_1, value_equal_2), run_time=1)
        self.wait(2)
        self.play(ReplacementTransform(value_equal_2, price_frac), run_time=1)
        self.wait(1.5)
        self.play(ReplacementTransform(price_frac, final_price_per_btc), run_time=1)
        self.wait(1.5)

        ##### 이것은 모두 미리 작성된 프로그래밍 언어의 스크립트를 실행하는 것으로 이루어집니다
        ##### 스마트 컨트랙트 덕분에 우리는 중앙화 거래서와 같은 제3자를 거치지 않을 수 있게 됐습니다
        all_thanks_to = Tex('Without a third party entity', 'All thanks to Smart Contract').arrange(D).shift(D * 3)
        self.play(ReplacementTransform(final_price_per_btc, all_thanks_to))
        self.wait(11)

        liq_prov_graph.clear_updaters()
        self.play(FadeOut(Group(*self.mobjects)))
        self.wait(0.5)

class working2(Scene):
    def construct(self):
        self.add(NumberPlane().set_z_index(1))
        speak(self, title='Scene2', txt=
        '간단하게 오토매틱 마켓 메이커를 통해 덱스가 돌아가는 원리를 배웟는데, 이젠 약간의 수학과 함께 더욱 자세히 알아보겠습니다#1'
        '엑스와이는 케이에서 엑스를 이항시키면 와이는 엑스분의 케이 형태입니다#1'
        '여러분 모두 중학교 때 함수를 배웠을 것이고, 기본적인 와이는 이엑스도 배웠고 와이는 엑스분의 1을 배운 기억이 날겁니다#1'
        '그중에 엑스분의 1함수는 반비례함수라고 배웠고 쌍곡선의 형태를 띄는 함수입니다. 그리고 이 반비레함수는 케이값에 따라서 보이는 것과 같이 원점에서 점점 멀어지는 함수입니다#1'
        '일반적인 오토매틱 마켓메이커는 이 함수를 사용해 가격을 결정합니다. 도대체 어떻게 가격을 결정하는지 알아보겠습니다#1'
        '여기서 엑스는 에이코인의 양, 와이는 비코인의 양입니다#1 '
        '페어라는 것이 원래 양방향이어서 서로 바꿔도 무방하나 앞으로 이해하기 쉽게 풀내부의 베이스에셋의 양이 엑스, 쿼트에셋의 양이 와이라고 하겠습니다#1'



              , keep_pitch=True, update=True, speed=1.4)

        # TODO 7.877 secs간단하게 오토매틱 마켓 메이커를 통해 덱스가 돌아가는 원리를 배웟는데, 이젠 약간의 수학과 함께 더욱 자세히 알아보겠습니다

        # TODO 1.0 secs pause

        amm_text = Tex('AMM').scale(2)
        with_math_text = Tex('with Math').next_to(amm_text, D)

        self.play(Create(amm_text), run_time=2)
        self.wait(1.5)
        self.play(Create(with_math_text), run_time=2)
        self.wait(1)

        self.play(Uncreate(VGroup(amm_text, with_math_text)), run_time=1)
        self.wait(0.5)

        # TODO 4.615 secs엑스와이는 케이에서 엑스를 이항시키면 와이는 엑스분의 케이 형태입니다

        # TODO 1.0 secs pause


        xyk = MathTex('x', r'\times', 'y', '=', 'k').scale(2)
        self.play(Write(xyk), run_time=1)
        self.wait(1)

        xyk_fraction = MathTex('y', '=', r'\frac{k}{x}').scale(2)
        self.play(TransformMatchingShapes(xyk, xyk_fraction), run_time=1.5)
        self.wait(1)

        # TODO 7.84 secs여러분 모두 중학교 때 함수를 배웠을 것이고, 기본적인 와이는 이엑스도 배웠고 와이는 엑스분의 1을 배운 기억이 날겁니다

        # TODO 1.0 secs pause


        self.play(xyk_fraction.animate.scale(0.5).to_edge(U).shift(L * 6), run_time=1)
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
                                 lag_ratio=0.5), run_time=3)
        self.wait(2)

        self.play(Circumscribe(func_3), run_time=1)
        self.wait(1)

        self.play(AnimationGroup(Uncreate(func_1),
                                 Uncreate(func_2),
                                 Uncreate(func_3),
                                 Uncreate(func_4),
                                 Uncreate(func_5),
                                 lag_ratio=0.5), run_time=1)



        self.wait(0.5)
        # TODO 11.331 secs그중에 엑스분의 1함수는 반비례함수라고 배웠고 쌍곡선의 형태를 띄는 함수입니다. 그리고 이 반비레함수는 케이값에 따라서 보이는 것과 같이 원점에서 점점 멀어지는 함수입니다

        # TODO 1.0 secs pause

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
        self.wait(1)

        self.play(k_tracker.animate.set_value(300), run_time=7)
        self.wait(1)

        # TODO 7.502 secs일반적인 오토매틱 마켓메이커는 이 함수를 사용해 가격을 결정합니다. 도대체 어떻게 가격을 결정하는지 알아보겠습니다

        # TODO 1.0 secs pause
        self.wait(5)

        self.play(Uncreate(k_var),run_time=0.5)
        self.play(Uncreate(ax),run_time=0.5)
        self.play(Uncreate(xyk_graph),run_time=0.5)
        self.wait(0.5)

        # TODO 3.54 secs여기서 엑스는 에이코인의 양 와이는 비코인의 양입니다

        # TODO 1.0 secs pause

        # TODO 9.351 secs 페어라는 것이 원래 양방향이어서 서로 바꿔도 무방하나 앞으로 이해하기 쉽게 베이스에셋의 양이 풀내부의 엑스코인의 양, 쿼트에셋의 양이 와이라고 하겠습니다

        # TODO 1.0 secs pause

        B_coin_amt = Tex('B coin amount').shift(L * 4.5)
        A_coin_amt = Tex('A coin amount')
        A_coin_base = Tex('Base asset').next_to(A_coin_amt, D)
        B_coin_quote = Tex('Quote asset').next_to(B_coin_amt, D)
        A_coin_BTC = Tex('BTC').next_to(A_coin_base, D)
        B_coin_USDT = Tex('USDT').next_to(B_coin_quote, D)
        A_coin_texts = VGroup(A_coin_amt, A_coin_base, A_coin_BTC)
        B_coin_texts = VGroup(B_coin_amt, B_coin_quote, B_coin_USDT)

        x_arrow = Arrow(end=A_coin_amt.get_top(), start=xyk_fraction[ 2 ].get_bottom())
        y_arrow = Arrow(end=B_coin_amt.get_top(), start=xyk_fraction[ 0 ].get_bottom())

        self.play(GrowArrow(x_arrow),
                  GrowArrow(y_arrow)
                  , run_time=1)
        self.wait(1)

        self.play(Create(A_coin_texts),
                  Create(B_coin_texts), run_time=2)

        self.wait(7)
        self.play(ApplyWave(A_coin_texts))
        self.play(ApplyWave(B_coin_texts))
        self.wait(0.5)

        self.play(Uncreate(A_coin_texts),
                  Uncreate(B_coin_texts),
                Unwrite(x_arrow),
                  Unwrite(y_arrow)
                  , run_time=1.5)
        self.wait(0.5)
