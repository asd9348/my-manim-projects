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

class L02S00(MovingCameraScene):
    def construct(self):
        speak(self, title='Scene2', txt=
        '이제 본격적으로 디파이에 대해 알아보겠습니다#1'
        '디파이의 가장 근간이 되는 것은 탈중앙화 거래소입니다#1'
        '탈중앙화 거래소는 디센트럴라이즈드 익스체인지로 줄여서 덱스라고 부릅니다#1'
        '탈중앙화 거래소는 말그대로 중앙화된 주체가 없는 거래소입니다#1'
        '모든 거래들이 중앙 주체를 거치지 않고 블록체인에 트랜잭션으로 기록되는 것입니다#1'
        '마치 비트코인 네트워크가 만든사람도 없어진 뒤에 스스로 혼자 계속 작동하듯#1'
        '덱스도 중앙화된 주체 없이 블록체인상에서 끊임없이 돌아갑니다#1'
              , keep_pitch=True, update=False, speed=1.4)

        # TODO 2.912 secs 이제 본격적으로 디파이에 대해 알아보겠습니다
        # TODO 1.0 secs pause
        self.camera.frame.save_state()

        DEFI_lec2_title = Tex(r'DEFI Series\\Episode 2').scale(2)
        DEFI_lec2_subtitle = Tex(r'DEX and AMM').next_to(DEFI_lec2_title, D)

        self.play(Create(DEFI_lec2_title),run_time=0.5)
        self.play(Create(DEFI_lec2_subtitle),run_time=0.5)
        self.wait(1)
        self.play(Uncreate(VGroup(DEFI_lec2_title, DEFI_lec2_subtitle)))
        self.wait(0.912)

        # TODO 3.492 secs 디파이의 가장 근간이 되는 것은 탈중앙화 거래소입니다
        # TODO 1.0 secs pause
        decentralized_ex = Tex('Decentralized Exchange', substrings_to_isolate=[ 'D', 'E' ]).scale(2)

        dex_text = Tex('DEX').scale(2)

        self.play(Create(decentralized_ex, run_time=3))
        self.wait(1.4)

        # TODO 4.724 secs 탈중앙화 거래소는 디센트럴라이즈드 익스체인지로 줄여서 덱스라고 부릅니다
        # TODO 1.0 secs pause
        self.play(ReplacementTransform(decentralized_ex, dex_text), run_time=2)
        self.wait(3.724)

        # self.play(Uncreate(dex_text), run_time=1.724)

        # TODO 3.974 secs 그동안 설명했던 중앙화 거래소와 어떻게 다른지 알아보겠습니다

        # TODO 1.0 secs pause

        # TODO 3.987 secs 탈중앙화 거래소는 말그대로 중앙화된 주체가 없는 거래소입니다

        dex_expl_text = Tex(r'Exchange\\without centralized entities').scale(2)
        self.play(ReplacementTransform( dex_text, dex_expl_text), run_time=2)
        self.wait(1.5)
        self.play(Uncreate(dex_expl_text))

        # TODO 1.0 secs pause

        # TODO 5.171 secs 모든 거래들이 중앙 주체를 거치지 않고 블록체인에 트랜잭션으로 기록되는 것입니다

        # TODO 1.0 secs pause

        ex_server_rect = RoundedRectangle(width=1.2, height=0.5, corner_radius=0.1)
        ex_server_led_1 = Dot(radius=0.05, fill_color=GREEN).shift(RIGHT * 0.2)
        ex_server_led_2 = Dot(radius=0.05, fill_color=GREEN).shift(RIGHT * 0.4)

        ex_server_1 = VGroup(ex_server_rect, ex_server_led_1, ex_server_led_2)
        ex_server_2 = ex_server_1.copy().next_to(ex_server_1,D,buff=0)
        ex_server_3 = ex_server_1.copy().next_to(ex_server_2,D,buff=0)

        ex_server = VGroup(ex_server_1,ex_server_2,ex_server_3).shift(L*4)

        order_box = Rectangle(width=1, height=1.6)
        order_text = Tex(r'Alice\\gave\\Bob\\1 BTC').scale(0.4)
        order = VGroup(order_box,order_text).shift(L*10)




        block = Square(2.5)
        block_txs = Tex(r'1010111100010100\\'
                        r'0101011001000111\\'
                        r'1110100000111100\\'
                        r'0001011111001000\\'
                        r'0101001100010010\\'
                        r'0001010001101101\\'
                        r'1101001011101011\\'
                        ).arrange(D).scale(0.5)

        block_text_1 = Tex(r'Alice gave Bob 1 BTC','Kenny gave Ron 3 BTC','Rick gave Morty 6 BTC',r'\vdots').arrange(D).scale(0.4)

        # block_text =VGroup(block_text_1,block_text_2,block_text_3,block_text_4)

        block_txs.save_state()
        self.play(Create(block))
        self.play(Create(ex_server))
        self.play(order.animate.next_to(ex_server,L,buff=0.75))

        # order_arc = ArcBetweenPoints(order.get_center(), order.get_center()+R*3.5,radius=-5)
        # self.play(MoveAlongPath(order,order_arc))
        self.play(FadeOut(ex_server, shift=U))

        self.play(ReplacementTransform(order, block_txs))

        # self.play(Create(block_txs))
        # self.wait(0.5)
        self.play(self.camera.frame.animate.set(width=block.width * 1.2),
                  Transform(block_txs, block_text_1), run_time=1.5)

        self.wait(0.5)
        self.play(Restore(self.camera.frame),
                  Restore(block_txs), run_time=1)

        # TODO 4.929 secs 마치 비트코인 네트워크가 만든사람도 없어진 뒤에 스스로 혼자 계속 작동하듯

        # TODO 1.0 secs pause

        # TODO 4.24 secs 덱스도 중앙화된 주체 없이 블록체인상에서 끊임없이 돌아갑니다

        # TODO 1.0 secs pause

        curve_arrow_1 = CurvedArrow(L * 2, U * 2, radius=-2).scale(0.85)
        curve_arrow_2 = CurvedArrow(U * 2, R * 2, radius=-2).scale(0.85)
        curve_arrow_3 = CurvedArrow(R * 2, D * 2, radius=-2).scale(0.85)
        curve_arrow_4 = CurvedArrow(D * 2, L * 2, radius=-2).scale(0.85)

        curve_arrows = VGroup(curve_arrow_1, curve_arrow_2, curve_arrow_3, curve_arrow_4).scale(1.3)

        self.play(Create(curve_arrows))

        self.play(Rotate(curve_arrow_1, angle=-PI, about_point=O),
                  Rotate(curve_arrow_2, angle=-PI, about_point=O),
                  Rotate(curve_arrow_3, angle=-PI, about_point=O),
                  Rotate(curve_arrow_4, angle=-PI, about_point=O),
                  rate_func=linear, run_time=10)

        self.wait(5)


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

        shit_coin = create_circle_asset(Tex(r'\textbf{SHIT}', color=WHITE, font_size=25), fill_color=C0492).scale_to_fit_width(2).shift(U * 2).to_edge(L)
        poop_coin = create_circle_asset(Tex(r'\textbf{POOP}', color=WHITE, font_size=25), fill_color=C0493).scale_to_fit_width(2).shift(D * 3).to_edge(L)
        btc_coin = create_circle_asset(Tex(r'\textbf{BTC}',color=WHITE, font_size =30),  fill_color=C_BTC).scale_to_fit_width(2).to_edge(L).shift(0.5 * D)

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

        # SHIT_COIN = create_circle_asset(Tex(r'\textbf{SHIT}', color=WHITE, font_size=25), fill_color=C0492)
        # POOP_COIN = create_circle_asset(Tex(r'\textbf{POOP}', color=WHITE, font_size=25), fill_color=C0493)

        shit_coin = create_circle_asset(Tex(r'\textbf{SHIT}', color=WHITE, font_size=25), fill_color=C0492).scale_to_fit_width(1).shift(U * 1).to_edge(L)
        poop_coin = create_circle_asset(Tex(r'\textbf{POOP}', color=WHITE, font_size=25), fill_color=C0493).scale_to_fit_width(1).shift(D * 1).to_edge(L)

        any_pairs = Tex('Anyone can make pairs', 'POOP-USDT', 'SHIT-BTC', 'SHIT-POOP', r'\vdots').arrange(D).next_to(dex_text, D, buff=1)

        random_coin_1 = create_circle_asset(Tex(r'\textbf{BLAH}', color=WHITE, font_size=25), fill_color=C0893).scale_to_fit_width(1).shift(U * 3).to_edge(L)
        random_coin_2 = create_circle_asset(Tex(r'\textbf{BLUH}', color=WHITE, font_size=25), fill_color=C2593).scale_to_fit_width(1).shift(D * 3).to_edge(L)

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


class L02S04(Scene):
    def construct(self):
        speak(self, title='L02S04', txt=
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

class L02S05(Scene):
    def construct(self):
        speak(self, title='Scene2', txt=
        '간단하게 오토매틱 마켓 메이커를 통해 덱스가 돌아가는 원리를 배웟는데, 이젠 약간의 수학과 함께 더욱 자세히 알아보겠습니다#1'
        '엑스와이는 케이에서 엑스를 이항시키면 와이는 엑스분의 케이 형태입니다#1'
        '여러분 모두 중학교 때 함수를 배웠을 것이고, 기본적인 와이는 이엑스도 배웠고 와이는 엑스분의 1을 배운 기억이 날겁니다#1'
        '그중에 엑스분의 1함수는 반비례함수라고 배웠고 쌍곡선의 형태를 띄는 함수입니다. 그리고 이 반비레함수는 케이값에 따라서 보이는 것과 같이 원점에서 점점 멀어지는 함수입니다#1'
        '일반적인 오토매틱 마켓메이커는 이 함수를 사용해 가격을 결정합니다. 도대체 어떻게 가격을 결정하는지 알아보겠습니다#1'
        '여기서 엑스는 에이코인의 양, 와이는 비코인의 양입니다#1 '
        '페어라는 것이 원래 양방향이어서 서로 바꿔도 무방하나 앞으로 이해하기 쉽게 풀내부의 베이스에셋의 양이 엑스, 쿼트에셋의 양이 와이라고 하겠습니다#1'
        '복잡하게 생각할 건 없고 와이는 엑스분의 케이 그래프에서 케이는 그냥 어떤 값입니다#1'
        '그런데 아까 우리는 케이가 엑스 곱하기 와이인 걸 봤습니다#1'
        '그렇다면 현재 비티씨테더 풀에 10비트코인과 3000테더가 있으니 k는 10곱하기 3000인 30000입니다#1'
        '아까 말한 것처럼 가격은 풀에 각 코인이 얼마나 있는지로 결정되기 때문에 우리는 풀의 상태, 정확히 얘기하면 풀 내부의 베이스 에셋과 쿼트 에셋의 비율로 가격을 계산할 수 있습니다#1'
        '풀의 상태는 아까 본 와이는 엑스분의 케이라는 함수의 그래프 위의 한 점으로 나타낼 수 있습니다. 여기에는 가격정보도 들어있는 것입니다#1'
        '거래자가 풀에서 비티씨를 매수하거나 매도한다는 것은 풀의 상태를 변화 시키는 것이기에 현재 있는 지점에서 그래프 상의 다른 지점으로 이동한다는 것입니다#1'
        '유동성 제공자가 유동성을 공급하거나 제거한다는 것은 케이값을 움직이는 것입니다.#1'
        '유동성을 공급하는 것은 비티씨와 테더를 같이 넣어주는 것이고, 그건 엑스와 와이가 둘다 늘어나기 때문에 케이값이 커지는 것입니다#1'
        '유동성을 제거하면 비티씨와 테더가 같이 빠져나가는 것이고, 엑스와 와이가 둘다 줄면 당연히 케이값도 줄어듭니다#1'

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

        self.play(Uncreate(k_var), run_time=0.5)
        self.play(Uncreate(ax), run_time=0.5)
        self.play(Uncreate(xyk_graph), run_time=0.5)
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
                  Unwrite(y_arrow),
                  run_time=1.5)
        self.wait(0.5)

        ############################################################################

        # TODO 5.448 secs복잡하게 생각할 건 없고 와이는 엑스분의 케이 그래프에서 케이는 그냥 어떤 값입니다
        # TODO 1.0 secs pause
        # TODO 3.612 secs그런데 아까 우리는 케이가 엑스 곱하기 와이인 걸 봤습니다
        # TODO 1.0 secs pause
        # TODO 4.325 secs그렇다면 현재 비티씨테더 풀의 식은 10곱하기 3000인 30000입니다
        # TODO 1.0 secs pause

        k_var = Variable(1, MathTex("k"), var_type=Integer).next_to(xyk_fraction, R, buff=2)
        k_tracker = k_var.tracker
        k_tracker.set_value(1)

        xyk_form = MathTex(r'x\times y=k').scale(2)

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

        coor_sys = VGroup(xyk_graph_btc, ax, axis_labels)

        self.play(Create(xyk_form), run_time=1.5)
        self.wait(1)
        self.play(Uncreate(xyk_form), run_time=1.5)
        self.play(Create(k_var), run_time=1)
        self.play(Create(coor_sys), run_time=2)
        self.wait(1)

        # self.play(Create(axis_labels))
        # self.play(Create(xyk_graph_btc))

        ##### 자 그렇다면 현재 비티씨테더 풀의 함10비트코인과 3000테더이기에 곱하기 3000인 30000입니다다
        # 케이값은 30000으로 변경
        self.play(k_tracker.animate.set_value(30000), run_time=6)
        self.wait(t)

        # TODO 11.139 secs아까 말한 것처럼 가격은 풀에 각 코인이 얼마나 있는지로 결정되기 때문에 우리는 풀의 상태, 정확히 얘기하면 풀 내부의 베이스 에셋과 쿼트 에셋의 비율로 가격을 계산할 수 있습니다
        # TODO 1.0 secs pause
        # TODO 8.276 secs풀의 상태는 아까 본 와이는 엑스분의 케이라는 함수의 그래프 위의 한 점으로 나타낼 수 있습니다. 여기에는 가격정보도 들어있는 것입니다
        # TODO 1.0 secs pause

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

        self.play(Create(curr_dot), run_time=1.5)
        self.play(Create(dot_label), run_time=2)

        self.wait(1)

        dot_label_2 = MathTex(
            rf'({btc_tracker.get_value():.0f},{usdt_tracker.get_value():.0f})\  {usdt_tracker.get_value() / btc_tracker.get_value():.0f}USDT',
            font_size=35).next_to(curr_dot, UR)

        self.play(ReplacementTransform(dot_label, dot_label_2), run_time=5)
        dot_label_2.add_updater(lambda dot: dot.become(MathTex(
            rf'({btc_tracker.get_value():.0f},{usdt_tracker.get_value():.0f})\  {usdt_tracker.get_value() / btc_tracker.get_value():.0f}USDT',
            font_size=35).next_to(
            curr_dot, UR)))

        self.wait(11)

        # TODO 9.109 secs거래자가 풀에서 비티씨를 매수하거나 매도한다는 것은 풀의 상태를 변화 시키는 것이기에 현재 있는 지점에서 그래프 상의 다른 지점으로 이동한다는 것입니다
        # TODO 1.0 secs pause

        buy_btc = Tex(r'BUY', 'BTC').arrange(D).scale(2).shift(R * 4)
        buy_btc.set_color_by_tex("BUY", GREEN)
        # buy_btc.set_color_by_tex("T", RED)
        # buy_btc.set_color_by_tex("B", BLUE)
        sell_btc = Tex(r'SELL', 'BTC').arrange(D).scale(2).shift(R * 4)
        sell_btc.set_color_by_tex("SELL", RED)

        self.play(Create(buy_btc), run_time=1)
        self.wait(1)
        self.play(btc_tracker.animate.set_value(7),
                  usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
                  run_time=1)
        self.wait(1)

        self.play(Uncreate(buy_btc), run_time=1)
        self.wait(1)

        self.play(Create(sell_btc), run_time=1)
        self.wait(1)
        self.play(btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)),
                  run_time=1)
        self.wait(1)

        self.play(Uncreate(sell_btc), run_time=1)

        # TODO 5.267 secs유동성 제공자가 유동성을 공급하거나 제거한다는 것은 케이값을 움직이는 것입니다.
        # TODO 1.0 secs pause
        # TODO 8.457 secs유동성을 공급하는 것은 비티씨와 테더를 같이 넣어주는 것이고, 그건 엑스와 와이가 둘다 늘어나기 때문에 케이값이 커지는 것입니다
        # TODO 1.0 secs pause
        add_liq = Tex(r'ADD', 'Liquidity').arrange(D).scale(2).shift(R * 4)
        add_liq.set_color_by_tex("ADD", GREEN)

        rmv_liq = Tex(r'REMOVE', 'Liquidity').arrange(D).scale(2).shift(R * 4)
        rmv_liq.set_color_by_tex("REMOVE", RED)
        self.wait(5)

        self.play(Create(add_liq), run_time=1)
        self.wait(1)

        self.play(k_tracker.animate.set_value(35000),
                  btc_tracker.animate.set_value(sqrt(35000 * 13 ** 2 / 30000)),
                  usdt_tracker.animate.set_value(35000 / sqrt(35000 * 13 ** 2 / 30000)),
                  run_time=4)
        self.wait(1)

        self.play(Uncreate(add_liq), run_time=1)
        self.wait(1)

        # TODO 7.55 secs유동성을 제거하면 비티씨와 테더가 같이 빠져나가는 것이고, 엑스와 와이가 둘다 줄면 당연히 케이값도 줄어듭니다
        # TODO 1.0 secs pause

        self.play(Create(rmv_liq), run_time=1)
        self.wait(1)

        self.play(k_tracker.animate.set_value(25000),
                  btc_tracker.animate.set_value(sqrt(25000 * 13 ** 2 / 30000)),
                  usdt_tracker.animate.set_value(25000 / sqrt(25000 * 13 ** 2 / 30000)), run_time=4)
        self.wait(1)
        self.play(Uncreate(rmv_liq), run_time=1)
        self.wait(1)

        self.play(Uncreate(VGroup(xyk_fraction, k_var, curr_dot, dot_label_2, coor_sys)), run_time=1)
        self.wait(1)

        self.wait(5)
