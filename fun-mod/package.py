#資料夾必有__init__.py，才算一個封包
#完整的模組呼叫：import 封包.模組 as 變數

import modules.geometry
import modules.point as p

print(p.dis(3,4))

print(modules.geometry.distance(2,6,2,6))
print(modules.geometry.slope(0,3,3,0))