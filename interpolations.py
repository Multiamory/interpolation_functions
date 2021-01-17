import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import math
from random import randint

def main():
  fig = plt.figure(figsize=(10, 8))
  ax = fig.add_subplot(111)

  points = []
  for i in range(0, 101):
    i = float(i)
    val = calculate_curve(i/100, 0.5, .25)
    points.append(val* 100.0)
    
  ax.plot(points)
  fig.savefig('graph.png')

def interpolate_to_curve(input_val, input_min, input_max, output_min, output_max, curve_value):
  if curve_value == 1:
    return interpolate_linear(input_val, input_min, input_max, output_min, output_max)
  curve_value = abs(curve_value)
  multiplier = output_max - output_min
  top = pow(curve_value, input_val - input_min) - 1
  bottom = pow(curve_value, input_max - input_min) - 1
  res = multiplier * (top / bottom) + output_min
  return res

def interpolate_linear(input_val, input_min, input_max, output_min, output_max):
  input_range = input_max - input_min
  output_range = output_max - output_min
  ratio = (input_val - input_min)/input_range
  return max(min(ratio * output_range + output_min, output_max), output_min)

def sigmoid(input_val):
  return 1/(1 + math.exp(-input_val))

# Adjustable sigmoid/smoothstep
def half_curve(x, n, curve_coefficient):
  return pow(x, curve_coefficient) / pow(n, curve_coefficient-1)

def calculate_curve(input_val, curve_point=0.5, curve_slope=0.5):
  curve_coefficient = 2/(1-curve_slope)-1
  if input_val <= 0.5:
    return half_curve(input_val, curve_point, curve_coefficient)
  else:
    return 1 - half_curve(1-input_val, 1-curve_point, curve_coefficient)


if __name__ == "__main__":
  main()