class L02S06(MovingCameraScene):
    def construct(self):
        # self.add(NumberPlane().set_z_index(1))
        speak(self, title='L02S06', txt=
        '아까본 10비트와 3000테더를 원점으로 생각하고 실제 상황에 따라 어떻게 변하는지 보겠습니다#1'
        '지금부터 최초로 유동성을 공급하고 일부를 제거하는 상황을 알아보겠습니다#1'
        '지금보시는 건 최초의 유동성제공자로 이 사람이 풀을 최초로 만들게 됩니다.#1'
        '비트코인과 테더를 같이 풀에 넣어서, 즉 엑스와 와이값이 증가하면서 엑스 곱하기 와이였던 케이의 값도 30000이 됐습니다#1'
        '그리고 케이는 엑스 곱하기 와이이기 때문에 현재 보고있는 파란 사각형의 넓이이기도 합니다.#1'
        '그런데 유동성을 공급하는데는 조건이 있습니다. 반드시 비티씨와 테더를 함께 같은 가치만큼 넣어야된다는 것입니다#1'
        '여기에는 이유가 있습니다. 쉽게 생각하면 유동성 공급 자체는 가격을 움직일 이유가 아니기 때문입니다#1'
        '비유하자면 하우스와 도박꾼같은 것인데 하우스는 장소와 환경을 제공할 뿐이지 카드를 조작한다든가 하는 식으로 도박 자체를 조작하면 안 됩니다. #1'
        '덱스에서 가격은 풀 내부의 비티씨와 테더 비율에 따라 결정됩니다. 1비티씨가 몇 테더에 상응하는지로 우리는 가격을 생각합니다 #1'
        '만약 현재 가격대로 같은 가치만큼의 비티씨와 테더를 넣지 않으면 풀 내부의 비율이 깨지게 되고, 우리는 단순히 유동성을 공급했는데 가격을 변화시켜버립니다#1'
        '비티씨를 12개를 넣었다면 가격은 보시는 것과 같이 250테더가 되어버립니다#1'
        '그래서 현재 비티씨가 300테더라면 그에 맞게 넣어야합니다. 지금은 초기공급자이기 때문에 마음대로 넣을 수 있고 앞으로 유동성을 추가할 때는 무조건 가격에 맞게 넣어야합니다#1'
        '그럼 초기 공급자가 가격을 맘대로 하는 거냐고 생각하실 수도 있는데 그것은 영상 마지막에 다루겠습니다#1'
        '그리고 이것과 연결되어 유동성 풀의 지분을 확인할 수 없게 됩니다#1'
        '유동성 풀의 지분은 엘피 토큰으로 증명합니다. 유동성 제공자는 비티씨와 테더를 풀에 넣고 그에 상응하는 엘피 토큰을 받습니다#1'
        '최초로 풀을 만들게 되면 엘피 토큰이 루트 엑스와이 만큼 초기 발행되고 이후 유동성을 추가하면 토큰이 추가 발행되고, 유동성을 제거하면 풀에서 전체 발행량분의 자신의 발행량만큼의 비티씨와 테더를 빼가고 엘피 토큰은 없어집니다#1'
        '풀내부의 비티씨 테더 비율을 깨거나 테더와 비트코인 중 하나만 넣는다는 것은 가격을 움직이는 것이고 유동성을 추가하거나 제거하면 미래에 가격이 변동하면서 풀내부의 비율이 변해버릴 때 유동성 공급자의 지분을 산정할 수 없습니다#1'
        '위와 같은 이유로 유동성 풀에는 두 코인을 현재 풀에서 계산되는 가격에 맞게 같은 가치만큼만 넣게 설정되어 있습니다#1'
        '이쯤 되면 도대체 왜 유동성 공급을 해야하는가 궁금해집니다. 이건 뭐 자선사업도 아니고 그냥 남좋은 일 하는 걸까요#1'
        '유동성공급을 할 이유가 없다면 사람들이 안 할 것이고 그러면 덱스도 존재할 수 없게 됩니다#1'
        '그래서 유동성 공급을 하면 수수료를 벌 수있게 만들어놧습니다#1'
        '아까처럼 풀에서 코인을 사고 팔 때 수수료가 들고 그 수수료느 풀에 쌓이고 유동성 공급자들은 유동성을 제거할 때, 그동안 수수료가 쌓인 더 커진 풀에서 본인 지분을 가져오기 때문에 수익을 얻을 수 있습니다.#1'
              , keep_pitch=True, update=1, speed=1.4)

        # TODO 6.209 secs아까본 10비트와 3000테더를 원점으로 생각하고 실제 상황에 따라 어떻게 변하는지 보겠습니다

        # TODO 1.0 secs pause

        # TODO 3.189 secs지금부터 유동성을 공급하는 상황을 알아보겠습니다

        # TODO 1.0 secs pause

        xyk_fraction = MathTex('y', '=', r'\frac{k}{x}').to_edge(UL)

        liq_pool_rect = RoundedRectangle(height=6.3, width=4, corner_radius=0.5)
        liq_pool_text = Tex('Liquidity Pool').next_to(liq_pool_rect, UP)
        liq_pool = VGroup(liq_pool_rect, liq_pool_text).to_edge(UL).shift(R * 0.5)
        liq_pool.set_z_index(3)

        k_var = Variable(30000, MathTex("k"), var_type=Integer).to_edge(UR)
        k_tracker = k_var.tracker
        k_tracker.set_value(30000)

        # TODO 4.868 secs지금보시는 건 최초의 유동성제공자로 이 사람이 풀을 최초로 만들게 됩니다.

        # TODO 1.0 secs pause

        liq_provider = create_entity(Tex(r' \emph{Init Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", C_BTC, 1.4,
                                     0.3,asset_text_color=WHITE).next_to(liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", C_USDT, 1.4, 0.3,asset_text_color=WHITE)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)
        liq_provider.add(usdt_asset)

        self.play(Create(liq_provider), run_time=3)
        self.wait(6.498)

        # TODO 7.997 secs비트코인과 테더를 같이 풀에 넣어서, 즉 엑스와 와이값이 증가하면서 엑스 곱하기 와이였던 케이의 값도 30000이 됐습니다

        # TODO 1.0 secs pause

        # TODO 5.847 secs그리고 케이는 엑스 곱하기 와이이기 때문에 현재 보고있는 파란 사각형의 넓이이기도 합니다.

        # TODO 1.0 secs pause



        ax = Axes(x_range=[ 0, 18, 4 ], y_range=[ 0, 6500, 1000 ], x_length=5, y_length=5, tips=True,
                  axis_config={"include_numbers": False, 'color': WHITE, 'include_ticks': False, 'font_size': 20}, ).to_edge(DR, buff=0.8)

        ax.shift(U * (liq_pool_rect.get_bottom()[ 1 ] - ax[ 0 ].get_y()))

        y_axis_label = ax.get_y_axis_label(MathTex('Amount of USDT in Pool', color=WHITE).rotate(PI / 2).scale(0.4), edge=LEFT,
                                           direction=LEFT, buff=0.37)
        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool', color=WHITE).scale(0.4), edge=DOWN, direction=DOWN, buff=0.37)
        axis_labels = VGroup(x_axis_label, y_axis_label)

        usdt_bar = Rectangle(height=3, width=1.2, fill_color=C_USDT, fill_opacity=1, color=C_USDT)
        btc_bar = Rectangle(height=1, width=1.2, fill_color=C_BTC, fill_opacity=1, color=C_BTC)
        bars = VGroup(btc_bar, usdt_bar)
        bars.arrange(RIGHT, aligned_edge=DOWN).move_to(liq_pool_rect).align_to(liq_pool_rect, DOWN)

        usdt_bar_pos = usdt_bar.get_bottom()
        btc_bar_pos = btc_bar.get_bottom()

        btc_var = Variable(10, MathTex("BTC"), var_type=Integer)
        usdt_var = Variable(3000, MathTex("USDT"), var_type=Integer).next_to(btc_var, DOWN, aligned_edge=LEFT)
        btc_tracker = btc_var.tracker
        usdt_tracker = usdt_var.tracker
        usdt_var[ 0 ][ 0 ].set_color(C_USDT)
        btc_var[ 0 ][ 0 ].set_color(C_BTC)

        vars = VGroup(btc_var, usdt_var).arrange(DOWN, aligned_edge=LEFT).next_to(liq_pool_rect, DOWN, buff=0.25)
        # self.play(Create(liq_pool), run_time=1)
        # self.wait(1)

        self.play(Create(liq_pool),
                  ReplacementTransform(usdt_asset, usdt_bar),
                  ReplacementTransform(btc_asset, btc_bar), run_time=6)
        self.wait(1)
        self.play(Write(usdt_var),
                  Write(btc_var), run_time=2)
        self.wait(1)
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=C_USDT, fill_opacity=1, color=C_USDT).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=C_BTC, fill_opacity=1, color=C_BTC).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        pool_price = Variable(100, 'Price', var_type=DecimalNumber, num_decimal_places=2).next_to(
            liq_pool_rect, RIGHT, buff=0.5).scale(0.8).to_edge(UP)
        pool_price_tracker = pool_price.tracker
        pool_price.add_updater(lambda v: pool_price_tracker.set_value(usdt_tracker.get_value() / btc_tracker.get_value()))
        pool_price_unit = Tex(r'USDT').scale(0.75).next_to(pool_price, buff=0.1)
        pool_price.add(pool_price_unit)
        self.play(Write(k_var[ 0 ]), run_time=1.5)
        self.wait(1)
        self.play(Create(ax),
                  Create(axis_labels),
                  Create(pool_price),
                  TransformMatchingShapes(Group(btc_var[ 1 ].copy(), usdt_var[ 1 ].copy()), k_var[ 1 ]),
                  Create(xyk_fraction.next_to(k_var, LEFT, buff=1)), run_time=5
                  )

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
        x_marker = Triangle(color=C_BTC, fill_color=C_BTC, fill_opacity=1).scale(0.1).next_to(vertical_line, DOWN, buff=0)
        x_marker.add_updater(lambda marker: marker.next_to(vertical_line, DOWN, buff=0))
        x_marker_val = Integer(btc_tracker.get_value())
        x_marker_val.add_updater(
            lambda integer: integer.become(Integer(btc_tracker.get_value()).scale(0.4).next_to(vertical_line, DOWN, buff=0.3)))

        y_marker = Triangle(color=C_USDT, fill_color=C_USDT, fill_opacity=1).scale(0.1).rotate(-PI / 2).next_to(horizontal_line, LEFT,
                                                                                                                buff=0)
        y_marker.add_updater(lambda marker: marker.next_to(horizontal_line, LEFT, buff=0))
        y_marker_val = Integer(usdt_tracker.get_value())
        y_marker_val.add_updater(lambda integer: integer.become(
            Integer(usdt_tracker.get_value()).scale(0.4).rotate(PI / 2).next_to(horizontal_line, LEFT, buff=0.3)))

        lines = VGroup(vertical_line, horizontal_line)
        markers = VGroup(x_marker, x_marker_val, y_marker, y_marker_val)

        self.play(Create(xyk_graph_btc), run_time=0.5)
        self.wait(0.5)
        self.play(Create(curr_dot), run_time=0.5)
        self.play(Create(lines), run_time=1.5)
        self.play(Create(markers), run_time=0.5)
        self.wait(0.5)

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
        self.play(Create(area), run_time=0.5)
        self.play(Create(area_text), run_time=0.5)

        self.wait(5.5)
        # TODO 7.345 secs그런데 유동성을 공급하는데는 조건이 있습니다. 반드시 비티씨와 테더를 함께 같은 가치만큼 넣어야된다는 것입니다

        # TODO 1.0 secs pause

        self.play(Circumscribe(pool_price))
        self.play(Circumscribe(VGroup(btc_var, usdt_var)))

        # TODO 6.488 secs여기에는 이유가 있습니다. 쉽게 생각하면 유동성 공급 자체는 가격을 움직일 이유가 아니기 때문입니다
        # TODO 1.0 secs pause
        # TODO 8.891 secs비유하자면 하우스와 도박꾼같은 것인데 하우스는 장소와 환경을 제공할 뿐이지 카드를 조작한다든가 하는 식으로 도박 자체를 조작하면 안 됩니다.
        # TODO 1.0 secs pause

        self.wait(20.379)
        # TODO 8.021 secs덱스에서 가격은 풀 내부의 비티씨와 테더 비율에 따라 결정됩니다. 1비티씨가 몇 테더예 상응하는지로 우리는 가격을 생각합니다
        # TODO 1.0 secs pause
        # TODO 10.075 secs만약 현재 가격대로 같은 가치만큼의 비티씨와 테더를 넣지 않으면 풀 내부의 비율이 깨지게 되고, 우리는 단순히 유동성을 공급했는데 가격을 변화시켜버립니다
        # TODO 1.0 secs pause
        # TODO 5.243 secs비티씨를 12개를 넣었다면 가격은 보시는 것과 같이 250테더가 되어버립니다
        # TODO 1.0 secs pause
        # TODO 11.163 secs그래서 현재 비티씨가 300테더라면 그에 맞게 넣어야합니다. 지금은 초기공급자이기 때문에 마음대로 넣을 수 있고 앞으로 유동성을 추가할 때는 무조건 가격에 맞게 넣어야합니다
        # TODO 1.0 secs pause
        # TODO 6.451 secs그럼 초기 공급자가 가격을 맘대로 하는 거냐고 생각하실 수도 있는데 그것은 영상 마지막에 다루겠습니다
        # TODO 1.0 secs pause

        btc_10_equals_usdt_3000 = Tex('10 BTC = 3000 USDT').next_to(liq_provider[0],D).scale(0.6)
        self.play(ApplyWave(VGroup(btc_var, usdt_var)))
        self.play(ApplyWave(pool_price))

        self.play(Create(btc_10_equals_usdt_3000))
        self.play(ApplyWave(btc_10_equals_usdt_3000))
        self.wait(1)
        self.wait(9)
        self.play(Uncreate(btc_10_equals_usdt_3000))

        self.play(btc_tracker.animate.set_value(12),
                  k_tracker.animate.set_value(36000), run_time=6)
        self.wait(4)
        self.play(btc_tracker.animate.set_value(10),
                  k_tracker.animate.set_value(30000), run_time=6)
        self.wait(6)

        only_init_is_an_exception = Tex(r'Only Init provider is\\an exception.').next_to(liq_provider[0],U)
        self.wait(3)
        #3초앞으로 보내기만

        self.play(Create(only_init_is_an_exception))
        self.wait(2)
        self.play(Uncreate(only_init_is_an_exception))
        self.wait(1.5)

        how_much= Tex('How much share?').next_to(liq_provider[0],U)
        q_marks = VGroup(Tex('?'),Tex('?').scale(1.5),Tex('?')).arrange(R).move_to(how_much)

        self.play(Create(how_much))
        self.wait(1)
        self.play(ReplacementTransform(how_much,q_marks))
        self.wait(1)
        self.play(Uncreate(q_marks))
        self.wait(0.5)

        #확인할 수 없게 됩니다 텍스트
        # TODO 4.096 secs그리고 이것과 연결되어 유동성 풀의 지분을 확인할 수 없게 됩니다

        # TODO 1.0 secs pause

        # TODO 8.106 secs유동성 풀의 지분은 엘피 토큰으로 증명합니다. 유동성 제공자는 비티씨와 테더를 풀에 넣고 그에 상응하는 엘피 토큰을 받습니다

        # TODO 1.0 secs pause

        # TODO 14.497 secs최초로 풀을 만들게 되면 엘피 토큰이 초기 발행되고 이후 유동성을 추가하면 토큰이 추가 발행되고, 유동성을 제거하면 전체 발행량분의 자신의 발행량으로 계산되는 비율대로 풀에서 비티씨와 테더를 빼가고 엘피 토큰은 없어집니다

        # TODO 1.0 secs pause

        # TODO 11.743 secs풀내부의 비티씨 테더 비율을 깨면서 즉 가격을 움직이면서 유동성을 추가하거나 제거하면 미래에 가격이 변동하면서 풀내부의 비율이 변해버릴 때 유동성 공급자의 지분을 산정할 수 없습니다

        # TODO 1.0 secs pause

        # TODO 8.782 secs테더 없이 비트코인만 넣었는데 비트코인과 테더의 가치가 변동하면 그 풀에서는 얼마만큼의 지분을 가지는지 명료하게 판단할 수가 없습니다

        # TODO 1.0 secs pause

        # TODO 7.55 secs위와 같은 이유로 유동성 풀에는 두 코인을 현재 풀에서 계산되는 가격에 맞게 같은 가치만큼만 넣게 설정되어 있습니다

        # TODO 1.0 secs pause

        lp_token = Tex('LP token').scale(1.5).next_to(liq_provider[ 0 ], UP)
        lp_amt_form_1 = MathTex(r'Init\  l =\sqrt{x \times y}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_2 = MathTex(r'Init\  l =\sqrt{10 \times 3000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_form_3 = MathTex(r'Init\  l =\sqrt{30000}').next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_amt_int = Tex(rf'{int(30000 ** (1 / 2))} LP token').move_to(lp_amt_form_1).scale(0.7)

        self.play(Create(lp_token), run_time=1)
        self.wait(1)
        # 1초 뒤에 나오기
        self.wait(4)
        self.play(TransformMatchingShapes(lp_token, lp_amt_form_1), run_time=1)
        self.wait(2)
        self.play(TransformMatchingShapes(lp_amt_form_1, lp_amt_form_2), run_time=1)
        self.wait(0.5)
        self.play(TransformMatchingShapes(lp_amt_form_2, lp_amt_form_3), run_time=1)
        self.wait(0.5)
        self.play(TransformMatchingShapes(lp_amt_form_3, lp_amt_int), run_time=1)
        self.wait(0.5)

        box = Rectangle(width=1.6, height=1, fill_color=WHITE, stroke_color=WHITE, fill_opacity=1)
        text = Tex(r"173\\BTC-USDT\\LP", color=BLACK).scale(0.5)
        lp_asset = VGroup(box, text).scale(1.3).next_to(liq_provider[ 0 ], DOWN, buff=0.1)

        self.play(FadeIn(lp_asset,target_position=liq_pool_rect),
                  Uncreate(lp_amt_int), run_time=1)
        self.wait(0.5)

        def create_lp_token(text):
            box = Rectangle(width=1.6, height=1, fill_color=WHITE, stroke_color=WHITE, fill_opacity=1)
            text = Tex(text, color=BLACK).scale(0.5)
            return VGroup(box, text)

        # self.play(FadeOut(liq_provider[ 0 ]),
        #           FadeOut(lp_asset), run_time=1)

        # self.play(Create(liq_provider[ 0 ]),
        #           Create(lp_asset), run_time=1)
        lp_asset_121 = create_lp_token(r"121\\BTC-USDT\\LP").scale(1).next_to(liq_provider[ 0 ], DOWN, buff=0.1)
        lp_asset_51 = create_lp_token(r"52\\BTC-USDT\\LP").scale(0.7).next_to(lp_asset_121, DOWN, buff=0.1)
        lp_asset_divided = VGroup(lp_asset_121, lp_asset_51)

        btc_asset = create_entity("A", 0.5, WHITE, "3 BTC", C_BTC, 1.4, 0.3,asset_text_color=WHITE)[ 1 ].next_to(lp_asset_121, D, buff=0.1)
        usdt_asset = create_entity("A", 0.5, WHITE, "900 USDT", C_USDT, 1.4, 0.3,asset_text_color=WHITE)[ 1 ].next_to(btc_asset, DOWN, buff=0.1)
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

        scene4_1500usdt_fill_box = scene4_1500usdt_box.copy().set_fill(C_USDT, opacity=1)
        scene4_5btc_fill_box = scene4_5btc_box.copy().set_fill(C_BTC, opacity=1)

        scene4_5btc_fill_box.set_stroke(width=0, opacity=0)
        scene4_1500usdt_fill_box.set_stroke(width=0, opacity=0)
        scene4_5btc_fill_box.set_z_index(3)
        scene4_1500usdt_fill_box.set_z_index(3)

        self.play(Create(VGroup(scene4_5btc_box, scene4_1500usdt_box)), run_time=0.5)
        self.wait(0.5)

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
            Rectangle(height=2100 / 1000, width=1.2, fill_color=C_USDT, fill_opacity=1, color=C_USDT).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=7 / 10, width=1.2, fill_color=C_BTC, fill_opacity=1, color=C_BTC).move_to(
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
                  Create(scene4_brace_labels), run_time=0.5)
        self.wait(0.5)

        dummydot = Dot(1, color=RED).move_to(liq_pool_rect)

        # self.play(Create(origin_dot))
        self.play(ReplacementTransform(lp_asset, lp_asset_divided), run_time=1)
        self.wait(1)

        self.play(k_tracker.animate.set_value(14700),
                  btc_tracker.animate.set_value(7),
                  usdt_tracker.animate.set_value(14700 / 7),
                  Transform(scene4_1500usdt_fill_box, usdt_asset),
                  Transform(scene4_5btc_fill_box, btc_asset),
                  FadeOut(lp_asset_51, target_position=dummydot),
                  run_time=4, rate_func=rate_functions.ease_in_out_quint)

        self.wait(1)

        self.play(Uncreate(VGroup(scene4_braces,scene4_brace_labels,scene4_5btc_box,scene4_1500usdt_box)))

        btc_bar.clear_updaters()
        usdt_bar.clear_updaters()

        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=C_USDT, fill_opacity=1, color=C_USDT).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=C_BTC, fill_opacity=1, color=C_BTC).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))


        self.play(btc_tracker.animate.set_value(5),
                  usdt_tracker.animate.set_value(2940))
        self.play(btc_tracker.animate.set_value(8),
                  usdt_tracker.animate.set_value(1838))
        self.play(btc_tracker.animate.set_value(12),
                  usdt_tracker.animate.set_value(1225))
        self.play(btc_tracker.animate.set_value(5),
                  usdt_tracker.animate.set_value(2940))
        self.play(btc_tracker.animate.set_value(8),
                  usdt_tracker.animate.set_value(1838))

        now_how_much = Tex(r'Now\\how much share?').next_to(liq_provider[ 0 ], UP)
        cant_calculate_after_fluc = Tex(r"Can't calculate\\how much share").next_to(liq_provider[ 0 ], UP)

        self.play(Create(now_how_much))
        self.wait(3)
        self.play(ReplacementTransform(now_how_much,cant_calculate_after_fluc))
        self.wait(7)

        self.play(Uncreate(cant_calculate_after_fluc))

        self.wait(3)





        # TODO 7.417 secs이쯤 되면 도대체 왜 유동성 공급을 해야하는가 궁금해집니다. 이건 뭐 자선사업도 아니고 그냥 남좋은 일 하는 걸까요
        # TODO 1.0 secs pause
        # TODO 5.461 secs유동성공급을 할 이유가 없다면 사람들이 안 할 것이고 그러면 덱스도 존재할 수 없게 됩니다
        # TODO 1.0 secs pause
        # TODO 3.95 secs그래서 유동성 공급을 하면 수수료를 벌 수있게 만들어놧습니다
        # TODO 1.0 secs pause

        profit= Tex(r'Profit from fees').scale(1.2).next_to(liq_provider[0],U)
        no_defi= Tex(r'Without Pool,\\ No DEX').scale(1.2).next_to(liq_provider[0],U)
        why_lp= Tex(r'Why LP?').scale(1.2).next_to(liq_provider[0],U)
        self.play(Create(why_lp))
        self.wait(9)

        self.play(ReplacementTransform(why_lp,no_defi))
        self.wait(5)
        self.play(ReplacementTransform(no_defi,profit))
        self.wait(15)
        # self.play(Uncreate(profit))

        # TODO 13.156 secs아까처럼 풀에서 코인을 사고 팔 때 수수료가 들고 그 수수료느 풀에 쌓이고 유동성 공급자들은 유동성을 제거할 때, 그동안 수수료가 쌓인 더 커진 풀에서 본인 지분을 가져오기 때문에 수익을 얻을 수 있습니다.

        # TODO 1.0 secs pause

        # self.wait(15)

