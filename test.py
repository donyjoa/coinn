import pyupbit

access = "PqxoO0th43dZB7x8QwAmM1hPENxqZleKwxtITixT"          # 본인 값으로 변경
secret = "a33KiLx9Cd01NuVm7jzhr11AsGzAYlRrSYgnoeHW"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회
