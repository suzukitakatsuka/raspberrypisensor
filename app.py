import json
import random
import time
from datetime import datetime, timedelta
import re
import csv
import os
import sqlite3
import matplotlib.pyplot as plt
import japanize_matplotlib
from waitress import serve
import logging
logging.basicConfig(level=logging.DEBUG)
import numpy as np

from flask import Flask, Response, render_template, stream_with_context, jsonify, request

application = Flask(__name__, static_folder='./images/')
random.seed()  # Initialize the random number generator
raspi_data = '0 0 0'
raspi_data1 = '0 0 0'
sensordata = 0
def timer():
    t = time.time()  # UNIX時間（1970/01/01 00:00:00からの経過時刻）を取得
    local_time = time.localtime(t)  # ローカル時刻をtime.struct_time型として取得
    asc_time = time.asctime(local_time)  # 上のlocal_timeを文字列表現に変換
    dt = datetime.now().strptime(asc_time, '%a %b %d %H:%M:%S %Y')
    return dt

nowtime = timer()
conn1 = sqlite3.connect('sensor4.db')
cur1 = conn1.cursor()
cur1.execute('select * from sensor where date = "2024-07-11 00:00:00" OR date = "2024-07-11 01:00:00" ')
sensordata2 = cur1.fetchall()
a1 = sensordata2[0][2]
a2 = sensordata2[0][3]
a3 = sensordata2[0][4]
a4 = sensordata2[1][2]
a5 = sensordata2[1][3]
a6 = sensordata2[1][4]
print("sensor", sensordata2)
print("chenchay1",a1)
print("chenchay2",a2)
print("chenchay3",a3)
cur1.execute('select * from sensor where date = "2024-07-11 20:00:00" OR date = "2024-07-11 03:00:00" ')
sensordata3 = cur1.fetchall()
b1 = sensordata3[0][2]
b2 = sensordata3[0][3]
b3 = sensordata3[0][4]
b4 = sensordata3[1][2]
b5 = sensordata3[1][3]
b6 = sensordata3[1][4]
print("sensor", sensordata3)
print("chenchay1",b1)
print("chenchay2",b2)
print("chenchay3",b3)
cur1.execute('select * from sensor where date = "2024-07-11 04:00:00" OR date = "2024-07-11 05:00:00" ')
sensordata4 = cur1.fetchall()
c1 = sensordata4[0][2]
c2 = sensordata4[0][3]
c3 = sensordata4[0][4]
c4 = sensordata4[1][2]
c5 = sensordata4[1][3]
c6 = sensordata4[1][4]
print("sensor", sensordata4)
cur1.execute('select * from sensor where date = "2024-07-11 06:00:00" OR date = "2024-07-11 07:00:00" ')
sensordata5 = cur1.fetchall()
d1 = sensordata5[0][2]
d2 = sensordata5[0][3]
d3 = sensordata5[0][4]
d4 = sensordata5[1][2]
d5 = sensordata5[1][3]
d6 = sensordata5[1][4]
print("sensor", sensordata5)
cur1.execute('select * from sensor where date = "2024-07-11 08:00:00" OR date = "2024-07-11 09:00:00" ')
sensordata6 = cur1.fetchall()
e1 = sensordata6[0][2]
e2 = sensordata6[0][3]
e3 = sensordata6[0][4]
e4 = sensordata6[1][2]
e5 = sensordata6[1][3]
e6 = sensordata6[1][4]
print("sensor", sensordata6)
cur1.execute('select * from sensor where date = "2024-07-11 10:00:00" OR date = "2024-07-11 11:00:00" ')
sensordata7 = cur1.fetchall()
f1 = sensordata7[0][2]
f2 = sensordata7[0][3]
f3 = sensordata7[0][4]
f4 = sensordata7[1][2]
f5 = sensordata7[1][3]
f6 = sensordata7[1][4]
print("sensor", sensordata7)
cur1.execute('select * from sensor where date = "2024-07-11 12:00:00" OR date = "2024-07-11 13:00:00" ')
sensordata8 = cur1.fetchall()
g1 = sensordata8[0][2]
g2 = sensordata8[0][3]
g3 = sensordata8[0][4]
g4 = sensordata8[1][2]
g5 = sensordata8[1][3]
g6 = sensordata8[1][4]
print("sensor", sensordata8)
cur1.execute('select * from sensor where date = "2024-07-11 14:00:00" OR date = "2024-07-11 15:00:00" ')
sensordata9 = cur1.fetchall()
h1 = sensordata9[0][2]
h2 = sensordata9[0][3]
h3 = sensordata9[0][4]
h4 = sensordata9[1][2]
h5 = sensordata9[1][3]
h6 = sensordata9[1][4]
print("sensor", sensordata9)
cur1.execute('select * from sensor where date = "2024-07-11 16:00:00" OR date = "2024-07-11 17:00:00" ')
sensordata10 = cur1.fetchall()
i1 = sensordata10[0][2]
i2 = sensordata10[0][3]
i3 = sensordata10[0][4]
i4 = sensordata10[1][2]
i5 = sensordata10[1][3]
i6 = sensordata10[1][4]
print("sensor", sensordata10)
cur1.execute('select * from sensor where date = "2024-07-11 18:00:00" OR date = "2024-07-11 19:00:00" ')
sensordata11 = cur1.fetchall()
j1 = sensordata11[0][2]
j2 = sensordata11[0][3]
j3 = sensordata11[0][4]
j4 = sensordata11[1][2]
j5 = sensordata11[1][3]
j6 = sensordata11[1][4]
print("sensor", sensordata11)
cur1.execute('select * from sensor where date = "2024-07-11 20:00:00" OR date = "2024-07-11 21:00:00" ')
sensordata12 = cur1.fetchall()
k1 = sensordata12[0][2]
k2 = sensordata12[0][3]
k3 = sensordata12[0][4]
k4 = sensordata12[1][2]
k5 = sensordata12[1][3]
k6 = sensordata12[1][4]
print("sensor", sensordata12)
cur1.execute('select * from sensor where date = "2024-07-11 22:00:00" OR date = "2024-07-11 23:00:00" ')
sensordata13 = cur1.fetchall()
l1 = sensordata13[0][2]
l2 = sensordata13[0][3]
l3 = sensordata13[0][4]
l4 = sensordata13[1][2]
l5 = sensordata13[1][3]
l6 = sensordata13[1][4]
print("sensor", sensordata13)
aaa = sensordata2
conn1.commit()
conn1.close()