class L02S07(MovingCameraScene):
    def construct(self):
        # self.add(NumberPlane().set_z_index(1))

        speak(self, title='L02S07', txt=
        '#9'
        '#9'
        '#9'
        '#9'
        '#1'
        '이번에는 다시 원점으로 돌아와서 최초 유동성 공급자가 유동성을 공급하고 추가적으로 다른 사람이 공급하는 경우를 알아보겠습니다#1'
        '유동성을 추가하려고 하니 현재가격에 맞게 3 비티씨를 넣는다면 900테더를 함께 넣어줘야 합니다#1'
        '아까 풀 내부에 비율을 깨면서 안 된다고 한 것처럼 여기서 3비티씨와 800달러, 이렇게 넣을 수는 없습니다#1'
        '최초 공급 이후에 수많은 제공자들이 유동성을 공급하기 시작합니다#1'
        '이렇게 공급할 때마다 전체발행량 분에 자신의 보유량으로 지분을 증명할 수 있도록 발행되고 공급됩니다#1'
        '나중에 누군가가 추가로 공급해도 그 순간마다 두 자산을 같은 비율로 넣어 가격을 바꾸지 않았으면서 넣었다면 공정한 것이고#1'
        '이에 따른 엘피토큰으로 확실히 지분을 몇 퍼센트라고 이견없이 정리할 수 있습니다#1 '
        '그리고 유동성을 제거할 때는 엘피 토큰이 사라지고 자신의 지분만큼 풀에서 돌려받는 것입니다#1'
              , keep_pitch=True, update=1, speed=1.4)

        xyk_fraction = MathTex('y', '=', r'\frac{k}{x}').to_edge(UL)

        liq_pool_rect = RoundedRectangle(height=6.3, width=4, corner_radius=0.5)
        liq_pool_text = Tex('Liquidity Pool').next_to(liq_pool_rect, UP)
        liq_pool = VGroup(liq_pool_rect, liq_pool_text).to_edge(UL).shift(R * 0.5)
        liq_pool.set_z_index(3)

        k_var = Variable(30000, MathTex("k"), var_type=Integer).to_edge(UR)
        k_tracker = k_var.tracker
        k_tracker.set_value(30000)

        liq_provider = create_entity(Tex(r' \emph{Init Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", C_BTC, 1.4,
                                     0.3,asset_text_color=WHITE).next_to(liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", C_USDT, 1.4, 0.3,asset_text_color=WHITE)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)
        liq_provider.add(usdt_asset)

        self.play(Create(liq_provider), run_time=3)
        self.wait(6.498)

        ax = Axes(x_range=[ 0, 18, 4 ], y_range=[ 0, 6500, 1000 ], x_length=5, y_length=5, tips=True,
                  axis_config={"include_numbers": False, 'color': WHITE, 'include_ticks': False, 'font_size': 20}, ).to_edge(DR, buff=0.8)

        ax.shift(U * (liq_pool_rect.get_bottom()[ 1 ] - ax[ 0 ].get_y()))

        y_axis_label = ax.get_y_axis_label(MathTex('Amount of USDT in Pool', color=WHITE).rotate(PI / 2).scale(0.4), edge=LEFT,
                                           direction=LEFT, buff=0.37)
        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool', color=WHITE).scale(0.4), edge=DOWN, direction=DOWN, buff=0.37)
        axis_labels = VGroup(x_axis_label, y_axis_label)

        usdt_bar = Rectangle(height=3, width=1.2, fill_color=C_USDT, fill_opacity=1, color=C_USDT)
        btc_bar = Rectangle(height=1, width=1.2, fill_color=C_BTC, fill_opacity=1, color=C_BTC)
        bars = VGroup(btc_bar, usdt_bar)
        bars.arrange(RIGHT, aligned_edge=DOWN).move_to(liq_pool_rect).align_to(liq_pool_rect, DOWN)

        usdt_bar_pos = usdt_bar.get_bottom()
        btc_bar_pos = btc_bar.get_bottom()

        btc_var = Variable(10, MathTex("BTC"), var_type=Integer)
        usdt_var = Variable(3000, MathTex("USDT"), var_type=Integer).next_to(btc_var, DOWN, aligned_edge=LEFT)
        btc_tracker = btc_var.tracker
        usdt_tracker = usdt_var.tracker
        usdt_var[ 0 ][ 0 ].set_color(C_USDT)
        btc_var[ 0 ][ 0 ].set_color(C_BTC)

        vars = VGroup(btc_var, usdt_var).arrange(DOWN, aligned_edge=LEFT).next_to(liq_pool_rect, DOWN, buff=0.25)
        # self.play(Create(liq_pool), run_time=1)
        # self.wait(1)

        self.play(Create(liq_pool),
                  ReplacementTransform(usdt_asset, usdt_bar),
                  ReplacementTransform(btc_asset, btc_bar), run_time=6)
        self.wait(1)
        self.play(Create(usdt_var),
                  Write(btc_var), run_time=2)
        self.wait(1)
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=C_USDT, fill_opacity=1, color=C_USDT).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=C_BTC, fill_opacity=1, color=C_BTC).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        pool_price = Variable(100, 'Price', var_type=DecimalNumber, num_decimal_places=2).next_to(
            liq_pool_rect, RIGHT, buff=0.5).scale(0.8).to_edge(UP)
        pool_price_tracker = pool_price.tracker
        pool_price.add_updater(lambda v: pool_price_tracker.set_value(usdt_tracker.get_value() / btc_tracker.get_value()))
        pool_price_unit = Tex(r'USDT').scale(0.75).next_to(pool_price, buff=0.1)
        pool_price.add(pool_price_unit)
        self.play(Write(k_var[ 0 ]), run_time=1.5)
        self.wait(1)
        self.play(Create(ax),
                  Create(axis_labels),
                  Create(pool_price),
                  TransformMatchingShapes(Group(btc_var[ 1 ].copy(), usdt_var[ 1 ].copy()), k_var[ 1 ]),
                  Create(xyk_fraction.next_to(k_var, LEFT, buff=1)), run_time=5
                  )

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
        x_marker = Triangle(color=C_BTC, fill_color=C_BTC, fill_opacity=1).scale(0.1).next_to(vertical_line, DOWN, buff=0)
        x_marker.add_updater(lambda marker: marker.next_to(vertical_line, DOWN, buff=0))
        x_marker_val = Integer(btc_tracker.get_value())
        x_marker_val.add_updater(
            lambda integer: integer.become(Integer(btc_tracker.get_value()).scale(0.4).next_to(vertical_line, DOWN, buff=0.3)))

        y_marker = Triangle(color=C_USDT, fill_color=C_USDT, fill_opacity=1).scale(0.1).rotate(-PI / 2).next_to(horizontal_line, LEFT,
                                                                                                                buff=0)
        y_marker.add_updater(lambda marker: marker.next_to(horizontal_line, LEFT, buff=0))
        y_marker_val = Integer(usdt_tracker.get_value())
        y_marker_val.add_updater(lambda integer: integer.become(
            Integer(usdt_tracker.get_value()).scale(0.4).rotate(PI / 2).next_to(horizontal_line, LEFT, buff=0.3)))

        lines = VGroup(vertical_line, horizontal_line)
        markers = VGroup(x_marker, x_marker_val, y_marker, y_marker_val)

        self.play(Create(xyk_graph_btc), run_time=0.5)
        self.wait(0.5)
        self.play(Create(curr_dot), run_time=0.5)
        self.play(Create(lines), run_time=1.5)
        self.play(Create(markers), run_time=0.5)
        self.play(Uncreate(liq_provider), run_time=0.5)
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
        self.play(Create(area), run_time=0.5)
        self.play(Create(area_text), run_time=0.5)

        self.wait(5.5)
        # TODO 8.034 secs이번에는 다시 원점으로 돌아와서 최초 유동성 공급자가 유동성을 공급하고 추가적으로 다른 사람이 공급하는 경우를 알아보겠습니다
        # TODO 0:00:37.000  ~  0:00:45.034
        # TODO 1.0secs pause
        # TODO 0:00:45.034  ~  0:00:46.034

        btc_bar.clear_updaters()
        usdt_bar.clear_updaters()

        liq_provider = create_entity(Tex(r' \emph{New Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "3 BTC", C_BTC, 1.4,
                                     0.3, asset_text_color=WHITE).next_to(
            liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "900 USDT", C_USDT, 1.4, 0.3, asset_text_color=WHITE)[ 1 ].next_to(liq_provider, DOWN,
                                                                                                                       buff=0.1)
        self.wait(3)
        self.play(Create(VGroup(liq_provider[ 0 ])), run_time=3)
        self.wait(3.034)

        scene3_13btc_box = Rectangle(width=btc_bar.width, height=btc_bar.height * 0.3, stroke_width=3,
                                     stroke_color=GREEN_E).next_to(btc_bar, UP, buff=0)
        scene3_3900usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.3, stroke_width=3,
                                        stroke_color=GREEN_E).next_to(usdt_bar, UP, buff=0)

        # TODO 6.161 secs유동성을 추가려고 하니 현재가격에 맞게 3 비티씨를 넣는다면 900테더를 함께 넣어줘야 합니다
        # TODO 0:00:46.034  ~  0:00:52.195
        # TODO 1.0secs pause
        # TODO 0:00:52.195  ~  0:00:53.195

        scene3_3900usdt_fill_box = scene3_3900usdt_box.copy().set_fill(C_USDT, opacity=1)
        scene3_13btc_fill_box = scene3_13btc_box.copy().set_fill(C_BTC, opacity=1)
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

        self.play(Create(VGroup(liq_provider[ 1 ], usdt_asset)), run_time=2)
        self.wait(1.5)

        self.play(Create(VGroup(scene3_13btc_box, scene3_3900usdt_box)), run_time=2)
        self.wait(1.661)

        # TODO 6.946 secs아까 풀 내부에 비율을 깨면서 안 된다고 한 것처럼 여기서 3비티씨와 800달러, 이렇게 넣을 수는 없습니다
        # TODO 0:00:53.195  ~  0:01:00.141
        # TODO 1.0secs pause
        # TODO 0:01:00.141  ~  0:01:01.141
        # TODO 6.778 secs정확하게 맞춰서 넣으면 현재 풀에서 13분의 3, 즉 23퍼센트를 소유한 것이라는 걸 알 수 있습니다
        # TODO 0:01:01.141  ~  0:01:07.919
        # TODO 1.0secs pause
        # TODO 0:01:07.919  ~  0:01:08.919
        # TODO 4.506 secs최초 공급 이후에 수많은 제공자들이 유동성을 공급하기 시작합니다
        # TODO 0:01:08.919  ~  0:01:13.425
        # TODO 1.0secs pause
        # TODO 0:01:13.425  ~  0:01:14.425

        self.play(Create(scene3_braces),
                  Create(scene3_brace_labels), run_time=2)

        box = Rectangle(width=1.6, height=1, fill_color=WHITE, stroke_color=WHITE, fill_opacity=1)
        text = Tex(r"51\\BTC-USDT\\LP", color=BLACK).scale(0.5)
        new_liq_provider_lp_asset = VGroup(box, text).next_to(liq_provider[ 0 ], DOWN, buff=0.1)

        self.wait(2)
        usdt_asset.save_state()
        btc_asset.save_state()
        self.play(k_tracker.animate.set_value(50700),
                  btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(50700 / 13),
                  ReplacementTransform(usdt_asset, scene3_3900usdt_fill_box),
                  ReplacementTransform(btc_asset, scene3_13btc_fill_box),
                  FadeIn(new_liq_provider_lp_asset, target_position=liq_pool_rect),
                  run_time=7)
        self.wait(0.452)

        # TODO 6.475 secs이렇게 공급할 때마다 전체발행량 분에 자신의 보유량으로 지분을 증명할 수 있도록 발행되고 공급됩니다
        # TODO 0:01:14.425  ~  0:01:20.900
        # TODO 1.0secs pause 1초 플러스 됨
        # TODO 0:01:20.900  ~  0:01:21.900
        lp_add_form_1 = MathTex(r"Added\  {l}' =l\times\frac{{x}'}{x}").next_to(liq_provider[ 0 ], UP).scale(0.7)
        lp_add_form_2 = MathTex(r"Added\  {l}' =\sqrt{30000}\times\frac{3}{10}").move_to(lp_add_form_1).scale(0.7)
        lp_add_form_3 = MathTex(r"Added\  {l}' =173\times0.3").move_to(lp_add_form_1).scale(0.7)
        lp_add_int = Tex(rf"{int(30000 ** (1 / 2) * 3 / 10)} LP token").move_to(lp_add_form_1).scale(0.7)
        total_lp_supply_1 = MathTex(r"Total\  l =l+{l}'").next_to(lp_add_form_1, UP).scale(0.7)
        total_lp_supply_2 = MathTex(r"Total\  l =173+51").move_to(lp_add_form_1).scale(0.7)
        total_lp_supply_int = Tex(rf"{int(30000 ** (1 / 2) + 30000 ** (1 / 2) * 3 / 10)} LP token").move_to(lp_add_form_1).scale(0.7)

        detail_1 = Tex('Init Supply : 173')
        detail_2 = Tex('Added Supply : 51')
        detail_3 = Tex('Total Supply : 225')
        detail_4 = Tex(r'Share : 23\%')
        details = VGroup(detail_1, detail_2, detail_3, detail_4).arrange(D, aligned_edge=L).scale(0.6).next_to(new_liq_provider_lp_asset, D)

        self.play(Create(lp_add_form_1),
                  Create(details), run_time=1)
        self.wait(1)
        self.play(TransformMatchingShapes(lp_add_form_1, lp_add_form_2), run_time=1)
        self.wait(1)
        self.play(TransformMatchingShapes(lp_add_form_2, lp_add_form_3), run_time=1)
        self.wait(1)
        self.play(TransformMatchingShapes(lp_add_form_3, lp_add_int), run_time=1)
        self.wait(1)
        self.play(Uncreate(lp_add_int), run_time=0.475)

        # TODO 7.864 secs나중에 누군가가 추가로 공급해도 그 순간마다 두 자산을 같은 비율로 넣어 가격을 바꾸지 않았으면서 넣었다면 공정한 것이고
        # TODO 0:01:21.900  ~  0:01:29.764
        # TODO 1.0secs pause
        # TODO 0:01:29.764  ~  0:01:30.764

        self.play(Create(total_lp_supply_1), run_time=1)
        self.wait(1)
        self.play(TransformMatchingShapes(total_lp_supply_1, total_lp_supply_2), run_time=1)
        self.wait(1)
        self.play(TransformMatchingShapes(total_lp_supply_2, total_lp_supply_int), run_time=1)
        self.wait(1)
        self.play(Uncreate(total_lp_supply_int), run_time=0.5)
        self.wait(0.364)

        # TODO 5.001 secs이에 따른 엘피토큰으로 확실히 지분을 몇 퍼센트라고 이견없이 정리할 수 있습니다
        # TODO 0:01:30.764  ~  0:01:35.765
        # TODO 1.0secs pause
        # TODO 0:01:35.765  ~  0:01:36.765

        new_user_share_1 = MathTex(r"Share =\frac{UserLP}{TotSupply}").move_to(lp_add_form_1).scale(0.7)
        new_user_share_2 = MathTex(r"Share =\frac{51}{173+51}").move_to(lp_add_form_1).scale(0.7)
        new_user_share_3 = MathTex(r"Share =0.23").move_to(lp_add_form_1).scale(0.7)
        new_user_share_4 = Tex(r"23\%").move_to(lp_add_form_1)

        self.play(Create(new_user_share_1), run_time=0.5)
        self.wait(1)

        self.play(ReplacementTransform(new_user_share_1, new_user_share_2), run_time=0.5)
        self.wait(1)
        self.play(TransformMatchingShapes(new_user_share_2, new_user_share_3), run_time=0.5)
        self.wait(1)
        self.play(TransformMatchingShapes(new_user_share_3, new_user_share_4), run_time=0.5)
        self.wait(0.5)
        self.play(Uncreate(new_user_share_4),
                  Uncreate(details), run_time=0.501)

        # TODO 6.041 secs 그리고 유동성을 제거할 때는 엘피 토큰이 사라지고 자신의 지분만큼 풀에서 돌려받는 것입니다
        # TODO 0:01:36.765  ~  0:01:42.806
        # TODO 1.0secs pause
        # TODO 0:01:42.806  ~  0:01:43.806

        usdt_asset.restore()
        btc_asset.restore()

        dummydot = Dot(1, color=RED).move_to(liq_pool_rect)

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(30000 / 10),
                  Transform(scene3_3900usdt_fill_box, usdt_asset),
                  Transform(scene3_13btc_fill_box, btc_asset),
                  FadeOut(new_liq_provider_lp_asset, target_position=dummydot),
                  run_time=5)
        self.wait(2.041)

        # self.wait(15)




