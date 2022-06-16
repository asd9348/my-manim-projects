데모 영상

영상과 이미지 데스모스같은 인터랙티브 수업의 차이



2디 그래프
미적분
삼각함수
음함수

카메라 움직이기


선형대수학
벡터 기본
트랜스폼
행렬

벡터필드
유체역학




테일러 급수
편미분
푸리에 변환
마님 물리엔진
스파이노그래프


'간단하게 오토매틱 마켓 메이커를 통해 덱스가 돌아가는 원리를 배웟는데#1'
'이젠 약간의 수학과 함께 더욱 자세히 알아보겠습니다#1'

'엑스와이는 케이에서 엑스를 이항시키면#1'
'와이는 엑스부느이 케이 형태입니다#1'
'여러분 모두 중학교 때 함수를 배웠을 것이고#1'
'기본적인  와이는 2엑스도 배웠고 와이는 엑스분의 1을 빼운기억이 날겁니다#1'
'그중에 엑스분의 1함수는 반비례함수라고 배웠고 쌍곡선의 형태를 띄는 함수입니다#1'
'그리고 이 반비레함수는 케이값에 따라서#1'
'보이는 것과 같이 원점에서 점점 멀어지는 함수입니다#1'
'일반적인 오토매틱 마켓메이커는 이 함수를 사용해 가격을 결정합니다#1'
'도대체 어떻게 가격을 결정하는지 알아보겠습니다#1'

'여기서 엑스는 a코인의 양 와이는 비코인의 양입니다#1'
'페어라는 것이 원래 양방향이어서 서로 바꿔도 무방하나#1'
'앞으로 이해하기 쉽게 풀내부의 베이스에셋의 양이 풀내부의 엑스 쿼트에셋의 양이 와이라고#1'
'우리가 살펴볼 비티씨테더 페어에서는#1'
'엑스는 풀내부 비티씨의 양#1'
'왕이는 풀내부 테더의 양입니다#1'

'복잡하게 생각할 건 없고 와이는 엑스분의케이 그래프에서 케이는 그냥 어떤 값입니다. #1'
'그런데 아까 우리는 케이가 엑스 곱하기 와이인 걸 봤습니다.#1'

'그렇다면 현재 비티씨테더 풀의 함수식은 10곱하기 3000인 30000입니다다#1'

'아까 말한 것처럼 가격은 풀에 각 코인이 얼마나 있는지로 결정되기 때문에#1'
'우리는 풀의 상태, 정확히 얘기하면 풀 내부의 베이스 에셋과 쿼트 에셋의 비율로 가격을 계산할 수 있습니다#1'
'엑스와이는 케이가 풀을 나타내는 방정식이고#1'
'풀의 상태는 아까 본 와이는 엑스분의 케이라는 함수의 그래프 위의#1'
'한 점으로 나타낼 수 있습니다. 여기에는 가격정보도 들어있는 것입니다.#1'

'거래자가 풀을 대상으로 비티씨를 매수하거나 매도한다는 것은#1'
'풀의 상태를 변화 시키는 것이기에 현재 있는 지점에서 그래프 상의 다른 지점으로 이동한다는 것입니다#1'

'유동성 제공자가 유동성을 공급하거나 제거한다는 것은 케이값을 움직이는 것입니다.#1'
'유동성을 공급하는 것은 비티씨와 테더를 같이 넣어주는 것이고#1'
'그건 엑스와 와이가 둘다 늘어나기 때문에 케이값이 커지는 것입니다#1'
'유동성을 제거하면 비티씨와 테더가 같이 빠져나가는 것이고#1'
'엑스와 와이가 둘다 줄면 당연히 케이값도 줄어듭니다#1'

