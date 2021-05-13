def map(val, min_val, max_val, min_new, max_new):
	val = min_new + ( (max_new - min_new)*1.0/(max_val - min_val)*1.0 ) * (val)
	if val < min_new:
		val = min_new
	if val > max_new:
		val = max_new
	return round(val)

print(map(4094, 0, 4095, 0, 7))