class L02S08(MovingCameraScene):
    def construct(self):
        # self.add(NumberPlane().set_z_index(1))

        speak(self, title='Scene2', txt=
        '#9'
        '#9'
        '#9'
        '#9'
        '#1'
        '이번에는 거래자 활동에 대해 알아보겟습니다. 풀에서 비티씨를 구매하는 경우입니다#1'
        '오더북에서와 마찬가지로 누군가 비티씨를 사면 가격이 올라갑니다#1'
        '왜냐하면 풀에서 비티씨가 빠져나가고 테더가 들어와서 비티씨 테더 비율이 변동했고 이게 비티씨의 가격을 바꾸게 됩니다#1'
        '우리가 생각한대로 내려갔습니다 그리고 케이값도 변하지 않고 그대로입니다. 그런데 구매자가 기분이 안 좋아보입니다#1'
        '구매자는 분명히 구매할 때 1비트코인에 300테더인 걸 보고 3개를 구매하려고 했는데 소요된 비용이 900테더가 아니라 1286테더였습니다#1'
        '어떻게 된걸까요.아까 말했듰이 케이값이 변하지 않기 때문입니다#1'
        '케이는 30000이고 엑스와이는 케이가 유지되렴녀 현재 엑스가 10에서 7로 변했기 때문에 와이는 4286테더가 되어야하고 구매자는 3비트를 구매하려면 4286달러와 원래 있던 3000테더의 차인 1286테더를 지불해야하는 것입니다#1'
        '우리는 이 실구매 평균단가와 우리가 지금 보고있는 현재가의 차이를 임팩트라고 부릅니다. 어 이거 중앙화거래소에서 봤던 슬리피지라 비슷하다고 생각되어 슬리피지라는 것과 프라이스 임팩트란 단어가 쉽게 혼용되는 것을 볼 수 있ㅅ브니다#1'
        '잠시 차이점을 알아보고 가겠습니다#1'
              , keep_pitch=True, update=1, speed=1.4)

        xyk_fraction = MathTex('y', '=', r'\frac{k}{x}').to_edge(UL)

        liq_pool_rect = RoundedRectangle(height=6.3, width=4, corner_radius=0.5)
        liq_pool_text = Tex('Liquidity Pool').next_to(liq_pool_rect, UP)
        liq_pool = VGroup(liq_pool_rect, liq_pool_text).to_edge(UL).shift(R * 0.5)
        liq_pool.set_z_index(3)

        k_var = Variable(30000, MathTex("k"), var_type=Integer).to_edge(UR)
        k_tracker = k_var.tracker
        k_tracker.set_value(30000)

        liq_provider = create_entity(Tex(r' \emph{Init Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", C_BTC, 1.4,
                                     0.3,asset_text_color=WHITE).next_to(liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", C_USDT, 1.4, 0.3,asset_text_color=WHITE)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)
        liq_provider.add(usdt_asset)

        self.play(Create(liq_provider), run_time=3)
        self.wait(6.498)

        ax = Axes(x_range=[ 0, 18, 4 ], y_range=[ 0, 6500, 1000 ], x_length=5, y_length=5, tips=True,
                  axis_config={"include_numbers": False, 'color': WHITE, 'include_ticks': False, 'font_size': 20}, ).to_edge(DR, buff=0.8)

        ax.shift(U * (liq_pool_rect.get_bottom()[ 1 ] - ax[ 0 ].get_y()))

        y_axis_label = ax.get_y_axis_label(MathTex('Amount of USDT in Pool', color=WHITE).rotate(PI / 2).scale(0.4), edge=LEFT,
                                           direction=LEFT, buff=0.37)
        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool', color=WHITE).scale(0.4), edge=DOWN, direction=DOWN, buff=0.37)
        axis_labels = VGroup(x_axis_label, y_axis_label)

        usdt_bar = Rectangle(height=3, width=1.2, fill_color=C_USDT, fill_opacity=1, color=C_USDT)
        btc_bar = Rectangle(height=1, width=1.2, fill_color=C_BTC, fill_opacity=1, color=C_BTC)
        bars = VGroup(btc_bar, usdt_bar)
        bars.arrange(RIGHT, aligned_edge=DOWN).move_to(liq_pool_rect).align_to(liq_pool_rect, DOWN)

        usdt_bar_pos = usdt_bar.get_bottom()
        btc_bar_pos = btc_bar.get_bottom()

        btc_var = Variable(10, MathTex("BTC"), var_type=Integer)
        usdt_var = Variable(3000, MathTex("USDT"), var_type=Integer).next_to(btc_var, DOWN, aligned_edge=LEFT)
        btc_tracker = btc_var.tracker
        usdt_tracker = usdt_var.tracker
        usdt_var[ 0 ][ 0 ].set_color(C_USDT)
        btc_var[ 0 ][ 0 ].set_color(C_BTC)

        vars = VGroup(btc_var, usdt_var).arrange(DOWN, aligned_edge=LEFT).next_to(liq_pool_rect, DOWN, buff=0.25)
        # self.play(Create(liq_pool), run_time=1)
        # self.wait(1)

        self.play(Create(liq_pool),
                  ReplacementTransform(usdt_asset, usdt_bar),
                  ReplacementTransform(btc_asset, btc_bar), run_time=6)
        self.wait(1)
        self.play(Create(usdt_var),
                  Write(btc_var), run_time=2)
        self.wait(1)
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=C_USDT, fill_opacity=1, color=C_USDT).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=C_BTC, fill_opacity=1, color=C_BTC).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        pool_price = Variable(100, 'Price', var_type=DecimalNumber, num_decimal_places=2).next_to(
            liq_pool_rect, RIGHT, buff=0.5).scale(0.8).to_edge(UP)
        pool_price_tracker = pool_price.tracker
        pool_price.add_updater(lambda v: pool_price_tracker.set_value(usdt_tracker.get_value() / btc_tracker.get_value()))
        pool_price_unit = Tex(r'USDT').scale(0.75).next_to(pool_price, buff=0.1)
        pool_price.add(pool_price_unit)
        self.play(Write(k_var[ 0 ]), run_time=1.5)
        self.wait(1)
        self.play(Create(ax),
                  Create(axis_labels),
                  Create(pool_price),
                  TransformMatchingShapes(Group(btc_var[ 1 ].copy(), usdt_var[ 1 ].copy()), k_var[ 1 ]),
                  Create(xyk_fraction.next_to(k_var, LEFT, buff=1)), run_time=5
                  )

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
        x_marker = Triangle(color=C_BTC, fill_color=C_BTC, fill_opacity=1).scale(0.1).next_to(vertical_line, DOWN, buff=0)
        x_marker.add_updater(lambda marker: marker.next_to(vertical_line, DOWN, buff=0))
        x_marker_val = Integer(btc_tracker.get_value())
        x_marker_val.add_updater(
            lambda integer: integer.become(Integer(btc_tracker.get_value()).scale(0.4).next_to(vertical_line, DOWN, buff=0.3)))

        y_marker = Triangle(color=C_USDT, fill_color=C_USDT, fill_opacity=1).scale(0.1).rotate(-PI / 2).next_to(horizontal_line, LEFT,
                                                                                                                buff=0)
        y_marker.add_updater(lambda marker: marker.next_to(horizontal_line, LEFT, buff=0))
        y_marker_val = Integer(usdt_tracker.get_value())
        y_marker_val.add_updater(lambda integer: integer.become(
            Integer(usdt_tracker.get_value()).scale(0.4).rotate(PI / 2).next_to(horizontal_line, LEFT, buff=0.3)))

        lines = VGroup(vertical_line, horizontal_line)
        markers = VGroup(x_marker, x_marker_val, y_marker, y_marker_val)

        self.play(Create(xyk_graph_btc), run_time=0.5)
        self.wait(0.5)
        self.play(Create(curr_dot), run_time=0.5)
        self.play(Create(lines), run_time=1.5)
        self.play(Create(markers), run_time=0.5)
        self.play(Uncreate(liq_provider), run_time=0.5)
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
        self.play(Create(area), run_time=0.5)
        self.play(Create(area_text), run_time=0.5)

        self.wait(5.5)

        # TODO 4.977 secs이번에는 거래자 활동에 대해 알아보겟습니다. 풀에서 비티씨를 구매하는 경우입니다
        # TODO 0:00:37.000  ~  0:00:41.977
        # TODO 1.0secs pause
        # TODO 0:00:41.977  ~  0:00:42.977

        # TODO 4.096 secs오더북에서와 마찬가지로 누군가 비티씨를 사면 가격이 올라갑니다
        # TODO 0:00:42.977  ~  0:00:47.073
        # TODO 1.0secs pause
        # TODO 0:00:47.073  ~  0:00:48.073

        user = create_entity(Tex(r' \emph{Trader}', color=BLACK), 1, WHITE, "1286 USDT", C_USDT, 1.4, 0.3,asset_text_color=WHITE).next_to(liq_pool_rect, RIGHT,
                                                                                                                  buff=1.5)
        user_asset_usdt = user[ 1 ]
        user_asset_pos = user_asset_usdt.get_center()
        user_asset_btc = create_entity("A", 0.5, WHITE, "3 BTC", C_BTC, 1.4, 0.3,asset_text_color=WHITE)[ 1 ].move_to(user_asset_pos)

        user_line = Tex(r'I want 3 BTC\\I have some USDT').scale(0.7).next_to(user, DOWN)

        self.wait(0.5)
        self.play(Create(user), run_time=0.5)
        self.wait(0.5)

        self.play(Create(user_line), run_time=0.5)
        self.wait(2)
        self.play(Uncreate(user_line), run_time=1)
        # self.wait(1.096)

        # self.add(index_labels(btc_bar))###

        # scene1_btc_dashed_box = Rectangle(color=RED).align_to(btc_bar[0],UL,alignment_vect=btc_bar[0].get_edge_center(UP))
        scene1_7btc_box = Rectangle(width=btc_bar.width, height=btc_bar.height * 0.3, stroke_width=3, stroke_color=RED_E).align_to(
            btc_bar[ 0 ], UL)
        scene1_1286usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.4286, stroke_width=3,
                                        stroke_color=GREEN_E).next_to(usdt_bar, UP, buff=0)

        scene1_7btc_fill_box = scene1_7btc_box.copy().set_fill(C_BTC, opacity=1)
        scene1_1286usdt_fill_box = scene1_1286usdt_box.copy().set_fill(C_USDT, opacity=1)
        scene1_7btc_fill_box.set_stroke(width=0, opacity=0)
        scene1_1286usdt_fill_box.set_stroke(width=0, opacity=0)
        scene1_7btc_fill_box.set_z_index(3)
        scene1_1286usdt_fill_box.set_z_index(3)


        self.play(Create(scene1_7btc_box), run_time=0.5)
        self.play(Create(scene1_1286usdt_box), run_time=0.5)
        self.wait(0.5)

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
                  Create(scene1_brace_labels), run_time=0.5)
        # self.wait(t)
        # TODO 6.56 secs왜냐하면 풀에서 비티씨가 빠져나가서 비티씨 테더 비율이 변동했고 이게 비티씨의 가격을 바꾸게 됩니다
        # TODO 0:00:48.073  ~  0:00:54.633
        # TODO 1.0secs pause
        # TODO 0:00:54.633  ~  0:00:55.633

        # TODO 6.946 secs우리가 생각한대로 올라갔습니다 그리고 케이값도 변하지 않고 그대로입니다. 그런데 구매자가 기분이 안 좋아보입니다
        # TODO 0:00:55.633  ~  0:01:02.579
        # TODO 1.0secs pause
        # TODO 0:01:02.579  ~  0:01:03.579

        usdt_bar.clear_updaters()
        btc_bar.clear_updaters()

        self.add(scene1_7btc_fill_box)
        # usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
        #     Rectangle(height=4283 / 1000, width=1.2, fill_color=BLUE, fill_opacity=1, color=BLUE).move_to(
        #         usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=7 / 10, width=1.2, fill_color=C_BTC, fill_opacity=1, color=C_BTC).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        origin_dot = curr_dot.copy()
        origin_dot.clear_updaters()
        origin_dot.set_color(GREEN)
        origin_dot.set_z_index(1.5)
        scene1_arrow = CurvedArrow(origin_dot.get_center(), curr_dot.get_center(), radius=-4, tip_length=0.25).shift(
            RIGHT * 0.3 + UP * 0.3)
        scene1_arrow_label = Tex('Buy BTC in exchange of USDT').scale(0.3).next_to(scene1_arrow, UR)


        self.play(Create(origin_dot))
        self.wait(t)
        self.play(btc_tracker.animate.set_value(7),
                  usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
                  ReplacementTransform(scene1_7btc_fill_box, user_asset_btc),
                  ReplacementTransform(user_asset_usdt, scene1_1286usdt_fill_box), run_time=6)
        self.play(Create(scene1_arrow))
        self.wait(0.5)


        # TODO 9.085 secs구매자는 분명히 구매할 때 1비트코인에 300달러인 걸 보고 3개를 구매하려고 했는데 소요된 비용이 900달러가 아니라 1286달러였습니다
        # TODO 0:01:03.579  ~  0:01:12.664
        # TODO 1.0secs pause
        # TODO 0:01:12.664  ~  0:01:13.664

        # TODO 4.567 secs어떻게 된걸까요.아까 말했듰이 케이값이 변하지 않기 때문입니다
        # TODO 0:01:13.664  ~  0:01:18.231
        # TODO 1.0secs pause
        # TODO 0:01:18.231  ~  0:01:19.231

        # TODO 15.971 secs케이는 30000이고 엑스와이는 케이가 유지되렴녀 현재 엑스가 10에서 7로 변했기 때문에 와이는 4286달러가 되어야하고 구매자는 3비트를 구매하려면 4286달러와 원래 있던 3000테더의 차인 1286테더를 지불해야하는 것입니다
        # TODO 0:01:19.231  ~  0:01:35.202
        # TODO 1.0secs pause
        # TODO 0:01:35.202  ~  0:01:36.202

        scene1_slippage_text = Tex(r'I used 1286 USDT \\to buy 3 BTC').scale(0.7).next_to(user_asset_pos, DOWN)
        scene1_slippage_form = MathTex(r'1286 \divisionsymbol 3').next_to(scene1_slippage_text, DOWN)
        scene1_slippage_result = MathTex(rf'{429}USDT \  per\ BTC ').scale(0.85).move_to(
            scene1_slippage_form.get_center())


        px_impact_text_1 = MathTex(r'k=30000').next_to(scene1_slippage_result,D,buff=0.75)
        px_impact_text_2 = MathTex(r'y = \frac{30000}{7}').move_to(px_impact_text_1)
        px_impact_text_3 = MathTex(r'y =4286').move_to(px_impact_text_1)
        px_impact_text_4 = Tex(r'There should be 4286 USDT').move_to(px_impact_text_1).scale(0.7)
        px_impact_text_5 = MathTex(r'4286-3000=1286').move_to(px_impact_text_1)

        self.play(Create(scene1_slippage_form),
                  Create(scene1_slippage_text), run_time=3)

        self.play(ReplacementTransform(scene1_slippage_form, scene1_slippage_result), run_time=t)

        self.wait(14)


        self.play(Create(px_impact_text_1),run_time=1)
        self.wait(3)
        self.play(ReplacementTransform(px_impact_text_1,px_impact_text_2),run_time=0.5)
        self.wait(3)
        self.play(ReplacementTransform(px_impact_text_2,px_impact_text_3),run_time=0.5)
        self.wait(3)
        self.play(ReplacementTransform(px_impact_text_3,px_impact_text_4),run_time=0.5)
        self.wait(3)
        self.play(ReplacementTransform(px_impact_text_4,px_impact_text_5),run_time=0.5)
        self.wait(3)

        self.wait(30)
        # TODO 14.026 secs우리는 이 실구매 평균단가와 우리가 지금 보고있는 현재가의 차이를 임팩트라고 부릅니다.
        #  어 이거 중앙화거래소에서 봤던 슬리피지라 비슷하다고 생각되어 슬리피지라는 것과 프라이스 임팩트란 단어가 쉽게 혼용되는 것을 볼 수 있ㅅ브니다
        # TODO 0:01:36.202  ~  0:01:50.228
        # TODO 1.0secs pause
        # TODO 0:01:50.228  ~  0:01:51.228

        # TODO 2.223 secs잠시 차이점을 알아보고 가겠습니다
        # TODO 0:01:51.228  ~  0:01:53.451
        # TODO 1.0secs pause
        # TODO 0:01:53.451  ~  0:01:54.451

        # self.wait(15)





class L02S09_px_impact(Scene):
    def construct(self):
        # self.add(NumberPlane().set_z_index(1))

        speak(self, title='L02S05', txt=
        '프라이스 임팩트는 내가 지금 하려는 트랜잭셕 즉 비트코인 3개를 풀에서 빼는 것이 가격에 주는 영향이라고 할 수 있습니다#1'
        '프라이스 임팩트 자체는 내가 트랜잭션을 요청하는 순간 이미 예상 된 것입니다#1'
        '3개를 받으려고 1286테더을 보냈는데 2.7개를 받았을 때 우리는 11퍼센트의 슬리피지와 0.3비티씨의 슬리피지비용이 발생했다고 합니다다#1'
        '300달러를 보고 비티씨를 주문하면 나는 이미 계산을 통해 내가 시장을 얼마나 움직일 것이고 그래서 사실상 비티씨를 300테더에 못 구매하고 429테더라는 가격에 구매할 것을 알고 있습니다 .이로인한 것은 프라이스 임팩트이지 슬리피지가 아닙니다#1'        
        '슬리피지는 그렇게 내가 평균단가 429테더에 구매할 것이라 예상하는데 예상치 못 한 이유로 인해 거기서부터 갈라지는 것입니다#1'
        '프라이스 임팩트는 429 테더 빼기 300 즉 129 달러 혹은 보통은 퍼센트로 나타내기에 429 빼기 300 나누기 429 곱하기 100 즉 43퍼센트가 됩니다#1'
        '명심할 것은 엑스와이는 케이모델에서 프라이스 임팩트가 없을 수는 없습니다#1'
        '프라이스 임팩트가 없으려면 그래프를 벗어나야되는데 거래라는 것이 케이값을 유지한 상태에서 풀의 상태를 변화시키는 것 즉, 기존 그래프상에서 점을 이동시키는 것이기 때문입니다#1'
              , keep_pitch=True, update=True, speed=1.4)

        # TODO 7.249 secs프라이스 임팩트는 내가 지금 하려는 트랜잭셕 즉 비트코인 2개를 풀에서 빼는 것이 가격에 주는 영향이라고 할 수 있습니다
        # TODO 0:00:00.000  ~  0:00:07.249
        # TODO 1.0secs pause
        # TODO 0:00:07.249  ~  0:00:08.249


        px_impact_title = Tex('Price Impact and Slippage').scale(2)

        self.play(Create(px_impact_title),run_time=3)
        self.wait(3.249)
        self.play(Uncreate(px_impact_title),run_time=2)

        # xyk = MathTex(r'x', r'\times', 'y', '=', 'k').scale(2)
        # num_30000 = MathTex('30000').scale(2).to_edge(R).align_to(xyk[ 4 ], L)
        # num_10_minus_3 = MathTex('(10-3)').scale(2).to_edge(L).align_to(xyk[ 0 ], R)
        # num_7 = MathTex('7').scale(2).to_edge(L).align_to(xyk[ 0 ], R)
        # y_is = MathTex(r'y', '=', r'\frac{30000}{7}').scale(2)
        # num_4286 = MathTex(r'4286').scale(2).to_edge(R).align_to(y_is[ 2 ], L)
        #
        # self.play(Create(xyk), run_time=1)
        # self.wait(t)
        # self.play(Transform(xyk[ 4 ], num_30000), run_time=1)
        # self.wait(t)
        #
        # self.play(Transform(xyk[ 0 ], num_10_minus_3), run_time=1)
        # self.wait(t)
        # self.play(Transform(xyk[ 0 ], num_7), run_time=1)
        # self.wait(t)
        # self.play(TransformMatchingShapes(xyk, y_is), run_time=1)
        # self.wait(t)
        # self.play(Transform(y_is[ 2 ], num_4286), run_time=1)
        #
        # self.wait(t)
        # self.play(Uncreate(y_is))
        #
        # TODO 4.857 secs프라이스 임팩트 자체는 내가 트랜잭션을 요청하는 순간 이미 예상 된 것입니다
        # TODO 0:00:08.249  ~  0:00:13.106
        # TODO 1.0secs pause
        # TODO 0:00:13.106  ~  0:00:14.106
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
        self.play(Create(dex_elements_without_amt),run_time=4)
        self.wait(1.857)


        # TODO 9.713 secs3개를 받으려고 1286테더을 보냈는데 2.7개를 받았을 때 우리는 11퍼센트의 슬리피지와 0.3비티씨의 슬리피지비용이 발생했다고 합니다다
        # TODO 0:00:14.106  ~  0:00:23.819
        # TODO 1.0secs pause
        # TODO 0:00:23.819  ~  0:00:24.819

        self.play(Create(input_box_1_amt), run_time=0.5)
        self.wait(0.5)
        self.play(Create(input_box_2_amt), run_time=0.5)
        self.wait(0.5)
        self.play(Transform(est_px, new_est_px),
                  Circumscribe(est_px), run_time=1)

        # self.wait(0.5)
        self.play(Indicate(swap_button_text, color=GREY), run_time=0.5)
        self.wait(0.5)
        self.play(dex_elements.animate.to_edge(L), run_time=0.5)
        self.wait(0.5)

        ##### 슬리피지는 그렇게 내가 평균단가 468.75 달러에 구매할 것이라 예상하는데 거기서부터 갈라지는 것입니다
        ##### 3개를 받으려고 1283을 보냈는데 2.8개를 받았을 때 우리는 0.2비티씨의 슬리피지가 생겼다고 합니다다
        # 돌려받은게 3비티씨가 아니라 2.8비티씨임
        returned_btc_2 = Tex('We just got 2.7 BTC', r'Slippage of 11\%', 'A slippage cost of 0.3 BTC').scale(0.8).arrange(D).shift(
            R * 4 + U * 2.5)
        self.play(Create(returned_btc_2), run_time=1)
        self.wait(4.713)



        # TODO 15.234 secs300달러를 보고 비티씨를 주문하면 나는 이미 계산을 통해 내가 시장을 얼마나 움직일 것이고 그래서 사실상 비티씨를
        #  300테더에 못 구매하고 429테더라는 가격에 구매할 것을 알고 있습니다 .이로인한 것은 프라이스 임팩트이지 슬리피지가 아닙니다
        # TODO 0:00:24.819  ~  0:00:40.053
        # TODO 1.0secs pause
        # TODO 0:00:40.053  ~  0:00:41.053




        i_know = Tex('I already know it', font_size=30).next_to(est_px, D,buff=0.1).align_to(est_px, L)

        # est_px = Tex('1 BTC = 300USDT', font_size=30).next_to(input_box_2, D).align_to(input_box_2, L)


        self.play(Create(i_know))
        self.wait(3)
        self.wait(2.734)
        self.wait(2)
        self.play(Circumscribe(VGroup(est_px,i_know)),run_time=2)
        # self.play(Circumscribe(i_know))

        self.play(Uncreate(i_know))


        px_impact_not_equal = MathTex(r'Price\  Imapact', r'\neq', 'Slippage').scale(0.9).arrange(D).move_to(np.array([4,-2,0]))
        self.play(Create(px_impact_not_equal), run_time=1)
        self.wait(3)
        self.play(Uncreate(px_impact_not_equal), run_time=0.5)

        # TODO 8.372 secs슬리피지는 그렇게 내가 평균단가 429테더에 구매할 것이라 예상하는데 예상치 못 한 이유로 인해 거기서부터 갈라지는 것입니다
        # TODO 0:00:41.077  ~  0:00:49.449
        # TODO 1.0secs pause
        # TODO 0:00:49.449  ~  0:00:50.449

        p1 = np.array([ -3, 1, 0 ])
        p1b = p1 + [ 1, 0, 0 ]
        l1 = Line(p1, p1b)
        p2 = np.array([ 3, -1, 0 ])
        p2b = p2 - [ 1, 0, 0 ]
        bezier_1 = CubicBezier(p1b, p1b + 3 * RIGHT, p2b - 3 * RIGHT, p2b)
        bezier_2 = CubicBezier(p2b, p2b - 3 * RIGHT, p1b + 3 * RIGHT, p1b).flip(axis=np.array([ 0, 1, 0 ])).shift(U * 2)
        curve_group = VGroup(l1, bezier_1, bezier_2).move_to(np.array([4,-2,0])).scale_to_fit_width(2).scale(0.7)
        slippage = MathTex('Slippage').scale(0.7).next_to(curve_group, LEFT)
        tech_problem = MathTex(r'Technical\\Problem', tex_environment='center').scale(0.7).next_to(bezier_2, R).shift(U * 0.5)
        low_liq = MathTex(r'Low\\Liquidity', tex_environment='center').scale(0.7).next_to(bezier_1, R).shift(D * 0.5)
        self.play(Create(slippage), run_time=1)
        self.play(Create(curve_group), run_time=1)
        self.play(Create(tech_problem),
                  Create(low_liq), run_time=2)
        self.wait(3.372)
        self.play(Uncreate(slippage), Uncreate(curve_group), Uncreate(tech_problem),
                  Uncreate(low_liq), run_time=1)
        self.wait(1)

        # TODO 10.836 secs프라이스 임팩트는 429 테더 빼기 300 즉 129 달러 혹은 보통은 퍼센트로 나타내기에 429 빼기 300 나누기 429 곱하기 100 즉 43퍼센트가 됩니다
        # TODO 0:00:49.156  ~  0:00:59.992
        # TODO 1.0secs pause
        # TODO 0:00:59.992  ~  0:01:00.992
        px_impact_text = Tex('Price Impact').shift(R * 4 + U * 0.5)
        px_impact_form = MathTex(r'\frac{429-300}{300} = ', '0.43').shift(R * 4 + D * 0.5)
        px_impact_30perc = MathTex(r'43\%').move_to(px_impact_form[ 1 ]).to_edge(R).align_to(px_impact_form[ 1 ], L)
        self.play(Create(px_impact_text), run_time=1)
        self.wait(3)
        self.play(Create(px_impact_form), run_time=1)
        self.wait(3)
        self.play(Transform(px_impact_form[ 1 ], px_impact_30perc), run_time=1)
        self.wait(2.836)


        # TODO 5.219 secs어쨋거나 명심할 것은 엑스와이는 케이모델에서 프라이스 임팩트가 없을 수는 없습니다
        # TODO 0:01:07.416  ~  0:01:12.635
        # TODO 1.0secs pause
        # TODO 0:01:12.635  ~  0:01:13.635

        trades = Tex(r'All trades\\inevitably involve\\price impact').next_to(returned_btc_2,D,buff= 0.8)
        self.play(Transform(VGroup(px_impact_text,px_impact_form), trades),run_time=2)
        self.wait(3.219)



        # TODO 10.703 secs프라이스 임팩트가 없으려면 그래프를 벗어나야되는데 거래라는 것이 케이값을 유지한 상태에서 풀의 상태를 변화시키는 것 즉, 기존 그래프상에서 점을 이동시키는 것이기 때문입니다
        # TODO 0:01:13.079  ~  0:01:23.782
        # TODO 1.0secs pause
        # TODO 0:01:23.782  ~  0:01:24.782


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
                  Create(curr_dot), run_time=1)
        self.wait(1)

        self.play(curr_dot.animate.shift(R * 0.5 + U * 0.5), rate_func=there_and_back_with_pause, run_time=5)
        self.wait(t)


        self.wait(30)


