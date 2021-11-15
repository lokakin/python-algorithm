def sqrt(x):
  low = 0
  high = x

  while (high - low) > 0.001:
    mid = (low + high)/2
    print(mid)

    square = mid * mid

    if abs(square - x) < 0.0001:
      return mid
    elif x < square:
      high = mid
    else:
      low = mid

  return round((high + low)/2, 3)

print(sqrt(5))