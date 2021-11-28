import time
import random
import IPython
import re
from google.colab import output


n = 0 
def chat(text, **kw):  #チャット用の関数（ここを書き換える）
  global n
  n += 1
  return 'ほ' * n

# アイコンの指定
BOT_ICON = 'https://3.bp.blogspot.com/-qbORCFE5qhk/UmTBJwEYKjI/AAAAAAAAZYY/nbjieynFcLQ/s800/job_uranaishi.png'
YOUR_ICON = 'https://2.bp.blogspot.com/-WplygmIuX28/VZ-PPsDMOmI/AAAAAAAAvDU/OKG7taU7wXo/s800/girl_think.png'

def run_chat(chat = chat, start='気になる人との相性を占います', **kw):

  def display_bot(bot_text):
    with output.redirect_to_element('#output'):
      bot_name = kw.get('bot_name', '占い師')
      bot_icon = kw.get('bot_icon', BOT_ICON)
      display(IPython.display.HTML(f'''
      <div class="sb-box">
        <div class="icon-img icon-img-left">
            <img src="{bot_icon}" width="60px">
        </div><!-- /.icon-img icon-img-left -->
        <div class="icon-name icon-name-left">{bot_name}</div>
        <div class="sb-side sb-side-left">
            <div class="sb-txt sb-txt-left">
              {bot_text}
            </div><!-- /.sb-txt sb-txt-left -->
        </div><!-- /.sb-side sb-side-left -->
    </div><!-- /.sb-box -->
      '''))

  def display_you(your_text):
    with output.redirect_to_element('#output'):
      your_name = kw.get('your_name', 'あなた')
      your_icon = kw.get('your_icon', YOUR_ICON)

      display(IPython.display.HTML(f'''
      <div class="sb-box">
        <div class="icon-img icon-img-right">
            <img src="{your_icon}" width="60px">
        </div><!-- /.icon-img icon-img-right -->
        <div class="icon-name icon-name-right">{your_name}</div>
        <div class="sb-side sb-side-right">
            <div class="sb-txt sb-txt-right">
              {your_text}
            </div><!-- /.sb-txt sb-txt-right -->
        </div><!-- /.sb-side sb-side-right -->
      </div><!-- /.sb-box -->
      '''))

  display(IPython.display.HTML('''
      <style>
        /* 全体 */
        .sb-box {
            position: relative;
            overflow: hidden;
        }

        /* アイコン画像 */
        .icon-img {
            position: absolute;
            overflow: hidden;
            top: 0;
            width: 80px;
            height: 80px;
        }

        /* アイコン画像（左） */
        .icon-img-left {
            left: 0;
        }

        /* アイコン画像（右） */
        .icon-img-right {
            right: 0;
        }

        /* アイコン画像 */
        .icon-img img {
            border-radius: 50%;
            border: 2px solid #eee;
        }

        /* アイコンネーム */
        .icon-name {
            position: absolute;
            width: 80px;
            text-align: center;
            top: 83px;
            color: #fff;
            font-size: 10px;
        }

        /* アイコンネーム（左） */
        .icon-name-left {
            left: 0;
        }

        /* アイコンネーム（右） */
        .icon-name-right {
            right: 0;
        }

        /* 吹き出し */
        .sb-side {
            position: relative;
            float: left;
            margin: 0 105px 40px 105px;
        }

        .sb-side-right {
            float: right;
        }

        /* 吹き出し内のテキスト */
        .sb-txt {
            position: relative;
            border: 2px solid #eee;
            border-radius: 6px;
            background: #eee;
            color: #333;
            font-size: 15px;
            line-height: 1.7;
            padding: 18px;
        }

        .sb-txt>p:last-of-type {
            padding-bottom: 0;
            margin-bottom: 0;
        }

        /* 吹き出しの三角 */
        .sb-txt:before {
            content: "";
            position: absolute;
            border-style: solid;
            top: 16px;
            z-index: 3;
        }

        .sb-txt:after {
            content: "";
            position: absolute;
            border-style: solid;
            top: 15px;
            z-index: 2;
        }

        /* 吹き出しの三角（左） */
        .sb-txt-left:before {
            left: -7px;
            border-width: 7px 10px 7px 0;
            border-color: transparent #eee transparent transparent;
        }

        .sb-txt-left:after {
            left: -10px;
            border-width: 8px 10px 8px 0;
            border-color: transparent #eee transparent transparent;
        }

        /* 吹き出しの三角（右） */
        .sb-txt-right:before {
            right: -7px;
            border-width: 7px 0 7px 10px;
            border-color: transparent transparent transparent #eee;
        }

        .sb-txt-right:after {
            right: -10px;
            border-width: 8px 0 8px 10px;
            border-color: transparent transparent transparent #eee;
        }

        /* 767px（iPad）以下 */

        @media (max-width: 767px) {

            .icon-img {
                width: 60px;
                height: 60px;
            }

            /* アイコンネーム */
            .icon-name {
                width: 60px;
                top: 62px;
                font-size: 9px;
            }

            /* 吹き出し（左） */
            .sb-side-left {
                margin: 0 0 30px 78px;
                /* 吹き出し（左）の上下左右の余白を狭く */
            }

            /* 吹き出し（右） */
            .sb-side-right {
                margin: 0 78px 30px 0;
                /* 吹き出し（右）の上下左右の余白を狭く */
            }

            /* 吹き出し内のテキスト */
            .sb-txt {
                padding: 12px;
                /* 吹き出し内の上下左右の余白を-6px */
            }
        }
    </style>
      <script>
        var inputPane = document.getElementById('input');
        inputPane.addEventListener('keydown', (e) => {
          if(e.keyCode == 13) {
            google.colab.kernel.invokeFunction('notebook.Convert', [inputPane.value], {});
            inputPane.value=''
          }
        });
      </script>
    <div id='output' style='background: #66d;'></div>
    <div style='text-align: right'><textarea id='input' style='width: 100%; background: #eee;'></textarea></div>
      '''))

  def convert(your_text):
    display_you(your_text)
    bot_text = chat(your_text, **kw)
    time.sleep(random.randint(0,4))
    display_bot(bot_text)

  output.register_callback('notebook.Convert', convert)
  if start is not None:
    display_bot(start)