class L02S10(MovingCameraScene):
    def construct(self):
        # self.add(NumberPlane().set_z_index(1))

        speak(self, title='Scene2', txt=
        '#9'
        '#9'
        '#9'
        '#9'
        '#1'
        '이번에는 비티씨를 파는 경우입니다#1'
        '아까와 같은 원리로 비티씨를 팔면 가격이 내려가고, 여기서도 프라이스 임팩트를 막을 수는 없습니다.#1'
        '가격은 예상대로 내려가고 매도자는 여전히 기분이 좋지 않습니다#1'
        '300달러를 보고 3개를 판매했지만 900달러가 아닌 692달러 밖에 못 받았기 때문입니다.#1'
        '괴리가 이렇게 큰 이유는  유동성즉 풀의 크기가 작기 때문입니다.#1'
              , keep_pitch=True, update=1, speed=1.4)

        xyk_fraction = MathTex('y', '=', r'\frac{k}{x}').to_edge(UL)

        liq_pool_rect = RoundedRectangle(height=6.3, width=4, corner_radius=0.5)
        liq_pool_text = Tex('Liquidity Pool').next_to(liq_pool_rect, UP)
        liq_pool = VGroup(liq_pool_rect, liq_pool_text).to_edge(UL).shift(R * 0.5)
        liq_pool.set_z_index(3)

        k_var = Variable(30000, MathTex("k"), var_type=Integer).to_edge(UR)
        k_tracker = k_var.tracker
        k_tracker.set_value(30000)

        liq_provider = create_entity(Tex(r' \emph{Init Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", C_BTC, 1.4,
                                     0.3,asset_text_color=WHITE).next_to(liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", C_USDT, 1.4, 0.3,asset_text_color=WHITE)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)
        liq_provider.add(usdt_asset)

        self.play(Create(liq_provider), run_time=3)
        self.wait(6.498)

        ax = Axes(x_range=[ 0, 18, 4 ], y_range=[ 0, 6500, 1000 ], x_length=5, y_length=5, tips=True,
                  axis_config={"include_numbers": False, 'color': WHITE, 'include_ticks': False, 'font_size': 20}, ).to_edge(DR, buff=0.8)

        ax.shift(U * (liq_pool_rect.get_bottom()[ 1 ] - ax[ 0 ].get_y()))

        y_axis_label = ax.get_y_axis_label(MathTex('Amount of USDT in Pool', color=WHITE).rotate(PI / 2).scale(0.4), edge=LEFT,
                                           direction=LEFT, buff=0.37)
        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool', color=WHITE).scale(0.4), edge=DOWN, direction=DOWN, buff=0.37)
        axis_labels = VGroup(x_axis_label, y_axis_label)

        usdt_bar = Rectangle(height=3, width=1.2, fill_color=C_USDT, fill_opacity=1, color=C_USDT)
        btc_bar = Rectangle(height=1, width=1.2, fill_color=C_BTC, fill_opacity=1, color=C_BTC)
        bars = VGroup(btc_bar, usdt_bar)
        bars.arrange(RIGHT, aligned_edge=DOWN).move_to(liq_pool_rect).align_to(liq_pool_rect, DOWN)

        usdt_bar_pos = usdt_bar.get_bottom()
        btc_bar_pos = btc_bar.get_bottom()

        btc_var = Variable(10, MathTex("BTC"), var_type=Integer)
        usdt_var = Variable(3000, MathTex("USDT"), var_type=Integer).next_to(btc_var, DOWN, aligned_edge=LEFT)
        btc_tracker = btc_var.tracker
        usdt_tracker = usdt_var.tracker
        usdt_var[ 0 ][ 0 ].set_color(C_USDT)
        btc_var[ 0 ][ 0 ].set_color(C_BTC)

        vars = VGroup(btc_var, usdt_var).arrange(DOWN, aligned_edge=LEFT).next_to(liq_pool_rect, DOWN, buff=0.25)
        # self.play(Create(liq_pool), run_time=1)
        # self.wait(1)

        self.play(Create(liq_pool),
                  ReplacementTransform(usdt_asset, usdt_bar),
                  ReplacementTransform(btc_asset, btc_bar), run_time=6)
        self.wait(1)
        self.play(Create(usdt_var),
                  Write(btc_var), run_time=2)
        self.wait(1)
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=C_USDT, fill_opacity=1, color=C_USDT).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=C_BTC, fill_opacity=1, color=C_BTC).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        pool_price = Variable(100, 'Price', var_type=DecimalNumber, num_decimal_places=2).next_to(
            liq_pool_rect, RIGHT, buff=0.5).scale(0.8).to_edge(UP)
        pool_price_tracker = pool_price.tracker
        pool_price.add_updater(lambda v: pool_price_tracker.set_value(usdt_tracker.get_value() / btc_tracker.get_value()))
        pool_price_unit = Tex(r'USDT').scale(0.75).next_to(pool_price, buff=0.1)
        pool_price.add(pool_price_unit)
        self.play(Write(k_var[ 0 ]), run_time=1.5)
        self.wait(1)
        self.play(Create(ax),
                  Create(axis_labels),
                  Create(pool_price),
                  TransformMatchingShapes(Group(btc_var[ 1 ].copy(), usdt_var[ 1 ].copy()), k_var[ 1 ]),
                  Create(xyk_fraction.next_to(k_var, LEFT, buff=1)), run_time=5
                  )

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
        x_marker = Triangle(color=C_BTC, fill_color=C_BTC, fill_opacity=1).scale(0.1).next_to(vertical_line, DOWN, buff=0)
        x_marker.add_updater(lambda marker: marker.next_to(vertical_line, DOWN, buff=0))
        x_marker_val = Integer(btc_tracker.get_value())
        x_marker_val.add_updater(
            lambda integer: integer.become(Integer(btc_tracker.get_value()).scale(0.4).next_to(vertical_line, DOWN, buff=0.3)))

        y_marker = Triangle(color=C_USDT, fill_color=C_USDT, fill_opacity=1).scale(0.1).rotate(-PI / 2).next_to(horizontal_line, LEFT,
                                                                                                                buff=0)
        y_marker.add_updater(lambda marker: marker.next_to(horizontal_line, LEFT, buff=0))
        y_marker_val = Integer(usdt_tracker.get_value())
        y_marker_val.add_updater(lambda integer: integer.become(
            Integer(usdt_tracker.get_value()).scale(0.4).rotate(PI / 2).next_to(horizontal_line, LEFT, buff=0.3)))

        lines = VGroup(vertical_line, horizontal_line)
        markers = VGroup(x_marker, x_marker_val, y_marker, y_marker_val)

        self.play(Create(xyk_graph_btc), run_time=0.5)
        self.wait(0.5)
        self.play(Create(curr_dot), run_time=0.5)
        self.play(Create(lines), run_time=1.5)
        self.play(Create(markers), run_time=0.5)
        self.play(Uncreate(liq_provider), run_time=0.5)
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
        self.play(Create(area), run_time=0.5)
        self.play(Create(area_text), run_time=0.5)

        self.wait(5.5)

        # TODO 2.199 secs이번에는 비티씨를 파는 경우입니다
        # TODO 0:00:37.000  ~  0:00:39.199
        # TODO 1.0secs pause
        # TODO 0:00:39.199  ~  0:00:40.199
        # TODO 6.741 secs아까와 같은 원리로 비티씨를 팔면 가격이 내려가고, 여기서도 프라이스 임팩트를 막을 수는 없습니다.
        # TODO 0:00:40.199  ~  0:00:46.940
        # TODO 1.0secs pause
        # TODO 0:00:46.940  ~  0:00:47.940


        user = create_entity(Tex(r' \emph{Trader}', color=BLACK), 1, WHITE, "3BTC", C_BTC, 1.4, 0.3,asset_text_color=WHITE).next_to(liq_pool_rect,
                                                                                                              RIGHT, buff=1.5)
        user_asset_btc = user[ 1 ]
        user_asset_pos = user_asset_btc.get_center()
        user_asset_usdt = create_entity("A", 0.5, WHITE, "692USDT", C_USDT, 1.4, 0.3,asset_text_color=WHITE)[ 1 ].move_to(user_asset_pos)

        user_line = Tex(r"I want to sell 3 BTC\\I don't have some USDT").scale(0.5).next_to(user, DOWN)

        self.wait(0.5)
        self.play(Create(user), run_time=0.5)
        self.play(Create(user_line), run_time=0.5)
        self.wait(2)
        self.play(Uncreate(user_line), run_time=0.5)

        # self.add(index_labels(btc_bar))###

        # scene2_btc_dashed_box = Rectangle(color=RED).align_to(btc_bar[0],UL,alignment_vect=btc_bar[0].get_edge_center(UP))
        scene2_2308usdt_box = Rectangle(width=usdt_bar.width, height=usdt_bar.height * 0.2307, stroke_width=3,
                                        stroke_color=RED_E).align_to(
            usdt_bar, UL)
        scene2_13btc_box = Rectangle(width=btc_bar.width, height=btc_bar.height * 0.3, stroke_width=3,
                                     stroke_color=GREEN_E).next_to(btc_bar, UP, buff=0)

        scene2_2308usdt_fill_box = scene2_2308usdt_box.copy().set_fill(C_USDT, opacity=1)
        scene2_13btc_fill_box = scene2_13btc_box.copy().set_fill(C_BTC, opacity=1)

        scene2_2308usdt_fill_box.set_stroke(width=0, opacity=0)
        scene2_13btc_fill_box.set_stroke(width=0, opacity=0)

        scene2_2308usdt_fill_box.set_z_index(3)
        scene2_13btc_fill_box.set_z_index(3)

        self.play(Create(scene2_2308usdt_box), run_time=0.5)


        self.play(Create(scene2_13btc_box), run_time=0.5)
        self.wait(0.5)

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
                  Create(scene2_brace_labels), run_time=0.5)
        self.wait(0.5)

        usdt_bar.clear_updaters()
        btc_bar.clear_updaters()

        self.add(scene2_2308usdt_fill_box)
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=2307 / 1000, width=1.2, fill_color=C_USDT, fill_opacity=1, color=C_USDT).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        # btc_bar.add_updater(lambda btc_bar: btc_bar.become(
        #     Rectangle(height=13 / 10, width=1.2, fill_color=BTC, fill_opacity=1, color=BTC).move_to(
        #         btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        origin_dot = curr_dot.copy()
        origin_dot.clear_updaters()
        origin_dot.set_color(RED)
        origin_dot.set_z_index(1.5)
        scene2_arrow = CurvedArrow(origin_dot.get_center(), curr_dot.get_center(), radius=4, tip_length=0.25).shift(
            RIGHT * 0.3 + UP * 0.3)
        scene2_arrow_label = Tex('Buy BTC in exchange of USDT').scale(0.3).next_to(scene2_arrow, UR)

        # TODO 4.107 secs가격은 예상대로 내려가고 매도자는 여전히 기분이 좋지 않습니다
        # TODO 0:00:47.940  ~  0:00:52.047 4.44초 받아옴
        # TODO 1.0secs pause
        # TODO 0:00:52.047  ~  0:00:53.047


        self.play(Create(origin_dot),run_time=0.5)
        self.wait(0.5)
        self.play(btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)),
                  Transform(scene2_2308usdt_fill_box, user_asset_usdt),
                  Transform(user_asset_btc, scene2_13btc_fill_box), run_time=6)
        self.play(Create(scene2_arrow))
        self.wait(0.547)


        # TODO 6.198 secs300달러를 보고 3개를 판매했지만 900달러가 아닌 692달러 밖에 못 받았기 때문입니다.
        # TODO 0:00:53.047  ~  0:00:59.245
        # TODO 1.0secs pause
        # TODO 0:00:59.245  ~  0:01:00.245

        # TODO 4.12 secs괴리가 이렇게 큰 이유는  유동성즉 풀의 크기가 작기 때문입니다.
        # TODO 0:01:00.245  ~  0:01:04.365
        # TODO 1.0secs pause
        # TODO 0:01:04.365  ~  0:01:05.365

        scene2_slippage_text = Tex(r'I sold 3 BTC \\and got 692 USDT').scale(0.7).next_to(user_asset_pos, DOWN)
        scene2_slippage_form = MathTex(r'692 \divisionsymbol 3').next_to(scene2_slippage_text, DOWN)
        scene2_slippage_result = MathTex(
            rf'{int(-(k_tracker.get_value() / btc_tracker.get_value() - 3000) / 3)}USDT \  per\ BTC ').scale(0.85).move_to(
            scene2_slippage_form.get_center())

        self.play(Create(scene2_slippage_form),
                  Create(scene2_slippage_text), run_time=3)
        self.play(ReplacementTransform(scene2_slippage_form, scene2_slippage_result), run_time=3)
        self.wait(30)



class L02S11(Scene):
    def construct(self):
        # self.add(NumberPlane().set_z_index(1))

        speak(self, title='L02S05', txt=
        '다음으로 넘어가기 전에 수수료예 대해 알아보겠습니다#1'
        '덱스에서 수수료는 독특한 방식으로 작동합니다#1'
        '거래를 하기 위해 코인을 풀로 보내면 코인이 풀에 도착하기 전에 수수료를 떼고 남은 금액만 풀에 들어가서 그거에 맞게 거래가 일어납니다#1'
        '그리고 거래가 종료되면 풀에 그냥 수수료를 추가합니다#1'
        '수수료는 거래가 발생할 때마다 풀에 쌓이기 때문에 매번 거래가 종료되면 케이값은 증가합니다#1'
        '중앙화 거래소에서는 거래소가 가져가니 우리의 수수료가 가격에 영향을 줄 일은 없었습니다#1'
        '그러나 덱스에서는 수수료가 풀 내부의 비트 테더 비율을 조금씩 바꾸기 때문에 우리가 생각한 것과 미세하게 가격이 차이가 납니다#1'
        '수수료가 1퍼인 상황을 생각해 보겠습니다#1'
        '비트 10개 3000테더가 있는 풀에 1비트를 보내면 수수료를 뗀 0.99비트가 전송됩니다#1'
        '그리고 0.99에 대한 교환이 일어나고 풀에는 30000나누기 10.99인 2729테더가 남습니다#1'
        '지금까지는 케이는 여전히 30000입니다 #1'
        '그뒤에 풀에 빼놨던 수수료인 0.01비트를 넣습니다. 풀에는 이제 11비트와 2729테더가 남아있습니다 #1'
        '케이는 30027.297로 약간 증가했습니다 현재 비트의 가격은 248.15테더입니다#1'
        '원래 1비트를 매도했다고 생각하면 가격은 30000나누기 11나누기 11인 247.93테더가 되어야합니다#1'
        '그러나 수수료가 있었다면 30000나누기 10.99 나누기 11인 248.15 테더가 됩니다#1'
        '즉 이전 거래자의 행동에 따라서 미세하게 이익이 바뀝니다#1'
        '비트를 매도하는 행위에서 수수료가 있던 경우가 가격이 덜 떨어졌으므로 같은 방향, 즉 이후에 매도할 사람은 원래 앞사람이 거래하고 247테더를 생각하고 있었으나 예상보다 돈을 좀 더 건질 수 있게 됐습니다#1'
        '반대로 앞사람과 반대방향 즉 매수를 하려던 사람은 자신이 앞사람을 보고 생각하던 247달러보다 높은 248테더에 매수를 해야해서 예상보다 지출이 늘었습니다 #1'
              , keep_pitch=True, update=True, speed=1.4)

        # TODO 3.165 secs다음으로 넘어가기 전에 수수료예 대해 알아보겠습니다
        # TODO 0:00:00.000  ~  0:00:03.165
        # TODO 1.0secs pause
        # TODO 0:00:03.165  ~  0:00:04.165
        fees = Tex('Fees').scale(2)

        self.play(Create(fees))
        self.wait(2)
        self.play(Uncreate(fees))
        self.wait(0.165)



        # TODO 3.213 secs덱스에서 수수료는 독특한 방식으로 작동합니다
        # TODO 0:00:04.165  ~  0:00:07.378
        # TODO 1.0secs pause
        # TODO 0:00:07.378  ~  0:00:08.378
        pool_rect = RoundedRectangle(width=7, height=4, corner_radius=0.5)
        pool_rect_text = Tex('BTC/USDT Pool').next_to(pool_rect, U)
        self.play(Create(pool_rect_text),
                  Create(pool_rect), run_time=1)
        self.wait(1)

        btc_lump = create_circle_asset(Tex(r'\textbf{BTC}',color=WHITE, font_size =30),  fill_color=C_BTC).scale_to_fit_height(2).shift(L * 1.5)
        usdt_lump = create_circle_asset(Tex(r'\textbf{USDT}',color=WHITE, font_size =25),  fill_color=C_USDT).scale_to_fit_height(2).shift(R * 1.5)
        # btc_lump.save_state()
        # usdt_lump.save_state()
        # btc_lump_arc = Arc(radius=2, angle=PI).flip(axis=np.array([ 0, 1, 0 ])).shift(L * 3.5)
        # usdt_lump_arc = Arc(radius=2, angle=PI).shift(R * 3.5)

        self.play(Create(btc_lump),
                  Create(usdt_lump), run_time=1)
        self.wait(0.213)



        # TODO 8.191 secs거래를 하기 위해 코인을 풀로 보내면 코인이 풀에 도착하기 전에 수수료를 떼고 남은 금액만 풀에 들어가서 그거에 맞게 거래가 일어납니다
        # TODO 0:00:08.378  ~  0:00:16.569
        # TODO 1.0secs pause
        # TODO 0:00:16.569  ~  0:00:17.569
        btc_lump_inflow = create_circle_asset(Tex(r'\textbf{BTC}',color=WHITE, font_size =30),  fill_color=C_BTC).scale_to_fit_height(2).shift(R * 5.5)

        self.play(Create(btc_lump_inflow), run_time=1)
        self.wait(1)
        self.play(btc_lump_inflow.animate.next_to(pool_rect, buff=1), run_time=1)
        self.wait(1)
        btc_lump_fee = create_circle_asset(Tex(r'\textbf{Fee}',color=WHITE, font_size =30),  fill_color=C_BTC).scale(0.65).move_to(btc_lump_inflow)
        btc_lump_fee.set_z_index(-1)

        self.play(btc_lump_inflow.animate.scale(0.8),
                  btc_lump_fee.animate.shift(D * 2), run_time=1)
        self.wait(1)

        self.play(FadeOut(btc_lump_inflow, target_position=btc_lump),
                  btc_lump.animate.scale(1.1), run_time=1)
        self.wait(1)
        usdt_lump_outflow = create_circle_asset(Tex(r'\textbf{USDT}',color=WHITE, font_size =25),  fill_color=C_USDT).scale_to_fit_height(2).shift(R * 5.5)
        self.play(FadeIn(usdt_lump_outflow, target_position=usdt_lump),
                  usdt_lump.animate.scale(1 / 1.1), run_time=1)
        self.wait(0.191)





        # TODO 3.66 secs그리고 거래가 종료되면 풀에 그냥 수수료를 추가합니다
        # TODO 0:00:17.569  ~  0:00:21.229
        # TODO 1.0secs pause
        # TODO 0:00:21.229  ~  0:00:22.229

        self.play(FadeOut(usdt_lump_outflow, shift=R), run_time=t)
        self.wait(1)
        self.play(FadeOut(btc_lump_fee, target_position=btc_lump),
                  btc_lump.animate.scale(1.05), run_time=2)
        self.wait(0.66)



        # TODO 6.185 secs수수료는 거래가 발생할 때마다 풀에 쌓이기 때문에 매번 거래가 종료되면 케이값은 증가합니다
        # TODO 0:00:22.229  ~  0:00:28.414
        # TODO 1.0secs pause
        # TODO 0:00:28.414  ~  0:00:29.414

        k_increase = Tex('K increased a bit', 'after every trade').arrange(D).next_to(pool_rect, D)

        self.play(Create(k_increase), run_time=3)
        self.wait(2)
        self.wait(2.185)


        # TODO 5.328 secs중앙화 거래소에서는 거래소가 가져가니 우리의 수수료가 가격에 영향을 줄 일은 없었습니다
        # TODO 0:00:29.414  ~  0:00:34.742
        # TODO 1.0secs pause
        # TODO 0:00:34.742  ~  0:00:35.742

        self.wait(6.328)

        # TODO 8.106 secs그러나 덱스에서는 수수료가 풀 내부의 비트 테더 비율을 조금씩 바꾸기 때문에 우리가 생각한 것과 미세하게 가격이 차이가 납니다
        # TODO 0:00:35.742  ~  0:00:43.848
        # TODO 1.0secs pause
        # TODO 0:00:43.848  ~  0:00:44.848
        self.wait(8.106)

        self.play(VGroup(pool_rect, pool_rect_text, btc_lump, usdt_lump, k_increase).animate.to_edge(L), run_time=1)


        # TODO 2.779 secs수수료가 1퍼인 상황을 생각해 보겠습니다
        # TODO 0:00:44.848  ~  0:00:47.627
        # TODO 1.0secs pause
        # TODO 0:00:47.627  ~  0:00:48.627


        #1.155의 역수
        #0.91부느이 1


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

        self.play(Create(fee_situation),run_time=1)
        self.play(Create(VGroup(k_var_fee, btc_var_fee, usdt_var_fee, price_var_fee, price_unit)),
                  usdt_lump.animate.scale (1/0.91),
                  btc_lump.animate.scale(1/1.155))
        new_usdt_lump=usdt_lump.copy().move_to(np.array([4,-2,0]))
        new_btc_lump = btc_lump.copy().move_to(np.array([4,-2,0])).shift(R*6)
        new_fee = create_circle_asset(Tex(r'\textbf{Fee}',color=WHITE, font_size =30),  fill_color=C_BTC).scale(0.65).move_to(np.array([4,-3.5,0]))


        self.wait(1.279)

        # TODO 5.895 secs비트 10개 3000테더가 있는 풀에 1비트를 보내면 수수료를 뗀 0.99비트가 전송됩니다
        # TODO 0:00:48.627  ~  0:00:54.522
        # TODO 1.0secs pause
        # TODO 0:00:54.522  ~  0:00:55.522

        self.play(new_btc_lump.animate.move_to(np.array([4,-2,0])))
        self.play(new_btc_lump.animate.scale(0.9),
                  FadeIn(new_fee, target_position=np.array([4,-2,0])))
        self.play(FadeOut(new_btc_lump,target_position=btc_lump),
                  btc_lump.animate.scale(1.1))

        self.play(btc_tracker_fee.animate.set_value(10.99),run_time=2.5)
        self.wait(1.395)


        # TODO 6.789 secs그리고 0.99에 대한 교환이 일어나고 풀에는 30000나누기 10.99인 2729테더가 남습니다
        # TODO 0:00:55.522  ~  0:01:02.311
        # TODO 1.0secs pause
        # TODO 0:01:02.311  ~  0:01:03.311

        k_div_by_10_99_1 = MathTex(r'y= \frac{30000}{10.99}').move_to(np.array([4,-2,0]))
        k_div_by_10_99_2= MathTex(r'y= 2729').move_to(np.array([4,-2,0]))

        self.play(Create(k_div_by_10_99_1))
        self.wait(0.5)
        self.play(TransformMatchingShapes(k_div_by_10_99_1,k_div_by_10_99_2))
        self.wait(1.5)
        self.play(Uncreate(k_div_by_10_99_2))
        self.wait(1)


        self.play(usdt_tracker_fee.animate.set_value(30000 / 10.99),
        FadeIn(new_usdt_lump,target_position=usdt_lump),
                  run_time=1)

        self.play(FadeOut(new_usdt_lump,shift=R),run_time=0.789)
        # self.wait(0.789)


        # TODO 2.537 secs지금까지는 케이는 여전히 30000입니다
        # TODO 0:01:03.311  ~  0:01:05.848
        # TODO 1.0secs pause
        # TODO 0:01:05.848  ~  0:01:06.848

        self.play(Circumscribe(k_var_fee),run_time=2)
        self.wait(1.537)


        # TODO 7.611 secs그뒤에 풀에 빼놨던 수수료인 0.01비트를 넣습니다. 풀에는 이제 11비트와 2729테더가 남아있습니다
        # TODO 0:01:06.848  ~  0:01:14.459
        # TODO 1.0secs pause
        # TODO 0:01:14.459  ~  0:01:15.459
        self.play(FadeOut(new_fee, target_position=btc_lump),
                  btc_lump.animate.scale(1.05))
        self.play(btc_tracker_fee.animate.set_value(11),run_time=5)
        self.wait(3.611)

        # TODO 6.366 secs케이는 30027.297로 약간 증가했습니다 현재 비트의 가격은 248.15테더입니다
        # TODO 0:01:15.459  ~  0:01:21.825
        # TODO 1.0secs pause
        # TODO 0:01:21.825  ~  0:01:22.825
        self.play(k_tracker_fee.animate.set_value(11 * (30000 / 10.99)), run_time=4)

        self.play(Circumscribe(price_var_fee),run_time=2)
        self.wait(1.366)


        # TODO 7.417 secs원래 1비트를 매도했다고 생각하면 가격은 30000나누기 11나누기 11인 247.93테더가 되어야합니다
        # TODO 0:01:22.825  ~  0:01:30.242
        # TODO 1.0secs pause
        # TODO 0:01:30.242  ~  0:01:31.242


        k_div_by_11_1 = MathTex(r'\frac{30000}{11} \divisionsymbol 11').move_to(np.array([4,-2,0]))
        # k_div_by_11_2= MathTex(r'247.93').move_to(np.array([4,-2,0]))


        if_fee = Tex(r'If it were 11 BTC,', 'it would be 247.93 USDT').arrange(D).next_to(price_var_fee, D, buff=1).align_to(price_var_fee,
                                                                                                                            L)
        self.play(Create(k_div_by_11_1))
        self.wait(3)

        self.play(TransformMatchingShapes(k_div_by_11_1,if_fee))
        self.play(Circumscribe(if_fee))
        self.wait(2.417)


        # TODO 6.693 secs그러나 수수료가 있었다면 30000나누기 10.99 나누기 11인 248.15 테더가 됩니다
        # TODO 0:01:31.242  ~  0:01:37.935
        # TODO 1.0secs pause
        # TODO 0:01:37.935  ~  0:01:38.935

        self.wait(5.693)
        self.play(Circumscribe(price_var_fee))

        # TODO 3.636 secs즉 이전 거래자의 행동에 따라서 미세하게 이익이 바뀝니다
        # TODO 0:01:38.935  ~  0:01:42.571
        # TODO 1.0secs pause
        # TODO 0:01:42.571  ~  0:01:43.571

        self.play(Uncreate(VGroup(if_fee)),run_time=2)
        self.play(Uncreate(VGroup(fee_situation,k_var_fee, btc_var_fee, usdt_var_fee, price_var_fee, price_unit)),run_time=2)


        # TODO 12.781 secs비트를 매도하는 행위에서 수수료가 있던 경우가 가격이 덜 떨어졌으므로 같은 방향, 즉 이후에 매도할 사람은 원래 앞사람이 거래하고 247테더를 생각하고 있었으나 예상보다 돈을 좀 더 건질 수 있게 됐습니다
        # TODO 0:01:43.571  ~  0:01:56.352
        # TODO 1.0secs paus
        # TODO 0:01:56.352  ~  0:01:57.352

        if_same_direction = Tex(r'Another seller\\sells at a better price.\\ \quad \\247.93 USDT\\ $\Downarrow$ \\ 248.16 USDT').arrange(D,buff=1).shift(R*4)
        self.wait(5)
        self.play(Create(if_same_direction))
        self.wait(8)

        # TODO 6.765 secs반대로 앞사람과 반대방향 즉 매수를 하려던 사람은 자신이 앞사람을 보고 생각하던 247달러보다
        # TODO 0:01:57.352  ~  0:02:04.117
        # TODO 1.0secs pause
        # TODO 0:02:04.117  ~  0:02:05.117
        if_opps_direction = Tex(r'Another buyer\\buys at a worse price.\\ \quad \\247.93 USDT\\ $\Downarrow$ \\ 248.16 USDT').arrange(D,buff=1).shift(R*4)
        self.play(TransformMatchingTex(if_same_direction,if_opps_direction))
        self.wait(5)

        # TODO 4.434 secs높은 248테더에 매수를 해야해서 예상보다 지출이 늘었습니다
        # TODO 0:02:05.117  ~  0:02:09.551
        # TODO 1.0secs pause
        # TODO 0:02:09.551  ~  0:02:10.551




        self.wait(30)



