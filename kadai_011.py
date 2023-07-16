planet = ["水","金","地","火","木","土","天","海","冥"]
for planet in planet:
    print(planet)

planet = ["水", "金", "地", "火", "木", "土", "天", "海", "冥"]
i = 0

while i < len(planet):
    if i == 8:
        break
    else:
        print(planet[i])
        i = i + 1