# Divide two integers and give a rounded down value without the use of multiplication/division or modulus operators

# Minimum runtime solution using range and XOR for sign indentification
def divide(self, dividend: int, divisor: int) -> int:
  # Handle overflow
  INT_MAX = 2**31 - 1
  INT_MIN = -2**31
  absDivisor, absDividend = abs(divisor), abs(dividend)
  multiple = -len(range(absDivisor, absDividend+1, absDivisor)) if (dividend < 0) ^ (divisor < 0) else len(range(absDivisor, absDividend+1, absDivisor))
  
  return min(max(INT_MIN, multiple), INT_MAX)

# Bitwise operation solution
def divide(self, dividend: int, divisor: int) -> int:
  # Handle overflow
  INT_MAX = 2**31 - 1
  INT_MIN = -2**31
  if dividend == INT_MIN and divisor == -1:
      return INT_MAX
  
  # Determine the sign of the result
  sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
  
  # Work with absolute values
  dividend, divisor = abs(dividend), abs(divisor)
  quotient = 0
  
  # Bit shifting method
  while dividend >= divisor:
      temp, multiple = divisor, 1
      while dividend >= (temp << 1):
          temp <<= 1
          multiple <<= 1
      dividend -= temp
      quotient += multiple
  
  # Apply the sign
  quotient *= sign
  
  # Clamp the result to the 32-bit signed integer range
  return max(INT_MIN, min(INT_MAX, quotient))