class L02S12(MovingCameraScene):
    def construct(self):
        # self.add(NumberPlane().set_z_inex(1))

        speak(self, title='Scene2', txt=
        '#9'
        '#9'
        '#9'
        '#9'
        '#1'
        '잠시 복습해보고 좀 더 복잡한 상황을 다뤄보겠습니다#1'
        '케이가 증가하는 상황은 색을 좀 더 진하게 감소하는 상황은 연하게, 가격이 내려가는 것은 빨간색 올라가는 것은 초록색으로 표시했습니다. 원점은 회색입니다#1'

        '비티씨 매수로 가격이 상승하는 상황입니다#1'
        '비티씨 매도로 가격이 하락하는 상황입니다#3'
        '유동성 공급으로 케이가 상승하는 상황입니다#1'
        '유동성 제거로 케이가 하락하는 상황입니다#1'
        '다시 한번 명심할 것은 유동성 공급, 제거는 가격과 관계가 없습니다#1'
        '그냥 지금 가격에 맞게 풀 사이즈만 변화시키기에 가격을 움직이는 행위가 아닙니다#1'
        '그러므로 거래자 활동과 달리 프라이스 임팩트와 관계가 전혀 없습니다#1'

        '기본적인 상황들을 복습해봤습니다#1'

        '케이상승 후 가격상승 또는 하락하는 경우를 보겠습니다#1'
        '케이가 상승했다는 것은 유동성이 풍부해졌다는 것이고 이전과 같은 양의 비티씨를 거래하더라도 프라이스 임팩트가 적어집니다#1'
        '아까 300테더에서 3개를 매도할 때는 프라이스 임팩트가 23퍼센트 발생했지만#1'
        '지금은 유동성으 풍부하고 3개 매도할 때 프라이스 임팩트가 19퍼센트만 발생했습니다#1'
        '아까 300테더에서 3개를 매수할 때는 프라이스 임팩트가 43퍼센트 발생했지만#1'
        '지금은 유동성이 풍부하고 3개 매수할 때  프라이스 임팩트가 30퍼센트 발생했습니다#1'
        '같은 3비티씨지만 풀에서 차지하는 비율이 적어졌다#1'
        '아까는 10분에 3 지금은 13분에 3, 퍼센트로 따지면 33퍼와 23퍼센트입니다#1'

        '케이하락 후 가격상승 또는 하락하는 경우를 보겠습니다#1'
        '케이가 하락했다는 것은 유동성이 줄었다는 것이고 이전과 같은 양의 비티씨를 거래하더라도 프라이스 임팩트가 커집니다#1'
        '아까 300데터에서 3개를 매도할 때는 프라이스 임팩트가  23퍼센트 발생했지만 #1'
        '지금은 유동성으 적어졌고 3개 매도할 때 프라이스 임팩트가 30퍼센트 발생했습니다#1'
        '아까 300테더에서 3개를 매수할 때는 프라이스 임팩트가 43퍼센트 발생했지만#1'
        '지금은 유동성으 적어졌고 3개 매수할 때 프라이스 임팩트가 75퍼센트 발생했습니다#1'
        '같은 3비티씨지만 풀에서 차지하는 비율이 커졌습니다#1'
        '아까는 10분에 3 지금은 7 분에 3, 퍼센트로 따지면 33퍼와 42퍼센트입니다#1'

        '이번에는 가격이 먼저 상승하고 케이상승 또는 하락하는 상황입니다#1'
        '아까와 달리 현재 가격은 이미 움직인 상태고 이 가격에 맞게 같은 가치를 넣어줘야합니다#1'
        '아까와 같이 3비티씨만큼 유동성을 공급하려고 하면 1개당 올라버린 가격인 612 테더를 넣어줘야합니다#1'
        '그래서 풀에서 같은 비중을 차지하기 위해서 더 많은 자금이 필요하게 됐습니다#1'
        '만약 아까 넣은 3비티씨와 900테더에 대한 엘피토큰을 가지고 유동성을 빼려고 하면 올라가있는 현재 가격대로 비티씨 한 개당 612테더를 돌려받게 됩니다#3'

        '이번에는 가격이 먼저 하락하고 케이상승 및 하락하는 상황입니다#1'
        '어번에도 현재가격에 맞게 같은 가치를 넣어줘야합니다#1'
        '아까와 같이 3비티씨만큼 유동성을 공급하려고 하면 1개당 내려버린 가격인 177 테더를 넣어줘야합니다#1'
        '그래서 풀에서 같은 비중을 차지하기 위해서 더 적은 자금이 필요하게 됏습니다#1'
        '만약 아까 넣은 3비티씨와 900테더에 대한 엘피토큰을 가지고 유동성을 빼려고 하면 내려가있는 현재 가격대로 비티씨 한 개당 177테더를 돌려받게 됩니다#3'

        '각 케이스마다 눈에 잘 보이게 선으로 연결해봤습니다#1'
        '동영상을 다시 보면서 천천히 곱씹어보시면 더 이해가 잘 될겁니다#1'
              , keep_pitch=True, update=1, speed=1.4)

        xyk_fraction = MathTex('y', '=', r'\frac{k}{x}').to_edge(UL)

        liq_pool_rect = RoundedRectangle(height=6.3, width=4, corner_radius=0.5)
        liq_pool_text = Tex('Liquidity Pool').next_to(liq_pool_rect, UP)
        liq_pool = VGroup(liq_pool_rect, liq_pool_text).to_edge(UL).shift(R * 0.5)
        liq_pool.set_z_index(3)

        k_var = Variable(30000, MathTex("k"), var_type=Integer).to_edge(UR)
        k_tracker = k_var.tracker
        k_tracker.set_value(30000)

        liq_provider = create_entity(Tex(r' \emph{Init Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", C_BTC, 1.4,
                                     0.3, asset_text_color=WHITE).next_to(liq_pool_rect, RIGHT, buff=1.5)
        btc_asset = liq_provider[ 1 ]
        usdt_asset = create_entity("A", 0.5, WHITE, "3000 USDT", C_USDT, 1.4, 0.3, asset_text_color=WHITE)[ 1 ].next_to(liq_provider, DOWN,
                                                                                                                        buff=0.1)
        liq_provider.add(usdt_asset)

        self.play(Create(liq_provider), run_time=3)
        self.wait(6.498)

        ax = Axes(x_range=[ 0, 18, 4 ], y_range=[ 0, 6500, 1000 ], x_length=5, y_length=5, tips=True,
                  axis_config={"include_numbers": False, 'color': WHITE, 'include_ticks': False, 'font_size': 20}, ).to_edge(DR, buff=0.8)

        ax.shift(U * (liq_pool_rect.get_bottom()[ 1 ] - ax[ 0 ].get_y()))

        y_axis_label = ax.get_y_axis_label(MathTex('Amount of USDT in Pool', color=WHITE).rotate(PI / 2).scale(0.4), edge=LEFT,
                                           direction=LEFT, buff=0.37)
        x_axis_label = ax.get_x_axis_label(MathTex('Amount of BTC in Pool', color=WHITE).scale(0.4), edge=DOWN, direction=DOWN, buff=0.37)
        axis_labels = VGroup(x_axis_label, y_axis_label)

        usdt_bar = Rectangle(height=3, width=1.2, fill_color=C_USDT, fill_opacity=1, color=C_USDT)
        btc_bar = Rectangle(height=1, width=1.2, fill_color=C_BTC, fill_opacity=1, color=C_BTC)
        bars = VGroup(btc_bar, usdt_bar)
        bars.arrange(RIGHT, aligned_edge=DOWN).move_to(liq_pool_rect).align_to(liq_pool_rect, DOWN)

        usdt_bar_pos = usdt_bar.get_bottom()
        btc_bar_pos = btc_bar.get_bottom()

        btc_var = Variable(10, MathTex("BTC"), var_type=Integer)
        usdt_var = Variable(3000, MathTex("USDT"), var_type=Integer).next_to(btc_var, DOWN, aligned_edge=LEFT)
        btc_tracker = btc_var.tracker
        usdt_tracker = usdt_var.tracker
        usdt_var[ 0 ][ 0 ].set_color(C_USDT)
        btc_var[ 0 ][ 0 ].set_color(C_BTC)

        vars = VGroup(btc_var, usdt_var).arrange(DOWN, aligned_edge=LEFT).next_to(liq_pool_rect, DOWN, buff=0.25)
        # self.play(Create(liq_pool), run_time=1)
        # self.wait(1)

        self.play(Create(liq_pool),
                  ReplacementTransform(usdt_asset, usdt_bar),
                  ReplacementTransform(btc_asset, btc_bar), run_time=6)
        self.wait(1)
        self.play(Create(usdt_var),
                  Write(btc_var), run_time=2)
        self.wait(1)
        usdt_bar.add_updater(lambda usdt_bar: usdt_bar.become(
            Rectangle(height=usdt_tracker.get_value() / 1000, width=1.2, fill_color=C_USDT, fill_opacity=1, color=C_USDT).move_to(
                usdt_bar_pos).align_to(liq_pool_rect, DOWN)))
        btc_bar.add_updater(lambda btc_bar: btc_bar.become(
            Rectangle(height=btc_tracker.get_value() / 10, width=1.2, fill_color=C_BTC, fill_opacity=1, color=C_BTC).move_to(
                btc_bar_pos).align_to(liq_pool_rect, DOWN)))

        pool_price = Variable(100, 'Price', var_type=DecimalNumber, num_decimal_places=2).next_to(
            liq_pool_rect, RIGHT, buff=0.5).scale(0.8).to_edge(UP)
        pool_price_tracker = pool_price.tracker
        pool_price.add_updater(lambda v: pool_price_tracker.set_value(usdt_tracker.get_value() / btc_tracker.get_value()))
        pool_price_unit = Tex(r'USDT').scale(0.75).next_to(pool_price, buff=0.1)
        pool_price.add(pool_price_unit)
        self.play(Write(k_var[ 0 ]), run_time=1.5)
        self.wait(1)
        self.play(Create(ax),
                  Create(axis_labels),
                  Create(pool_price),
                  TransformMatchingShapes(Group(btc_var[ 1 ].copy(), usdt_var[ 1 ].copy()), k_var[ 1 ]),
                  Create(xyk_fraction.next_to(k_var, LEFT, buff=1)), run_time=5
                  )

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
        x_marker = Triangle(color=C_BTC, fill_color=C_BTC, fill_opacity=1).scale(0.1).next_to(vertical_line, DOWN, buff=0)
        x_marker.add_updater(lambda marker: marker.next_to(vertical_line, DOWN, buff=0))
        x_marker_val = Integer(btc_tracker.get_value())
        x_marker_val.add_updater(
            lambda integer: integer.become(Integer(btc_tracker.get_value()).scale(0.4).next_to(vertical_line, DOWN, buff=0.3)))

        y_marker = Triangle(color=C_USDT, fill_color=C_USDT, fill_opacity=1).scale(0.1).rotate(-PI / 2).next_to(horizontal_line, LEFT,
                                                                                                                buff=0)
        y_marker.add_updater(lambda marker: marker.next_to(horizontal_line, LEFT, buff=0))
        y_marker_val = Integer(usdt_tracker.get_value())
        y_marker_val.add_updater(lambda integer: integer.become(
            Integer(usdt_tracker.get_value()).scale(0.4).rotate(PI / 2).next_to(horizontal_line, LEFT, buff=0.3)))

        lines = VGroup(vertical_line, horizontal_line)
        markers = VGroup(x_marker, x_marker_val, y_marker, y_marker_val)

        self.play(Create(xyk_graph_btc), run_time=0.5)
        self.wait(0.5)
        self.play(Create(curr_dot), run_time=0.5)
        self.play(Create(lines), run_time=1.5)
        self.play(Create(markers), run_time=0.5)
        self.play(Uncreate(liq_provider), run_time=0.5)
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
        self.play(Create(area), run_time=0.5)
        self.play(Create(area_text), run_time=0.5)

        self.wait(5.5)

        # E##############################################

        # TODO 3.479 secs잠시 복습해보고 좀 더 복잡한 상황을 다뤄보겠습니다
        # TODO 0:00:37.000  ~  0:00:40.479
        # TODO 1.0secs pause
        # TODO 0:00:40.479  ~  0:00:41.479

        # TODO 10.16 secs케이가 증가하는 상황은 색을 좀 더 진하게 감소하는 상황은 연하게, 가격이 내려가는 것은 빨간색 올라가는 것은
        #  초록색으로 표시했습니다. 원점은 회색입니다
        # TODO 0:00:41.479  ~  0:00:51.639
        # TODO 1.0secs pause
        # TODO 0:00:51.639  ~  0:00:52.639

        k_org_px_org_dot = curr_dot.copy().clear_updaters().set_color(GREY).set_z_index(1.5).scale(1.2)
        self.play(Create(k_org_px_org_dot))
        self.wait(14.639)

        # 가격 상승#####################################################################################
        # TODO 2.899 secs비티씨 매수로 가격이 상승하는 상황입니다
        # TODO 0:00:52.639  ~  0:00:55.538
        # TODO 1.0secs pause
        # TODO 0:00:55.538  ~  0:00:56.538

        def get_halfway(point_A, point_B, z=0):
            x_dist = (abs(point_A[ 0 ]) + abs(point_B[ 0 ])) / 2
            y_dist = (abs(point_A[ 1 ]) + abs(point_B[ 1 ])) / 2

            if point_A[ 0 ] < point_B[ 0 ]:
                x = point_A[ 0 ] + x_dist
            else:
                x = point_A[ 0 ] + x_dist

            if point_A[ 1 ] < point_B[ 1 ]:
                y = point_A[ 1 ] + y_dist
            else:
                y = point_A[ 1 ] + y_dist

            return np.array([ x, y, z ])

        position = get_halfway(np.array([ liq_pool_rect.get_right()[ 0 ], liq_pool_rect.get_right()[ 1 ], 0 ]),
                               np.array([ ax.get_left()[ 0 ], liq_pool_rect.get_right()[ 1 ], 0 ]))
        position[ 1 ] = position[ 1 ] + 1
        px_up = MathTex(r'Price \  \Uparrow').move_to(position)
        self.play(Write(px_up))

        self.play(
            btc_tracker.animate.set_value(7),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
            run_time=1, rate_func=rate_functions.ease_in_out_quint)

        self.wait(1)
        self.play(Unwrite(px_up), run_time=0.899)
        # self.wait(2)

        k_org_px_up_dot = curr_dot.copy().clear_updaters().set_color(GREEN_C).set_z_index(1.5)
        self.add(k_org_px_up_dot)

        # 가격 하락#####################################################################################

        # TODO 2.875 secs비티씨 매도로 가격이 하락하는 상황입니다

        # TODO 0:00:56.538  ~  0:00:59.413

        # TODO 1.0secs pause

        # TODO 0:00:59.413  ~  0:01:00.413
        px_dn = MathTex(r'Price \  \Downarrow').move_to(position)
        self.play(Write(px_dn))

        self.play(
            btc_tracker.animate.set_value(13),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)),
            run_time=1, rate_func=rate_functions.ease_in_out_quint)

        self.wait(1)
        self.play(Unwrite(px_dn), run_time=0.875)

        k_org_px_dn_dot = curr_dot.copy().clear_updaters().set_color(RED_C).set_z_index(1.5)
        self.add(k_org_px_dn_dot)

        # 원점#####################################################################################
        k_origin_px_origin = MathTex(r'ORIGIN').move_to(position)
        self.play(Write(k_origin_px_origin), run_time=0.5)

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=0.5, rate_func=rate_functions.ease_in_out_quint)

        self.wait(0.5)
        self.play(Unwrite(k_origin_px_origin), run_time=0.5)

        # K 하락#####################################################################################
        # TODO 2.851 secs유동성 제거로 케이가 하락하는 상황입니다

        # TODO 0:01:04.301  ~  0:01:07.152
        # TODO 1.0secs pause
        # TODO 0:01:07.152  ~  0:01:08.152
        k_dn = MathTex(r'K \  \Downarrow').move_to(position)
        self.play(Write(k_dn), run_time=1)

        self.play(k_tracker.animate.set_value(14700),
                  btc_tracker.animate.set_value(7),
                  usdt_tracker.animate.set_value(14700 / 7),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # 케이가 하락한다는 건 풀에서 누군가 유동성을 빼간 것입니다.
        # 명심할 것은 케이의 변동은 가격과 관계가 없음
        # 내가 유동성 풀에 제거하고 싶으면
        # 그냥 지금 가격에 맞게 빼가면 됨
        # 스왑처럼 내가 가격을 움직이며 하는 행위가 아님
        # 왜냐하면 가격이란 풀 내부의 비율인데
        # 지금 비율(1개에 300달러) 그대로 빼기 때문에
        # 가격은 움직이지 않고 그로인해 슬리피지등이 발생하지 않는다
        # 착각 금지

        self.wait(1)
        self.play(Unwrite(k_dn), run_time=0.851)

        k_dn_px_org_dot = curr_dot.copy().clear_updaters().set_color(WHITE).set_z_index(1.5)
        self.add(k_dn_px_org_dot)

        # K 상승#####################################################################################

        # TODO 2.888 secs유동성 공급으로 케이가 상승하는 상황입니다
        # TODO 0:01:00.413  ~  0:01:03.301
        # TODO 1.0secs pause
        # TODO 0:01:03.301  ~  0:01:04.301

        k_up = MathTex(r'K \  \Uparrow').move_to(position)
        self.play(Write(k_up), run_time=1)

        self.play(k_tracker.animate.set_value(50700),
                  btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(50700 / 13),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        # 케이가 상승한다는 건 풀에 누군가 추가 유동성을 공급하는 것입니다.
        # 마찬가지로 가격은 전혀 움직이지 않음
        # 현재 가격에 맞게 비티씨와 유에스디티를 그대로 추가함
        # 풀사이즈는 커짐

        self.wait(1)
        self.play(Unwrite(k_up), run_time=0.888)

        k_up_px_org_dot = curr_dot.copy().clear_updaters().set_color(DARK_GREY).set_z_index(1.5)
        self.add(k_up_px_org_dot)

        # TODO 4.7 secs다시 한번 명심할 것은 유동성 공급, 제거는 가격과 관계가 없습니다
        # TODO 0:01:08.152  ~  0:01:12.852
        # TODO 1.0secs pause
        # TODO 0:01:12.852  ~  0:01:13.852
        # TODO 4.977 secs그냥 지금 가격에 맞게 풀 사이즈만 변화시키기에 가격을 움직이는 행위가 아닙니다
        # TODO 0:01:13.852  ~  0:01:18.829
        # TODO 1.0secs pause
        # TODO 0:01:18.829  ~  0:01:19.829
        # TODO 4.349 secs그러므로 거래자 활동과 달리 프라이스 임팩트와 관계가 전혀 없습니다
        # TODO 0:01:19.829  ~  0:01:24.178
        # TODO 1.0secs pause
        # TODO 0:01:24.178  ~  0:01:25.178
        # TODO 2.175 secs기본적인 상황들을 복습해봤습니다
        # TODO 0:01:25.178  ~  0:01:27.353
        # TODO 1.0secs pause
        # TODO 0:01:27.353  ~  0:01:28.353

        # K 원점#####################################################################################
        k_origin = MathTex(r'ORIGIN').move_to(position)
        self.play(Write(k_origin), run_time=0.5)

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        self.wait(0.5)
        self.play(Unwrite(k_origin), run_time=1)

        self.wait(18.201)

        # TODO 3.697 secs케이상승 후 가격상승 또는 하락하는 경우를 보겠습니다
        # TODO 0:01:28.353  ~  0:01:32.050
        # TODO 1.0secs pause
        # TODO 0:01:32.050  ~  0:01:33.050

        # TODO 7.611 secs케이가 상승했다는 것은 유동성이 풍부해졌다는 것이고 이전과 같은 양의 비티씨를 거래하더라도 프라이스 임팩트가 적어집니다
        # TODO 0:01:33.050  ~  0:01:40.661
        # TODO 1.0secs pause
        # TODO 0:01:40.661  ~  0:01:41.661

        self.wait(5)
        k_up_px_dn = MathTex(r'K \  \Uparrow', r'Price\  \Downarrow').arrange(D).move_to(position)
        k_up_px_up = MathTex(r'K \  \Uparrow', r'Price\  \Uparrow').arrange(D).move_to(position)
        self.play(Write(k_up_px_dn[ 0 ]))

        self.play(k_tracker.animate.set_value(50700),
                  btc_tracker.animate.set_value(13),
                  usdt_tracker.animate.set_value(50700 / 13),
                  run_time=2, rate_func=rate_functions.ease_in_out_quint)

        self.wait(5.308)

        # K 상승 가격 하락#####################################################################################

        # TODO 5.581 secs아까 300테더에서 3개를 매도할 때는 프라이스 임팩트가 23퍼센트 발생했지만
        # TODO 0:01:55.102  ~  0:02:00.683
        # TODO 1.0secs pause
        # TODO 0:02:00.683  ~  0:02:01.683

        # TODO 5.932 secs지금은 유동성으 풍부하고 3개 매도할 때 프라이스 임팩트가 19퍼센트만 발생했습니다
        # TODO 0:02:01.683  ~  0:02:07.615
        # TODO 1.0secs pause
        # TODO 0:02:07.615  ~  0:02:08.615
        share_change_1 = MathTex(r'Moving\\ 30\% $\rightarrow$ 23\% \\of\  the\  pool', tex_environment='center').move_to(position)
        k_up_px_dn_text_1 = MathTex(r'Price Impact\\23\% \\ $\downarrow$ \\ 19\%', tex_environment='center').arrange(D).next_to(k_up_px_dn,
                                                                                                                                D,
                                                                                                                                buff=0.75)
        k_up_px_up_text_1 = MathTex(r'Price Impact\\43\% \\ $\downarrow$ \\ 30\%', tex_environment='center').arrange(D).next_to(k_up_px_dn,
                                                                                                                                D,
                                                                                                                                buff=0.75)

        self.play(Write(k_up_px_dn[ 1 ]))

        self.play(
            btc_tracker.animate.set_value(16),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(16)),
            run_time=5, rate_func=rate_functions.ease_in_out_quint)

        self.play(Create(k_up_px_dn_text_1))
        self.wait(4)
        self.play(Uncreate(k_up_px_dn_text_1))

        self.play(Unwrite(k_up_px_dn[ 1 ]))

        self.wait(0.513)
        k_up_px_dn_dot = curr_dot.copy().clear_updaters().set_color(C0193).set_z_index(1.5)
        self.add(k_up_px_dn_dot)

        # TODO 5.69 secs아까 300테더에서 3개를 매수할 때는 프라이스 임팩트가 43퍼센트 발생했지만
        # TODO 0:01:41.661  ~  0:01:47.351
        # TODO 1.0secs pause
        # TODO 0:01:47.351  ~  0:01:48.351

        # TODO 5.751 secs지금은 유동성으 풍부하고 3개 매수할 때  프라이스 임팩트가 30퍼센트 발생했습니다
        # TODO 0:01:48.351  ~  0:01:54.102
        # TODO 1.0secs pause
        # TODO 0:01:54.102  ~  0:01:55.102
        self.play(Write(k_up_px_up[ 1 ]))

        self.play(
            btc_tracker.animate.set_value(10),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(10)),
            run_time=5, rate_func=rate_functions.ease_in_out_quint)

        self.play(Create(k_up_px_up_text_1))
        self.wait(4)
        self.play(Uncreate(k_up_px_up_text_1))

        self.play(Unwrite(k_up_px_up[ 1 ]), Unwrite(k_up_px_dn[ 0 ]))
        self.wait(0.441)

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

        # TODO 3.636 secs같은 3비티씨지만 풀에서 차지하는 비율이 적어졌다
        # TODO 0:02:08.615  ~  0:02:12.251
        # TODO 1.0secs pause
        # TODO 0:02:12.251  ~  0:02:13.251

        # TODO 6.113 secs아까는 10분에 3 지금은 13분에 3, 퍼센트로 따지면 33퍼와 23퍼센트입니다
        # TODO 0:02:13.251  ~  0:02:19.364
        # TODO 1.0secs pause
        # TODO 0:02:19.364  ~  0:02:20.364

        self.wait(2)

        self.play(Create(share_change_1))
        self.wait(5)
        self.play(Uncreate(share_change_1))

        k_up_px_up_dot = curr_dot.copy().clear_updaters().set_color(C1193).set_z_index(1.5)
        self.add(k_up_px_up_dot)

        # K 원점#####################################################################################
        k_origin_px_origin = MathTex(r'ORIGIN').move_to(position)
        self.play(Write(k_origin_px_origin), run_time=0.5)

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        self.wait(0.5)
        self.play(Unwrite(k_origin_px_origin), run_time=0.749)

        k_dn_px_dn = MathTex(r'K\  \Downarrow', r'Price \  \Downarrow').arrange(D).move_to(position)
        k_dn_px_up = MathTex(r'K\  \Downarrow', r'Price \  \Uparrow').arrange(D).move_to(position)

        share_change_2 = MathTex(r'Moving\\ 30\%$\rightarrow$42\% \\of\  the\  pool', tex_environment='center').move_to(position)

        k_dn_px_dn_text_1 = MathTex(r'Price Impact\\23\% \\ $\downarrow$ \\ 30\%', tex_environment='center').arrange(D).next_to(k_dn_px_dn,
                                                                                                                                D,
                                                                                                                                buff=0.75)
        k_dn_px_up_text_1 = MathTex(r'Price Impact\\43\% \\ $\downarrow$ \\ 75\%', tex_environment='center').arrange(D).next_to(k_dn_px_dn,
                                                                                                                                D,
                                                                                                                                buff=0.75)

        self.play(Write(k_dn_px_dn[ 0 ]))

        self.play(k_tracker.animate.set_value(14700),
                  btc_tracker.animate.set_value(7),
                  usdt_tracker.animate.set_value(14700 / 7),
                  run_time=2, rate_func=rate_functions.ease_in_out_quint)

        self.wait(9.8)

        self.play(Write(k_dn_px_dn[ 1 ]))

        self.play(
            btc_tracker.animate.set_value(10),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(10)),
            run_time=5, rate_func=rate_functions.ease_in_out_quint)

        self.play(Create(k_dn_px_dn_text_1))
        self.wait(4)
        self.play(Uncreate(k_dn_px_dn_text_1))

        self.play(Unwrite(k_dn_px_dn[ 1 ]), run_time=1)
        self.wait(1.308)

        k_dn_px_dn_dot = curr_dot.copy().clear_updaters().set_color(RED_A).set_z_index(1.5)
        self.add(k_dn_px_dn_dot)

        self.play(Write(k_dn_px_up[ 1 ]))

        self.play(
            btc_tracker.animate.set_value(4),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(4)),
            # area_text.animate.rotate(PI / 2),
            run_time=5, rate_func=rate_functions.ease_in_out_quint)

        self.play(Create(k_dn_px_up_text_1))
        self.wait(4)
        self.play(Uncreate(k_dn_px_up_text_1))

        self.play(Unwrite(k_dn_px_up[ 1 ]),
                  Unwrite(k_dn_px_dn[ 0 ]))

        self.wait(0.417)

        self.wait(2)
        self.play(Create(share_change_2))
        self.wait(5)
        self.play(Uncreate(share_change_2))

        k_dn_px_up_dot = curr_dot.copy().clear_updaters().set_color(GREEN_A).set_z_index(1.5)
        self.add(k_dn_px_up_dot)

        # 원점#####################################################################################
        k_origin_px_origin = MathTex(r'ORIGIN').move_to(position)
        self.play(Write(k_origin_px_origin), run_time=0.5)

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=1, rate_func=rate_functions.ease_in_out_quint)

        self.wait(0.5)
        self.play(Unwrite(k_origin_px_origin), run_time=0.5)
        self.wait(0.334)

        # TODO 4.277 secs이번에는 가격이 먼저 상승하고 케이상승 또 하락하는 상황입니다
        # TODO 0:03:11.928  ~  0:03:16.205
        # TODO 1.0secs pause
        # TODO 0:03:16.205  ~  0:03:17.205

        # TODO 5.738 secs아까와 달리 현재 가격은 이미 움직인 상태고 이 가격에 맞게 같은 가치를 넣어줘야합니다
        # TODO 0:03:17.205  ~  0:03:22.943
        # TODO 1.0secs pause
        # TODO 0:03:22.943  ~  0:03:23.943

        px_up_k_up = MathTex(r'Price \  \Uparrow', r'K\  \Uparrow').arrange(D).move_to(position)
        px_up_k_dn = MathTex(r'Price \  \Uparrow', r'K\  \Downarrow').arrange(D).move_to(position)

        self.play(Write(px_up_k_up[ 0 ]), run_time=1)

        self.play(
            btc_tracker.animate.set_value(7),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(7)),
            run_time=2, rate_func=rate_functions.ease_in_out_quint)

        self.wait(9.06)
        # 이제는 가격이 상승한 상태에서 k를 움직여보겟습니다

        # 가격 상승에서 K상승#####################################################################################
        ##### 가격상승 후 케이상승 및 하락
        ##### 아까와 달리 현재 가격은 이미 움직인 상태고 이 가격에 맞게 같은 가치를 넣어줘야합니다
        ##### 아까와 같이 2비티씨만큼 유동성을 공급하려고 하면 올라버린 가격에 맞게 테더를 넣어줘야합니다
        ##### 그래서 풀에서 같은 비중을 차지하기 위해서 더 많은 자금이 필요하게 됏ㅅ브니다
        ##### 만약 아까 넣은 2비티씨를 유동성을 빼려고 하면 현재 가격대로 돌려받게 됩니다

        # TODO 6.959 secs아까와 같이 3비티씨만큼 유동성을 공급하려고 하면 1개당 올라버린 가격인 612 테더를 넣어줘야합니다
        # TODO 0:03:23.943  ~  0:03:30.902
        # TODO 1.0secs pause
        # TODO 0:03:30.902  ~  0:03:31.902
        # TODO 4.591 secs그래서 풀에서 같은 비중을 차지하기 위해서 더 많은 자금이 필요하게 됐습니다
        # TODO 0:03:31.902  ~  0:03:36.493
        # TODO 1.0secs pause
        # TODO 0:03:36.493  ~  0:03:37.493

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

        self.wait(3)
        self.play(Unwrite(px_up_k_up[ 1 ]))
        self.wait(0.868)

        px_up_k_up_dot = curr_dot.copy().clear_updaters().set_color(TEAL_E).set_z_index(1.5)
        self.add(px_up_k_up_dot)

        # 가격 상승에서 K하락#####################################################################################

        # TODO 9.737 secs만약 아까 넣은 3비티씨와 900테더에 대한 엘피토큰을 가지고 유동성을 빼려고 하면 올라가있는 현재 가격대로 비티씨 한 개당 612테더를 돌려받게 됩니다
        # TODO 0:03:37.493  ~  0:03:47.230
        # TODO 1.0secs pause
        # TODO 0:03:47.230  ~  0:03:48.230

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

        self.wait(3)
        self.play(Unwrite(px_up_k_dn[ 1 ]),
                  Uncreate(px_up_k_up[ 0 ]))
        self.wait(0.737)

        px_up_k_dn_dot = curr_dot.copy().clear_updaters().set_color(TEAL_A).set_z_index(1.5)
        self.add(px_up_k_dn_dot)

        # 원점점#####################################################################################

        k_origin_px_origin = MathTex(r'ORIGIN').move_to(position)
        self.play(Write(k_origin_px_origin), run_time=0.5)

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=0.5, rate_func=rate_functions.ease_in_out_quint)

        self.wait(0.5)
        self.play(Unwrite(k_origin_px_origin), run_time=0.5)
        # self.wait(2)

        # TODO 4.059 secs이번에는 가격이 먼저 하락하고 케이상승 및 하락하는 상황입니다
        # TODO 0:03:48.230  ~  0:03:52.289
        # TODO 1.0secs pause
        # TODO 0:03:52.289  ~  0:03:53.289

        # TODO 3.564 secs어번에도 현재가격에 맞게 같은 가치를 넣어줘야합니다
        # TODO 0:03:53.289  ~  0:03:56.853
        # TODO 1.0secs pause
        # TODO 0:03:56.853  ~  0:03:57.853

        px_dn_k_up = MathTex(r'Price \  \Downarrow', r'K\  \Uparrow').arrange(D).move_to(position)
        px_dn_k_dn = MathTex(r'Price \  \Downarrow', r'K\  \Downarrow').arrange(D).move_to(position)

        self.play(Write(px_dn_k_up[ 0 ]))

        self.play(
            btc_tracker.animate.set_value(13),
            usdt_tracker.animate.set_value(xyk_graph_btc.underlying_function(13)),
            run_time=2, rate_func=rate_functions.ease_in_out_quint)

        # self.wait(2)
        self.wait(6.623)

        # 가격 하락에서 K상승#####################################################################################

        #####
        ##### 가격하락 후 케이상승 및 하락
        ##### 아까와 달리 현재 가격은 이미 움직인 상태고 이 가격에 맞게 같은 가치를 넣어줘야합니다
        ##### 아까와 같이 2비티씨만큼 유동성을 공급하려고 하면 떨어진 가격에 맞게 테더를 넣어줘야합니다
        ##### 그래서 풀에서 같은 비중을 차지하기 위해서 더 적은 자금이 필요하게 됏습니다
        ##### 만약 아까 넣은 2비티씨를 유동성을 빼려고 하면 현재 가격대로 돌려받게 됩니다

        # TODO 7.103 secs아까와 같이 3비티씨만큼 유동성을 공급하려고 하면 1개당 내려버린 가격인 177 테더를 넣어줘야합니다

        # TODO 0:03:57.853  ~  0:04:04.956

        # TODO 1.0secs pause

        # TODO 0:04:04.956  ~  0:04:05.956

        # TODO 4.615 secs그래서 풀에서 같은 비중을 차지하기 위해서 더 적은 자금이 필요하게 됏습니다

        # TODO 0:04:05.956  ~  0:04:10.571

        # TODO 1.0secs pause

        # TODO 0:04:10.571  ~  0:04:11.571
        self.play(Write(px_dn_k_up[ 1 ]))

        self.play(k_tracker.animate.set_value(7680000 / 169),
                  btc_tracker.animate.set_value(16),
                  usdt_tracker.animate.set_value(7680000 / 169 / 16),
                  run_time=5, rate_func=rate_functions.ease_in_out_quint)

        self.wait(3)
        self.play(Unwrite(px_dn_k_up[ 1 ]))
        self.wait(3.718)

        px_dn_k_up_dot = curr_dot.copy().clear_updaters().set_color(MAROON_E).set_z_index(1.5)
        self.add(px_dn_k_up_dot)

        # TODO 9.918 secs만약 아까 넣은 3비티씨와 900테더에 대한 엘피토큰을 가지고 유동성을 빼려고 하면 내려가있는 현재 가격대로 비티씨 한 개당 177테더를 돌려받게 됩니다
        # TODO 0:04:11.571  ~  0:04:21.489
        # TODO 1.0secs pause
        # TODO 0:04:21.489  ~  0:04:22.489

        self.play(Write(px_dn_k_dn[ 1 ]))

        self.play(k_tracker.animate.set_value(3000000 / 169),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000000 / 169 / 10),
                  run_time=5, rate_func=rate_functions.ease_in_out_quint)

        # 마찬가지로 하락한 상태에서 유동성을 제거하면
        # 비티씨 한 개를 뺄 때 떨어진 가격만큼의 테더만 되찾을 수 있습니다

        self.wait(3)
        self.play(Unwrite(px_dn_k_dn[ 1 ]),
                  Unwrite(px_dn_k_up[ 0 ]))
        self.wait(1)

        px_dn_k_dn_dot = curr_dot.copy().clear_updaters().set_color(MAROON_A).set_z_index(1.5)
        self.add(px_dn_k_dn_dot)

        # 가격 원점#####################################################################################
        px_origin = MathTex(r'ORIGIN').move_to(position)
        self.play(Write(px_origin), run_time=0.5)

        self.play(k_tracker.animate.set_value(30000),
                  btc_tracker.animate.set_value(10),
                  usdt_tracker.animate.set_value(3000),
                  run_time=0.5, rate_func=rate_functions.ease_in_out_quint)

        self.wait(0.5)
        self.play(Unwrite(px_origin), run_time=0.5)

        # TODO 3.322 secs각 케이스마다 눈에 잘 보이게 선으로 연결해봤습니다
        # TODO 0:04:22.489  ~  0:04:25.811
        # TODO 1.0secs pause
        # TODO 0:04:25.811  ~  0:04:26.811
        # TODO 4.12 secs동영상을 다시 보면서 천천히 곱씹어보시면 더 이해가 잘 될겁니다
        # TODO 0:04:26.811  ~  0:04:30.931
        # TODO 1.0secs pause
        # TODO 0:04:30.931  ~  0:04:31.931

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
        self.play(Create(k_px_org_line))
        k_px_up_line = making_a_line_3points(k_dn_px_up_dot, k_org_px_up_dot, k_up_px_up_dot, GREEN_E)
        self.play(Create(k_px_up_line))
        k_px_dn_line = making_a_line_3points(k_dn_px_dn_dot, k_org_px_dn_dot, k_up_px_dn_dot, RED_E)
        self.play(Create(k_px_dn_line))
        px_up_k_line = making_a_line_3points(px_up_k_dn_dot, k_org_px_up_dot, px_up_k_up_dot, TEAL_E)
        self.play(Create(px_up_k_line))
        px_dn_k_line = making_a_line_3points(px_dn_k_dn_dot, k_org_px_dn_dot, px_dn_k_up_dot, MAROON_E)
        self.play(Create(px_dn_k_line))

        self.wait(30)