지환 박, [6/16/2022 9:41 PM]
╭─────────────────────────────── Traceback (most recent call last) ────────────────────────────────╮
│ C:\Users\JB\AppData\Local\Programs\Python\Python310\lib\site-packages\manim\cli\render\commands. │
│ py:118 in render                                                                                 │
│                                                                                                  │
│   115 │   │   for SceneClass in scene_classes_from_file(file):                                   │
│   116 │   │   │   try:                                                                           │
│   117 │   │   │   │   scene = SceneClass()                                                       │
│ ❱ 118 │   │   │   │   scene.render()                                                             │
│   119 │   │   │   except Exception:                                                              │
│   120 │   │   │   │   error_console.print_exception()                                            │
│   121 │   │   │   │   sys.exit(1)                                                                │
│                                                                                                  │
│ C:\Users\JB\AppData\Local\Programs\Python\Python310\lib\site-packages\manim\scene\scene.py:222   │
│ in render                                                                                        │
│                                                                                                  │
│    219 │   │   """                                                                               │
│    220 │   │   self.setup()                                                                      │
│    221 │   │   try:                                                                              │
│ ❱  222 │   │   │   self.construct()                                                              │
│    223 │   │   except EndSceneEarlyException:                                                    │
│    224 │   │   │   pass                                                                          │
│    225 │   │   except RerunSceneException as e:                                                  │
│                                                                                                  │
│ C:\Users\JB\PycharmProjects\pythonProject1\main.py:51 in construct                               │
│                                                                                                  │
│    48 │   │   # TODO 1.0 secs pause                                                              │
│    49 │   │                                                                                      │
│    50 │   │   s_1_text_font_size = 150                                                           │
│ ❱  51 │   │   text_1 = Tex('침체', font_size=s_1_text_font_size).shift(L * 4)                    │
│    52 │   │   text_2 = Tex('불황', font_size=s_1_text_font_size).shift(R * 4)                    │
│    53 │   │   q_mark = Tex('?', font_size=s_1_text_font_size + 50).scale(2)                      │
│    54                                                                                            │
│                                                                                                  │
│ C:\Users\JB\AppData\Local\Programs\Python\Python310\lib\site-packages\manim\mobject\text\tex_mob │
│ ject.py:434 in init                                                                          │
│                                                                                                  │
│   431 │   def init(                                                                          │
│   432 │   │   self, *tex_strings, arg_separator="", tex_environment="center", **kwargs           │
│   433 │   ):                                                                                     │
│ ❱ 434 │   │   super().init(                                                                  │

지환 박, [6/16/2022 9:41 PM]
│   435 │   │   │   *tex_strings,                                                                  │
│   436 │   │   │   arg_separator=arg_separator,                                                   │
│   437 │   │   │   tex_environment=tex_environment,                                               │
│                                                                                                  │
│ C:\Users\JB\AppData\Local\Programs\Python\Python310\lib\site-packages\manim\mobject\text\tex_mob │
│ ject.py:303 in init                                                                          │
│                                                                                                  │
│   300 │   │   │   │   │   │   """,                                                               │
│   301 │   │   │   │   │   ),                                                                     │
│   302 │   │   │   │   )                                                                          │
│ ❱ 303 │   │   │   raise compilation_error                                                        │
│   304 │   │   self.set_color_by_tex_to_color_map(self.tex_to_color_map)                          │
│   305 │   │                                                                                      │
│   306 │   │   if self.organize_left_to_right:                                                    │
│                                                                                                  │
│ C:\Users\JB\AppData\Local\Programs\Python\Python310\lib\site-packages\manim\mobject\text\tex_mob │
│ ject.py:282 in init                                                                          │
│                                                                                                  │
│   279 │   │   self.brace_notation_split_occurred = False                                         │
│   280 │   │   self.tex_strings = self._break_up_tex_strings(tex_strings)                         │
│   281 │   │   try:                                                                               │
│ ❱ 282 │   │   │   super().init(                                                              │
│   283 │   │   │   │   self.arg_separator.join(self.tex_strings),                                 │
│   284 │   │   │   │   tex_environment=self.tex_environment,                                      │
│   285 │   │   │   │   tex_template=self.tex_template,                                            │
│                                                                                                  │
│ C:\Users\JB\AppData\Local\Programs\Python\Python310\lib\site-packages\manim\mobject\text\tex_mob │
│ ject.py:93 in init                                                                           │
│                                                                                                  │
│    90 │   │                                                                                      │
│    91 │   │   assert isinstance(tex_string, str)                                                 │
│    92 │   │   self.tex_string = tex_string                                                       │
│ ❱  93 │   │   file_name = tex_to_svg_file(                                                       │
│    94 │   │   │   self._get_modified_expression(tex_string),                                     │
│    95 │   │   │   environment=self.tex_environment,                                              │
│    96 │   │   │   tex_template=self.tex_template,                                                │
│                                                                                                  │
│ C:\Users\JB\AppData\Local\Programs\Python\Python310\lib\site-packages\manim\utils\tex_file_writi │
│ ng.py:48 in tex_to_svg_file                                                                      │
│                                                                                                  │

지환 박, [6/16/2022 9:41 PM]
│    45 │   if tex_template is None:                                                               │
│    46 │   │   tex_template = config["tex_template"]                                              │
│    47 │   tex_file = generate_tex_file(expression, environment, tex_template)                    │
│ ❱  48 │   dvi_file = compile_tex(                                                                │
│    49 │   │   tex_file,                                                                          │
│    50 │   │   tex_template.tex_compiler,                                                         │
│    51 │   │   tex_template.output_format,                                                        │
│                                                                                                  │
│ C:\Users\JB\AppData\Local\Programs\Python\Python310\lib\site-packages\manim\utils\tex_file_writi │
│ ng.py:191 in compile_tex                                                                         │
│                                                                                                  │
│   188 │   │   exit_code = os.system(command)                                                     │
│   189 │   │   if exit_code != 0:                                                                 │
│   190 │   │   │   log_file = tex_file.replace(".tex", ".log")                                    │
│ ❱ 191 │   │   │   print_all_tex_errors(log_file, tex_compiler, tex_file)                         │
│   192 │   │   │   raise ValueError(                                                              │
│   193 │   │   │   │   f"{tex_compiler} error converting to"                                      │
│   194 │   │   │   │   f" {output_format[1:]}. See log output above or"                           │
│                                                                                                  │
│ C:\Users\JB\AppData\Local\Programs\Python\Python310\lib\site-packages\manim\utils\tex_file_writi │
│ ng.py:253 in print_all_tex_errors                                                                │
│                                                                                                  │
│   250 │   │   │   "Check your LaTeX installation.",                                              │
│   251 │   │   )                                                                                  │
│   252 │   with open(log_file) as f:                                                              │
│ ❱ 253 │   │   tex_compilation_log = f.readlines()                                                │
│   254 │   │   error_indices = [                                                                  │
│   255 │   │   │   index                                                                          │
│   256 │   │   │   for index, line in enumerate(tex_compilation_log)                              │
╰──────────────────────────────────────────────────────────────────────────────────────────────────╯
UnicodeDecodeError: 'cp949' codec can't decode byte 0xa8 in position 8149: illegal multibyte sequence
