import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import matplotlib as mpl


mpl.rcParams['axes.unicode_minus'] = False
font_path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
font_name = font_manager.FontProperties(fname=font_path).get_name()
plt.rcParams["font.family"] = font_name