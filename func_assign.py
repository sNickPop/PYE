def computepay(h, r):
    if h > 40:
        hr = h - 40
    if h > 40:
        rt = 1.5 * r
    if h > 40:
        gross = (40 * r)
    else:
        gross = h * r
    if h > 40:
        ovt = hr * rt
        gpay = gross + ovt
        return gpay
    else:
        return gross
hrs = input('Enter Hours:')
h = float(hrs)
rate = input('Enter Rate:')
r = float(rate)
p = computepay(h, r)
print('Pay', p)