def generate_data():
    data_decode = "25.0 50.0 1013.25"
    return data_decode

@application.route('/post', methods=['POST', 'GET'])
def post_handler():
    # raspiがここにrequestを送る。。。。
    data = request.data.decode('utf-8')
    time.sleep(1)
    nowtime = timer()
    split = re.split('\s+', data)
    # print("split", split)  
    temperature = float(split[0])
    humidity = float(split[1])
    pressure = float(split[2])
    sensor = [
        {
            "temperature": temperature,
            "huminity": humidity,
            "pressure": pressure
        }
    ]
    global raspi_data
    raspi_data = data
    return "data receive"

@application.route('/post1', methods=['POST', 'GET'])
def post_handler1():
    # raspiがここにrequestを送る。。。。
    data1 = request.data.decode('utf-8')
    global raspi_data1
    raspi_data1 = data1
    return "data receive"

@application.route('/')
def index():
    split = re.split('\s+', raspi_data)
    split1 = re.split('\s+', raspi_data1)
    # print("split", split)
    # print("split1", split1) 
    temperature = float(split[0])
    humidity = float(split[1])
    pressure = float(split[2])
    temperature1 = float(split1[0])
    humidity1 = float(split1[1])
    pressure1 = float(split1[2])
    sensor = [
        {
            "temperature": temperature,      
            "huminity": humidity,  
            "pressure": pressure
        }
    ]
    sensor1 = [
        {
            "temperature": temperature1,
            "huminity": humidity1,
            "pressure": pressure1
        }
    ]
    plt.rcParams["font.size"] = 10
    fig, ax = plt.subplots(facecolor='white')
    xs = ['00:00', '01:00', '02:00' , '03:00','04:00','05:00','06:00','07:00','08:00','09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
    ax.plot(xs, [a1, a4, b1, b4, c1, c4, d1, d4, e1, e4, f1, f4, g1, g4, h1, h4, i1, i4, j1, j4, k1, k4, l1, l4], label='開発ルーム', marker='o')
    ax.plot(xs, [a1, 28, 26,27,24,26,28,26,27,24,25,26,25,24,24,25,26,25,26,24,24,23,25,24], label='小会議室', marker = 'o')
    ax.set_title('温度',fontsize=25)
    ax.set_xticklabels(xs, rotation=60)
    # ax.set_ylabel(rotation='horizontal')
    ax.set_yticks([10, 15, 20, 25, 30, 35, 40])
    ax.grid()
    ax.legend()
    dirname = "images/"
    filename = dirname + "img.png"
    fig.savefig(filename)
    fig1, ax1 = plt.subplots(facecolor='white')
    ax1.plot(xs, [a2,a5,b2,b5,c2,c5,d2,d5,e2,e5,f2,f5,g2,g5,h2,h5,i2,i5,j2,j5,k2,k5,l2,l5], label='開発ルーム', marker='o')
    ax1.plot(xs, [a2,a5,b2,73,72,72,73,73,72,75,72,71,73,71,76,74,75,74,73,72,79,73,71,73], label='小会議室', marker = 'o')
    ax1.set_title('湿度',fontsize=25)
    ax1.set_xticklabels(xs, rotation=60)
    # ax.set_ylabel(rotation='horizontal')
    ax1.set_yticks([60, 65, 70, 75, 80, 85, 90])
    ax1.grid()
    ax1.legend()
    dirname1 = "images/"
    filename1 = dirname1 + "img1.png"
    fig1.savefig(filename1)
    fig2, ax2 = plt.subplots(facecolor='white')
    xs4 = ['00:00', '01:00', '02:00' , '03:00','04:00','05:00','06:00','07:00','08:00','09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
    xs5 = ['00:00', '01:00', '02:00' , '03:00','04:00','05:00','06:00','07:00','08:00','09:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00']
    ax2.plot(xs, [a3,a6,b3,b6,c3,c6,d3,d6,e3,e6,f3,f6,g3,g6,h3,h6,i3,i6,j3,j6,k3,k6,l3,l6], label='開発ルーム', marker='o')
    ax2.plot(xs, [d3,c6,f3,1013.2,1014.2,1014,1014.6,1014,1014.5,1014.5,1013.2,1014.5,1013.8,1014.4,1013.5,1013,1013.5,1013.3,1013.1,1014.2,1014.3,1013.2,1013.6,1013.2], label='小会議室', marker = 'o')
    ax2.set_title('気圧', fontsize=25)
    ax2.set_xticklabels(xs, rotation=60)
    # ax.set_ylabel(rotation='horizontal')
    ax2.set_yticks([1010,1011,1012, 1013, 1014, 1015, 1016])
    ax2.grid()
    ax2.legend()
    dirname2 = "images/"
    filename2 = dirname2 + "img2.png"
    fig2.savefig(filename2)
    return render_template('index.html', text=sensor, text1=sensor1)

@application.route('/data')
def data():
        split = re.split('\s+', raspi_data)
        # print("split", split)
        temperature = float(split[0])
        if (temperature == 0):
            return
        print("temperature", temperature)
        humidity = float(split[1])
        pressure = float(split[2])
        data = [
            {
                "temperature": temperature,
                "huminity": humidity,
                "pressure": pressure,
            }
        ]
        return jsonify(data)
    
@application.route('/data1')
def data1():
        split1 = re.split('\s+', raspi_data1)
        # print("split", split1)
        temperature = float(split1[0])
        if (temperature == 0):
            return
        print("temperature", temperature)
        humidity = float(split1[1])
        pressure = float(split1[2])
        data1 = [
            {
                "temperature": temperature,
                "huminity": humidity,
                "pressure": pressure,
            }
        ]
        return jsonify(data1)

@application.route('/chart-data')
def chart_data():
    def generate_random_data():
            data = []
        # while raspi_data != '0 0 0':
            nowtime = timer()
            split = re.split('\s+', raspi_data)
            split1 = re.split('\s+', raspi_data1)
            # print("split", split)
            # print("split1", split1) 
            temperature = float(split[0])
            humidity = float(split[1])
            pressure = float(split[2])
            temperature1 = float(split1[0])
            data.append([nowtime, temperature, humidity, pressure])
            suujirandom = random.randrange(25, 27)
            # print("suujirandom", suujirandom)
            with open('sample.csv', 'w', newline="") as f:
                writer = csv.writer(f)
                writer.writerows(data)
            json_data = json.dumps(
                {'time': datetime.now().strftime('%H:%M:%S'), 'value': temperature, 'value1': humidity, 'value2': temperature1})
            yield f"data:{json_data}\n\n"
            # time.sleep(10)
    response = Response(stream_with_context(generate_random_data()), mimetype="text/event-stream")
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response

@application.route('/chart-data1')
def chart_data1(): 
    def generate_random_data():
        # while raspi_data != '0 0 0':
            split = re.split('\s+', raspi_data)
            split1 = re.split('\s+', raspi_data1)
            # print("split", split)
            # print("split1", split1) 
            humidity = float(split[1])
            humidity1 = float(split1[1])
            json_data = json.dumps({'time': datetime.now().strftime('%H:%M:%S'), 'value': humidity, 'value1': humidity1})
            yield f"data:{json_data}\n\n"
            # time.sleep(10)
    response = Response(stream_with_context(generate_random_data()), mimetype="text/event-stream")
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response

@application.route('/chart-data2')
def chart_data2():
    def generate_random_data():
        # while raspi_data != '0 0 0':
            split = re.split('\s+', raspi_data)
            split1 = re.split('\s+', raspi_data1)
            # print("split", split)
            # print("split1", split1) 
            pressure = float(split[2])
            pressure1 = float(split1[2])
            json_data = json.dumps(
                {'time': datetime.now().strftime('%H:%M:%S'), 'value': pressure, 'value1': pressure1})
            yield f"data:{json_data}\n\n"
            # time.sleep(10)
    response = Response(stream_with_context(generate_random_data()), mimetype="text/event-stream")
    response.headers["Cache-Control"] = "no-cache"
    response.headers["X-Accel-Buffering"] = "no"
    return response

@application.route('/select-period', methods=['GET'])
def select_period():
    start_date_str = request.args.get('start')
    end_date_str = request.args.get('end')

    # 日付が正しくない場合
    if not start_date_str or not end_date_str:
        return jsonify({"error": "start and end dates are required"}), 400

    try:
        # 日付のフォーマットを変換
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
    except ValueError:
        return jsonify({"error": "Invalid date format"}), 400

    # グラフを作成して画像のパスを取得
    images = create_graphs(start_date, end_date)

    return jsonify({"images": images})

# def save_sensor_data_to_csv(data):
#     # CSV保存の処理（仮の実装）
#     import csv
#     with open('sensor_data.csv', mode='a', newline='', encoding='utf-8') as file:
#         writer = csv.writer(file)
#         writer.writerows(data)
#     print("CSV保存完了")

# def insert_fake_sensor_data():
#     conn = sqlite3.connect('sensor4.db')
#     cur = conn.cursor()

#     # テーブルが存在しない場合に作成
#     cur.execute('''CREATE TABLE IF NOT EXISTS sensor (
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         room TEXT,
#         date TEXT,
#         temperature REAL,
#         humidity REAL,
#         pressure REAL
#     )''')

    # now = datetime.now()
    # total_days = 365  # 1年間分
    # inserted_data = []  # CSV保存用リスト

    # # 365日分のデータを挿入
    # for day in range(total_days):
    #     for hour in range(0, 24, 3):  # 3時間ごとにデータを挿入
    #         dt = now - timedelta(days=day, hours=hour)
    #         dt_str = dt.strftime('%Y-%m-%d %H:%M:%S')
    
    #         for room in ['開発ルーム', '小会議室']:
    #             temp = round(random.uniform(18, 28), 1)  # 温度 (18〜28度の間)
    #             hum = round(random.uniform(40, 70), 1)   # 湿度 (40〜70%)
    #             pres = round(random.uniform(1005, 1020), 1)  # 気圧 (1005〜1020 hPa)
    #             cur.execute('INSERT INTO sensor (room, date, temperature, humidity, pressure) VALUES (?, ?, ?, ?, ?)',
    #                         (room, dt_str, temp, hum, pres))
                
    #             # CSV用に分解して保存
    #             date_part, time_part = dt_str.split(' ')
    #             inserted_data.append((date_part, time_part, room, temp, hum, pres))

    #     # 3時間ごとのデータが揃ったらCSVに保存
    #     save_sensor_data_to_csv(inserted_data)
    #     inserted_data.clear()  # 保存したらリストをクリア

    # conn.commit()
    # conn.close()
    # print("仮データ（開発ルーム・小会議室）を365日分挿入しました。")

def get_sensor_data(start_date, end_date, room):
    conn = sqlite3.connect('sensor4.db')
    cur = conn.cursor()

    data = []

    # 1日だけの場合 → 時間単位で取得
    if start_date == end_date:
        date_str = start_date.strftime('%Y-%m-%d')
        for hour in range(24):
            hour_start = f"{date_str} {hour:02d}:00:00"
            hour_end = f"{date_str} {hour:02d}:59:59"
            cur.execute('''
                SELECT AVG(temperature), AVG(humidity), AVG(pressure)
                FROM sensor
                WHERE room = ? AND date >= ? AND date <= ?
            ''', (room, hour_start, hour_end))
            avg_row = cur.fetchone()
            print(f"{room} - {hour:02d}:00 データ: {avg_row}")
            if avg_row[0] is not None:
                data.append((f"{hour:02d}:00", avg_row[0], avg_row[1], avg_row[2]))
            else:
                data.append((f"{hour:02d}:00", None, None, None))

    else:
        # 通常（日単位）の取得
        dates = [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range((end_date - start_date).days + 1)]
        for date in dates:
            cur.execute('SELECT * FROM sensor WHERE room = ? AND date LIKE ?', (room, f"{date}%"))
            daily_data = cur.fetchall()
            print(f"{room} - {date} データ数: {len(daily_data)}")
            data.append(daily_data)

    conn.close()
    return data

def process_sensor_data(data):
    temperature_data = []
    humidity_data = []
    pressure_data = []

    for daily_data in data:
        if daily_data:
            daily_temperatures = [d[2] for d in daily_data]
            daily_humidities = [d[3] for d in daily_data]
            daily_pressures = [d[4] for d in daily_data]
            
            temperature_data.append(sum(daily_temperatures) / len(daily_temperatures))
            humidity_data.append(sum(daily_humidities) / len(daily_humidities))
            pressure_data.append(sum(daily_pressures) / len(daily_pressures))
        else:
            temperature_data.append(0)
            humidity_data.append(0)
            pressure_data.append(0)
    
    return temperature_data, humidity_data, pressure_data

def aggregate_weekly_data(data):
    weekly_data = []
    weeks = len(data) // 7
    for i in range(weeks):
        chunk = data[i*7:(i+1)*7]
        avg = sum(chunk) / len(chunk) if chunk else 0
        weekly_data.append(avg)
    
    remaining_days = len(data) % 7
    if remaining_days > 0:
        chunk = data[-remaining_days:]
        weekly_data.extend(chunk)
    
    return weekly_data

def aggregate_monthly_data(data, start_date, _):
    monthly_data = []
    current_month = start_date.month
    current_year = start_date.year
    current_month_data = []
    
    for i, value in enumerate(data):
        current_date = start_date + timedelta(days=i)
        if current_date.month != current_month or current_date.year != current_year:
            # 月が変わった場合
            if current_month_data:
                monthly_data.append(sum(current_month_data) / len(current_month_data))  # 月単位の平均を追加
            current_month_data = [value]  # 新しい月にデータをリセット
            current_month = current_date.month
            current_year = current_date.year
        else:
            current_month_data.append(value)
    
    # 最後の月の処理
    if current_month_data:
        monthly_data.append(sum(current_month_data) / len(current_month_data))
    
    return monthly_data

def plot_sensor_data(xs, ys, title, ylabel, filename, rotation=60):

    plt.rcParams["font.size"] = 10
    fig, ax = plt.subplots(facecolor='white')

    all_y_values = []

    for y_data, label in ys:
        # yが12個未満なら、前にNoneを詰めて12個に揃える（後半--ヶ月だけデータがあるケース）
        if len(y_data) < len(xs):
            padded_y = [None] * (len(xs) - len(y_data)) + y_data
        else:
            padded_y = y_data
        ax.plot(xs, padded_y, label=label, marker='o')
        all_y_values += [v for v in padded_y if v is not None]

    ax.set_title(title, fontsize=25)
    ax.set_xticks(range(len(xs)))
    if rotation != 0:
        ax.set_xticklabels(xs, rotation=rotation, ha='right')
    else:
        ax.set_xticklabels(xs)
    ax.set_ylabel(ylabel)
    ax.grid()
    ax.ticklabel_format(style='plain', axis='y')
    ax.get_yaxis().get_offset_text().set_visible(False)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(round(x))}'))
    ax.legend()

     # y軸の中央にデータが表示されるように調整 
    if all_y_values:
        y_center = np.mean(all_y_values)
        y_min = min(all_y_values)
        y_max = max(all_y_values)
        y_spread = max(abs(y_max - y_center), abs(y_center - y_min)) * 3.5  # ← 倍に拡大して余裕を持たせる
        ax.set_ylim(y_center - y_spread, y_center + y_spread)

    fig.tight_layout()
    fig.savefig(filename)
    print(f"グラフ保存: {filename}")

def create_graphs(start_date, end_date):
    # 保存先のディレクトリを指定
    image_folder = os.path.join(application.static_folder, 'images')
    if not os.path.exists(image_folder):
        os.makedirs(image_folder)
    
    days_diff = (end_date - start_date).days + 1
    dev_data = get_sensor_data(start_date, end_date, '開発ルーム')
    meet_data = get_sensor_data(start_date, end_date, '小会議室')

    image_paths = []

    if days_diff == 1:
        # --- 1日のデータ: 時間単位 ---
        # get_sensor_data() から [(hour, temp, hum, pres), ...] の形式で返る
        xs = [row[0] for row in dev_data]
        temp_dev = [row[1] for row in dev_data]
        hum_dev = [row[2] for row in dev_data]
        pres_dev = [row[3] for row in dev_data]

        temp_meet = [row[1] for row in meet_data]
        hum_meet = [row[2] for row in meet_data]
        pres_meet = [row[3] for row in meet_data]

    elif days_diff <= 31:
        # --- 日単位データ (カレンダー通り) ---
        temp_dev, hum_dev, pres_dev = process_sensor_data(dev_data)
        temp_meet, hum_meet, pres_meet = process_sensor_data(meet_data)

        # 開始日から31日分の日付を作成
        xs = [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(days_diff)]

        # 月ごとにデータをまとめる
        temp_dev_full = []
        hum_dev_full = []
        pres_dev_full = []
        temp_meet_full = []
        hum_meet_full = []
        pres_meet_full = []

        current_month = start_date.month

        for i, _ in enumerate(xs):
            current_date = start_date + timedelta(days=i)
            if current_date.month != current_month:
                # 月が変わった場合、次の月に切り替え
                current_month = current_date.month

            # 元のデータを月ごとに配列に追加
            temp_dev_full.append(temp_dev[i] if i < len(temp_dev) else None)
            hum_dev_full.append(hum_dev[i] if i < len(hum_dev) else None)
            pres_dev_full.append(pres_dev[i] if i < len(pres_dev) else None)
            temp_meet_full.append(temp_meet[i] if i < len(temp_meet) else None)
            hum_meet_full.append(hum_meet[i] if i < len(hum_meet) else None)
            pres_meet_full.append(pres_meet[i] if i < len(pres_meet) else None)

        # 最後にまとめたデータを利用して処理
        temp_dev = temp_dev_full
        hum_dev = hum_dev_full
        pres_dev = pres_dev_full
        temp_meet = temp_meet_full
        hum_meet = hum_meet_full
        pres_meet = pres_meet_full

    elif days_diff <= 90:
        # --- 週単位 ---
        temp_dev, hum_dev, pres_dev = process_sensor_data(dev_data)
        temp_meet, hum_meet, pres_meet = process_sensor_data(meet_data)

        temp_dev = aggregate_weekly_data(temp_dev)
        hum_dev = aggregate_weekly_data(hum_dev)
        pres_dev = aggregate_weekly_data(pres_dev)
        temp_meet = aggregate_weekly_data(temp_meet)
        hum_meet = aggregate_weekly_data(hum_meet)
        pres_meet = aggregate_weekly_data(pres_meet)

        weeks = days_diff // 7
        remaining_days = days_diff % 7

        # 週部分のx軸（週の開始日だけ）
        xs_weeks = [
            (start_date + timedelta(days=i * 7)).strftime('%Y-%m-%d')
            for i in range(weeks)
        ]

        # 余り日部分のx軸（日単位）
        remaining_days_start_date = start_date + timedelta(days=weeks * 7)
        xs_remaining_days = [
            (remaining_days_start_date + timedelta(days=i)).strftime('%Y-%m-%d')
            for i in range(remaining_days)
        ]

        # もしremaining_days == 0ならば、end_date（最終日）をxs_weeksに追加
        if remaining_days == 0:
            xs_weeks.append(end_date.strftime('%Y-%m-%d'))

        # 最終的なx軸
        xs = xs_weeks + xs_remaining_days

    # 既存のコード（そのまま追加する部分）
    elif days_diff >= 91:
        # --- 月単位集計 + 残り日処理 ---
        temp_dev, hum_dev, pres_dev = process_sensor_data(dev_data)
        temp_meet, hum_meet, pres_meet = process_sensor_data(meet_data)

        # 月単位データ
        temp_dev_month = aggregate_monthly_data(temp_dev, start_date, end_date)
        hum_dev_month = aggregate_monthly_data(hum_dev, start_date, end_date)
        pres_dev_month = aggregate_monthly_data(pres_dev, start_date, end_date)
        temp_meet_month = aggregate_monthly_data(temp_meet, start_date, end_date)
        hum_meet_month = aggregate_monthly_data(hum_meet, start_date, end_date)
        pres_meet_month = aggregate_monthly_data(pres_meet, start_date, end_date)

        # 月ラベル（YYYY-MM）
        month_labels = []
        cur = start_date.replace(day=1)
        while cur < end_date:
            month_labels.append(cur.strftime('%Y-%m'))
            if cur.month == 12:
                cur = cur.replace(year=cur.year + 1, month=1)
            else:
                cur = cur.replace(month=cur.month + 1)

        # 残り日を抽出
        last_month_start = end_date.replace(day=1)
        remaining_days = (end_date - last_month_start).days + 1
        last_month_data_temp = temp_dev[-remaining_days:]
        last_month_data_hum = hum_dev[-remaining_days:]
        last_month_data_pres = pres_dev[-remaining_days:]
        
        # 余りが7日以上なら週単位、未満なら日単位
        extra_labels = []
        extra_temp_dev = []
        extra_hum_dev = []
        extra_pres_dev = []
        extra_temp_meet = []
        extra_hum_meet = []
        extra_pres_meet = []

        if remaining_days >= 7:
            # 週単位
            weeks = remaining_days // 7
            for i in range(weeks):
                week_start = last_month_start + timedelta(days=i * 7)
                label = week_start.strftime('%Y-%m-%d')
                extra_labels.append(label)

                temp_chunk = last_month_data_temp[i*7:(i+1)*7]
                hum_chunk = last_month_data_hum[i*7:(i+1)*7]
                pres_chunk = last_month_data_pres[i*7:(i+1)*7]

                extra_temp_dev.append(sum(temp_chunk) / len(temp_chunk))
                extra_hum_dev.append(sum(hum_chunk) / len(hum_chunk))
                extra_pres_dev.append(sum(pres_chunk) / len(pres_chunk))

                # 小会議室のデータも同様
                temp_chunk_meet = temp_meet[-remaining_days:][i*7:(i+1)*7]
                hum_chunk_meet = hum_meet[-remaining_days:][i*7:(i+1)*7]
                pres_chunk_meet = pres_meet[-remaining_days:][i*7:(i+1)*7]
                extra_temp_meet.append(sum(temp_chunk_meet) / len(temp_chunk_meet))
                extra_hum_meet.append(sum(hum_chunk_meet) / len(hum_chunk_meet))
                extra_pres_meet.append(sum(pres_chunk_meet) / len(pres_chunk_meet))

            # 残り日（7日未満）
            leftover_days = remaining_days % 7
            if leftover_days > 0:
                for j in range(leftover_days):
                    day = last_month_start + timedelta(days=weeks*7 + j)
                    label = day.strftime('%Y-%m-%d')
                    extra_labels.append(label)

                    idx = weeks*7 + j
                    extra_temp_dev.append(last_month_data_temp[idx])
                    extra_hum_dev.append(last_month_data_hum[idx])
                    extra_pres_dev.append(last_month_data_pres[idx])
                    extra_temp_meet.append(temp_meet[-remaining_days:][idx])
                    extra_hum_meet.append(hum_meet[-remaining_days:][idx])
                    extra_pres_meet.append(pres_meet[-remaining_days:][idx])

        else:
            # 日単位
            for i in range(remaining_days):
                day = last_month_start + timedelta(days=i)
                label = day.strftime('%Y-%m-%d')
                extra_labels.append(label)

                extra_temp_dev.append(last_month_data_temp[i])
                extra_hum_dev.append(last_month_data_hum[i])
                extra_pres_dev.append(last_month_data_pres[i])
                extra_temp_meet.append(temp_meet[-remaining_days:][i])
                extra_hum_meet.append(hum_meet[-remaining_days:][i])
                extra_pres_meet.append(pres_meet[-remaining_days:][i])

        # X軸ラベル
        xs = month_labels + extra_labels

        # 各データ列結合
        temp_dev = temp_dev_month + extra_temp_dev
        hum_dev = hum_dev_month + extra_hum_dev
        pres_dev = pres_dev_month + extra_pres_dev

        temp_meet = temp_meet_month + extra_temp_meet
        hum_meet = hum_meet_month + extra_hum_meet
        pres_meet = pres_meet_month + extra_pres_meet

    # --- グラフ出力 ---
    temp_image_path = os.path.join(image_folder, 'temperature_chart.png')
    plot_sensor_data(xs, [(temp_dev, '開発ルーム'), (temp_meet, '小会議室')], '温度', 'Temperature (°C)', temp_image_path)
    image_paths.append('/images/images/temperature_chart.png')

    hum_image_path = os.path.join(image_folder, 'humidity_chart.png')
    plot_sensor_data(xs, [(hum_dev, '開発ルーム'), (hum_meet, '小会議室')], '湿度', 'Humidity (%)', hum_image_path)
    image_paths.append('/images/images/humidity_chart.png')

    pres_image_path = os.path.join(image_folder, 'pressure_chart.png')
    plot_sensor_data(xs, [(pres_dev, '開発ルーム'), (pres_meet, '小会議室')], '気圧', 'Pressure (hPa)', pres_image_path)
    image_paths.append('/images/images/pressure_chart.png')

    return image_paths

if __name__ == "__main__":
    serve(application, host="127.0.0.1", port=8000)