def soulnumber(s):
    while len(s) > 3:
      s = str(sum(int(x) for x in s))
    if le(s) == 2 and s[0] == s[1]:
      return s
    else:
      s = str(sum(int(x) for x in s))
      return s


def pattern(m):
  pattern1 = r'\d\d\d\d\d\d\d\d'
  pattern1 = re.compile(pattern1)
  pattern2 = r'(\d\d\d\d)年(\d\d?)月(\d\d?)日'
  pattern2 = re.compile(pattern2)
  pattern3 = r'(\d\d\d\d)\\(\d\d?)\\(\d\d?)'
  pattern3 = re.compile(pattern3)
  pattern4 = r'(\d\d\d\d)-(\d\d?)-(\d\d?)'
  pattern4 = re.compile(pattern4)
  s1 = pattern1.findall(m)
  if len(s1) == 0:
    s1 = pattern2.findall(m)
  if len(s1) == 0:
    s1 = pattern3.findall(m)
  if len(s1) == 0:
    s1 = pattern4.findall(m)
  s2 = s1[0]
  s3 = list(s2)
  n = ''.join(s3)
  return n

def patternYN(s):
  patternA = r'\D+(はい)'
  patternA = re.compile(patternA)
  patternB = r'\D+(いいえ)'
  patternB = re.compile(patternB)
  s1 = patternA.findall(s)
  if len(s1) == 0:
    s1 = patternB.findall(s)
  s2 = s1[0]
  s3 = list(s2)
  n = ''.join(s3)
  return n    

frame = {}

def uranaisan(input_text):
  global frame #外部の状態を参照する
  if 'asking' in frame: #askingから更新する
    frame[frame['asking']] = input_text

  if 'name' not in frame:
    frame['asking'] = 'name' #名前を尋ねる
    return 'あなたの名前は？'

  if 'name' in frame and 'Xbirthday' not in frame:
    frame['asking'] = 'Xbirthday'
    a = frame['name']
    return f'{a}さんの生年月日は？'
  
  if 'name' in frame and 'Xbirthday' in frame and 'Yname' not in frame and 'onemore' not in frame:
    frame['asking'] = 'Yname'
    return '気になる人の名前は？'

  if 'name' in frame and 'Xbirthday' in frame and 'Yname' in frame and 'Ybirthday' not in frame and 'onemore' not in frame:
    frame['asking'] = 'Ybirthday'
    b = frame['Yname']
    return f'{b}さんの生年月日は？'

  if 'name' in frame and 'Xbirthday' in frame and 'Yname' not in frame and 'Ybirthday' not in frame and 'onemore' in frame:
      del frame['onemore']
      frame['asking'] = 'Yname'
      return 'あなたとの相性を占いたい人の名前は？'


  if 'name' in frame and 'Xbirthday' in frame and 'Yname' in frame and 'Ybirthday' in frame and 'onemore' not in frame:
    #占います
    x = int(soulnumber(pattern(frame['Xbirthday'])))
    y = int(soulnumber(pattern(frame['Ybirthday'])))
    if abs(x - y) >= 5:
      frame['asking'] = 'onemore'
      return 'ごめんなさい、相性は良くないようです・・・。他の人との相性を占ってみませんか？(はい or いいえ)'
    elif abs(x - y) == 0:
      return '相性抜群です！その人とうまくやっていけそうです！！　占い終了です。ありがとうございました！'
    else:
      return '相性は良いです！その人とうまくやっていけそうですね！　占い終了です。ありがとうございました！' 
  
  if 'name' in frame and 'Xbirthday' in frame and 'Yname' in frame and 'Ybirthday' in frame and 'onemore' in frame:
    c = patternYN(frame['onemore'])
    if c == 'はい':
      del frame['Ybirthday']
      del frame['Yname']
      return '他の人との相性を占います'
    else:
      return '占い終了です。ありがとうございました！'

  return output_text

def start():
  run_chat(chat=uranaisan) 
