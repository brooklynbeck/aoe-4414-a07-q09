# max_bitrate.py
#
# Usage: python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz
# Calculates the maximum achievable bitrate
# Parameters:
# tx_w : transmitter power (W)
# tx_gain_db : transmitter gain (dB)
# freq_hz : transmission frequency (Hz)
# dist_km : distance between transmitter and receiver (km)
# rx_gain_db : receiver gain (dB)
# n0_j : noise spectral density (J)
# bw_hz : bandwidth (Hz)
# Output:
# Prints maxiumum bitrate
#
# Written by Brooklyn Beck
# Other contributors: None
#
# import Python modules
import math # math module
import sys # argv

# initialize script arguments
tx_w = float('nan') #transmitter power (W)
tx_gain_db = float('nan') #transmitter gain (dB)
freq_hz = float('nan') #transmission frequency (Hz)
dist_km = float('nan') #distance between transmitter and receiver (km)
rx_gain_db = float('nan') #receiver gain (dB)
n0_j = float('nan') #noise spectral density (J)
bw_hz = float('nan') #bandwidth (Hz)

# parse script arguments
if len(sys.argv)==8:
  tx_w = float(sys.argv[1])
  tx_gain_db = float(sys.argv[2])
  freq_hz = float(sys.argv[3])
  dist_km = float(sys.argv[4])
  rx_gain_db = float(sys.argv[5])
  n0_j = float(sys.argv[6])
  bw_hz = float(sys.argv[7])
else:
  print(\
  'Usage: '\
  'python3 max_bitrate.py tx_w tx_gain_db freq_hz dist_km rx_gain_db n0_j bw_hz'\
  )
  exit()

#helper function
def db_to_base_ten(db):
  return (10**(db/10))

# main script
L_l_db = -1 #db
atmosphericLoss = 0 #db
c = 2.99792458 * 10**8 #m/s

P = tx_w #w
L_l = db_to_base_ten(L_l_db)
G_t = db_to_base_ten(tx_gain_db)
e_a_wavelength = c/freq_hz
S = dist_km * 1000 #m
L_a = db_to_base_ten(atmosphericLoss)
G_r = db_to_base_ten(rx_gain_db)
N_0 = 1.42262*10**-20

B = bw_hz
C = P * L_l * G_t * (e_a_wavelength / (4 * math.pi *S))**2 * L_a * G_r
N = N_0 * B
r_max = B * math.log2(1+C/N)

print(math.floor(r_max))