class L02S13(Scene):
    def construct(self):
        # self.add(NumberPlane().set_z_index(1))

        speak(self, title='L02S05', txt=
        '아비트라지를 설명하고 마치겠습니다#1'
        '수익이라는 것은 기본적으로 시장의 비효율성이나 에러를 이용하는 것입니다#1'
        '그리고 시장이 많으면 많을수록 그런 기회가 많아지기에 덱스를 마다할 이유는 없습니다#1'
        '아비트라지란 한국어로 재정거래라고 불리고 두 개의 시장 사이이서 가격차가 발생하면 그 차익을 노리고 거래하는 것입니다#1'
        '싼데서 사서 비싼데 팔기에 보따리장사라고도 부릅니다#1'
        '지금 덱스 에이에서 비트코인이 500테더, 덱스 비에서 470테더인 상황을 가정합니다#1'
        '덱스비에서 사서 바로 덱스 에이에 팔면 이득을 얻을 수 있습니다#1'

        '그러나 고려할 것들이 있습니다#1'
        '덱스 비에서 비트코인을 구매하면 수수료를 내고 비티씨 가격변동에 노출이 됩니다#1'
        '혹시나 다른 중앙화 거래소로 옮긴다면 비싼 전송수수료도 들 것이고, 블록체인 처리시간과 중앙화 거래소의 자체 서버 처리시간에 거래수수료도 지불합니다#1'
        '다른 덱스로 옮긴다면 전송수수료와 블록체인 상 처리시간 비싼 거래수수료도 지불합니다#1'
        '다른 블록체인으로 브릿지를 해도 비싼 브릿지 수수료가 들것이고 시간도 더 걸립니다#1'
        '각거래마다 슬리피지도 발생할 수도 있습니다#1'
        '성공할지 안 할지 보장도 없구요 이 모든 것을 계산하고도 남는 장사라고 생각하면 아비트라지를 하는 것입니다#1'
        '보통은 미세한 차이를 보고 하기 때문에 규모가 커야지 수익이 좀 남는 편이고, 얼핏보면 하는 거 없이 돈 버는 것 같지만 생각보다 리스크가 있고 인간의 손으로 하기에는 24시간 못 하고 너무 느려서 보통 컴퓨터로 봇을 만들어 돌리게 됩니다#1'

        '아비트라지가 중요한 이유는 코인 가격을 맞춰주고 안정화 하기 때문입니다#1'
        '여러분이 사용하는 거래소의 가격이 싸면 좋겠지만 만약 이상하게 비싼 상태로 유지되고 있다면 당연히 코인을 사는데 불리한 상황이겠지만 곧 아비트라저들의 와서 모든 시장의 가격의 평형을 이루게 합니다#1'
        '수많은 거래소 사이에서 이 아비트라지 봇들이 코인을 사고 팔며 가격을 전부 똑같이 맞춰주고 그래서 우리는 어느 거래소든 다 비슷한 가격을 보게 됩니다.#1'
        '마찬가지로 덱스에서 내가 최초로 풀을 만들 때 말도안 되는 가격으로 만든다는 상상을 할 수도 있습니다#1'
        '내가 비트코인이 비싸지길 바라면서 10비트와 5000테더를 넣으면 그 순간 1비트의 가격은 500테더입니다#1'
        '곧 아비트라저들이 와서 시장가격으로 맞춰줍니다.덱스도 중앙화거래소에 영향을 주고 중앙화 거래소도 덱스에 영향을 줍니다#1'
        '모든 거래소가 아비트라지 봇으로 묶여있어 서로가 서로에게 영향을 줍니다#1'
        '아비트라지도 금융 생태계를 이루는 중요한 요소 중 하나이므로 잘 이해하고 있어야합니다#1'
              , keep_pitch=True, update=True, speed=1.4)

        # TODO 3.165 secs다음으로 넘어가기 전에 수수료예 대해 알아보겠습니다
        # TODO 0:00:00.000  ~  0:00:03.165
        # TODO 1.0secs pause
        # TODO 0:00:03.165  ~  0:00:04.165
        inefficiency_profit = MathTex(r'Inefficiency \  \Rightarrow\  Profit')

        ##### 아비트라지를 설명하고 마치겠습니다
        # 아비트라지 제목

        # TODO 2.151 secs아비트라지를 설명하고 마치겠습니다
        # TODO 0:00:00.000  ~  0:00:02.151
        # TODO 1.0secs pause
        # TODO 0:00:02.151  ~  0:00:03.151

        arb = Tex('Arbitrage').scale(2)
        self.play(Create(arb))
        self.wait(1)

        self.play(Uncreate(arb), run_time=1.151)

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
        dex_2_px_unit = Tex(r'USDT').next_to(dex_2_px, R, buff=0.1)
        dex_2_px.add(dex_2_px_unit).scale(0.65).move_to(dex_2_rect)
        # TODO 4.687 secs수익이라는 것은 기본적으로 시장의 비효율성이나 에러를 이용하는 것입니다
        # TODO 0:00:03.151  ~  0:00:07.838
        # TODO 1.0secs pause
        # TODO 0:00:07.838  ~  0:00:08.838

        profit = Tex('Profit').scale(2.5)
        inefficiency = Tex('Inefficiency').scale(2.5)
        inefficiency_1 = inefficiency.copy().scale(0.8).to_edge(UL, buff=1)
        inefficiency_2 = inefficiency.copy().scale(0.7).to_edge(DL, buff=1)
        inefficiency_3 = inefficiency.copy().scale(0.6).to_edge(UR, buff=1)
        inefficiency_4 = inefficiency.copy().scale(0.5).to_edge(DR, buff=1)
        profit_1 = profit.copy().scale(0.8).move_to(inefficiency_1)
        profit_2 = profit.copy().scale(0.7).move_to(inefficiency_2)
        profit_3 = profit.copy().scale(0.6).move_to(inefficiency_3)
        profit_4 = profit.copy().scale(0.5).move_to(inefficiency_4)

        self.play(Create(inefficiency))

        self.play(Transform(inefficiency, profit))
        self.wait(3.687)

        # TODO 5.001 secs그리고 시장이 많으면 많을수록 그런 기회가 많아지기에 덱스를 마다할 이유는 없습니다
        # TODO 0:00:08.838  ~  0:00:13.839
        # TODO 1.0secs pause
        # TODO 0:00:13.839  ~  0:00:14.839

        self.play(Create(inefficiency_1), run_time=0.5)
        self.play(Transform(inefficiency_1, profit_1), run_time=0.5)
        self.play(Create(inefficiency_2), run_time=0.5)
        self.play(Transform(inefficiency_2, profit_2), run_time=0.5)
        self.play(Create(inefficiency_3), run_time=0.5)
        self.play(Transform(inefficiency_3, profit_3), run_time=0.5)
        self.play(Create(inefficiency_4), run_time=0.5)
        self.play(Transform(inefficiency_4, profit_4), run_time=0.5)

        self.play(Uncreate(VGroup(inefficiency, inefficiency_1, inefficiency_2, inefficiency_3, inefficiency_4), run_time=2.001))

        # TODO 5.28 secs아비트라지란 한국어로 재정거래라고 불리고 두 개의 시장 사이이서 가격차가 발쌩하면
        # TODO 0:00:14.839  ~  0:00:20.119
        # TODO 1.0secs pause
        # TODO 0:00:20.119  ~  0:00:21.119
        # TODO 2.308 secs그 차익을 노리고 거래하는 것입니다
        # TODO 0:00:21.119  ~  0:00:23.427
        # TODO 1.0secs pause
        # TODO 0:00:23.427  ~  0:00:24.427
        # TODO 3.564 secs싼데서 사서 비싼데 팔기에 보따리장사라고도 부릅니다
        # TODO 0:00:24.427  ~  0:00:27.991
        # TODO 1.0secs pause
        # TODO 0:00:27.991  ~  0:00:28.991

        arbitrage_text = Tex('Arbitrage').scale(2)
        arbitrage_text_kor = Tex('재정거래').scale(2)
        boddari = Tex('보따리장사').scale(2)

        self.play(Create(arbitrage_text))
        self.wait(0.5)
        self.play(ReplacementTransform(arbitrage_text, arbitrage_text_kor))
        self.wait(5.5)
        self.play(ReplacementTransform(arbitrage_text_kor, boddari))
        self.wait(5.152)

        # TODO 6.222 secs지금 덱스 에이에서 비트코인이 500테더, 덱스 비에서 470테더인 상황을 가정합니다
        # TODO 0:00:28.991  ~  0:00:35.213
        # TODO 1.0secs pause
        # TODO 0:00:35.213  ~  0:00:36.213
        # TODO 3.939 secs덱스비에서 사서 바로 덱스 에이에 팔면 이득을 얻을 수 있습니다
        # TODO 0:00:36.213  ~  0:00:40.152
        # TODO 1.0secs pause
        # TODO 0:00:40.152  ~  0:00:41.152
        # TODO 1.861 secs그러나 고려할 것들이 있습니다
        # TODO 0:00:41.152  ~  0:00:43.013
        # TODO 1.0secs pause
        # TODO 0:00:43.013  ~  0:00:44.013

        self.play(Create(dex_1),
                  Create(dex_2), run_time=1)
        self.wait(1)
        self.play(Create(dex_1_px),
                  Create(dex_2_px), run_time=1)
        self.wait(4)
        self.play(Uncreate(boddari), run_time=1)
        self.wait(4.022)

        blist = BulletedList("Exposure to BTC fluctuation",
                             "Fees, time from DEX B",
                             r"In case of CEX, time, \\trade fees and high tx fees",
                             r"In case of DEX, time, \\high trade fees and tx fees",
                             r"In case of another blockchain,\\time and bridging fees",
                             "Slippage risk from every trade", height=7, width=7)

        # TODO 5.315 secs덱스 비에서 비트코인을 구매하면 수수료를 내고 비티씨 가격변동에 노출이 됩니다

        # TODO 0:00:44.013  ~  0:00:49.328

        # TODO 1.0secs pause

        # TODO 0:00:49.328  ~  0:00:50.328

        self.play(Create(blist[ 0 ]), run_time=1)
        self.wait(2)

        self.play(Create(blist[ 1 ]), run_time=1)
        self.wait(2.315)

        # TODO 9.809 secs혹시나 다른 중앙화 거래소로 옮긴다면 비싼 전송수수료도 들 것이고, 블록체인 처리시간과 중앙화 거래소의 자체 서버 처리시간에 거래수수료도 지불합니다

        # TODO 0:00:50.328  ~  0:01:00.137

        # TODO 1.0secs pause

        # TODO 0:01:00.137  ~  0:01:01.137

        self.play(Create(blist[ 2 ]), run_time=1)
        self.wait(9.809)

        # TODO 5.618 secs다른 덱스로 옮긴다면 전송수수료와 블록체인 상 처리시간 비싼 거래수수료도 지불합니다

        # TODO 0:01:01.137  ~  0:01:06.755

        # TODO 1.0secs pause

        # TODO 0:01:06.755  ~  0:01:07.755

        self.play(Create(blist[ 3 ]), run_time=1)
        self.wait(5.618)

        # TODO 5.424 secs다른 블록체인으로 브릿지를 해도 비싼 브릿지 수수료가 들것이고 시간도 더 걸립니다

        # TODO 0:01:07.755  ~  0:01:13.179

        # TODO 1.0secs pause

        # TODO 0:01:13.179  ~  0:01:14.179

        self.play(Create(blist[ 4 ]), run_time=1)
        self.wait(5.424)
        # TODO 2.888 secs각거래마다 슬리피지도 발생할 수도 있습니다

        # TODO 0:01:14.179  ~  0:01:17.067

        # TODO 1.0secs pause

        # TODO 0:01:17.067  ~  0:01:18.067

        self.play(Create(blist[ 5 ]), run_time=1)
        self.wait(2.888)

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
        # TODO 6.512 secs성공할지 안 할지 보장도 없구요 이 모든 것을 계산하고도 남는 장사라고 생각하면 아비트라지를 하는 것입니다

        # TODO 0:01:18.067  ~  0:01:24.579

        # TODO 1.0secs pause

        # TODO 0:01:24.579  ~  0:01:25.579

        still_not_sure = Tex('Still not sure...').scale(1.5)

        self.play(ReplacementTransform(blist, still_not_sure), run_time=1)
        self.wait(3)

        self.play(Uncreate(still_not_sure), run_time=1)
        self.wait(2.512)

        ##### 싼데서 사서 비싼데 팔기에 보따리장사라고도 부릅니다.
        ##### 얼핏보면 하는 거 없이 돈 버는 것 같지만
        ##### 보통은 미세한 차이를 보고 하기 때문에 규모가 커야지 수익이 좀 남는 편이고
        ##### 생각보다 리스크가 있고 인간의 손으로 하기에는 24시간 못 하고 너무 느려서
        ##### 보통 컴퓨터로 봇을 만ㄷ르어 돌리게 됩니다.
        # 불릿 더 라저 더 베터
        # 왓치 24 앤 패스트 핸드
        # 보통 컴퓨터 프로그램 오토메이티드
        # TODO 14.449 secs보통은 미세한 차이를 보고 하기 때문에 규모가 커야지 수익이 좀 남는 편이고, 얼핏보면 하는 거 없이 돈 버는 것 같지만 생각보다 리스크가 있고 인간의 손으로 하기에는 24시간 못 하고 너무 느려서 보통 컴퓨터로 봇을 만들어 돌리게 됩니다

        # TODO 0:01:25.579  ~  0:01:40.028

        # TODO 1.0secs pause

        # TODO 0:01:40.028  ~  0:01:41.028
        blist_2 = BulletedList("The Larger, The Better",
                               "Watch 24/7, Act Fast",
                               r"Normally automated\\with programming", height=7, width=7)

        self.wait(1)
        self.play(Create(blist_2[ 0 ]), run_time=1)
        self.wait(7)
        self.play(Create(blist_2[ 1 ]), run_time=1)
        self.wait(3)
        self.play(Create(blist_2[ 2 ]), run_time=1)
        self.wait(1.449)

        ##### 그리고 결정적으로 아비트라지는 가격 안정에 매우 중요한 역할을 합니다
        ##### 여러분이 사용하는 거래소의 가격이 싸면 좋겠지만 만약 이상하게 비싼 상태로 유지되고 있다면
        ##### 당연히 코인을 사는데 불리한 상황이겠지만 곧 아비트라저들의 와서 모든 시장의 가격의 평형을 이루게 합니다
        # 가격 전부 다르게 해놓고 똑같이 맞춰짐
        # 3번정도 반복
        # TODO 4.349 secs아비트라지가 중요한 이유는 코인 가격을 맞춰주고 안정화 하기 때문입니다

        # TODO 0:01:41.028  ~  0:01:45.377

        # TODO 1.0secs pause

        # TODO 0:01:45.377  ~  0:01:46.377

        # TODO 12.105 secs여러분이 사용하는 거래소의 가격이 싸면 좋겠지만 만약 이상하게 비싼 상태로 유지되고 있다면 당연히 코인을 사는데 불리한 상황이겠지만 곧 아비트라저들의 와서 모든 시장의 가격의 평형을 이루게 합니다

        # TODO 0:01:46.377  ~  0:01:58.482

        # TODO 1.0secs pause

        # TODO 0:01:58.482  ~  0:01:59.482

        # TODO 9.218 secs수많은 거래소 사이에서 이 아비트라지 봇들이 코인을 사고 팔며 가격을 전부 똑같이 맞춰주고 그래서 우리는 어느 거래소든 다 비슷한 가격을 보게 됩니다.

        # TODO 0:01:59.482  ~  0:02:08.700

        # TODO 1.0secs pause

        # TODO 0:02:08.700  ~  0:02:09.700

        dex_3_rect = RoundedRectangle(height=5, width=3, corner_radius=0.5)
        dex_3_text = Tex('DEX C').next_to(dex_3_rect, UP)
        dex_3 = VGroup(dex_3_rect, dex_3_text)

        dex_3_px = Variable(500, 'BTC', var_type=Integer)
        dex_3_px_tracker = dex_3_px.tracker
        dex_3_px_unit = Tex(r'USDT').next_to(dex_3_px, R)
        dex_3_px.add(dex_3_px_unit).scale(0.65).move_to(dex_3_rect)

        self.play(ReplacementTransform(blist_2, dex_3),
                  Create(dex_3_px), run_time=2)
        self.wait(2)

        ##### 수많은 거래소 사이에서 이 아비트라지 봇들이 코인을 사고 팔며 가격을 전부 똑같이 맞춰주고
        ##### 그래서 우리는 어느 거래소든 다 비슷한 가격을 보게 됩니다.
        self.play(dex_1_px_tracker.animate.set_value(510),
                  dex_2_px_tracker.animate.set_value(550),
                  dex_3_px_tracker.animate.set_value(540), run_time=2)
        self.wait(2)
        self.play(dex_1_px_tracker.animate.set_value(530),
                  dex_2_px_tracker.animate.set_value(530),
                  dex_3_px_tracker.animate.set_value(530), run_time=2)
        self.wait(2)

        self.play(dex_1_px_tracker.animate.set_value(420),
                  dex_2_px_tracker.animate.set_value(480),
                  dex_3_px_tracker.animate.set_value(450), run_time=2)
        self.wait(2)

        self.play(dex_1_px_tracker.animate.set_value(455),
                  dex_2_px_tracker.animate.set_value(455),
                  dex_3_px_tracker.animate.set_value(455), run_time=2)
        self.wait(2)

        self.play(dex_1_px_tracker.animate.set_value(755),
                  dex_2_px_tracker.animate.set_value(741),
                  dex_3_px_tracker.animate.set_value(787), run_time=2)
        self.wait(2)

        self.play(dex_1_px_tracker.animate.set_value(751),
                  dex_2_px_tracker.animate.set_value(751),
                  dex_3_px_tracker.animate.set_value(751), run_time=2)
        self.wait(2)

        ##### 마찬가지로 덱스에서 내가 최초로 풀을 만들 때 말도안 되는 가격으로 공급해도
        ##### 곧 아비트라저들이 와서 시장가격으로 맞춰줍니다.
        # 다 없애고 덱스에 최초로 코인 상장해서 비트를 올릴 때 올라가는데 내가 뉴코인 10개와 5000달러를 넣어 개당 500달러로 만들어놓으면
        # 전부 없어짐 아비트라지로 민주화 당함

        self.play(Uncreate(VGroup(dex_1, dex_1_px, dex_2, dex_2_px, dex_3, dex_3_px)),run_time=0.672)
        self.wait(t)
        # TODO 6.27 secs마찬가지로 덱스에서 내가 최초로 풀을 만들 때 말도안 되는 가격으로 만든다는 상상을 할 수도 있습니다

        # TODO 0:02:09.700  ~  0:02:15.970

        # TODO 1.0secs pause

        # TODO 0:02:15.970  ~  0:02:16.970
        # TODO 6.693 secs내가 비트코인이 비싸지길 바라면서 10비트와 5000테더를 넣으면 그 순간 1비트의 가격은 500테더입니다

        # TODO 0:02:16.970  ~  0:02:23.663

        # TODO 1.0secs pause

        # TODO 0:02:23.663  ~  0:02:24.663

        pool_rect = RoundedRectangle(width=7, height=4, corner_radius=0.5)
        pool_rect_text = Tex('BTC/USDT Pool').next_to(pool_rect, U)
        pool_btc_px = Variable(500, 'BTC', var_type=Integer)
        px_unit = Tex(r'USDT').next_to(pool_btc_px, R)
        pool_btc_px.add(px_unit).scale(1.5).next_to(pool_rect, D)

        self.play(Create(pool_rect_text),
                  Create(pool_rect), run_time=3)
        self.wait(1)


        usdt_lump_tracker = ValueTracker(5000)
        btc_lump_tracker = ValueTracker(10)

        btc_lump = create_circle_asset(Tex(rf'\textbf{{{int(btc_lump_tracker.get_value())}}} \\ \textbf{{BTC}}', color=WHITE, font_size=25),
                                       fill_color=C_BTC).scale_to_fit_height(2).shift(L * 1.5)
        usdt_lump = create_circle_asset(Tex(rf'\textbf{{{int(usdt_lump_tracker.get_value())}}} \\ \textbf{{USDT}}', color=WHITE, font_size=25),
                                        fill_color=C_USDT).scale_to_fit_height(2).shift(R * 1.5)

        liq_provider = create_entity(Tex(r' \emph{Init Liq\\Provider}', color=BLACK).scale(0.8), 1, WHITE, "10 BTC", C_BTC, 1.4,
                                     0.3,asset_text_color=WHITE).shift(R * 5)
        btc_asset_liq_prov = liq_provider[ 1 ]
        usdt_asset_liq_prov = create_entity("A", 0.5, WHITE, "5000 USDT", C_USDT, 1.4, 0.3, asset_text_color=WHITE)[ 1 ].next_to(liq_provider, DOWN, buff=0.1)
        liq_provider.add(usdt_asset_liq_prov)
        arbitrager = create_entity(Tex(r' \emph{Arbitrager}', color=BLACK).scale(0.7), 1, WHITE, "2.9 BTC", C_BTC, 1.4,
                                   0.3,asset_text_color=WHITE).shift(L * 5)
        btc_asset_arbitrager = arbitrager[ 1 ]
        usdt_asset_arbitrager = create_entity("A", 0.5, WHITE, "1127 USDT", C_USDT, 1.4, 0.3,asset_text_color=WHITE)[ 1 ].move_to(btc_asset_arbitrager)

        self.play(FadeIn(liq_provider, target_position=R * 10), run_time=2)
        self.wait(1.27)

        self.play(ReplacementTransform(liq_provider[ 1 ], btc_lump),
                  ReplacementTransform(liq_provider[ 2 ], usdt_lump), run_time=3)
        self.wait(2)

        self.play(Create(pool_btc_px), run_time=1)
        self.wait(0.693)
        # TODO 8.13 secs곧 아비트라저들이 와서 시장가격으로 맞춰줍니다.덱스도 중앙화거래소에 영향을 주고 중앙화 거래소도 덱스에 영향을 줍니다

        # TODO 0:02:24.663  ~  0:02:32.793

        # TODO 1.0secs pause

        # TODO 0:02:32.793  ~  0:02:33.793

        self.play(FadeIn(arbitrager, target_position=L * 10), run_time=1)
        self.wait(1)

        btc_lump.add_updater(lambda x: x.become(
            create_circle_asset(Tex(rf'\textbf{{{round(btc_lump_tracker.get_value(),1)}}} \\ \textbf{{BTC}}', color=WHITE, font_size=25),
                                fill_color=C_BTC).scale_to_fit_height(2).shift(L * 1.5)))
        usdt_lump.add_updater(lambda x: x.become(
            create_circle_asset(Tex(rf'\textbf{{{int(usdt_lump_tracker.get_value())}}} \\ \textbf{{USDT}}', color=WHITE, font_size=25),
                                fill_color=C_USDT).scale_to_fit_height(2).shift(R * 1.5)))
        self.play(pool_btc_px.tracker.animate.set_value(300),
                  usdt_lump_tracker.animate.set_value(3873),
                  btc_lump_tracker.animate.set_value(12.9),
                  FadeOut(btc_asset_arbitrager, target_position=btc_lump),
                  FadeIn(usdt_asset_arbitrager, target_position=usdt_lump), run_time=5)
        self.wait(1.13)

        btc_lump.clear_updaters()
        usdt_lump.clear_updaters()
        self.play(FadeOut(VGroup(
            pool_btc_px, pool_rect, pool_rect_text, btc_lump, usdt_lump, arbitrager, usdt_asset_arbitrager, liq_provider[ 0 ])), run_time=1)

        # TODO 4.615 secs모든 거래소가 아비트라지 봇으로 묶여있어 서로가 서로에게 영향을 줍니다

        # TODO 0:02:33.793  ~  0:02:38.408

        # TODO 1.0secs pause

        # TODO 0:02:38.408  ~  0:02:39.408

        # TODO 5.134 secs아비트라지도 금융 생태계를 이루는 중요한 요소 중 하나이므로 잘 이해하고 있어야합니다

        # TODO 0:02:39.408  ~  0:02:44.542

        # TODO 1.0secs pause

        # TODO 0:02:44.542  ~  0:02:45.542

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

        self.play(Create(ex_group), run_time=0.5)

        self.play(Create(arbigrager_circle), run_time=0.5)

        self.play(Create(line_group), run_time=0.5)

        self.play(rotation_val_tracker.animate.set_value(3), run_time=2, rate_functions=exponential_decay)
        self.wait(0.5)

        cex_line_5.set_color(RED_E)
        self.wait(0.25)
        cex_line_2.set_color(RED_E)
        self.wait(0.25)
        cex_line_5.set_color(WHITE)
        cex_line_2.set_color(WHITE)
        self.wait(0.25)

        dex_line_5.set_color(RED_E)
        self.wait(0.25)
        cex_line_3.set_color(RED_E)
        self.wait(0.25)
        dex_line_5.set_color(WHITE)
        cex_line_3.set_color(WHITE)
        self.wait(0.25)

        dex_line_1.set_color(RED_E)
        self.wait(0.25)
        cex_line_1.set_color(RED_E)
        self.wait(0.25)
        dex_line_1.set_color(WHITE)
        cex_line_1.set_color(WHITE)
        self.wait(0.25)

        dex_line_2.set_color(RED_E)
        self.wait(0.25)
        cex_line_7.set_color(RED_E)
        self.wait(0.25)
        dex_line_2.set_color(WHITE)
        cex_line_7.set_color(WHITE)
        self.wait(0.25)

        dex_line_3.set_color(RED_E)
        self.wait(0.25)
        dex_line_4.set_color(RED_E)
        self.wait(0.25)
        dex_line_3.set_color(WHITE)
        dex_line_4.set_color(WHITE)
        self.wait(0.25)
        self.wait(30)


