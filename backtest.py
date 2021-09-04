import pyupbit
import numpy as np

# ohlcv란 시가, 고가, 저가, 종가, 거래량을 뜻한다, count는 기간
df = pyupbit.get_ohlcv("KRW-BTC", count=30)

# range = 변동폭, 변동성 돌파 기준 범위 계산, (고가-저가)*k값
df['range'] = (df['high'] - df['low']) * 0.5

# target = 매수가, range 컬럼을 한칸씩 밑으로 내림(.shift(1)), 하루 전 변동폭값이라고 생각
df['target'] = df['open'] + df['range'].shift(1)

# ror=수익률, np.where(조건문, 참일때 값, 거짓일때 값)
fee = 0.0015
df['ror'] = np.where(df['high'] > df['target'],
                     df['close'] / df['target'] - fee,
                     1)

# 누적 곱 계산(cumprod) => 누적 수익률
df['hpr'] = df['ror'].cumprod()

# draw down 계산 (누적 최대값과 현재 hpr 차이 / 누적 최대값 *100)
df['dd'] = (df['hpr'].cummax() - df['hpr']) / df['hpr'].cummax() * 100

# mdd 표시
print("MDD(%): ", df['dd'].max())

# 엑설로 출력
df.to_excel("dd.xlsx")
