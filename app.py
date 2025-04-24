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

@application.route('/data-range', methods=['GET'])
def data_range():
    range_type = request.args.get('range', '1d')

    if range_type == "1d":
        images = ["images/img.png", "images/img1.png", "images/img2.png"]
    elif range_type == "7d":
        images = ["images/weekly_temperature.png", "images/weekly_humidity.png", "images/weekly_pressure.png"]
    elif range_type == "30d":
        images = ["images/monthly_temperature.png", "images/monthly_humidity.png", "images/monthly_pressure.png"]
    elif range_type == "90d":
        images = ["images/3months_temperature.png", "images/3months_humidity.png", "images/3months_pressure.png"]
    elif range_type == "180d":
        images = ["images/6months_temperature.png", "images/6months_humidity.png", "images/6months_pressure.png"]
    elif range_type == "365d":
        images = ["images/yearly_temperature.png", "images/yearly_humidity.png", "images/yearly_pressure.png"]
    else:
        return jsonify({"error": "Invalid range type"}), 400

    return jsonify({"images": images})

def insert_fake_sensor_data():
    conn = sqlite3.connect('sensor4.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS sensor (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        room TEXT,
        date TEXT,
        temperature REAL,
        humidity REAL,
        pressure REAL
    )''')

    # now = datetime.now()
    # total_days = 365
    # inserted_data = []  # CSV保存用リスト

    # for day in range(total_days):
    #     for hour in range(0, 24, 3):  # 3時間ごとに1件
    #         dt = now - timedelta(days=day, hours=hour)
    #         dt_str = dt.strftime('%Y-%m-%d %H:%M:%S')
    
    #         for room in ['開発ルーム', '小会議室']:
    #             temp = round(random.uniform(18, 28), 1)
    #             hum = round(random.uniform(40, 70), 1)
    #             pres = round(random.uniform(1005, 1020), 1)
    #             cur.execute('INSERT INTO sensor (room, date, temperature, humidity, pressure) VALUES (?, ?, ?, ?, ?)',
    #                         (room, dt_str, temp, hum, pres))
                
    #             # CSV用に分解して保存
    #             date_part, time_part = dt_str.split(' ')
    #             inserted_data.append((date_part, time_part, room, temp, hum, pres))

    #         # CSVに保存（3時間ごとの2部屋分）
    #         save_sensor_data_to_csv(inserted_data)
            
    # conn.commit()
    # conn.close()
    # print("仮データ（開発ルーム・小会議室）を365日分挿入しました。")


def get_sensor_data(days, room):
    conn = sqlite3.connect('sensor4.db')
    cur = conn.cursor()
    
    today = datetime.now()
    start_date = today - timedelta(days=days)
    dates = [(start_date + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(days)]
    
    data = []
    for date in dates:
        cur.execute('SELECT * FROM sensor WHERE room = ? AND date LIKE ?', (room, f"{date}%"))
        daily_data = cur.fetchall()
        print(f"{room} - {date} データ数: {len(daily_data)}")
        data.append(daily_data)
    
    conn.close()
    return data, start_date, today


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

def plot_sensor_data(xs, ys, title, ylabel, filename, rotation=60):
    import numpy as np

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
    # ax.set_xticklabels(xs, rotation=rotation)
    if rotation != 0:
        ax.set_xticklabels(xs, rotation=rotation, ha='right')
    else:
        ax.set_xticklabels(xs)
    ax.set_ylabel(ylabel)
    ax.grid()
    ax.ticklabel_format(style='plain', axis='y')
    ax.get_yaxis().get_offset_text().set_visible(False)
    # ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{int(x)}'))
    # ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'{x:.1f}')) 
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

def aggregate_monthly_data(data, months):
    monthly_data = []
    days_per_month = len(data) // months
    for i in range(months):
        chunk = data[i*days_per_month:(i+1)*days_per_month]
        if chunk:
            avg = sum(chunk) / len(chunk)
        else:
            avg = 0
        monthly_data.append(avg)
    return monthly_data

def create_all_graphs():
    for period, days in [('weekly', 7), ('monthly', 30), ('3months', 90), ('6months', 180), ('yearly', 365)]:
        dev_data, start_dev, _ = get_sensor_data(days, '開発ルーム')
        meet_data, _, _ = get_sensor_data(days, '小会議室')

        temp_dev, hum_dev, pres_dev = process_sensor_data(dev_data)
        temp_meet, hum_meet, pres_meet = process_sensor_data(meet_data)

        if days >= 90:
            # データを月平均に変換
            months = days // 30
            temp_dev = aggregate_monthly_data(temp_dev, months)
            hum_dev = aggregate_monthly_data(hum_dev, months)
            pres_dev = aggregate_monthly_data(pres_dev, months)

            temp_meet = aggregate_monthly_data(temp_meet, months)
            hum_meet = aggregate_monthly_data(hum_meet, months)
            pres_meet = aggregate_monthly_data(pres_meet, months)

            # x軸は常に12ヶ月固定（現在から過去12ヶ月）
            xs = [(datetime.now() - timedelta(days=30*i)).strftime('%Y/%m') for i in range(11, -1, -1)]

            # yデータは不足分をNoneで前詰め
            def pad_to_12months(data):
                return [None] * (12 - len(data)) + data

            temp_dev = pad_to_12months(temp_dev)
            hum_dev = pad_to_12months(hum_dev)
            pres_dev = pad_to_12months(pres_dev)

            temp_meet = pad_to_12months(temp_meet)
            hum_meet = pad_to_12months(hum_meet)
            pres_meet = pad_to_12months(pres_meet)
        else:
            xs = [(start_dev + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(days)]

        plot_sensor_data(xs, [(temp_dev, '開発ルーム'), (temp_meet, '小会議室')],
                 '温度', 'Temperature (°C)', f'images/{period}_temperature.png')

        plot_sensor_data(xs, [(hum_dev, '開発ルーム'), (hum_meet, '小会議室')],
                 '湿度', 'Humidity (%)', f'images/{period}_humidity.png')

        plot_sensor_data(xs, [(pres_dev, '開発ルーム'), (pres_meet, '小会議室')],
                 '気圧', 'Pressure (hPa)', f'images/{period}_pressure.png')

def save_sensor_data_to_csv(data, filename='output.csv'):
    
    write_header = not os.path.exists(filename)

    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        if write_header:
            writer.writerow(['日付', '時刻', '部屋名', '温度', '湿度', '気圧'])

        for row in data:
            writer.writerow(row)

    print(f"CSVに保存しました: {filename}")

if __name__ == "__main__":
    insert_fake_sensor_data()
    create_all_graphs()
    print("全期間のグラフが生成されました。")
    serve(application, host="192.168.3.9", port=5000)
