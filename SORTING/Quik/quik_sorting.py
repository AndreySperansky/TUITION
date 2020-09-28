def qSort ( m, nStart, nEnd ):
  if nStart >= nEnd:
      return
  l = nStart; r = nEnd
  x = m[(l+r)//2]
  while l <= r:
    while m[l] < x:
        l += 1
    while m[r] > x:
        r -= 1
    if l <= r:
      m[l], m[r] = m[r], m[l]
      l += 1; r -= 1
  qSort(m, nStart, r)
  qSort(m, l, nEnd)
  print(m)

a = [12, 36, 18, 54, 35, 88, 52, 92, 33, 67]

qSort(a, 0, (len(a)-1))